# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TheoreticalUniverse'
html_title = 'Theoretical Universe'
copyright = '2023, Stéphane Haussler'
author = 'Stéphane Haussler'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    #'sphinxcontrib.tikz',
    'sphinx.ext.todo',
    'sphinxcontrib.googleanalytics',
    'sphinx_sitemap',
    'sphinx.ext.autosectionlabel',
    'sphinx_togglebutton',
]

# Automated labels labels
# -----------------------

autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_css_files = ['custom.css']
html_baseurl = 'https://shaussler.github.io/TheoreticalUniverse/'
html_static_path = ['_static']

# Google analytics
# ----------------

googleanalytics_id="G-9HQ1J8VKRB"
googleanalytics_enabled=True

# Sitemap
# -------

sitemap_locales = []
sitemap_url_scheme = "{link}"

todo_include_todos = True

mathjax3_config = {
    'chtml': {
        'displayAlign': 'left',
         'displayIndent': '2em'
    },
    'tex': {
       'packages': {'[+]': ['ams']},
       'macros': {
            'Et': r'\tilde{E^{t}}',
            'Ex': r'\tilde{E^{x}}',
            'Ey': r'\tilde{E^{y}}',
            'Ez': r'\tilde{E^{z}}',
            'Bt': r'B^{t}',
            'Bx': r'B^{x}',
            'By': r'B^{y}',
            'Bz': r'B^{z}',
            #'BM': r'\begin{bmatrix}',
            #'EM': r'\end{bmatrix}',
            '{': r'\begin{bmatrix}',
            '}': r'\end{bmatrix}',
            'ph': r'\phantom',
            #'etatsharp': r'\BM  1 \\  0 \\  0 \\  0 \EM',
            #'etaxsharp': r'\BM  0 \\ -1 \\ -1 \\  0 \EM',
            #'etaysharp': r'\BM  0 \\  0 \\ -1 \\  0 \EM',
            #'etazsharp': r'\BM  0 \\  0 \\  0 \\ -1 \EM',
            #'etatflat': r'\BM  1 &  0 &  0 &  0 \EM',
            #'etaxflat': r'\BM  0 & -1 & -1 &  0 \EM',
            #'etayflat': r'\BM  0 &  0 & -1 &  0 \EM',
            #'etazflat': r'\BM  0 &  0 &  0 & -1 \EM',
            'EtatSharp': r'\{+1 \\  0 \\  0 \\  0 \}',
            'EtaxSharp': r'\{ 0 \\ -1 \\  0 \\  0 \}',
            'EtaySharp': r'\{ 0 \\  0 \\ -1 \\  0 \}',
            'EtazSharp': r'\{ 0 \\  0 \\  0 \\ -1 \}',
            'EtatFlat': r'\{+1 &  0 &  0 &  0 \}',
            'EtaxFlat': r'\{ 0 & -1 & -1 &  0 \}',
            'EtayFlat': r'\{ 0 &  0 & -1 &  0 \}',
            'EtazFlat': r'\{ 0 &  0 &  0 & -1 \}',
            'EtaSharpSharp': r'''
                \begin{bmatrix}
                    +1 &  0 &  0 &  0 \\
                     0 & -1 &  0 &  0 \\
                     0 &  0 & -1 &  0 \\
                     0 &  0 &  0 & -1 \\
                \end{bmatrix}^{\sharp\flat}''',
            'FaradaySharpFlat': r'''
                \begin{bmatrix}
                         & +\Ex & +\Ey & +\Ez \\
                    +\Ex &      & +\Bz & -\By \\
                    +\Ey & -\Bz &      & +\Bx \\
                    +\Ez & +\By & -\Bx &      \\
                \end{bmatrix}^{\sharp\flat}''',
            'FaradaySharpSharp': r'''
                \begin{bmatrix}
                         & +\Ex & +\Ey & +\Ez \\
                    -\Ex &      & +\Bz & -\By \\
                    -\Ey & -\Bz &      & +\Bx \\
                    -\Ez & +\By & -\Bx &      \\
                \end{bmatrix}^{\sharp\flat}'''
        }
    }
}


