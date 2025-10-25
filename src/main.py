"""
Notion to GPT Exporter - Main CLI Interface

This is the entry point for the tool. Run this to export and consolidate
Notion externship content into a single file for custom GPT training.

Usage:
    python main.py --url "https://www.notion.so/your-externship-page"

Or interactively:
    python main.py
"""

import click
import os
import sys
from tqdm import tqdm
from typing import Dict, Any, List

from config import get_config
from notion_exporter import NotionExporter
from consolidator import MarkdownConsolidator


class ExternshipExporter:
    """
    Main orchestrator for exporting Notion externships to GPT-ready format.

    This class coordinates the export process:
    1. Connects to Notion API
    2. Fetches all pages recursively
    3. Consolidates into one markdown file
    4. Saves and reports statistics
    """

    def __init__(self, api_key: str):
        """Initialize the exporter with Notion API credentials."""
        self.notion = NotionExporter(api_key)
        self.page_cache = {}  # Cache to avoid re-fetching pages

    def export_externship(
        self,
        page_url: str,
        output_dir: str = "output",
        custom_name: str = None
    ) -> Dict[str, Any]:
        """
        Export an entire externship from Notion.

        Args:
            page_url: URL of the main externship page
            output_dir: Directory to save the output file
            custom_name: Optional custom name for the externship

        Returns:
            dict: Export results including file path and statistics
        """
        print(f"\n{'='*60}")
        print("NOTION EXTERNSHIP EXPORTER")
        print(f"{'='*60}\n")

        # Step 1: Extract page ID from URL
        print("📋 Step 1: Extracting page information...")
        try:
            page_id = self.notion.extract_page_id(page_url)
            print(f"   ✓ Page ID: {page_id}")
        except Exception as e:
            print(f"   ✗ Error: {str(e)}")
            sys.exit(1)

        # Step 2: Fetch main page
        print("\n📥 Step 2: Fetching externship page from Notion...")
        try:
            main_page = self.notion.get_page(page_id)
            externship_title = custom_name or self.notion.get_page_title(main_page)
            print(f"   ✓ Externship: {externship_title}")
        except Exception as e:
            print(f"   ✗ Error: {str(e)}")
            sys.exit(1)

        # Step 3: Build hierarchical structure
        print("\n🌳 Step 3: Building content hierarchy...")
        try:
            structure = self._build_hierarchy(page_id, externship_title)
            total_pages = self._count_pages(structure)
            print(f"   ✓ Found {total_pages} pages total")
        except Exception as e:
            print(f"   ✗ Error: {str(e)}")
            sys.exit(1)

        # Step 4: Export all content
        print(f"\n📝 Step 4: Exporting content from {total_pages} pages...")
        try:
            consolidator = MarkdownConsolidator(externship_title)
            consolidator.add_header()

            # Process with progress bar
            self._process_hierarchy(structure, consolidator)

            print(f"   ✓ All content exported successfully")
        except Exception as e:
            print(f"   ✗ Error: {str(e)}")
            sys.exit(1)

        # Step 5: Save to file
        print("\n💾 Step 5: Saving consolidated file...")
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Generate filename and save
            filename = consolidator.generate_filename()
            output_path = os.path.join(output_dir, filename)
            consolidator.save_to_file(output_path)

            print(f"   ✓ Saved to: {output_path}")
        except Exception as e:
            print(f"   ✗ Error: {str(e)}")
            sys.exit(1)

        # Step 6: Show statistics
        print("\n📊 Export Statistics:")
        stats = consolidator.get_statistics()
        print(f"   • Characters: {stats['character_count']:,}")
        print(f"   • Words: {stats['word_count']:,}")
        print(f"   • Lines: {stats['line_count']:,}")
        print(f"   • File size: {stats['estimated_size_kb']} KB ({stats['estimated_size_mb']} MB)")

        # Check if size is reasonable for GPT
        if stats['estimated_size_mb'] > 10:
            print(f"\n   ⚠️  Warning: File is quite large ({stats['estimated_size_mb']} MB)")
            print(f"   Consider splitting into multiple files if GPT upload fails")
        else:
            print(f"\n   ✓ File size is good for GPT training!")

        print(f"\n{'='*60}")
        print("EXPORT COMPLETE! 🎉")
        print(f"{'='*60}\n")

        return {
            'success': True,
            'output_path': output_path,
            'statistics': stats,
            'externship_name': externship_title
        }

    def _build_hierarchy(
        self,
        page_id: str,
        title: str,
        level: int = 0,
        max_level: int = 3
    ) -> Dict[str, Any]:
        """
        Recursively build the page hierarchy.

        Args:
            page_id: Notion page ID
            title: Page title
            level: Current hierarchy level (0=externship, 1=project, 2=step, 3=substep)
            max_level: Maximum depth to traverse

        Returns:
            dict: Hierarchical structure of pages
        """
        node = {
            'id': page_id,
            'title': title,
            'level': level,
            'children': []
        }

        # Don't go deeper than max_level
        if level >= max_level:
            return node

        # Get child pages
        child_page_ids = self.notion.get_child_pages(page_id)

        # Recursively process children
        for child_id in child_page_ids:
            try:
                child_page = self.notion.get_page(child_id)
                child_title = self.notion.get_page_title(child_page)

                child_node = self._build_hierarchy(
                    child_id,
                    child_title,
                    level + 1,
                    max_level
                )

                node['children'].append(child_node)
            except Exception as e:
                print(f"   ⚠️  Warning: Could not fetch child page {child_id}: {str(e)}")
                continue

        return node

    def _count_pages(self, structure: Dict[str, Any]) -> int:
        """
        Count total pages in the hierarchy.

        Args:
            structure: Hierarchical structure

        Returns:
            int: Total page count
        """
        count = 1  # Count this page

        if 'children' in structure:
            for child in structure['children']:
                count += self._count_pages(child)

        return count

    def _process_hierarchy(
        self,
        structure: Dict[str, Any],
        consolidator: MarkdownConsolidator
    ):
        """
        Process the hierarchy and add content to consolidator.

        Args:
            structure: Hierarchical structure
            consolidator: MarkdownConsolidator instance
        """
        # Get page content
        page_id = structure['id']
        title = structure['title']
        level = structure['level']

        # Fetch and convert blocks to markdown
        blocks = self.notion.get_blocks(page_id)
        content_parts = []

        for block in blocks:
            markdown = self.notion.block_to_markdown(block)
            if markdown:
                content_parts.append(markdown)

        content = '\n'.join(content_parts)

        # Add to consolidator (skip the root externship page itself)
        if level > 0:
            consolidator.add_page_content(
                title=title,
                content=content,
                level=level
            )

        # Process children
        if 'children' in structure:
            for child in structure['children']:
                self._process_hierarchy(child, consolidator)


@click.command()
@click.option(
    '--url',
    prompt='Notion Page URL',
    help='The URL of the Notion externship page'
)
@click.option(
    '--output',
    default='output',
    help='Output directory (default: output/)'
)
@click.option(
    '--name',
    default=None,
    help='Custom externship name (optional, will use Notion page title if not provided)'
)
def main(url: str, output: str, name: str):
    """
    Export a Notion externship to a GPT-ready markdown file.

    This tool fetches all content from a Notion externship page (including all
    projects, steps, and sub-steps) and consolidates it into a single markdown
    file optimized for custom GPT training.

    Example usage:

        python main.py --url "https://www.notion.so/your-externship"

    The tool will:
    1. Connect to Notion API
    2. Fetch all pages recursively
    3. Convert to markdown format
    4. Consolidate into one file
    5. Save to the output directory
    """
    try:
        # Load configuration
        config = get_config()

        # Create exporter
        exporter = ExternshipExporter(config.notion_api_key)

        # Run export
        result = exporter.export_externship(
            page_url=url,
            output_dir=output,
            custom_name=name
        )

        # Success message
        print(f"\n✅ Ready to upload to OpenAI!")
        print(f"   File: {result['output_path']}")
        print(f"\nNext steps:")
        print(f"   1. Go to https://platform.openai.com/playground")
        print(f"   2. Create or edit a custom GPT")
        print(f"   3. Upload this file to the 'Knowledge' section")
        print(f"   4. Your GPT will now have access to the {result['externship_name']} content!\n")

    except ValueError as e:
        print(f"\n❌ Configuration Error: {str(e)}")
        print(f"\nPlease make sure you have:")
        print(f"   1. Created a .env file (copy from .env.example)")
        print(f"   2. Added your NOTION_API_KEY to the .env file")
        print(f"\nSee README.md for setup instructions.\n")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Unexpected Error: {str(e)}")
        print(f"\nIf this persists, please check:")
        print(f"   • Your Notion API key is valid")
        print(f"   • The page URL is correct")
        print(f"   • The integration has access to the page\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
