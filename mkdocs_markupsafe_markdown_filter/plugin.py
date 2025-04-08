"""
Registers the markupsafe 'Markup' function as a filter with the name 'markdown'
"""
from mkdocs.plugins import BasePlugin
import markdown
import markupsafe

class MarkupSafeMarkdownFilterPlugin(BasePlugin):

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
        self.config = config
        env.filters['markdown'] = self.md_filter
        return env
