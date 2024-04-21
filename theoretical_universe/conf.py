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
    'sphinx.ext.autosectionlabel',
    'sphinx_togglebutton',
    # 'sphinx.ext.imgmath',  # This should allow to create images for epub
]

# imgmath config
# --------------

imgmath_image_format = 'svg'  # This should allow to create images for epub

# epub configuration
# ------------------

epub_title = 'Theoretical Universe'
epub_author = 'Stéphane Haussler'
epub_language = 'en'


# Automated labels labels
# -----------------------

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
    "use_sidenotes": True
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

import theoretical_python

mathjax3_config = theoretical_python.mathjax3_config()

