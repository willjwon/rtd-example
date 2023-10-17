project = 'RTD Example'
copyright = '2023, Will Won'
author = 'Will Won'

extensions = ['myst_parser',
              'sphinx_rtd_theme'
             ]

myst_enable_extensions = ['colon_fence']

templates_path = ['_templates']

exclude_patterns = ['_build', '.DS_Store']

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static', 'README.md']
