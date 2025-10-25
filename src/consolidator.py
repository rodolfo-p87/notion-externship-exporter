"""
Markdown Consolidation Engine

This module takes multiple Notion pages and combines them into a single,
well-structured markdown file optimized for GPT training.

Key features:
- Preserves hierarchical structure (Externship > Projects > Steps > Sub-steps)
- Adds clear section headers for navigation
- Removes duplicate content
- Formats optimally for AI knowledge retrieval
"""

from typing import List, Dict, Any
from slugify import slugify
from datetime import datetime


class MarkdownConsolidator:
    """
    Combines multiple Notion pages into a single markdown file.

    Maintains the hierarchical structure and formats content for
    optimal GPT training and knowledge retrieval.
    """

    def __init__(self, externship_name: str):
        """
        Initialize the consolidator.

        Args:
            externship_name: Name of the externship (for file naming and headers)
        """
        self.externship_name = externship_name
        self.content_parts = []

    def add_header(self):
        """Add document header with metadata."""
        header = f"""# {self.externship_name} - Complete Knowledge Base

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

**Purpose:** This document contains the complete curriculum and content for the {self.externship_name}.
It is structured hierarchically: Projects → Steps → Sub-steps.

---

"""
        self.content_parts.append(header)

    def add_page_content(
        self,
        title: str,
        content: str,
        level: int,
        metadata: Dict[str, Any] = None
    ):
        """
        Add a page's content to the consolidated document.

        Args:
            title: Page title
            content: Page content in markdown format
            level: Hierarchy level (1=Project, 2=Step, 3=Sub-step)
            metadata: Optional metadata about the page
        """
        # Determine header level based on hierarchy
        # Level 1 (Projects) = ##
        # Level 2 (Steps) = ###
        # Level 3 (Sub-steps) = ####
        header_level = level + 1
        header_prefix = "#" * header_level

        # Add the section
        section = f"{header_prefix} {title}\n\n"

        # Add any metadata if provided
        if metadata:
            section += self._format_metadata(metadata)

        # Add the actual content
        if content.strip():
            section += f"{content}\n\n"

        # Add spacing between sections
        section += "\n"

        self.content_parts.append(section)

    def _format_metadata(self, metadata: Dict[str, Any]) -> str:
        """
        Format metadata as a subtle info box.

        Args:
            metadata: Dictionary of metadata key-value pairs

        Returns:
            str: Formatted metadata section
        """
        if not metadata:
            return ""

        meta_lines = []
        for key, value in metadata.items():
            if value:  # Only include non-empty values
                meta_lines.append(f"**{key}:** {value}")

        if not meta_lines:
            return ""

        return "> " + " | ".join(meta_lines) + "\n\n"

    def add_section_separator(self, section_name: str = None):
        """
        Add a visual separator between major sections.

        Args:
            section_name: Optional name for the section
        """
        if section_name:
            separator = f"\n---\n\n## {section_name}\n\n"
        else:
            separator = "\n---\n\n"

        self.content_parts.append(separator)

    def get_consolidated_content(self) -> str:
        """
        Get the complete consolidated markdown content.

        Returns:
            str: Full markdown document
        """
        return ''.join(self.content_parts)

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about the consolidated content.

        Returns:
            dict: Statistics including word count, character count, estimated file size
        """
        content = self.get_consolidated_content()

        return {
            'character_count': len(content),
            'word_count': len(content.split()),
            'line_count': len(content.split('\n')),
            'estimated_size_kb': round(len(content.encode('utf-8')) / 1024, 2),
            'estimated_size_mb': round(len(content.encode('utf-8')) / (1024 * 1024), 2)
        }

    def save_to_file(self, output_path: str):
        """
        Save the consolidated content to a file.

        Args:
            output_path: Path where the file should be saved
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(self.get_consolidated_content())
            return True
        except Exception as e:
            raise Exception(f"Failed to save file: {str(e)}")

    def generate_filename(self) -> str:
        """
        Generate a clean filename based on the externship name.

        Returns:
            str: Sanitized filename
        """
        slug = slugify(self.externship_name)
        timestamp = datetime.now().strftime('%Y%m%d')
        return f"{slug}-knowledge-base-{timestamp}.md"


def create_table_of_contents(structure: List[Dict[str, Any]]) -> str:
    """
    Generate a table of contents from the page structure.

    Args:
        structure: Hierarchical structure of pages

    Returns:
        str: Markdown table of contents
    """
    toc_lines = ["## Table of Contents\n"]

    for i, project in enumerate(structure, 1):
        toc_lines.append(f"{i}. [{project['title']}](#{slugify(project['title'])})")

        if 'children' in project:
            for j, step in enumerate(project['children'], 1):
                toc_lines.append(f"   {i}.{j}. [{step['title']}](#{slugify(step['title'])})")

                if 'children' in step:
                    for k, substep in enumerate(step['children'], 1):
                        toc_lines.append(f"      {i}.{j}.{k}. [{substep['title']}](#{slugify(substep['title'])})")

    toc_lines.append("\n---\n")
    return '\n'.join(toc_lines)
