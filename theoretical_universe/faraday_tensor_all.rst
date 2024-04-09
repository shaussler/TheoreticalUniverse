All Faraday Tensors
===================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

In this article, I derive the Maxwell equations in the frame of Cartan's
formalism and derive all Faraday tensors.

The inhomogenous equations
--------------------------

Her we concentrate on the inhomogenous equations. In a previous article, we
have derived from the 1865 Maxell equations the following relations. 

.. math::

   \begin{matrix}
                       & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho  \\
       +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x     \\
       +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y     \\
       +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z
   \end{matrix}

Wich were then written in the following matrix form.

.. math::

   \begin{bmatrix}
       \partial_t & \partial_x & \partial_y & \partial_z \\
   \end{bmatrix}
   \begin{bmatrix}
            & +\Ex & +\Ey & +\Ez \\
       +\Ex &      & +\Bz & -\By \\
       +\Ey & -\Bz &      & +\Bx \\
       +\Ez & +\By & -\Bx &      \\
   \end{bmatrix}
   =
   \begin{bmatrix}
       + \mu_0 c \rho & - \mu_0 J^x  & - \mu_0 J^y  & - \mu_0 J^z \\
   \end{bmatrix}

From there, we had deduced the tensor formulation in Abstract Index Notation.

Rotation
--------

.. math::

   \begin{equation}
   B^{♯♯}
   = \begin{bmatrix}
     a \; ∂_t ∧ ∂_x \\
     b \; ∂_t ∧ ∂_y \\
     c \; ∂_t ∧ ∂_z \\
     d \; ∂_x ∧ ∂_y \\
     e \; ∂_y ∧ ∂_z \\
     f \; ∂_z ∧ ∂_x \\
   \end{bmatrix}
   \end{equation}

.. math::

   \begin{align}
   (B^{♯♯})^{♭♭}
   &= \begin{bmatrix}
     a \; ∂_t^♭ ∧ ∂_x^♭ \\
     b \; ∂_t^♭ ∧ ∂_y^♭ \\
     c \; ∂_t^♭ ∧ ∂_z^♭ \\
     d \; ∂_x^♭ ∧ ∂_y^♭ \\
     e \; ∂_y^♭ ∧ ∂_z^♭ \\
     f \; ∂_z^♭ ∧ ∂_x^♭ \\
   \end{bmatrix}
   = \begin{bmatrix}
     a \; η_{αt} \; dx^t ∧ η_{βx} \; dx^x \\
     b \; η_{αt} \; dx^t ∧ η_{βy} \; dx^y \\
     c \; η_{αt} \; dx^t ∧ η_{βz} \; dx^z \\
     d \; η_{αx} \; dx^x ∧ η_{βy} \; dx^y \\
     e \; η_{αy} \; dx^y ∧ η_{βz} \; dx^z \\
     f \; η_{αz} \; dx^z ∧ η_{βx} \; dx^x \\
   \end{bmatrix}
   = \begin{bmatrix}
     a \; η_{tt} \; dx^t ∧ η_{xx} \; dx^x \\
     b \; η_{tt} \; dx^t ∧ η_{yy} \; dx^y \\
     c \; η_{tt} \; dx^t ∧ η_{zz} \; dx^z \\
     d \; η_{xx} \; dx^x ∧ η_{yy} \; dx^y \\
     e \; η_{yy} \; dx^y ∧ η_{zz} \; dx^z \\
     f \; η_{zz} \; dx^z ∧ η_{xx} \; dx^x \\
   \end{bmatrix}
   \\&= \begin{bmatrix}
     a \; (+1) \; dx^t ∧ (-1) \; dx^x \\
     b \; (+1) \; dx^t ∧ (-1) \; dx^y \\
     c \; (+1) \; dx^t ∧ (-1) \; dx^z \\
     d \; (-1) \; dx^x ∧ (-1) \; dx^y \\
     e \; (-1) \; dx^y ∧ (-1) \; dx^z \\
     f \; (-1) \; dx^z ∧ (-1) \; dx^x \\
   \end{bmatrix}
   = \begin{bmatrix}
     - a \; dx^t ∧ dx^x \\
     - b \; dx^t ∧ dx^y \\
     - c \; dx^t ∧ dx^z \\
     + d \; dx^x ∧ dx^y \\
     + e \; dx^y ∧ dx^z \\
     + f \; dx^z ∧ dx^x \\
   \end{bmatrix}
   \end{align}


Redefining/reordering the terms:

.. math::

   R = \begin{bmatrix}
     -a \; dx^t ∧ dx^x \\
     -b \; dx^t ∧ dx^y \\
     -c \; dx^t ∧ dx^z \\
      d \; dx^y ∧ dx^z \\
      e \; dx^z ∧ dx^x \\
      f \; dx^x ∧ dx^y \\
   \end{bmatrix}

.. math::

   dR = \begin{bmatrix}
     (∂_y (-a) dx^y ∧ dx^t ∧ dx^x+ ∂_z (-a) dx^z ∧ dx^t ∧ dx^x) \\
     (∂_x (-b) dx^x ∧ dx^t ∧ dx^y+ ∂_z (-b) dx^z ∧ dx^t ∧ dx^y) \\
     (∂_x (-c) dx^x ∧ dx^t ∧ dx^z+ ∂_y (-c) dx^y ∧ dx^t ∧ dx^z) \\
     (∂_t (+d) dx^t ∧ dx^y ∧ dx^z+ ∂_x (+d) dx^x ∧ dx^y ∧ dx^z) \\
     (∂_t (+e) dx^t ∧ dx^z ∧ dx^x+ ∂_y (+e) dx^y ∧ dx^z ∧ dx^x) \\
     (∂_t (+f) dx^t ∧ dx^x ∧ dx^y+ ∂_z (+f) dx^z ∧ dx^x ∧ dx^y) \\
   \end{bmatrix}

.. math::

   dR = \begin{bmatrix}
     ∂_y (-a) dx^t ∧ dx^x ∧ dx^y + ∂_z (-a) dx^t ∧ dx^x ∧ dx^z \\
     ∂_x (+b) dx^t ∧ dx^x ∧ dx^y + ∂_z (-b) dx^t ∧ dx^y ∧ dx^z \\
     ∂_x (+c) dx^t ∧ dx^x ∧ dx^z + ∂_y (+c) dx^t ∧ dx^y ∧ dx^z \\
     ∂_t (+d) dx^t ∧ dx^y ∧ dx^z + ∂_x (+d) dx^x ∧ dx^y ∧ dx^z \\
     ∂_t (-e) dx^t ∧ dx^x ∧ dx^z + ∂_y (+e) dx^x ∧ dx^y ∧ dx^z \\
     ∂_t (+f) dx^t ∧ dx^x ∧ dx^y + ∂_z (+f) dx^x ∧ dx^y ∧ dx^z \\
   \end{bmatrix}

.. math::

   dR = \begin{bmatrix}
   ∂_y (-a) dx^t ∧ dx^x ∧ dx^y + ∂_x (+b) dx^t ∧ dx^x ∧ dx^y + ∂_t (+f) dx^t ∧ dx^x ∧ dx^y \\
   ∂_x (-c) dx^t ∧ dx^x ∧ dx^z + ∂_z (+a) dx^t ∧ dx^x ∧ dx^z + ∂_t (+e) dx^t ∧ dx^z ∧ dx^x \\
   ∂_z (-b) dx^t ∧ dx^y ∧ dx^z + ∂_y (+c) dx^t ∧ dx^y ∧ dx^z + ∂_t (+d) dx^t ∧ dx^y ∧ dx^z \\
   ∂_x (+d) dx^x ∧ dx^y ∧ dx^z + ∂_y (+e) dx^x ∧ dx^y ∧ dx^z + ∂_z (+f) dx^x ∧ dx^y ∧ dx^z \\
   \end{bmatrix}

.. math::

   dR = \begin{bmatrix}
            & + ∂_x d & + ∂_y e & + ∂_z f & dt \\
   + ∂_t d  &         & + ∂_y c & - ∂_z b & dx \\
   + ∂_t e  & - ∂_x c &         & + ∂_z a & dy \\
   + ∂_t f  & + ∂_x b & - ∂_y a &         & dz \\
   \end{bmatrix}

