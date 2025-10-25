"""
Batch Export Script

Export multiple externships at once from a list of URLs.

Usage:
    python src/batch_export.py urls.txt

Where urls.txt contains one Notion URL per line.
Lines starting with # are treated as comments.
"""

import sys
import os
from typing import List

from config import get_config
from main import ExternshipExporter


def read_urls_from_file(file_path: str) -> List[str]:
    """
    Read URLs from a text file.

    Args:
        file_path: Path to the file containing URLs

    Returns:
        list: Valid URLs (ignoring comments and empty lines)
    """
    urls = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Remove whitespace
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue

                urls.append(line)

        return urls

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)


def batch_export(urls: List[str], output_dir: str = "output"):
    """
    Export multiple externships.

    Args:
        urls: List of Notion page URLs
        output_dir: Output directory for all files
    """
    print(f"\n{'='*60}")
    print(f"BATCH EXPORT: {len(urls)} EXTERNSHIPS")
    print(f"{'='*60}\n")

    # Load configuration
    try:
        config = get_config()
        exporter = ExternshipExporter(config.notion_api_key)
    except ValueError as e:
        print(f"Configuration Error: {str(e)}")
        sys.exit(1)

    # Track results
    results = {
        'successful': [],
        'failed': []
    }

    # Export each externship
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Processing: {url}")
        print("-" * 60)

        try:
            result = exporter.export_externship(
                page_url=url,
                output_dir=output_dir
            )

            results['successful'].append({
                'url': url,
                'name': result['externship_name'],
                'file': result['output_path'],
                'size': result['statistics']['estimated_size_mb']
            })

        except Exception as e:
            print(f"\n❌ Failed to export: {str(e)}\n")
            results['failed'].append({
                'url': url,
                'error': str(e)
            })

    # Print summary
    print(f"\n{'='*60}")
    print("BATCH EXPORT COMPLETE")
    print(f"{'='*60}\n")

    print(f"✓ Successful: {len(results['successful'])}/{len(urls)}")
    if results['successful']:
        print("\nExported files:")
        for result in results['successful']:
            print(f"  • {result['name']}")
            print(f"    File: {result['file']}")
            print(f"    Size: {result['size']} MB")

    if results['failed']:
        print(f"\n✗ Failed: {len(results['failed'])}/{len(urls)}")
        print("\nFailed URLs:")
        for failure in results['failed']:
            print(f"  • {failure['url']}")
            print(f"    Error: {failure['error']}")

    print(f"\nAll files saved to: {output_dir}/")
    print("\nNext: Upload these files to OpenAI to create your custom GPTs!")
    print()


def main():
    """Main entry point for batch export."""
    if len(sys.argv) < 2:
        print("\nUsage: python src/batch_export.py <urls_file>")
        print("\nExample:")
        print("  python src/batch_export.py batch-export-example.txt")
        print("\nThe file should contain one Notion URL per line.")
        print("Lines starting with # are treated as comments.\n")
        sys.exit(1)

    urls_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"

    # Read URLs
    urls = read_urls_from_file(urls_file)

    if not urls:
        print("Error: No valid URLs found in the file.")
        sys.exit(1)

    print(f"Found {len(urls)} externship(s) to export.")

    # Confirm before proceeding
    response = input(f"\nProceed with batch export? (y/n): ")
    if response.lower() != 'y':
        print("Export cancelled.")
        sys.exit(0)

    # Run batch export
    batch_export(urls, output_dir)


if __name__ == '__main__':
    main()
