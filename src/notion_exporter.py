"""
Notion API Client for recursive page fetching

This module handles all interactions with the Notion API, including:
- Authenticating with API key
- Fetching pages and their content
- Recursively retrieving all child pages (projects, steps, sub-steps)
- Converting Notion blocks to markdown format
"""

from notion_client import Client
from typing import List, Dict, Any
import time


class NotionExporter:
    """
    Wrapper for Notion API to export pages and all their children.

    This class handles the complexity of Notion's API structure and provides
    simple methods to extract content hierarchically.
    """

    def __init__(self, api_key: str):
        """
        Initialize the Notion client.

        Args:
            api_key: Notion integration API token
        """
        self.client = Client(auth=api_key)
        self.rate_limit_delay = 0.35  # Notion API limit: ~3 requests/second

    def extract_page_id(self, page_url: str) -> str:
        """
        Extract the page ID from a Notion URL.

        Notion URLs look like:
        https://www.notion.so/Page-Name-abc123def456...

        Args:
            page_url: Full Notion page URL

        Returns:
            str: The 32-character page ID

        Example:
            >>> extract_page_id("https://www.notion.so/My-Page-abc123")
            "abc123"
        """
        # Remove URL parameters
        clean_url = page_url.split('?')[0]

        # Extract the last part (contains the ID)
        page_id = clean_url.split('-')[-1]

        # Remove any trailing slashes
        page_id = page_id.rstrip('/')

        return page_id

    def get_page(self, page_id: str) -> Dict[str, Any]:
        """
        Fetch a single page's metadata from Notion.

        Args:
            page_id: Notion page ID

        Returns:
            dict: Page metadata including title, properties, etc.
        """
        try:
            time.sleep(self.rate_limit_delay)  # Rate limiting
            return self.client.pages.retrieve(page_id=page_id)
        except Exception as e:
            raise Exception(f"Failed to fetch page {page_id}: {str(e)}")

    def get_blocks(self, page_id: str) -> List[Dict[str, Any]]:
        """
        Fetch all content blocks from a page.

        Notion pages are made of blocks (paragraphs, headings, lists, etc.)
        This retrieves them all, handling pagination automatically.

        Args:
            page_id: Notion page ID

        Returns:
            list: All blocks from the page
        """
        blocks = []
        start_cursor = None

        try:
            while True:
                time.sleep(self.rate_limit_delay)  # Rate limiting

                response = self.client.blocks.children.list(
                    block_id=page_id,
                    start_cursor=start_cursor
                )

                blocks.extend(response['results'])

                # Check if there are more blocks to fetch
                if not response['has_more']:
                    break

                start_cursor = response['next_cursor']

            return blocks

        except Exception as e:
            raise Exception(f"Failed to fetch blocks for page {page_id}: {str(e)}")

    def get_child_pages(self, page_id: str) -> List[str]:
        """
        Get all child page IDs under a parent page.

        Args:
            page_id: Parent page ID

        Returns:
            list: List of child page IDs
        """
        child_page_ids = []

        try:
            blocks = self.get_blocks(page_id)

            for block in blocks:
                block_type = block.get('type')

                # Child pages appear as 'child_page' blocks
                if block_type == 'child_page':
                    child_page_ids.append(block['id'])

                # Some pages might be embedded as links
                elif block_type == 'link_to_page':
                    link_type = block['link_to_page']['type']
                    if link_type == 'page_id':
                        child_page_ids.append(block['link_to_page']['page_id'])

            return child_page_ids

        except Exception as e:
            print(f"Warning: Could not fetch child pages for {page_id}: {str(e)}")
            return []

    def block_to_markdown(self, block: Dict[str, Any]) -> str:
        """
        Convert a Notion block to markdown format.

        Args:
            block: Notion block object

        Returns:
            str: Markdown representation of the block
        """
        block_type = block.get('type')

        # Handle different block types
        if block_type == 'paragraph':
            return self._extract_rich_text(block['paragraph']['rich_text'])

        elif block_type == 'heading_1':
            text = self._extract_rich_text(block['heading_1']['rich_text'])
            return f"# {text}"

        elif block_type == 'heading_2':
            text = self._extract_rich_text(block['heading_2']['rich_text'])
            return f"## {text}"

        elif block_type == 'heading_3':
            text = self._extract_rich_text(block['heading_3']['rich_text'])
            return f"### {text}"

        elif block_type == 'bulleted_list_item':
            text = self._extract_rich_text(block['bulleted_list_item']['rich_text'])
            return f"- {text}"

        elif block_type == 'numbered_list_item':
            text = self._extract_rich_text(block['numbered_list_item']['rich_text'])
            return f"1. {text}"

        elif block_type == 'to_do':
            text = self._extract_rich_text(block['to_do']['rich_text'])
            checked = block['to_do']['checked']
            checkbox = "[x]" if checked else "[ ]"
            return f"- {checkbox} {text}"

        elif block_type == 'code':
            text = self._extract_rich_text(block['code']['rich_text'])
            language = block['code'].get('language', '')
            return f"```{language}\n{text}\n```"

        elif block_type == 'quote':
            text = self._extract_rich_text(block['quote']['rich_text'])
            return f"> {text}"

        elif block_type == 'callout':
            text = self._extract_rich_text(block['callout']['rich_text'])
            return f"> **Note:** {text}"

        elif block_type == 'divider':
            return "---"

        # Skip child_page blocks (handled separately)
        elif block_type == 'child_page':
            return ""

        # For unsupported blocks, return empty string
        else:
            return ""

    def _extract_rich_text(self, rich_text_array: List[Dict]) -> str:
        """
        Extract plain text from Notion's rich text format.

        Notion stores text with formatting annotations. This extracts just the text.

        Args:
            rich_text_array: Array of rich text objects from Notion

        Returns:
            str: Plain text content
        """
        if not rich_text_array:
            return ""

        text_parts = []
        for text_obj in rich_text_array:
            if text_obj.get('type') == 'text':
                plain_text = text_obj['text']['content']

                # Apply markdown formatting based on annotations
                annotations = text_obj.get('annotations', {})
                if annotations.get('bold'):
                    plain_text = f"**{plain_text}**"
                if annotations.get('italic'):
                    plain_text = f"*{plain_text}*"
                if annotations.get('code'):
                    plain_text = f"`{plain_text}`"

                text_parts.append(plain_text)

        return ''.join(text_parts)

    def get_page_title(self, page_data: Dict[str, Any]) -> str:
        """
        Extract the title from a page's metadata.

        Args:
            page_data: Page object from Notion API

        Returns:
            str: Page title
        """
        try:
            # Try to get title from properties (for database pages)
            if 'properties' in page_data:
                for prop_name, prop_data in page_data['properties'].items():
                    if prop_data.get('type') == 'title':
                        title_array = prop_data['title']
                        if title_array:
                            return title_array[0]['plain_text']

            # For regular pages, title is in child_page block
            if 'child_page' in page_data:
                return page_data['child_page'].get('title', 'Untitled')

            return "Untitled"

        except Exception:
            return "Untitled"
