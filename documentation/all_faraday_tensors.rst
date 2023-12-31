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

.. admonition:: Relation to the *regular* doubly contravariant Faraday tensor
   :class: dropdown

   .. include:: ./musical_notation_notable_difference.rst

.. }}}

Covariant-covariant
'''''''''''''''''''

.. {{{

.. warning::

   Doesn't match when I try to get back the Maxwell equations. Actually, this
   one kinda makes sense and has the form I would like to have.

   .. math::
    
      {\scriptsize
          F^{\flat\flat}
          = \eta{\flat\flat} F^{\sharp\flat}
          = \EtaFlatFlat \FaradaySharpFlat
          = \FaradayFlatFlat
      }

.. warning::
   :class: dropdown

   .. rubric:: Step by step 

   Getting a form I kinda like but not getting the Maxwell equations back with
   that.

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
   :class: dropdown

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

.. rubric:: Contravariant-covariant

.. rubric:: Contravariant-contravariant

.. rubric:: Covariant-covariant

.. rubric:: Covariant-contravariant

Explicit formulation of Maxwell equations
-----------------------------------------

Contravariant-covariant
'''''''''''''''''''''''

.. rubric:: Inhomogenous Equations

.. {{{

.. math::

   \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \\ \}^{\flat} &
   \FaradaySharpFlat
   = \{ +\mu_0 c \rho \\ -\mu_0 J^x \\ -\mu_0 J^y \\ -\mu_0 J^z \\ \}^{\flat}

.. admonition:: Back to the 1865 Maxwell's Equations
   :class: dropdown

   Applying matrix multiplication rules directly result in:

   .. math::

      \begin{matrix}
                          & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
          +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x    \\
          +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y    \\
          +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z    \\
      \end{matrix}

.. }}}

.. rubric:: Homogenous Equations

Contravariant-contravariant
'''''''''''''''''''''''''''

.. {{{

.. math::

   \{ \partial_t \\ \partial_x \\ \partial_y \\ \partial_z \}^{\flat} \FaradaySharpSharp
   = \{ \mu_0 c \rho \\ \mu_0 J^x \\ \mu_0 J^y \\ \mu_0 J^z \}^{\sharp}

.. admonition:: Back to the 1865 Maxwell's Equations
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

.. }}}

Covariant-covariant
'''''''''''''''''''

.. rubric:: Inhomogenous Equations

.. {{{

.. math::

   \{ +\partial_t \\
      -\partial_x \\
      -\partial_y \\
      -\partial_z \\
   \}^{\sharp}
   \FaradayFlatFlat
   =
   \{ +\mu_0 c \rho \\
      -\mu_0 J^x    \\
      -\mu_0 J^y    \\
      -\mu_0 J^z    \}^{\flat}

.. tip::
   :class: dropdown

   The easy way to get  back to Maxwell equations is to use the identity from
   tensor calculus:

   .. math::

      {\small
      \{ \partial^\sharp F^{\flat\flat} \}_\mu
      =
      \partial^\gamma F_\gamma{}_\mu = \partial_\gamma F^\gamma{}_\mu
      }

   However doing that we loose indsight on how to explicitely get back to the
   1865 Maxwell equations from the doubly covariant electromagnetic tensor. In
   particular this permits to clarify matrix multiplication rules of a
   contravariant vector from the left.

.. admonition:: Back to the 1865 Maxwell's Equations
   :class: dropdown

   Upacking the musical tensor notation result in:

   .. math::

      {\small
      \begin{align}
      \partial^{\sharp} F^{\flat\flat}
      & = \{
              +\partial_t \\
              -\partial_x \\
              -\partial_y \\
              -\partial_z
          \}^{\sharp}
          \FaradayFlatFlat \\
      \end{align}
      }

   To apply a vector to a matrix from the left clearly is not standard. However
   it can be stated with tensor notation:

   .. math::

      {\small
      \{ \partial^\sharp F^{\flat\flat} \}_\mu
      =
      \partial^\gamma F_\gamma{}_\mu = \partial^\gamma F^T_\mu{}_\gamma
      }

   The rule for matrix multiplication can then formulated as *Applying each row
   of the vector to each column of the transposed column-column matrix*. This
   is nearly the same as applying a vector to a matrix, with the twist that the
   transpose of the matrix is taken, and the partial derivatives are applied
   from the left.

   .. math::

      {\small
      \begin{align}
      \partial^{\sharp} F^{\flat\flat} 
      & = \{
              +\partial_t \\
              -\partial_x \\
              -\partial_y \\
              -\partial_z
          \}^{\sharp}
          \{
              \{   0  \\ +\Ex \\ +\Ey \\ +\Ez \}^\flat &
              \{ -\Ex \\   0  \\ -\Bz \\ +\By \}^\flat &
              \{ -\Ey \\ +\Bz \\   0  \\ -\Bx \}^\flat &
              \{ -\Ez \\ -\By \\ +\Bx \\   0  \}^\flat
          \} \\
      & = \{
          +\partial_t \{   0  \\ +\Ex \\ +\Ey \\ +\Ez \}^\flat
          -\partial_x \{ -\Ex \\   0  \\ -\Bz \\ +\By \}^\flat
          -\partial_y \{ -\Ey \\ +\Bz \\   0  \\ -\Bx \}^\flat
          -\partial_z \{ -\Ez \\ -\By \\ +\Bx \\   0  \}^\flat \} \\
      & =
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
              +\partial_x Bz \\
              -\partial_x By \\
          \end{matrix} &
          \begin{matrix}
              +\partial_y \Ey \\
              -\partial_y \Bz \\
                              \\
              +\partial_y \Bx \\
          \end{matrix} &
          \begin{matrix}
              +\partial_z \Ez \\
              +\partial_z \By \\
              -\partial_z \Bx \\
                              \\
          \end{matrix}
      \}^{\flat}
      \end{align}
      }

   The full expression :math:`{\small \partial^\sharp F^{\flat\flat} = J_\flat}` is then:

   .. math::

      {\small
      \{
          \begin{matrix}                 \\ +\partial_t \Ex \\ +\partial_t \Ey \\ +\partial_t \Ez \\ \end{matrix} &
          \begin{matrix} +\partial_x \Ex \\                 \\ +\partial_x \Bz \\ -\partial_x \By \\ \end{matrix} &
          \begin{matrix} +\partial_y \Ey \\ -\partial_y \Bz \\                 \\ +\partial_y \Bx \\ \end{matrix} &
          \begin{matrix} +\partial_z \Ez \\ +\partial_z \By \\ -\partial_z \Bx \\                 \\ \end{matrix}
      \}^{\flat}
      =
      \{ + \mu_0 c \rho \\ -\mu_0 J^x \\ -\mu_0 J^y \\ -\mu_0 Jz \}^\flat
      }

   Which corresponds to the 1865 Maxwell Equations

   .. math::

      {\small
      \begin{matrix}
                          & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho \\
          +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x    \\
          +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y    \\
          +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z    \\
      \end{matrix}
      }

.. }}}


.. rubric:: Homogenous Equations

Covariant-contravariant
'''''''''''''''''''''''

.. rubric:: Inhomogenous Equations

.. rubric:: Homogenous Equations

