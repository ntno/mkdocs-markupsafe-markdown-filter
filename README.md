# mkdocs-markupsafe-markdown-filter

This plugin adds [pallets' MarkupSafe] template filter to mkdocs.

[pallets' MarkupSafe]: https://github.com/pallets/markupsafe/

## Setup

Install the plugin using pip:

`pip install mkdocs-markupsafe-markdown-filter`

Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - markupsafe-markdown-filter
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. This is because MkDocs enables the `search` plugin by default if there is no `plugins` entry set.  When you add a external plugin like `markupsafe-markdown-filter` you have to enable the `search` plugin explicitly.  

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## Usage

Enabling this plugin will filter jinja template code through a markdown filter:

    {% set code_content %}
    ```php linenums="1"
    <?php
    foo = 1;
    bar = 3;
    if (foo == bar ) {
      // do something 
    }
    ?>
    ```
    {% endset %}
    {{ code_content|markdown }}

## See Also

More information about templates [here][mkdocs-template].

More information about blocks [here][mkdocs-block].

[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables
[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks
