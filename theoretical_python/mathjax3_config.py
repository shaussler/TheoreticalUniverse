def mathjax3_config():

    return {

        'chtml': {
            'displayAlign': 'left',
            'displayIndent': '2em'
        },
    
        'tex': {
           'packages': {'[+]': ['ams']},
           'macros': {
    
                # Define variables
                # ----------------
    
                'Et': r'\tilde{E^{t}}',
                'Ex': r'\tilde{E^{x}}',
                'Ey': r'\tilde{E^{y}}',
                'Ez': r'\tilde{E^{z}}',
    
                'Bt': r'B^{t}',
                'Bx': r'B^{x}',
                'By': r'B^{y}',
                'Bz': r'B^{z}',
    
                # Redefine vectors
                # ----------------
    
                'vect': r'\overrightarrow',
                'av': r'\overrightarrow', # Arrow vector
                'bv': r'\mathbf', # Bold vector
    
                # Redefine matrices
                # -----------------
    
                '{': r'\begin{bmatrix}',
                '}': r'\end{bmatrix}',
    
                # Redefine phantom
                # ----------------
    
                'ph': r'\phantom',
    
                # Define Minkowski Metric components
                # ----------------------------------
    
                'EtatSharp': r'\{+1 \\  0 \\  0 \\  0 \}',
                'EtaxSharp': r'\{ 0 \\ -1 \\  0 \\  0 \}',
                'EtaySharp': r'\{ 0 \\  0 \\ -1 \\  0 \}',
                'EtazSharp': r'\{ 0 \\  0 \\  0 \\ -1 \}',
    
                'EtatFlat': r'\{+1 &  0 &  0 &  0 \}',
                'EtaxFlat': r'\{ 0 & -1 & -1 &  0 \}',
                'EtayFlat': r'\{ 0 &  0 & -1 &  0 \}',
                'EtazFlat': r'\{ 0 &  0 &  0 & -1 \}',
    
                'EtatCol': r'\{+1 \\  0 \\  0 \\  0 \}',
                'EtaxCol': r'\{ 0 \\ -1 \\  0 \\  0 \}',
                'EtayCol': r'\{ 0 \\  0 \\ -1 \\  0 \}',
                'EtazCol': r'\{ 0 \\  0 \\  0 \\ -1 \}',
    
                'EtatRow': r'\{+1 &  0 &  0 &  0 \}',
                'EtaxRow': r'\{ 0 & -1 &  0 &  0 \}',
                'EtayRow': r'\{ 0 &  0 & -1 &  0 \}',
                'EtazRow': r'\{ 0 &  0 &  0 & -1 \}',
    
                'EtaRowRow': r'\{ \EtatRow & \EtaxRow & \EtayRow & \EtazRow \}',
                'EtaColCol': r'\{ \EtatCol \\ \EtaxCol \\ \EtayCol \\ \EtazCol \}',
    
                'EtaSharpSharp': r'''
                    \begin{bmatrix}
                        +1 &  0 &  0 &  0 \\
                         0 & -1 &  0 &  0 \\
                         0 &  0 & -1 &  0 \\
                         0 &  0 &  0 & -1 \\
                    \end{bmatrix}^{\sharp\sharp}
                ''',
    
                'EtaFlatFlat': r'''
                    \begin{bmatrix}
                        +1 &  0 &  0 &  0 \\
                         0 & -1 &  0 &  0 \\
                         0 &  0 & -1 &  0 \\
                         0 &  0 &  0 & -1 \\
                    \end{bmatrix}^{\flat\flat}
                ''',
    
                # Current
                # -------
    
                'CurrentCol': r'''\{
                    \mu_0 c \rho \\
                    \mu_0 J^x    \\
                    \mu_0 J^y    \\
                    \mu_0 J^z    \\
                \}''',
    
                # Define Faraday Tensors
                # ----------------------
    
                'FaradayColCol': r'''\{
                    \{      \\ -\Ex \\ -\Ey \\ -\Ez \} \\
                    \{ +\Ex \\      \\ -\Bz \\ +\By \} \\
                    \{ +\Ey \\ +\Bz \\      \\ -\Bx \} \\
                    \{ +\Ez \\ -\By \\ +\Bx \\      \}
                \}''',
    
                'FaradayRowRow': r'''\{
                    \{   0 , -\Ex, -\Ey, -\Ez \}  &
                    \{ +\Ex,   0 , +\Bz, -\By \} &
                    \{ +\Ey, -\Bz,   0 , +\Bx \} &
                    \{ +\Ez, +\By, -\Bx,   0  \}
                \}''',
    
                # Define Faraday Tensors
                # ----------------------
    
                'FaradaySharpFlat': r'''
                    \begin{bmatrix}
                             & +\Ex & +\Ey & +\Ez \\
                        +\Ex &      & +\Bz & -\By \\
                        +\Ey & -\Bz &      & +\Bx \\
                        +\Ez & +\By & -\Bx &      \\
                    \end{bmatrix}^{\sharp\flat}
                ''',
    
                'FaradayFlatSharp': r'''
                    \begin{bmatrix}
                             & +\Ex & +\Ey & +\Ez \\
                        ?\Ex &      & +\Bz & -\By \\
                        ?\Ey & -\Bz &      & +\Bx \\
                        ?\Ez & +\By & -\Bx &      \\
                    \end{bmatrix}^{\flat\sharp}
                ''',
    
                'FaradaySharpSharp': r'''
                    \begin{bmatrix}
                             & +\Ex & +\Ey & +\Ez \\
                        -\Ex &      & +\Bz & -\By \\
                        -\Ey & -\Bz &      & +\Bx \\
                        -\Ez & +\By & -\Bx &      \\
                    \end{bmatrix}^{\sharp\sharp}
                ''',
    
                'FaradayFlatFlat': r'''
                    \begin{bmatrix}
                             & +\Ex & +\Ey & +\Ez \\
                        -\Ex &      & -\Bz & +\By \\
                        -\Ey & +\Bz &      & -\Bx \\
                        -\Ez & -\By & +\Bx &      \\
                    \end{bmatrix}^{\flat\flat}
                ''',
    
                'FaradayDualSharpFlat': r'''
                    \begin{bmatrix}
                             & +\Bx & +\By & +\Bz \\
                        +\Bx &      & -\Ez & +\Ey \\
                        +\By & +\Ez &      & -\Ex \\
                        +\Bz & -\Ey & +\Ex &      \\
                    \end{bmatrix}^{\sharp\flat}
                ''',
    
            }
        }
    }
