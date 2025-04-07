from setuptools import setup, find_packages


setup(
    name='mkdocs-markupsafe-markdown-filter',
    version='0.0.0',
    description='A MkDocs plugin to add a markdown filter to jinja templates.',
    long_description='',
    keywords='mkdocs jinja',
    url='https://github.com/ntno/mkdocs-markupsafe-markdown-filter',
    author='Byrne Reese, Oliver Stueker, Natan Organick', 
    author_email='mkdocs.terminal@gmail.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'markupsafe-markdown-filter = mkdocs_markupsafe_markdown_filter.plugin:MarkupSafeMarkdownFilterPlugin'
        ]
    }
)
