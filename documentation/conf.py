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
    'sphinxcontrib.tikz',
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

# Math
# ----

# minkowski sharp sharp
# '''''''''''''''''''''

# {{{

etasharpsharp_string = r'''
\begin{bmatrix}
\begin{bmatrix}
           +1 \\
\phantom{+} 0 \\
\phantom{+} 0 \\
\phantom{+} 0 \\
\end{bmatrix} \\
\begin{bmatrix}
\phantom{+} 0 \\
           -1 \\
\phantom{+} 0 \\
\phantom{+} 0 \\
\end{bmatrix} \\
\begin{bmatrix}
\phantom{+} 0 \\
\phantom{+} 0 \\
           -1 \\
\phantom{+} 0 \\
\end{bmatrix} \\
\begin{bmatrix}
\phantom{+} 0 \\
\phantom{+} 0 \\
\phantom{+} 0 \\
           -1 \\
\end{bmatrix}
\end{bmatrix}
'''

etatsharp_string = r'''
\begin{bmatrix}
           +1 \\
\phantom{-} 0 \\
\phantom{-} 0 \\
\phantom{-} 0
\end{bmatrix}
'''

etaxsharp_string = r'''
\begin{bmatrix}
\phantom{+} 0 \\
           -1 \\
\phantom{-} 0 \\
\phantom{-} 0
\end{bmatrix}
'''

etaysharp_string = r'''
\begin{bmatrix}
\phantom{+} 0 \\
\phantom{-} 0 \\
           -1 \\
\phantom{-} 0
\end{bmatrix}
'''

etazsharp_string = r'''
\begin{bmatrix}
\phantom{+} 0 \\
\phantom{-} 0 \\
\phantom{-} 0 \\
           -1
\end{bmatrix}
'''

# }}}

# Minkowski flat flat
# '''''''''''''''''''

# {{{

etaflatflat_string = r'''
\begin{bmatrix}
\begin{bmatrix}
           +1 &
            0 &
            0 &
            0 &
\end{bmatrix} 
\begin{bmatrix}
            0 &
           -1 &
            0 &
            0 &
\end{bmatrix} 
\begin{bmatrix}
            0 &
            0 &
           -1 &
            0 &
\end{bmatrix} 
\begin{bmatrix}
            0 &
            0 &
            0 &
           -1 &
\end{bmatrix}
\end{bmatrix}
'''

etatflat_string = r'''
\begin{bmatrix}
           +1 & 
            0 &
            0 &
            0 
\end{bmatrix}
'''

etaxflat_string = r'''
\begin{bmatrix}
            0 &
           -1 &
            0 &
            0
\end{bmatrix}
'''

etayflat_string = r'''
\begin{bmatrix}
            0 &
            0 &
           -1 &
            0
\end{bmatrix}
'''

etazflat_string = r'''
\begin{bmatrix}
            0 &
            0 &
            0 &
           -1
\end{bmatrix}
'''

# }}}

mathjax3_config = {
    'chtml': {
        'displayAlign': 'left',
         'displayIndent': '2em'
    },
    'tex': {
       'packages': {'[+]': ['ams']},
       'macros': {
            'etasharpsharp': etasharpsharp_string,
            'etatsharp': etatsharp_string,
            'etaxsharp': etaxsharp_string,
            'etaysharp': etaysharp_string,
            'etazsharp': etazsharp_string,
            'etaflatflat': etaflatflat_string,
            'etatflat': etatflat_string,
            'etaxflat': etaxflat_string,
            'etayflat': etayflat_string,
            'etazflat': etazflat_string,
        }
    }
}


