"""
This module provides a plugin that can be used to make untrusted text
ready to insert into HTML either by escaping special characters
or by marking the text as safe.

See markupsafe for details: https://github.com/pallets/markupsafe
"""
import markdown
import markupsafe
import jinja2.environment
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.config.defaults import MkDocsConfig

class MarkupSafeMarkdownFilterPlugin(BasePlugin):
    """
    Registers the markupsafe 'Markup' function as a Jinja filter with the name 'markdown'
    """

    config_scheme = (
    )

    def __init__(self):
        self.enabled = True
        self.dirs = []

    def md_filter(self, text):
        """
        Converts the given text to a "safe" string
        taking into account the currently enabled markdown extensions.
        """
        md = markdown.Markdown(
            extensions=self.config['markdown_extensions'],
            extension_configs=self.config['mdx_configs'] or {}
        )
        return markupsafe.Markup(md.convert(text))

    def on_env(
        self, env: jinja2.Environment, /, *, config: MkDocsConfig, files: Files
    ) -> jinja2.Environment | None:
        """
        The `env` event is called after the Jinja template environment is created
        and can be used to alter the
        [Jinja environment](https://jinja.palletsprojects.com/en/latest/api/#jinja2.Environment).

        Args:
            env: global Jinja environment
            config: global configuration object
            files: global files collection

        Returns:
            global Jinja Environment
        """
        self.config = config
        env.filters['markdown'] = self.md_filter
        return env
