"""
Configuration management for Notion Export Tool

This module handles loading environment variables and application settings.
Supports both local .env files and Streamlit Cloud secrets.
Keeps all configuration separate from code logic.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()


class Config:
    """
    Configuration container for the Notion Export Tool.

    Loads sensitive data (API keys) from environment variables or Streamlit secrets.
    Works in both local CLI mode and Streamlit web app mode.
    """

    def __init__(self):
        # Try to get API key from Streamlit secrets first, then environment variables
        self.notion_api_key = self._get_notion_api_key()

        # Validate required configuration
        if not self.notion_api_key:
            raise ValueError(
                "NOTION_API_KEY not found. "
                "For CLI: Create a .env file based on .env.example. "
                "For Streamlit: Add NOTION_API_KEY to secrets in Streamlit Cloud."
            )

    def _get_notion_api_key(self):
        """
        Get Notion API key from Streamlit secrets or environment variables.

        Returns:
            str: Notion API key

        Note:
            Tries Streamlit secrets first (for web app), then falls back to
            environment variables (for CLI usage).
        """
        # Try Streamlit secrets (if running in Streamlit)
        try:
            import streamlit as st
            if hasattr(st, 'secrets') and 'NOTION_API_KEY' in st.secrets:
                return st.secrets['NOTION_API_KEY']
        except (ImportError, FileNotFoundError):
            # Streamlit not available or secrets file not found - that's okay
            pass

        # Fall back to environment variable
        return os.getenv('NOTION_API_KEY')

    def is_valid(self):
        """Check if all required configuration is present."""
        return bool(self.notion_api_key)


def get_config():
    """
    Factory function to create and validate configuration.

    Returns:
        Config: Validated configuration object

    Raises:
        ValueError: If required configuration is missing
    """
    return Config()
