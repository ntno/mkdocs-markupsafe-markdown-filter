"""
This module provides a plugin that can be used to escape special characters 
in Markdown text so that the text can be added to HTML. 
"""

from mkdocs.plugins import BasePlugin
import markdown
import markupsafe

class MarkupSafeMarkdownFilterPlugin(BasePlugin):
    """
    Registers the markupsafe 'Markup' function as a filter with the name 'markdown'
    """

    config_scheme = (
    )

    def __init__(self):
        self.enabled = True
        self.dirs = []

    def md_filter(self, text, **kwargs):
        md = markdown.Markdown(
            extensions=self.config['markdown_extensions'],
            extension_configs=self.config['mdx_configs'] or {}
        )
        return markupsafe.Markup(md.convert(text))

    def on_env(self, env, config, files):
        """
        A Global MkDocs event which will trigger once per build
        """
        self.config = config
        env.filters['markdown'] = self.md_filter
        return env
