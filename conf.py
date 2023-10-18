# Project Setup
project = 'RTD Example'
copyright = '2023, Will Won'
author = 'Will Won'

# Version of documentation
version = '1.0'
release = version

# Sphinx Setup: Extension and theme
extensions = ['myst_parser',
              'sphinx_rtd_theme',
              'sphinx_multiversion']
myst_enable_extensions = ['colon_fence']
html_theme = 'sphinx_rtd_theme'

# Sphinx Setup: Paths
templates_path = ['_templates']
exclude_patterns = ['_build', '.DS_Store', 'README.md']
html_static_path = ['_static']
