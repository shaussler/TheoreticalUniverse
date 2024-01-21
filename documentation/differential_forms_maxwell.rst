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

Tensor products
---------------

.. math::

   \dtWdx = \dtTdx - \dxTdt

.. math::

   dx^i \wedge dx^j = dx^i \otimes dx^j - dx^j \otimes dx^i

Like does that work?

.. math::

   dx^i \wedge \partial_j = dx^i \otimes \partial_j - \partial_j \otimes dx^i


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

.. rubric:: From Tensor Components Form to Tensor Products Form

.. math::

   \partial_\mu F^\mu{}_\nu = J_\nu \\

.. math::

   \partial_\mu \; \mathbf{e^\mu} \; F^\gamma{}_\nu \; \mathbf{e_\gamma} \otimes \mathbf{e^\nu}
   = J_\nu \; \mathbf{e^\nu}

.. rubric:: Full Explicit Tensor Product Form

.. math::

   \begin{bmatrix}
       \partial_t \eT \\
       \partial_x \eX \\
       \partial_y \eY \\
       \partial_z \eZ \\
   \end{bmatrix}
   \begin{bmatrix}
                   & +\Ex \etTEx & +\Ey \etTEy & +\Ez \etTEz \\
       +\Ex \exTEt &             & +\Bz \exTEy & -\By \exTEz \\
       +\Ey \eyTEt & -\Bz \eyTEx &             & +\Bx \eyTEz \\
       +\Ez \ezTEt & +\By \ezTEx & -\Bx \ezTEy &             \\
   \end{bmatrix}
   =
   \{ + \mu_0 c \rho \; \eT \\
      - \mu_0 J^x    \; \eX \\
      - \mu_0 J^y    \; \eY \\
      - \mu_0 J^z \; \eZ    \}
.. rubric:: From Tensor Components Form to Tensor Products Form

.. math::

   \partial_\mu F^\mu{}_\nu = J_\nu \\

.. math::

   \partial_\mu g^{\alpha\mu} g_{\beta\alpha} F^\beta{}_\nu = J_\nu \\

.. math::

   \partial_\mu \; \mathbf{e^\mu} \; F^\gamma{}_\nu \; \mathbf{e_\gamma} \otimes \mathbf{e^\nu}
   = J_\nu \; \mathbf{e^\nu}

.. rubric:: Full Explicit Tensor Product Form

.. math::

   {\scriptsize
   \begin{bmatrix}
       \partial_t \eT \\
       \partial_x \eX \\
       \partial_y \eY \\
       \partial_z \eZ \\
   \end{bmatrix}
   \begin{bmatrix}
       \et \otimes \et\\
       \ex \otimes \ex\\
       \ey \otimes \ey\\
       \ez \otimes \ez\\
   \end{bmatrix}
   \begin{bmatrix}
       \eT \otimes \eT \\
       \eX \otimes \eX \\
       \eY \otimes \eY \\
       \eZ \otimes \eZ \\
   \end{bmatrix}
   \begin{bmatrix}
                   & +\Ex \etTEx & +\Ey \etTEy & +\Ez \etTEz \\
       +\Ex \exTEt &             & +\Bz \exTEy & -\By \exTEz \\
       +\Ey \eyTEt & -\Bz \eyTEx &             & +\Bx \eyTEz \\
       +\Ez \ezTEt & +\By \ezTEx & -\Bx \ezTEy &             \\
   \end{bmatrix}
   =
   \{ + \mu_0 c \rho \; \eT \\
      - \mu_0 J^x    \; \eX \\
      - \mu_0 J^y    \; \eY \\
      - \mu_0 J^z \; \eZ    \}
   }

.. rubric:: Towards the Wedge Product form

I like that:

.. math::

   {\scriptsize
   \begin{bmatrix}
       \partial_t \eT \\
       \partial_x \eX \\
       \partial_y \eY \\
       \partial_z \eZ \\
   \end{bmatrix}
   \begin{bmatrix}
                                &                         &                         \\
       +\Ex \exTEt + \Ex \etTEx &                         &                         \\
       +\Ey \eyTEt + \Ey \etTEy & +\Bz \exTEy -\Bz \eyTEx &                         \\
       +\Ez \ezTEt + \Ez \etTEz & +\By \ezTEx -\By \exTEz & +\Bx \eyTEz -\Bx \ezTEy \\
   \end{bmatrix}
   =
   \{ + \mu_0 c \rho \; \eT \\
      - \mu_0 J^x    \; \eX \\
      - \mu_0 J^y    \; \eY \\
      - \mu_0 J^z \; \eZ    \}
   }


.. warning:: To be looked at

   Found this post with that very nice form:

   .. math::

      F = E_i \; dt \wedge dx^i - \star B_i \; dt \wedge dx^i

   Where I use Einstein summation convention.

   https://physics.stackexchange.com/questions/86510/maxwells-equations-using-differential-forms

Differential Form Formulation
-----------------------------

.. math::

   \star d \star F = J

Not sure about the sign:

.. math::

   {\small
   J = \star
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


