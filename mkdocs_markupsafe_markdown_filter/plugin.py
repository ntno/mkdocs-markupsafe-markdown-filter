"""
This module provides a plugin that can be used to make untrusted text
ready to insert into HTML either by escaping special characters
or by marking the text as safe.

See markupsafe for details: https://github.com/pallets/markupsafe
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
        """
        Converts the given text to a "safe" string
        taking into account the currently enabled markdown extensions.
        """
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
