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

Hodge Dual in Minkowski Space
-----------------------------

.. math::

   \star dt = - dx \wedge dy \wedge dz \\
   \star dx = - dt \wedge dy \wedge dz \\
   \star dy = - dt \wedge dz \wedge dx \\
   \star dz = - dt \wedge dx \wedge dy

.. math::

   \star (dt \wedge dx) = - dy \wedge dz \\
   \star (dt \wedge dy) = - dz \wedge dx \\
   \star (dt \wedge dz) = - dx \wedge dy \\
   \star (dx \wedge dy) =   dt \wedge dz \\
   \star (dz \wedge dx) =   dt \wedge dy \\
   \star (dy \wedge dz) =   dt \wedge dx

