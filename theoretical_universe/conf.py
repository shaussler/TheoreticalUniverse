# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project information
# -------------------

project = 'TheoreticalUniverse'
html_title = 'Theoretical Universe'
copyright = '2024, Stéphane Haussler'
author = 'Stéphane Haussler'
version = '0.1'

# General configuration
# ---------------------

extensions = [
    'sphinx.ext.todo',
    'sphinxcontrib.googleanalytics',
    'sphinx_sitemap',
    # 'sphinx.ext.autosectionlabel',
    'sphinx_togglebutton',
    'sphinx_reredirects',
    # 'sphinx.ext.imgmath',  # epub
    # 'sphinx.ext.mathjax',  # epub
    # 'sphinx.ext.ifconfig',  # epub
]

# source_encoding = 'utf-8'

# Redirects
# ---------

redirects = {
    'faraday_tensor_derivation': "faraday_tensor/faraday_tensor_derivation.html",
    'introduction/faraday_tensor_derivation': "../faraday_tensor/faraday_tensor_derivation.html",
    "differential_operators": "differential_operators/differential_operators.html",
    "free_matrix_representation": "the_cartan_hodge_formalism/the_free_matrix_representation.html",
    "differential_rotations": "differential_operators/the_exterior_derivative_of_rotations.html",
}

# imgmath config
# --------------

# imgmath_image_format = 'png'  # This should allow to create images for epub
# imgmath_font_size = 12  # Set the font size of the equations
# imgmath_dvipng_args = ['-gamma', '1.5', '-D', '110', '-bg', 'Transparent']
# imgmath_latex = 'latex'

latex_engine = 'xelatex'

# latex_elements = {
#     'preamble': r'''
# \usepackage{amsmath}
# \usepackage[T1]{fontenc}
# \usepackage[utf8]{inputenc}
# \newcommand{\E}{\tilde{E}}
# ''',
#     'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
#     'printindex': r'\footnotesize\raggedright\printindex',
# }

# latex_show_urls = 'footnote'

# epub configuration
# ------------------

epub_title = 'Theoretical Universe'
epub_author = 'Stéphane Haussler'
epub_language = 'en'

# Automated labels
# ----------------

autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Options for HTML output
# -----------------------

html_theme = 'sphinx_book_theme'
html_css_files = ['custom.css']
html_baseurl = 'https://shaussler.github.io/TheoreticalUniverse/'
html_static_path = ['_static']

html_theme_options = {
    "use_sidenotes": True,
    "navigation_with_keys": False,
}

# Google analytics
# ----------------

googleanalytics_id="G-9HQ1J8VKRB"
googleanalytics_enabled=True

# Sitemap
# -------

sitemap_locales = []
sitemap_url_scheme = "{link}"

# Include todos
# -------------

todo_include_todos = True

# Math configuration
# ------------------

mathjax3_config = {
    'chtml': {
        'displayAlign': 'left',
        'displayIndent': '2em'
    },
    'tex': {
       'packages': {'[+]': ['ams']},
       'macros': {
            'E': r'\tilde{E}',
        }
    },
    'tex2jax': {
        'ignoreClass': '.*',
        'processClass': 'math|output_area',
    }
}

