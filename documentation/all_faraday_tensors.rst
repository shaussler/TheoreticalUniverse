All Faraday Tensors
===================

.. rst-class:: custom-author

   by Stéphane Haussler

In a :ref:`previous article <faraday_tensor_derivation:Deriving the Faraday
Tensor from the 1865 Maxwell Equations>`, I derive the Faraday tensor and its
Hodge dual from the 1865 Maxwell equations. I also introduce a :ref:`musical
notation <musical_notation:The Musical Tensor Notation>` to facilitate
calculations. In this article, I systematically derive all variations of the
electromagnetic field tensor.

Rewriting
---------

.. admonition:: Preliminary

   .. math::

      \star \bv{e_t} \wedge \bv{e_x} = -\bv{e_y} \wedge \bv{e_z} \\
      \star \bv{e_t} \wedge \bv{e_y} = -\bv{e_z} \wedge \bv{e_x} \\
      \star \bv{e_t} \wedge \bv{e_z} = -\bv{e_x} \wedge \bv{e_y}

   .. math::

      \star \bv{e_y} \wedge \bv{e_z} = \bv{e_t} \wedge \bv{e_x} \\
      \star \bv{e_z} \wedge \bv{e_x} = \bv{e_t} \wedge \bv{e_y} \\
      \star \bv{e_x} \wedge \bv{e_y} = \bv{e_t} \wedge \bv{e_z}

   .. math::

      \begin{matrix}
                        & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
        +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x    \\
        +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y    \\
        +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z
      \end{matrix}

   .. math::

      \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \}^{\flat}
      \{                      & +\Ex \; dt \wedge dx & +\Ey \; dt \wedge dy & +\Ez \; dt \wedge dz \\
         +\Ex \; dx \wedge dt &                      & -\Bz \; dx \wedge dy & -\By \; dx \wedge dz \\
         +\Ey \; dy \wedge dt & -\Bz \; dy \wedge dx &                      & +\Bx \; dy \wedge dz \\
         +\Ez \; dz \wedge dt & -\By \; dz \wedge dx & +\Bx \; dz \wedge dy &                      \}
      =
      \{ +\mu_0 c \rho \\ -\mu_0 J^x \\ -\mu_0 J^y \\ -\mu_0 J^z \}^{\flat}

Inhomogenous equations
----------------------

Contravariant-covariant
'''''''''''''''''''''''

.. {{{

The starting point is the :ref:`contravariant/covariant form
<faraday_tensor_derivation:The Tensor of Mr. Faraday>`. From there, I
systematically apply the :ref:`Minkowski metric <minkowski_metric:The Minkowski
Metric>` to obtain the other forms. The electromagnetic field tensor is:

.. math::

   F^{\sharp\flat} = \FaradaySharpFlat

.. }}}

Contravariant-contravariant
'''''''''''''''''''''''''''

.. {{{

.. math::

   {\small
       F^{\sharp\sharp} = F^{\sharp\flat} \eta^{\sharp\sharp}
                        = \FaradaySharpFlat \EtaSharpSharp
                        = \FaradaySharpSharp
   }

.. admonition:: Step by step
   :class: dropdown

   .. math::

      {\scriptsize
          F^{\sharp\sharp}
          =
          \FaradaySharpSharp
          \{ \EtatSharp \\ \EtaxSharp \\ \EtaySharp \\ \EtazSharp \}
          =
          \begin{bmatrix}
              \begin{alignat}{1}
                0  & \EtatSharp &+\Ex & \EtaxSharp & +Ey & \EtaySharp &+\Ez & \EtazSharp \\
              +\Ex & \EtatSharp &  0  & \EtaxSharp & +Bz & \EtaySharp &-\By & \EtazSharp \\
              +\Ey & \EtatSharp &-\Bz & \EtaxSharp &  0  & \EtaySharp &+\Bx & \EtazSharp \\
              +\Ez & \EtatSharp &+\By & \EtaxSharp & -Bx & \EtaySharp &  0  & \EtazSharp
              \end{alignat}
          \end{bmatrix}
      }

   .. math::

      {\scriptsize
      F^{\sharp\sharp}
      =
      \begin{bmatrix}
          \{      \\ -\Ex \\ -\Ey \\ -\Ez \\ \} \\
          \{ +\Ex \\      \\ -\Bz \\ +\By \\ \} \\
          \{ +\Ey \\ +\Bz \\      \\ -\Bx \\ \} \\
          \{ +\Ez \\ -\By \\ +\Bx \\      \\ \}
      \end{bmatrix}
      =
      \FaradaySharpSharp
      }

.. note::

   .. include:: ./musical_notation_notable_difference.rst

.. }}}

Covariant-covariant
'''''''''''''''''''

.. {{{

.. math::
 
   {\small
       F^{\flat\flat}
       = \eta{\flat\flat} F^{\sharp\flat}
       = \EtaFlatFlat \FaradaySharpFlat
       = \FaradayFlatFlat
   }

.. admonition:: Step by step
   :class: dropdown

   .. math::

      {\scriptsize
      F^{\flat\flat}
      =
      \{ \EtatCol^\flat & \EtaxCol^\flat & \EtayCol^\flat & \EtazCol^\flat \}^\flat
      \FaradaySharpFlat
      }

   .. math::

      {\scriptsize
      F^{\flat\flat}=
      \begin{bmatrix}
          \begin{alignat}{1}
          + 0  & \EtatCol^\flat & +\Ex & \EtaxCol^\flat & +\Ey & \EtayCol^\flat & +\Ez & \EtazCol^\flat \\
          +\Ex & \EtatCol^\flat & + 0  & \EtaxCol^\flat & -\Bz & \EtayCol^\flat & +\By & \EtazCol^\flat \\
          +\Ey & \EtatCol^\flat & +\Bz & \EtaxCol^\flat & + 0  & \EtayCol^\flat & -\Bx & \EtazCol^\flat \\
          +\Ez & \EtatCol^\flat & -\By & \EtaxCol^\flat & +\Bx & \EtayCol^\flat & + 0  & \EtazCol^\flat \\
          \end{alignat}
      \end{bmatrix}^\flat
      =
      \begin{bmatrix}
          \{      \\ -\Ex \\ -\Ey \\ -\Ez \}^\flat \\
          \{ +\Ex \\      \\ +\Bz \\ -\By \}^\flat \\
          \{ +\Ey \\ -\Bz \\      \\ +\Bx \}^\flat \\
          \{ +\Ez \\ +\By \\ -\Bx \\ + 0  \}^\flat \\
      \end{bmatrix}^\flat
      = \FaradayFlatFlat
      }

.. }}}
 
Covariant-contravariant
'''''''''''''''''''''''

.. {{{

.. math::

   {\small
       F^{\flat\sharp}
       = \eta^{\flat\flat} F^{\sharp\sharp}
       = \EtaFlatFlat \FaradaySharpSharp
       = 
   }

.. admonition:: Step by step
   :class: dropdown, toggle-shown

   .. math::

      {\scriptsize
      F^{\flat\sharp}
      = \eta^{\flat\flat }F^{\sharp\sharp}
      =
      \begin{bmatrix}
          \EtatRow &
          \EtaxRow &
          \EtayRow &
          \EtazRow 
      \end{bmatrix}
      \begin{bmatrix}
          \{      \\ -\Ex \\ -\Ey \\ -\Ez \\ \} \\
          \{ +\Ex \\      \\ -\Bz \\ +\By \\ \} \\
          \{ +\Ey \\ +\Bz \\      \\ -\Bx \\ \} \\
          \{ +\Ez \\ -\By \\ +\Bx \\      \\ \}
      \end{bmatrix}
      }

   .. math::

      {\scriptsize
      F^{\flat\sharp}
      =
      \begin{bmatrix}
          \begin{alignat}{1}
            0  & \EtatCol^\flat & +\Ex & \EtaxCol^\flat & +\Ey & \EtayCol^\flat & +\Ez & \EtazCol^\flat \\
          -\Ex & \EtatCol^\flat & + 0  & \EtaxCol^\flat & -\Bz & \EtayCol^\flat & +\By & \EtazCol^\flat \\
          -\Ey & \EtatCol^\flat & +\Bz & \EtaxCol^\flat & + 0  & \EtayCol^\flat & -\Bx & \EtazCol^\flat \\
          -\Ez & \EtatCol^\flat & -\By & \EtaxCol^\flat & +\Bx & \EtayCol^\flat & + 0  & \EtazCol^\flat \\
          \end{alignat}
      \end{bmatrix}^\sharp
      =
      \begin{bmatrix}
               & -\Ex & -\Ey & -\Ez \\
          -\Ex &      & -\Bz & +\By \\
          -\Ey & -\Bz &      & -\Bx \\
          -\Ez & +\By & +\Bx &      \\
      \end{bmatrix}^\sharp
      }

.. }}}

Homogenous equations
--------------------

Contravariant-covariant
'''''''''''''''''''''''

.. {{{

.. math::

   {\small
   G^{\sharp\flat}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\flat}
   }

.. }}}

Contravariant-contravariant
'''''''''''''''''''''''''''

.. {{{

.. math::

   {\scriptsize
   G^{\sharp\sharp}
   =
   G^{\sharp\flat} \eta^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\flat}
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & -       B^x  & -       B^y  & -       B^z  \\
    +       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    +       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    +       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\sharp}
   }

.. }}}

.. .. rubric:: Covariant-covariant
..
.. .. {{{
.. 
.. .. warning::
.. 
..    I have not doubled check that one.
.. 
.. .. math::
.. 
..    {\scriptsize
..    G^{\flat\flat}
..    =
..    \eta^{\flat\flat} G^{\sharp\flat}
..    =
..    \begin{bmatrix}
..     1 &  0 &  0 &  0 \\
..     0 & -1 &  0 &  0 \\
..     0 &  0 & -1 &  0 \\
..     0 &  0 &  0 & -1
..    \end{bmatrix}^{\flat\flat}
..    \begin{bmatrix}
..                  & +       B^x  & +       B^y  & +       B^z  \\
..     +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
..     +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
..     +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
..    \end{bmatrix}^{\sharp\flat}
..    =
..    \begin{bmatrix}
..                  & +       B^x  & +       B^y  & +       B^z  \\
..     -       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
..     -       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
..     -       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
..    \end{bmatrix}^{\flat\flat}
..    }
.. 
.. .. }}}

Covariant-contravariant
'''''''''''''''''''''''

.. {{{

.. warning::

   I have not checked that one.

.. math::

   {\scriptsize
   G^{\flat\sharp}
   =
   G^{\flat\flat} \eta^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    -       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    -       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    -       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}^{\flat\flat}
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\flat\sharp}
   }

.. }}}

The Tensor Formulations
-----------------------

.. {{{

With that, we have obtained all tensor formulations of the Maxwell equations.

The homogenous equations can take one of four equivalent form. The full and
explicit matrix representation in musical notation can be found above. One can
go from one representation to the other by applying the metric tensor.

Contravariant-covariant
'''''''''''''''''''''''

.. math::

   \partial_{\mu} F^\mu{}_\nu = J_{\nu}

.. math::

   \partial_{\mu} G^\mu{}_\nu = 0

Contravariant-contravariant
'''''''''''''''''''''''''''

.. math::

   \partial_{\mu} F^{\mu\nu} = J^{\nu}

.. math::

   \partial_{\mu} G^{\mu\nu} = 0

Covariant-covariant
'''''''''''''''''''

.. math::

   \partial^{\mu} F_{\mu\nu} = J_{\nu}

.. math::

   \partial^{\mu} G_{\mu\nu} = 0

Covariant-contravariant
'''''''''''''''''''''''

.. math::

   \partial^{\mu} F_\mu{}^\nu = J^{\nu}

.. math::

   \partial^{\mu} G_\mu{}^\nu = 0

.. }}}

Explicit formulation of Maxwell equations
-----------------------------------------

Contravariant-covariant
'''''''''''''''''''''''

.. {{{

.. math::

   \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \\ \}^{\flat} &
   \FaradaySharpFlat
   = \{ +\mu_0 c \rho \\ -\mu_0 J^x \\ -\mu_0 J^y \\ -\mu_0 J^z \\ \}^{\flat}

.. admonition:: Back to the 1865 Maxwell Equations
   :class: dropdown

   Applying matrix multiplication rules directly result in:

   .. math::

      \begin{matrix}
                          & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
          +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x    \\
          +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y    \\
          +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z    \\
      \end{matrix}

.. math::

   \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \}^{\flat}
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp \flat}
   = \{ 0 \\ 0 \\ 0 \\ 0 \\ \}^{\flat}

.. }}}

Contravariant-contravariant
'''''''''''''''''''''''''''

.. {{{

.. math::

   \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \}^{\flat} \FaradaySharpSharp
   = \{ \mu_0 c \rho \\ \mu_0 J^x \\ \mu_0 J^y \\ \mu_0 J^z \}^{\sharp}

.. admonition:: Back to the 1865 Maxwell Equations
   :class: dropdown

   Upacking the musical tensor notation result in:

   .. math::

      {\scriptsize
          \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \}^{\flat} \FaradaySharpSharp
          =
          \{ \partial_t & \partial_x & \partial_y & \partial_z \}^{\flat}
          \FaradayColCol
      }

   Calculating the left-hand side with matrix multiplication rules results in:

   .. math::

      {\scriptsize
          \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \}^{\flat} \FaradaySharpSharp
          =
          \begin{matrix}
              \begin{alignat}{1}
               \partial_t & \{   0  \\ -\Ex \\ -\Ey \\ -\Ez \} &
              +\partial_x & \{ +\Ex \\   0  \\ -\Bz \\ +\By \} &
              +\partial_y & \{ +\Ey \\ +\Bz \\   0  \\ -\Bx \} &
              +\partial_z & \{ +\Ez \\ -\By \\ +\Bx \\   0  \} \\
              \end{alignat}
          \end{matrix}
      }

   .. math::

      {\scriptsize
          \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \}^{\flat} \FaradaySharpSharp
          =
          \begin{bmatrix}
              \begin{alignat}{1}
                              & +\partial_x \Ex & +\partial_y \Ey & +\partial_z \Ez \\
              -\partial_t \Ex &                 & +\partial_y \Bz & -\partial_z \By \\
              -\partial_t \Ey & -\partial_x \Bz &                 & +\partial_z \Bx \\
              -\partial_t \Ez & +\partial_x \By & -\partial_y \Bx &                 \\
              \end{alignat}
          \end{bmatrix}
      }

   With the left-hand side of the equation equal to the right-hand side, we get:

   .. math::

      {\scriptsize
          \begin{bmatrix}
              \begin{alignat}{1}
                              & +\partial_x \Ex & +\partial_y \Ey & +\partial_z \Ez \\
              -\partial_t \Ex &                 & +\partial_y \Bz & -\partial_z \By \\
              -\partial_t \Ey & -\partial_x \Bz &                 & +\partial_z \Bx \\
              -\partial_t \Ez & +\partial_x \By & -\partial_y \Bx &                 \\
              \end{alignat}
          \end{bmatrix}
          =
          \CurrentCol
      }

   Which is then unpacked in a system of equations:

   .. math::

      {\scriptsize
      \begin{matrix}
                          & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
          -\partial_t \Ex &                 & +\partial_y \Bz & -\partial_z \By & = & + \mu_0 J^x    \\
          -\partial_t \Ey & -\partial_x \Bz &                 & +\partial_z \Bx & = & + \mu_0 J^y    \\
          -\partial_t \Ez & +\partial_x \By & -\partial_y \Bx &                 & = & + \mu_0 J^z    \\
      \end{matrix}\\
      }

   And reordered to obtain back the Maxwell equations derived in
   :ref:`faraday_tensor_derivation:Deriving the Faraday Tensor from the 1865
   Maxwell Equations`

   .. math::

      {\scriptsize
      \begin{matrix}
                          & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
          +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x    \\
          +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y    \\
          +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z    \\
      \end{matrix}
      }

.. math::

   \begin{bmatrix}
   +\partial_t \\
   +\partial_x \\
   +\partial_y \\
   +\partial_z \\
   \end{bmatrix}^{\flat}
   \begin{bmatrix}
                 & -       B^x  & -       B^y  & -       B^z  \\
    +       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    +       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    +       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
   0 \\
   0 \\
   0 \\
   0 \\
   \end{bmatrix}^{\sharp}

.. }}}

Covariant-covariant
'''''''''''''''''''

.. {{{

.. math::

   \{ +\partial_t \\
      -\partial_x \\
      -\partial_y \\
      -\partial_z \\
   \}^{\sharp}
   \FaradayFlatFlat
   = \{ +\mu_0 c \rho \\ -\mu_0 J^x \\ -\mu_0 J^y \\ -\mu_0 J^z \}^{\flat}

.. warning::

   Bug.

.. admonition:: Back to the 1865 Maxwell Equations
   :class: dropdown, toggle-shown

   Upacking the musical tensor notation result in:

   .. math::

      {\scriptsize
      \begin{align}
      \partial^{\sharp} F^{\flat\flat}
      & = \{
              +\partial_t \\
              -\partial_x \\
              -\partial_y \\
              -\partial_z
          \}^{\sharp}
          \begin{bmatrix}
                    & -\Ex & -\Ey & -\Ez \\
               -\Ex &      & -\Bz & +\By \\
               -\Ey & +\Bz &      & -\Bx \\
               -\Ez & -\By & +\Bx &      \\
          \end{bmatrix}^{\flat\flat} \\
      & = \{
              +\partial_t \\
              -\partial_x \\
              -\partial_y \\
              -\partial_z
          \}^{\sharp}
          \{
              \{   0 , -\Ex, -\Ey, -\Ez \} &
              \{ -\Ex,   0 , +\Bz, -\By \} &
              \{ -\Ey, -\Bz,   0 , +\Bx \} &
              \{ -\Ez, +\By, -\Bx,   0  \}
          \} \\
      &=
          +\partial_t \{   0  \\ -\Ex \\ -\Ey \\ -\Ez \}^\flat
          -\partial_x \{ -\Ex \\   0  \\ +\Bz \\ -\By \}^\flat
          -\partial_y \{ -\Ey \\ -\Bz \\   0  \\ +\Bx \}^\flat
          -\partial_z \{ -\Ez \\ +\By \\ -\Bx \\   0  \}^\flat
      =
      \{
          \begin{matrix}
                              \\
              +\partial_t \Ex \\
              +\partial_t \Ey \\
              +\partial_t \Ez \\
          \end{matrix} &
          \begin{matrix}
              +\partial_x \Ex \\
                              \\
              -\partial_x \Bz \\
              +\partial_x \By \\
          \end{matrix} &
          \begin{matrix}
              +\partial_y \Ey \\
              +\partial_y \Bz \\
                              \\
              -\partial_y \Bx \\
          \end{matrix} &
          \begin{matrix}
              +\partial_z \Ez \\
              -\partial_z \By \\
              +\partial_z \Bx \\
                              \\
          \end{matrix}
      \}^{\flat}
      \end{align}
      }

   The full expression :math:`\partial^\sharp F^{\flat\flat} = J_\flat` is then:

   .. math::

      {\scriptsize
      \{
          \begin{matrix}                 \\ +\partial_t \Ex \\ +\partial_t \Ey \\ +\partial_t \Ez \\ \end{matrix} &
          \begin{matrix} +\partial_x \Ex \\                 \\ +\partial_x \Bz \\ -\partial_x \By \\ \end{matrix} &
          \begin{matrix} +\partial_y \Ey \\ -\partial_y \Bz \\                 \\ +\partial_y \Bx \\ \end{matrix} &
          \begin{matrix} +\partial_z \Ez \\ +\partial_z \By \\ -\partial_z \Bx \\                 \\ \end{matrix}
      \}^{\flat}
      =
      \{ + \mu_0 c \rho \\ -\mu_0 J^x \\ -\mu_0 J^y \\ -\mu_0 Jz \}^\flat
      }

   Which is then unpacked in a system of equations:

   .. math::

      {\scriptsize
      \begin{matrix}
                          & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
          +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x    \\
          +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y    \\
          +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z    \\
      \end{matrix}\\
      }

   And reordered to obtain back the Maxwell equations derived in
   :ref:`faraday_tensor_derivation:Deriving the Faraday Tensor from the 1865
   Maxwell Equations`

   .. math::

      {\scriptsize
      \begin{matrix}
                          & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
          +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x    \\
          +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y    \\
          +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z    \\
      \end{matrix}
      }


.. }}}

Covariant-contravariant
'''''''''''''''''''''''

.. {{{

.. }}}

Summary
-------

.. {{{

The derivatives are flat and therefore represent a covector with lower indices
in tensor notation :math:`\partial_\mu` While the left-hand side is sharp and
therefore represent a vector with high indices :math:`J^\nu`. The tensors in
the expressions above are necessarily one time contravariant and one time
covariant :math:`F^{\mu\nu}`.

.. math::

   F^{\sharp\flat}
   =
   \begin{bmatrix}
   F^\mu{}_\nu
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x} &              & -       B^z  & +        B^y  \\
    +\tilde{E^y} & +       B^z  &              & -        B^x  \\
    +\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}

.. math::

   G^{\sharp\flat}
   =
   \begin{bmatrix}
   G^\mu{}_\nu
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}

.. math::

   \begin{matrix}
   \partial_{\mu} F^\mu{}_\nu & = & J_{\nu} \\
   \partial_{\mu} G^\mu{}_\nu & = & 0       \\
   \end{matrix}

.. math::

   \begin{matrix}
   \partial^{\flat} F^{\sharp\flat} & = & J^{\flat} \\
   \partial^{\flat} G^{\sharp\flat} & = & 0^{\flat} \\
   \end{matrix}

.. note::

   Recall that :math:`\partial_{\mu} \eta^{\mu \nu}=\partial^{\nu}`. In matrix
   form, this is:

   .. math::

      \begin{bmatrix}
      \partial_t & \partial_x & \partial_y & \partial_z
      \end{bmatrix}
      \begin{bmatrix}
       1 &  0 &  0 &  0 \\
       0 & -1 &  0 &  0 \\
       0 &  0 & -1 &  0 \\
       0 &  0 &  0 & -1
      \end{bmatrix}
      = 
      \begin{bmatrix}
      + \partial_t \\
      - \partial_x \\
      - \partial_y \\
      - \partial_z \\
      \end{bmatrix}

In a next article, I show how the two tensors obtained in that manner are
related as one being the Hodge dual of the other.

.. }}}
