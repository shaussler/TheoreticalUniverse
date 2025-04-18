# Configuration file for the Sphinx documentation builder
# -------------------------------------------------------

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

def setup(app):
    draft = 'yes' if 'TERMUX_VERSION' in os.environ else 'no'
    app.add_config_value('draft', draft, 'env')

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
    'sphinx_togglebutton',
    'sphinx_reredirects',
    'sphinx.ext.ifconfig',
]

# Redirects
# ---------

redirects = {
    'faraday_tensor_derivation': "faraday_tensor/faraday_tensor_derivation.html",
    'introduction/faraday_tensor_derivation': "../faraday_tensor/faraday_tensor_derivation.html",
    'differential_operators/the_exterior_derivative_of_rotations': 'differential_operators/rotations.html',
    "differential_operators": "differential_operators/differential_operators.html",
    "free_matrix_representation": "the_cartan_hodge_formalism/the_free_matrix_representation.html",
    "differential_rotations": "differential_operators/the_exterior_derivative_of_rotations.html",
}

# include_patterns = [
#     'index.rst',
#     'cite.rst',
#     'contribute.rst',
#     'licence.rst',
#     'resources.rst',
#     'the_cartan_hodge_formalism/index.rst',
#     'the_cartan_hodge_formalism/basis_vectors.rst',
#     'the_cartan_hodge_formalism/hodge_duality.rst',
#     'the_cartan_hodge_formalism/musicality.rst',
#     'the_cartan_hodge_formalism/the_free_matrix_representation.rst',
#     'the_cartan_hodge_formalism/the_minkowski_metric.rst',
#     'differential_operators/index.rst',
#     'differential_operators/differential_operators.rst',
#     'differential_operators/the_exterior_derivative_of_rotations.rst',
#     'rotations/index.rst',
#     'rotations/rotations_in_3_dimensions.rst',
#     'rotations/rotations_in_minkowski_space.rst',
#     'faraday_tensor/index.rst',
#     'faraday_tensor/faraday_tensor_derivation.rst',
#     'faraday_tensor/of_maxwell_equations_and_rotations.rst',
#     'faraday_tensor/all_electromagnetic_field_tensors.rst',
# ]

# Link checks
# -----------

linkcheck_ignore = [
    r'https://www.jstor.org/stable/108892',  # The website seems to refuse linkcheck
]

# Set date format
# ---------------

# This can be used to automatically set the date

today_fmt = '%m-%d-%Y'

# Latex engine
# ------------

latex_engine = 'xelatex'

# epub configuration
# ------------------

epub_title = 'Theoretical Universe'
epub_author = 'Stéphane Haussler'
epub_language = 'en'

# Automated labels
# ----------------

autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]

# Options for HTML output
# -----------------------

html_theme = 'sphinx_book_theme'
html_css_files = ['custom.css']
html_baseurl = 'https://shaussler.github.io/TheoreticalUniverse/'
html_static_path = ['_static']

html_theme_options = {
    "use_sidenotes": False,
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

latex_elements = {
    'preamble': r'''
\usepackage{titling}
\usepackage{graphicx}
\usepackage[utf8]{inputenc}
\usepackage{fontspec}
\usepackage{unicode-math}
\usepackage{braket}

\newcommand{\E}{\tilde{E}}
''',
# 'fontpkg': r'\usepackage{lmodern}',
'papersize': r'a4paper',
'pointsize': '11pt',
# 'maketitle': r'''
#
#  \newcommand{\subtitle}[1]{%
#     \posttitle{
#     \par\end{center}
#     \begin{center}\large#1\end{center}
#     \vskip0.5em
#
#     % \begin{center}
#     %     \includegraphics[width=0.2\textwidth]{
#     %         ../../_static/title_pic.png}
#     %     \par\vspace{1em}
#     % \end{center}
#     }
# }
#
# \title{\Huge Theoretical Universe}
# \subtitle{\huge Maxwell Field Equations via Differential Forms}
# \author{by Stéphane Haussler}
# \date{\today}
#
# \maketitle
# '''
}

mathjax3_config = {
    'chtml': {
        'displayAlign': 'left',
        'displayIndent': '2em'
    },
    'tex': {
       'packages': {'[+]': ['ams']},
       'macros': {
            'E': r'\tilde{E}',
            '⌟': r'\:⌟\:',
        }
    },
    'tex2jax': {
        'ignoreClass': '.*',
        'processClass': 'math|output_area',
    }
}

# Set version and release to current commit
# -----------------------------------------

import subprocess
import os

# Function to get current Git commit hash
def get_current_commit_hash():
    try:
        # Run 'git rev-parse HEAD' command to get the current commit hash
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout.decode('utf-8').strip()
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Get current commit hash
commit_hash = get_current_commit_hash()
commit_hash = commit_hash[:8] if commit_hash else 'unknown'

rst_prolog = f"""
.. |commit_hash| replace:: {commit_hash}
"""

# Update the globals in conf.py
globals().update(locals())
