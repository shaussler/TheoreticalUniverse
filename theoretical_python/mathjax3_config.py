def mathjax3_config():

    return {

        'chtml': {
            'displayAlign': 'left',
            'displayIndent': '2em'
        },
    
        'tex': {
           'packages': {'[+]': ['ams']},
           'macros': {
    
                # Define Components and a phantom
                # -------------------------------
    
                'Et': r'\tilde{E^{t}}',
                'Ex': r'\tilde{E^{x}}',
                'Ey': r'\tilde{E^{y}}',
                'Ez': r'\tilde{E^{z}}',
    
                'Bt': r'B^{t}',
                'Bx': r'B^{x}',
                'By': r'B^{y}',
                'Bz': r'B^{z}',
    
                'Pp': r'\phantom{P^{p}}',
                'sPp': r'\phantom{+P^{p}}',

                # Basis vectors
                # -------------

                'pt': r'\; \partial_t',
                'px': r'\; \partial_x',
                'py': r'\; \partial_y',
                'pz': r'\; \partial_z',

                # Wedge products
                # --------------
    
                'dtWdt': r'\; dt \wedge dt',
                'dxWdt': r'\; dx \wedge dt',
                'dyWdt': r'\; dy \wedge dt',
                'dzWdt': r'\; dz \wedge dt',

                'dtWdx': r'\; dt \wedge dx',
                'dxWdx': r'\; dx \wedge dx',
                'dyWdx': r'\; dy \wedge dx',
                'dzWdx': r'\; dz \wedge dx',

                'dtWdy': r'\; dt \wedge dy',
                'dxWdy': r'\; dx \wedge dy',
                'dyWdy': r'\; dy \wedge dy',
                'dzWdy': r'\; dz \wedge dy',

                'dtWdz': r'\; dt \wedge dz',
                'dxWdz': r'\; dx \wedge dz',
                'dyWdz': r'\; dy \wedge dz',
                'dzWdz': r'\; dz \wedge dz',

                # Wedge products
                # --------------
    
                'dtWpt': r'\; dt \wedge \partial_t',
                'dxWpt': r'\; dx \wedge \partial_t',
                'dyWpt': r'\; dy \wedge \partial_t',
                'dzWpt': r'\; dz \wedge \partial_t',

                'dtWpx': r'\; dt \wedge \partial_x',
                'dxWpx': r'\; dx \wedge \partial_x',
                'dyWpx': r'\; dy \wedge \partial_x',
                'dzWpx': r'\; dz \wedge \partial_x',

                'dtWpy': r'\; dt \wedge \partial_y',
                'dxWpy': r'\; dx \wedge \partial_y',
                'dyWpy': r'\; dy \wedge \partial_y',
                'dzWpy': r'\; dz \wedge \partial_y',

                'dtWpz': r'\; dt \wedge \partial_z',
                'dxWpz': r'\; dx \wedge \partial_z',
                'dyWpz': r'\; dy \wedge \partial_z',
                'dzWpz': r'\; dz \wedge \partial_z',
    
                # Wedge products
                # --------------

                'ptWdt': r'\; \partial_t \wedge dt',
                'pxWdt': r'\; \partial_x \wedge dt',
                'pyWdt': r'\; \partial_y \wedge dt',
                'pzWdt': r'\; \partial_z \wedge dt',

                'ptWdx': r'\; \partial_t \wedge dx',
                'pxWdx': r'\; \partial_x \wedge dx',
                'pyWdx': r'\; \partial_y \wedge dx',
                'pzWdx': r'\; \partial_z \wedge dx',

                'ptWdy': r'\; \partial_t \wedge dy',
                'pxWdy': r'\; \partial_x \wedge dy',
                'pyWdy': r'\; \partial_y \wedge dy',
                'pzWdy': r'\; \partial_z \wedge dy',

                'ptWdz': r'\; \partial_t \wedge dy',
                'pxWdz': r'\; \partial_x \wedge dz',
                'pyWdz': r'\; \partial_y \wedge dz',
                'pzWdz': r'\; \partial_z \wedge dz',

                # Basis vectors
                # -------------
    
                'et': r'\mathbf{e_t}',
                'ex': r'\mathbf{e_x}',
                'ey': r'\mathbf{e_y}',
                'ez': r'\mathbf{e_z}',

                'eT': r'\mathbf{e^t}',
                'eX': r'\mathbf{e^x}',
                'eY': r'\mathbf{e^y}',
                'eZ': r'\mathbf{e^z}',

                # Tensor products
                # ---------------
    
                'etTEt': r'\; \mathbf{e_t} \otimes \mathbf{e^t}',
                'exTEt': r'\; \mathbf{e_x} \otimes \mathbf{e^t}',
                'eyTEt': r'\; \mathbf{e_y} \otimes \mathbf{e^t}',
                'ezTEt': r'\; \mathbf{e_z} \otimes \mathbf{e^t}',
                'etTEx': r'\; \mathbf{e_t} \otimes \mathbf{e^x}',
                'exTEx': r'\; \mathbf{e_x} \otimes \mathbf{e^x}',
                'eyTEx': r'\; \mathbf{e_y} \otimes \mathbf{e^x}',
                'ezTEx': r'\; \mathbf{e_z} \otimes \mathbf{e^x}',
                'etTEy': r'\; \mathbf{e_t} \otimes \mathbf{e^y}',
                'exTEy': r'\; \mathbf{e_x} \otimes \mathbf{e^y}',
                'eyTEy': r'\; \mathbf{e_y} \otimes \mathbf{e^y}',
                'ezTEy': r'\; \mathbf{e_z} \otimes \mathbf{e^y}',
                'etTEz': r'\; \mathbf{e_t} \otimes \mathbf{e^z}',
                'exTEz': r'\; \mathbf{e_x} \otimes \mathbf{e^z}',
                'eyTEz': r'\; \mathbf{e_y} \otimes \mathbf{e^z}',
                'ezTEz': r'\; \mathbf{e_z} \otimes \mathbf{e^z}',

                # Tensor products
                # ---------------
    
                'dtTdt': r'\; dt \otimes dt',
                'dxTdt': r'\; dx \otimes dt',
                'dyTdt': r'\; dy \otimes dt',
                'dzTdt': r'\; dz \otimes dt',
                'dtTdx': r'\; dt \otimes dx',
                'dxTdx': r'\; dx \otimes dx',
                'dyTdx': r'\; dy \otimes dx',
                'dzTdx': r'\; dz \otimes dx',
                'dtTdy': r'\; dt \otimes dy',
                'dxTdy': r'\; dx \otimes dy',
                'dyTdy': r'\; dy \otimes dy',
                'dzTdy': r'\; dz \otimes dy',
                'dtTdz': r'\; dt \otimes dz',
                'dxTdz': r'\; dx \otimes dz',
                'dyTdz': r'\; dy \otimes dz',
                'dzTdz': r'\; dz \otimes dz',

                # Tensor products
                # ---------------
    
                'ptTpt': r'\partial_t \otimes \partial_t',
                'pxTpt': r'\partial_x \otimes \partial_t',
                'pyTpt': r'\partial_y \otimes \partial_t',
                'pzTpt': r'\partial_z \otimes \partial_t',
                'ptTpx': r'\partial_t \otimes \partial_x',
                'pxTpx': r'\partial_x \otimes \partial_x',
                'pyTpx': r'\partial_y \otimes \partial_x',
                'pzTpx': r'\partial_z \otimes \partial_x',
                'ptTpy': r'\partial_t \otimes \partial_y',
                'pxTpy': r'\partial_x \otimes \partial_y',
                'pyTpy': r'\partial_y \otimes \partial_y',
                'pzTpy': r'\partial_z \otimes \partial_y',
                'ptTpz': r'\partial_t \otimes \partial_z',
                'pxTpz': r'\partial_x \otimes \partial_z',
                'pyTpz': r'\partial_y \otimes \partial_z',
                'pzTpz': r'\partial_z \otimes \partial_z',

                # Tensor products
                # ---------------
    
                'dtTpt': r'\; dt \otimes \partial_t',
                'dxTpt': r'\; dx \otimes \partial_t',
                'dyTpt': r'\; dy \otimes \partial_t',
                'dzTpt': r'\; dz \otimes \partial_t',

                'dtTpx': r'\; dt \otimes \partial_x',
                'dxTpx': r'\; dx \otimes \partial_x',
                'dyTpx': r'\; dy \otimes \partial_x',
                'dzTpx': r'\; dz \otimes \partial_x',

                'dtTpy': r'\; dt \otimes \partial_y',
                'dxTpy': r'\; dx \otimes \partial_y',
                'dyTpy': r'\; dy \otimes \partial_y',
                'dzTpy': r'\; dz \otimes \partial_y',

                'dtTpz': r'\; dt \otimes \partial_z',
                'dxTpz': r'\; dx \otimes \partial_z',
                'dyTpz': r'\; dy \otimes \partial_z',
                'dzTpz': r'\; dz \otimes \partial_z',

                # Tensor products
                # ---------------

                'ptTdt': r'\; \partial_t \otimes dt',
                'pxTdt': r'\; \partial_x \otimes dt',
                'pyTdt': r'\; \partial_y \otimes dt',
                'pzTdt': r'\; \partial_z \otimes dt',

                'ptTdx': r'\; \partial_t \otimes dx',
                'pxTdx': r'\; \partial_x \otimes dx',
                'pyTdx': r'\; \partial_y \otimes dx',
                'pzTdx': r'\; \partial_z \otimes dx',

                'ptTdy': r'\; \partial_t \otimes dy',
                'pxTdy': r'\; \partial_x \otimes dy',
                'pyTdy': r'\; \partial_y \otimes dy',
                'pzTdy': r'\; \partial_z \otimes dy',

                'ptTdz': r'\; \partial_t \otimes dy',
                'pxTdz': r'\; \partial_x \otimes dz',
                'pyTdz': r'\; \partial_y \otimes dz',
                'pzTdz': r'\; \partial_z \otimes dz',

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
                        +\Ex &      & +\Bz & -\By \\
                        +\Ey & -\Bz &      & +\Bx \\
                        +\Ez & +\By & -\Bx &      \\
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
