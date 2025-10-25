"""
Streamlit Web Interface for Notion Externship Exporter

This web app allows Program Managers and Teaching Assistants to export
Notion externship content to GPT-ready markdown files with zero technical knowledge.

Usage:
    streamlit run streamlit_app.py
"""

import streamlit as st
import sys
import os
from pathlib import Path
from datetime import datetime
import io

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from config import get_config
from notion_exporter import NotionExporter
from consolidator import MarkdownConsolidator


# Page configuration
st.set_page_config(
    page_title="Extern Notion Exporter",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 0.5rem;
    }
    .stButton > button:hover {
        background-color: #1557a0;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        margin: 1rem 0;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)


def display_header():
    """Display the application header with logo."""
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Try to load logo if it exists
        logo_path = Path("assets/extern-logo.png")
        if logo_path.exists():
            st.image(str(logo_path), width=200)

        st.markdown("<h1 class='main-header'>Notion Externship Exporter</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666;'>Export Notion externships to GPT-ready knowledge base files</p>", unsafe_allow_html=True)


def validate_notion_url(url):
    """
    Validate that the URL looks like a Notion URL.

    Args:
        url: URL string to validate

    Returns:
        tuple: (is_valid, error_message)
    """
    if not url:
        return False, "Please enter a Notion URL"

    if not url.startswith("http"):
        return False, "URL must start with http:// or https://"

    if "notion.so" not in url and "notion.site" not in url:
        return False, "This doesn't appear to be a Notion URL"

    return True, None


def export_externship(notion_url, custom_name=None):
    """
    Export an externship from Notion.

    Args:
        notion_url: URL of the Notion page
        custom_name: Optional custom name for the externship

    Returns:
        tuple: (success, result_dict_or_error_message)
    """
    try:
        # Get configuration
        config = get_config()

        # Create exporter
        exporter = NotionExporter(config.notion_api_key)

        # Extract page ID
        with st.status("Extracting page information...", expanded=True) as status:
            st.write("📋 Parsing Notion URL...")
            page_id = exporter.extract_page_id(notion_url)
            st.write(f"✓ Page ID extracted: `{page_id}`")
            status.update(label="Page information extracted", state="complete")

        # Fetch main page
        with st.status("Fetching externship page from Notion...", expanded=True) as status:
            st.write("📥 Connecting to Notion API...")
            main_page = exporter.get_page(page_id)
            externship_title = custom_name or exporter.get_page_title(main_page)
            st.write(f"✓ Externship: **{externship_title}**")
            status.update(label=f"Fetched: {externship_title}", state="complete")

        # Build hierarchy
        with st.status("Building content hierarchy...", expanded=True) as status:
            st.write("🌳 Discovering all pages and sub-pages...")

            # Build hierarchy recursively
            def build_hierarchy_with_progress(page_id, title, level=0, max_level=3):
                node = {
                    'id': page_id,
                    'title': title,
                    'level': level,
                    'children': []
                }

                if level >= max_level:
                    return node

                child_page_ids = exporter.get_child_pages(page_id)

                for i, child_id in enumerate(child_page_ids):
                    try:
                        child_page = exporter.get_page(child_id)
                        child_title = exporter.get_page_title(child_page)

                        # Show progress
                        if level == 1:  # Projects
                            st.write(f"  📁 Found project: {child_title}")

                        child_node = build_hierarchy_with_progress(
                            child_id,
                            child_title,
                            level + 1,
                            max_level
                        )
                        node['children'].append(child_node)
                    except Exception as e:
                        st.warning(f"⚠️ Skipped page {child_id}: {str(e)}")
                        continue

                return node

            structure = build_hierarchy_with_progress(page_id, externship_title)

            # Count total pages
            def count_pages(node):
                count = 1
                if 'children' in node:
                    for child in node['children']:
                        count += count_pages(child)
                return count

            total_pages = count_pages(structure)
            st.write(f"✓ Found **{total_pages}** pages total")
            status.update(label=f"Hierarchy built: {total_pages} pages", state="complete")

        # Export content
        with st.status("Exporting content from all pages...", expanded=True) as status:
            st.write(f"📝 Processing {total_pages} pages...")

            # Create consolidator
            consolidator = MarkdownConsolidator(externship_title)
            consolidator.add_header()

            # Process hierarchy
            def process_hierarchy(node, consolidator):
                page_id = node['id']
                title = node['title']
                level = node['level']

                # Get page content
                blocks = exporter.get_blocks(page_id)
                content_parts = []

                for block in blocks:
                    markdown = exporter.block_to_markdown(block)
                    if markdown:
                        content_parts.append(markdown)

                content = '\n'.join(content_parts)

                # Add to consolidator (skip root)
                if level > 0:
                    consolidator.add_page_content(
                        title=title,
                        content=content,
                        level=level
                    )

                # Process children
                if 'children' in node:
                    for child in node['children']:
                        process_hierarchy(child, consolidator)

            process_hierarchy(structure, consolidator)
            st.write("✓ All content exported successfully")
            status.update(label="Content export complete", state="complete")

        # Get statistics
        stats = consolidator.get_statistics()

        # Generate filename
        filename = consolidator.generate_filename()

        # Get content as bytes for download
        content = consolidator.get_consolidated_content()

        return True, {
            'content': content,
            'filename': filename,
            'stats': stats,
            'externship_name': externship_title,
            'total_pages': total_pages
        }

    except ValueError as e:
        return False, f"Configuration Error: {str(e)}\n\nPlease ensure the Notion API key is configured correctly."

    except Exception as e:
        error_msg = str(e)

        # Provide helpful error messages
        if "Could not find page" in error_msg or "object_not_found" in error_msg:
            return False, "Cannot access this Notion page. Please ensure:\n1. The URL is correct\n2. Your Notion integration has access to this page\n3. The page hasn't been deleted"

        elif "unauthorized" in error_msg.lower():
            return False, "Notion API authorization failed. Please check that your API key is valid."

        elif "rate_limited" in error_msg.lower():
            return False, "Too many requests to Notion API. Please wait a minute and try again."

        else:
            return False, f"Unexpected error: {error_msg}\n\nIf this persists, contact your technical team."


def main():
    """Main application logic."""

    # Display header
    display_header()

    # Divider
    st.markdown("---")

    # Instructions
    with st.expander("ℹ️ How to use this tool", expanded=False):
        st.markdown("""
        **⚠️ FIRST TIME SETUP (Do this once per externship):**

        Before you can export an externship, give the Notion integration access to the page:
        1. Open the externship page in Notion
        2. Click the **"..."** menu (top right of the page)
        3. Scroll down and click **"Add connections"**
        4. Select **"Extern GPT Exporter"**
        5. Click **"Confirm"**

        ✅ **You only need to do this once per externship page!** The integration will then have access to that page and all its sub-pages.

        ---

        **Step 1:** Copy the URL of your Notion externship page
        - Open the externship in Notion
        - Click "Share" and copy the link

        **Step 2:** Paste the URL below

        **Step 3:** (Optional) Enter a custom name

        **Step 4:** Click "Export Externship"

        **Step 5:** Download the generated file

        **Step 6:** Upload the file to your OpenAI custom GPT

        ---

        **Troubleshooting:**
        - **"Cannot access page"** → Make sure you completed the "First Time Setup" above
        - **"Configuration error"** → Contact your team lead to check the API key setup
        - **Other issues** → Reach out on Slack or email support@extern.com
        """)

    # Input form
    st.subheader("📋 Export Settings")

    # Notion URL input
    notion_url = st.text_input(
        "Notion Page URL",
        placeholder="https://www.notion.so/your-externship-page-...",
        help="Paste the full URL of your Notion externship page"
    )

    # Custom name input (optional)
    custom_name = st.text_input(
        "Custom Externship Name (optional)",
        placeholder="Leave blank to use Notion page title",
        help="Override the externship name from Notion"
    )

    # Export button
    st.markdown("")  # Spacing
    export_button = st.button("📥 Export Externship", type="primary", use_container_width=True)

    # Handle export
    if export_button:
        # Validate URL
        is_valid, error_msg = validate_notion_url(notion_url)

        if not is_valid:
            st.error(f"❌ {error_msg}")
            return

        # Run export
        success, result = export_externship(
            notion_url,
            custom_name if custom_name else None
        )

        if success:
            # Success! Show results
            st.success("✅ Export completed successfully!")

            # Statistics
            st.markdown("### 📊 Export Statistics")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Pages", result['total_pages'])
            with col2:
                st.metric("Words", f"{result['stats']['word_count']:,}")
            with col3:
                st.metric("Size", f"{result['stats']['estimated_size_kb']} KB")
            with col4:
                st.metric("Lines", f"{result['stats']['line_count']:,}")

            # Check file size
            if result['stats']['estimated_size_mb'] > 10:
                st.warning(f"⚠️ File is quite large ({result['stats']['estimated_size_mb']} MB). If GPT upload fails, consider splitting into multiple files.")
            else:
                st.info(f"✓ File size ({result['stats']['estimated_size_mb']} MB) is perfect for GPT training!")

            # Download button
            st.markdown("### 💾 Download File")
            st.download_button(
                label=f"📥 Download {result['filename']}",
                data=result['content'],
                file_name=result['filename'],
                mime="text/markdown",
                use_container_width=True
            )

            # Next steps
            with st.expander("📝 What to do next"):
                st.markdown(f"""
                **Your file is ready!** Here's what to do next:

                1. **Click the download button above** to save the file to your computer

                2. **Go to OpenAI**: Visit https://chat.openai.com/gpts/editor

                3. **Create or edit your custom GPT**

                4. **Upload the knowledge file**:
                   - Scroll to the "Knowledge" section
                   - Click "Upload files"
                   - Select the file you just downloaded: `{result['filename']}`

                5. **Your GPT now has access** to the complete {result['externship_name']} content!

                Need help with the custom GPT setup? Check the GPT configuration guide in the project folder.
                """)

        else:
            # Error occurred
            st.error(f"❌ Export failed\n\n{result}")

    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #666; font-size: 0.9rem;'>
            <p>Extern.com Notion Exporter | Need help? Contact <a href='mailto:support@extern.com'>support@extern.com</a></p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
