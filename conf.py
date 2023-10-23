# Project Setup
project = 'RTD Example'
copyright = '2023, Will Won'
author = 'Will Won'

# Version of documentation
version = '2.0'
release = version

# Sphinx Setup: Initialization
html_context = dict()

# Sphinx Setup: Extension and theme
extensions = ['myst_parser',
              'sphinx_rtd_theme']
myst_enable_extensions = ['colon_fence']
html_theme = 'sphinx_rtd_theme'

# Sphinx Setup: Paths
templates_path = ['_templates']
exclude_patterns = ['_build', '.DS_Store', 'README.md']
html_static_path = ['_static']

# Sphinx Setup: Versioning
from git import Repo
repo = Repo()
versions = [tag.name for tag in repo.tags]
versions.append('latest')

html_context['versions'] = list()
for version in versions:
    if version == 'latest':
        link = f''
    else:
        link = f'{version}/'
    version_value = (version, link)
    html_context['versions'].append(version_value)
