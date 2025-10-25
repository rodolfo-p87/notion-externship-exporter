"""
Basic tests for the Notion Export Tool

Run with: pytest tests/
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from consolidator import MarkdownConsolidator


def test_consolidator_initialization():
    """Test that consolidator initializes correctly."""
    consolidator = MarkdownConsolidator("Test Externship")
    assert consolidator.externship_name == "Test Externship"
    assert consolidator.content_parts == []


def test_add_header():
    """Test adding header to document."""
    consolidator = MarkdownConsolidator("Marketing Externship")
    consolidator.add_header()

    content = consolidator.get_consolidated_content()
    assert "Marketing Externship" in content
    assert "Complete Knowledge Base" in content


def test_add_page_content():
    """Test adding page content."""
    consolidator = MarkdownConsolidator("Test Externship")

    consolidator.add_page_content(
        title="Project 1",
        content="This is project 1 content.",
        level=1
    )

    content = consolidator.get_consolidated_content()
    assert "## Project 1" in content
    assert "This is project 1 content." in content


def test_hierarchy_levels():
    """Test that hierarchy levels produce correct markdown headers."""
    consolidator = MarkdownConsolidator("Test Externship")

    # Level 1 should be ##
    consolidator.add_page_content("Project", "Content", level=1)
    # Level 2 should be ###
    consolidator.add_page_content("Step", "Content", level=2)
    # Level 3 should be ####
    consolidator.add_page_content("Sub-step", "Content", level=3)

    content = consolidator.get_consolidated_content()

    assert "## Project" in content
    assert "### Step" in content
    assert "#### Sub-step" in content


def test_statistics():
    """Test statistics calculation."""
    consolidator = MarkdownConsolidator("Test Externship")
    consolidator.add_header()
    consolidator.add_page_content("Test", "Content here", level=1)

    stats = consolidator.get_statistics()

    assert 'character_count' in stats
    assert 'word_count' in stats
    assert 'line_count' in stats
    assert 'estimated_size_kb' in stats
    assert stats['character_count'] > 0
    assert stats['word_count'] > 0


def test_filename_generation():
    """Test that filenames are generated correctly."""
    consolidator = MarkdownConsolidator("Marketing Externship Q1 2025")
    filename = consolidator.generate_filename()

    assert filename.startswith("marketing-externship-q1-2025")
    assert filename.endswith(".md")
    assert "knowledge-base" in filename


def test_metadata_formatting():
    """Test metadata formatting."""
    consolidator = MarkdownConsolidator("Test")

    metadata = {
        "Duration": "4 weeks",
        "Level": "Intermediate"
    }

    consolidator.add_page_content(
        title="Test Page",
        content="Content",
        level=1,
        metadata=metadata
    )

    content = consolidator.get_consolidated_content()
    assert "Duration" in content
    assert "4 weeks" in content


if __name__ == "__main__":
    # Run basic smoke tests
    print("Running basic tests...")

    test_consolidator_initialization()
    print("✓ Consolidator initialization")

    test_add_header()
    print("✓ Add header")

    test_add_page_content()
    print("✓ Add page content")

    test_hierarchy_levels()
    print("✓ Hierarchy levels")

    test_statistics()
    print("✓ Statistics calculation")

    test_filename_generation()
    print("✓ Filename generation")

    test_metadata_formatting()
    print("✓ Metadata formatting")

    print("\nAll tests passed! ✓")
