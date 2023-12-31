Differential Form Of Maxwell Equations
======================================

Wedge products
--------------

.. math::

   \star d_t \wedge d_x = -d_y \wedge d_z \\
   \star d_t \wedge d_y = -d_z \wedge d_x \\
   \star d_t \wedge d_z = -d_x \wedge d_y

.. math::

   \star d_y \wedge d_z = d_t \wedge d_x \\
   \star d_z \wedge d_x = d_t \wedge d_y \\
   \star d_x \wedge d_y = d_t \wedge d_z

Maxwell 1865 Equations
----------------------

.. math::

   {\small
   \begin{matrix}
                     & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
     +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x    \\
     +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y    \\
     +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z
   \end{matrix}
   }

.. math::

   {\small
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
   }

Differential Form Formulation
-----------------------------

.. math::

   \star d \star F = J

Not sure about the sign:

.. math::

   {\small
   J =
   \{ +\mu_0 c \rho \; dx \wedge dy \wedge dz \\
      -\mu_0 J^x    \; dt \wedge dy \wedge dz \\
      -\mu_0 J^y    \; dt \wedge dz \wedge dx \\
      -\mu_0 J^z    \; dt \wedge dx \wedge dy \}
   }

.. math::

   {\small
   J =
   \{ +\mu_0 c \rho \; dt\\
      -\mu_0 J^x    \; dx\\
      -\mu_0 J^y    \; dy\\
      -\mu_0 J^z    \; dz\}
   }

.. math::

   \begin{align}
   F = & \Ex dx \wedge dt + \\
       & \Ey dy \wedge dt + \\
       & \Ez dz \wedge dt + \\
       & \Bx dy \wedge dz + \\
       & \By dz \wedge dx + \\
       & \Bz dx \wedge dy
   \end{align}

.. math::

   \begin{align}
   dF = & (\partial_y \; dy + \partial_z \; dz) \; \Ex \; dx \wedge dt + \\
        & (\partial_x \; dx + \partial_z \; dz) \; \Ey \; dy \wedge dt + \\
        & (\partial_x \; dx + \partial_y \; dz) \; \Ez \; dz \wedge dt + \\
        & (\partial_t \; dt + \partial_x \; dx) \; \Bx \; dy \wedge dz + \\
        & (\partial_t \; dt + \partial_y \; dy) \; \By \; dz \wedge dx + \\
        & (\partial_t \; dt + \partial_z \; dz) \; \Bz \; dx \wedge dy
   \end{align}


My matrix

.. math::

   {\small
   \{             & dt \wedge dx & dt \wedge dy & dt \wedge dz \\
     dx \wedge dt &              & dx \wedge dy & dx \wedge dz \\
     dy \wedge dt & dy \wedge dx &              & dy \wedge dz \\
     dz \wedge dt & dz \wedge dx & dz \wedge dy &              \}
   }

My matrix

.. math::

   {\small
   F=
   \{                     & -\Ex \; dt \wedge dx & -\Ey \; dt \wedge dy & -\Ez \; dt \wedge dz \\
     +\Ex \; dx \wedge dt &                      & +\Bz \; dx \wedge dy & -\By \; dx \wedge dz \\
     +\Ey \; dy \wedge dt & -\Bz \; dy \wedge dx &                      & +\Bx \; dy \wedge dz \\
     +\Ez \; dz \wedge dt & +\By \; dz \wedge dx & -\Bx \; dz \wedge dy &                   \}
   }


