.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Rotations in 3 Dimensions
=========================

.. rst-class:: custom-author

   by Stéphane Haussler

The Free Matrix Representation of Rotations
-------------------------------------------

.. {{{

:ref:`the free matrix representation` is powerfull when using a bivector basis,
since the elements of the matrix can be re-ordered at will. In three dimensions,
rotations are possible on the three planes. A rotation is expressed as a linear
combination of the three associated basis bivectors:

.. math::

   R = a \; ∂_y ∧ ∂_z + b \; ∂_z ∧ ∂_x + c \; ∂_x ∧ ∂_y

With free matrix representation, the bivector can be written as a single column:

.. topic:: Representation of rotations as a single column of bivectors

   .. math::

      R^{♯♯} = \begin{bmatrix}
        a \; ∂_y ∧ ∂_z \\
        b \; ∂_z ∧ ∂_x \\
        c \; ∂_x ∧ ∂_y \\
      \end{bmatrix}

Or alternatively with a row/column matrix notation:

.. math::

   R^{♯♯} = \left[ \begin{alignedat}{1}
                    & c \; ∂_x ∧ ∂_y &                \\
                    &                & a \; ∂_y ∧ ∂_z \\
     b \; ∂_z ∧ ∂_x &                &                \\
   \end{alignedat} \right]

The anti-symmetric property of the wedge product :math:`∂_i ∧ ∂_j = - ∂_j ∧ ∂_i`
permit to split the terms:

.. math::

   ∂_i ∧ ∂_j = \frac{1}{2} (∂_i ∧ ∂_j - ∂_j ∧ ∂_i)

With a row/column representation, we obtain:

.. topic:: The matrix representation of rotations

   .. math::

      R^{♯♯} = \frac{1}{2} \begin{bmatrix}
                       & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
      + c \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
      - b \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &               \\
      \end{bmatrix}

The doubly contravariant rotation object under consideration exclusively
operates on covectors. To fall back to matrix multiplication, we require a mixed
tensor that takes vectors as input, necessating the flattening of one of the
components.

.. }}}

:math:`♭♯` Representation
-------------------------

.. {{{

Flattening the first index of of the doubly contravariant form of the rotation
:math:`R`, we obtain:

.. math::

   R^{♭♯} = \begin{bmatrix}
                   & - c \; dy ∧ ∂_x & + b \; dz ∧ ∂_x \\
   + c \; dx ∧ ∂_y &                 & - a \; dz ∧ ∂_y \\
   - b \; dx ∧ ∂_z & + a \; dy ∧ ∂_z &                 \\
   \end{bmatrix}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Flatten the first index, keeping the second sharp

   .. math:: R^{♭♯} = (R^{♯♯})^{♭♯}

   .. rubric:: Take the rotation in its matrix form

   .. math::

      R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                        & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
      + c  \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
      - b  \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &                  \\
      \end{bmatrix}^{♭♯}

   .. rubric:: Distribute the musical operators

   .. math::

      R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                              & - c \; (∂_y ∧ ∂_x)^{♭♯} & + b \; (∂_z ∧ ∂_x)^{♭♯} \\
      + c \; (∂_x ∧ ∂_y)^{♭♯} &                         & - a \; (∂_z ∧ ∂_y)^{♭♯} \\
      - b \; (∂_x ∧ ∂_z)^{♭♯} & + a \; (∂_y ∧ ∂_z)^{♭♯} &                         \\
      \end{bmatrix}

   .. rubric:: Apply musical operators using the euclidean metric

   .. math::

      R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                               & - c \; δ_{yi} dx^i ∧ ∂_x & + b \; δ_{zi} dx^i ∧ ∂_x \\
      + c \; δ_{xi} dx^i ∧ ∂_y &                          & - a \; δ_{zi} dx^i ∧ ∂_y \\
      - b \; δ_{xi} dx^i ∧ ∂_z & + a \; δ_{yi} dx^i ∧ ∂_z &                          \\
      \end{bmatrix}

   .. rubric:: Identify the non-zero components

   .. math::

      R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                        & - c \; dx^y ∧ ∂_x & + b \; dx^z ∧ ∂_x \\
      + c \; dx^x ∧ ∂_y &                   & - a \; dx^z ∧ ∂_y \\
      - b \; dx^x ∧ ∂_z & + a \; dx^y ∧ ∂_z &                   \\
      \end{bmatrix}

   .. rubric:: Replace the covectors by their expressions and conclude

   .. math::

      dx^x = dx \\
      dx^y = dy \\
      dx^z = dz \\

   .. math::

      R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                      & - c \; dy ∧ ∂_x & + b \; dz ∧ ∂_x \\
      + c \; dx ∧ ∂_y &                 & - a \; dz ∧ ∂_y \\
      - b \; dx ∧ ∂_z & + a \; dy ∧ ∂_z &                 \\
      \end{bmatrix}

   .. }}}

Expanding the wedge product to its tensor form and simplifying, we find the
explicit expression of the mixed wedge products.

.. math::

   (∂_x ∧ ∂_y)^{♭♯} &= dx ⊗ ∂_y - dy ⊗ ∂_x \\
   (∂_y ∧ ∂_z)^{♭♯} &= dy ⊗ ∂_z - dz ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♭♯} &= dz ⊗ ∂_x - dx ⊗ ∂_z \\

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Expand the wedge product into tensor product

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♭♯} \\
      (∂_y ∧ ∂_z)^{♭♯} &= (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♭♯} \\
      (∂_z ∧ ∂_x)^{♭♯} &= (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♭♯} \\

   .. rubric:: Distribute the musical operators

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= ∂_x^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_x^♯ \\
      (∂_y ∧ ∂_z)^{♭♯} &= ∂_y^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_y^♯ \\
      (∂_z ∧ ∂_x)^{♭♯} &= ∂_z^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_z^♯ \\

   .. rubric:: Apply musical operators using the euclidean metric:

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= δ_{xi} dx^i ⊗ ∂_y - δ_{yi} dx^i ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &= δ_{yi} dx^i ⊗ ∂_z - δ_{zi} dx^i ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= δ_{zi} dx^i ⊗ ∂_x - δ_{xi} dx^i ⊗ ∂_z \\

   .. rubric:: Identify the non-zero terms

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= δ_{xx} dx^x ⊗ ∂_y - δ_{yy} dx^y ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &= δ_{yy} dx^y ⊗ ∂_z - δ_{zz} dx^z ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= δ_{zz} dx^z ⊗ ∂_x - δ_{xx} dx^x ⊗ ∂_z \\

   .. rubric: Apply numerical values

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= dx^x ⊗ ∂_y - dx^y ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &= dx^y ⊗ ∂_z - dx^z ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= dx^z ⊗ ∂_x - dx^x ⊗ ∂_z \\

   .. rubric:: Replace covectors by their expressions and conclude

   .. math::

      dx^x = dx \\
      dx^y = dy \\
      dx^z = dz \\

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= dx ⊗ ∂_y - dy ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &= dy ⊗ ∂_z - dz ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= dz ⊗ ∂_x - dx ⊗ ∂_z \\

   .. }}}

.. }}}

:math:`♯♭` Representation
-------------------------

.. {{{

Flattening the second index of of the doubly contravariant form of the rotation
:math:`R`, we obtain:

.. math::

   R^{♯♭} = \frac{1}{2} \begin{bmatrix}
                       & + c \; ∂_x ∧ dy & - b \; ∂_x ∧ dz \\
       - c \; ∂_y ∧ dx &                 & + a \; ∂_y ∧ dz \\
       + b \; ∂_z ∧ dx & - a \; ∂_z ∧ dy &                 \\
   \end{bmatrix}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Flatten the second index, keeping the first sharp:

   .. math:: R^{♯♭} = (R^{♯♯})^{♯♭}

   .. rubric:: Take the rotation in its matrix form:

   .. math::

      R^{♯♭} = \frac{1}{2} \begin{bmatrix}
                        & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
      + c  \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
      - b  \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &                  \\
      \end{bmatrix}^{♯♭}

   .. rubric:: Distribute the musical operators:

   .. math::

      R^{♯♭} = \frac{1}{2} \begin{bmatrix}
                              & - c \; (∂_y ∧ ∂_x)^{♯♭} & + b \; (∂_z ∧ ∂_x)^{♯♭} \\
      + c \; (∂_x ∧ ∂_y)^{♯♭} &                         & - a \; (∂_z ∧ ∂_y)^{♯♭} \\
      - b \; (∂_x ∧ ∂_z)^{♯♭} & + a \; (∂_y ∧ ∂_z)^{♯♭} &                         \\
      \end{bmatrix}

   .. rubric:: Apply the musical operators using the euclidean metric:

   .. math::

      R^{♯♭} = \frac{1}{2} \begin{bmatrix}
                                 & - c \; ∂_y ∧ δ_{xi} dx^i & + b \; ∂_z ∧ δ_{xi} dx^i \\
        + c \; ∂_x ∧ δ_{yi} dx^i &                          & - a \; ∂_z ∧ δ_{yi} dx^i \\
        - b \; ∂_x ∧ δ_{zi} dx^i & + a \; ∂_y ∧ δ_{zi} dx^i &                          \\
      \end{bmatrix}

   .. rubric:: Identify the non-zero components:

   .. math::

      R^{♯♭} = \frac{1}{2} \begin{bmatrix}
                          & - c \; ∂_y ∧ dx^x & + b \; ∂_z ∧ dx^x \\
        + c \; ∂_x ∧ dx^y &                   & - a \; ∂_z ∧ dx^y \\
        - b \; ∂_x ∧ dx^z & + a \; ∂_y ∧ dx^z &                   \\
      \end{bmatrix}

   .. rubric:: Replace the covectors by their expressions

   .. math::

      dx^x = dx \\
      dx^y = dy \\
      dx^z = dz \\

   .. math::

      R^{♯♭} = \frac{1}{2} \begin{bmatrix}
                        & - c \; ∂_y ∧ dx & + b \; ∂_z ∧ dx \\
        + c \; ∂_x ∧ dy &                 & - a \; ∂_z ∧ dy \\
        - b \; ∂_x ∧ dz & + a \; ∂_y ∧ dz &                 \\
      \end{bmatrix}

   .. rubric:: Reorder and conclude

   .. math::

      R^{♯♭} = \frac{1}{2} \begin{bmatrix}
                        & + c \; ∂_x ∧ dy & - b \; ∂_x ∧ dz \\
        - c \; ∂_y ∧ dx &                 & + a \; ∂_y ∧ dz \\
        + b \; ∂_z ∧ dx & - a \; ∂_z ∧ dy &                 \\
      \end{bmatrix}

   .. }}}

Expanding the wedge product to its tensor form and simplifying, we find the
explicit expression of the mixed wedge products.

.. math::

   (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ⊗ dy - ∂_y ⊗ dx \\
   (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ⊗ dz - ∂_z ⊗ dy \\
   (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ⊗ dx - ∂_x ⊗ dz \\

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Expand exterior products into tensor products

   .. math::

      (∂_x ∧ ∂_y)^{♯♭} &= (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♯♭} \\
      (∂_y ∧ ∂_z)^{♯♭} &= (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♯♭} \\
      (∂_z ∧ ∂_x)^{♯♭} &= (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♯♭} \\

   .. rubric:: Distribute the musical operators

   .. math::

      (∂_x ∧ ∂_y)^{♯♭} &= ∂_x^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_x^♭ \\
      (∂_y ∧ ∂_z)^{♯♭} &= ∂_y^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_y^♭ \\
      (∂_z ∧ ∂_x)^{♯♭} &= ∂_z^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_z^♭ \\

   .. rubric:: Apply the musical operators using the euclidean metric

   .. math::

      (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ⊗ δ_{yi} dx^i - ∂_y ⊗ δ_{xi} dx^i \\
      (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ⊗ δ_{zi} dx^i - ∂_z ⊗ δ_{yi} dx^i \\
      (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ⊗ δ_{xi} dx^i - ∂_x ⊗ δ_{zi} dx^i \\

   .. rubric:: Identify the non-zero terms

   .. math::

      (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ⊗ δ_{yy} dx^y - ∂_y ⊗ δ_{xx} dx^x \\
      (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ⊗ δ_{zz} dx^z - ∂_z ⊗ δ_{yy} dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ⊗ δ_{xx} dx^x - ∂_x ⊗ δ_{zz} dx^z \\

   .. rubric:: Apply numerical values

   .. math::

      (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ⊗ dx^y - ∂_y ⊗ dx^x \\
      (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ⊗ dx^z - ∂_z ⊗ dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ⊗ dx^x - ∂_x ⊗ dx^z \\

   .. rubric:: Replace the covectors by their expressions:

   .. math::

      dx^x = dx \\
      dx^y = dy \\
      dx^z = dz \\

   .. math::

      (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ⊗ dy - ∂_y ⊗ dx \\
      (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ⊗ dz - ∂_z ⊗ dy \\
      (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ⊗ dx - ∂_x ⊗ dz \\

   .. }}}

.. }}}

Symmetries of the Mixed Wedge Product
-------------------------------------

.. {{{

From the explicit calculation of the basis elements, we observe the following
properties:

================== =========================== ==========================
Basis element      Expression                  Row/column matrix symmetry
================== =========================== ==========================
:math:`∂_x ∧ dx^y` :math:`∂_x ⊗ dy - ∂_y ⊗ dx` Antisymetric
:math:`∂_y ∧ dx^z` :math:`∂_x ⊗ dz - ∂_z ⊗ dy` Antisymetric
:math:`∂_z ∧ dx^x` :math:`∂_x ⊗ dx - ∂_x ⊗ dz` Antisymetric
================== =========================== ==========================

.. }}}

The :math:`\mathfrak{so}(3)` Rotation Group
-------------------------------------------

.. {{{

Whether as a transpose or not, we identify the :math:`\mathfrak{so}(3)`
matrices as well as get a first hint that we are about to identify the
electromagnetic tensor. Choosing the implicit basis :math:`\mathbf{e}_i \wedge
\mathbf{e}_j` in a row major representation, we obtain:

.. math::
  :nowrap:

   \begin{align} R &= \frac{1}{2}
   \begin{bmatrix}
         & - c & + b \\
     + c &     & - a \\
     - b & + a &     \\
   \end{bmatrix} \\
   &= a \left[ \begin{alignedat}{1}
     \; 0 & \;   & 0 & \;  & 0 \\
     \; 0 & \;   & 0 & \;- & 1 \\
     \; 0 & \; + & 1 & \;  & 0 \\
   \end{alignedat} \right]
   + b \left[ \begin{alignedat}{1}
       & 0 & \quad 0 & \; + & 1 \\
       & 0 & \quad 0 & \;   & 0 \\
     - & 1 & \quad 0 & \;   & 0 \\
   \end{alignedat} \right]
   + c \left[ \begin{alignedat}{1}
       & 0 & - & 1 & \quad 0 \\
     + & 1 &   & 0 & \quad 0 \\
       & 0 &   & 0 & \quad 0 \\
   \end{alignedat} \right]
   \end{align}

Which is `a regular choice for the basis
<https://en.m.wikipedia.org/wiki/3D_rotation_group>`_ of the
:math:`\mathfrak{so}(3)` group.

.. }}}

The Cross Product
-----------------

.. {{{

Rotations in three dimensions have a dual. We can either express a rotation
along the three planes, or we can express a rotation along the three directions
of space. Indeed, through the use of the Hodge star :math:`⋆`, we fall back
to the description of rotations expressed as a cross product :math:`⨯`:

Apply the Hodge star:

.. math::

   ⋆R = ⋆(a \; ∂_y ∧ ∂_z + b \; ∂_z ∧ ∂_x + c \; ∂_x ∧ ∂_y)

Distribute the Hodge star:

.. math::

   ⋆R = a ⋆(∂_y ∧ ∂_z) + b ⋆(∂_z ∧ ∂_x) + c ⋆(∂_x ∧ ∂_y)

Identify the cross product:

.. math::

   ⋆R = a \; ∂_x + b \; ∂_y + c \; ∂_z

That is, the Hodge star of the rotation ∂_xpressed as a linear comibination of
bivectors is exactly a rotation in terms of cross products in the Hodge dual
space:

.. math::

   ⋆R = a \; ∂_y ⨯ ∂_z + b \; ∂_z ⨯ ∂_x + c \; ∂_x ⨯ ∂_y

We could have written a covector in the same explicit manner. This notation is
very conveniant when performing calculations in Cartan's framework as it
permits to identify and organize terms for practical calculations by falling
back to regular matrix multiplication.

.. }}}

