def mathjax3_config():

    return {

        'chtml': {
            'displayAlign': 'left',
            'displayIndent': '2em'
        },

        'tex': {
           'packages': {'[+]': ['ams']},
           'macros': {

                'et': r'\mathbf{e_t}',

                # Redefine vectors
                # ----------------

                'vect': r'\overrightarrow',

                # Redefine matrices
                # -----------------

                '{': r'\begin{bmatrix}',
                '}': r'\end{bmatrix}',

            }
        }
    }
