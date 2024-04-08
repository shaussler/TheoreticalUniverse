Rotations in 3 Dimensions
=========================

.. rst-class:: custom-author

   by Stéphane Haussler

The Free Matrix Representation of Rotations
-------------------------------------------

.. {{{

The :ref:`free matrix representation <formalism_free_matrix_representation:Free
Matrix Representation>` is powerfull when using a bivector basis, since the
elements of the matrix can be re-ordered at will. In three dimensions,
rotations are possible on the three planes. A general **rotation is a linear
combination of the three associated basis bivectors**:

.. math::

   \begin{equation}
   R = a \; ∂_y ∧ ∂_z + b \; ∂_z ∧ ∂_x + c \; ∂_x ∧ ∂_y
   \end{equation}

With free matrix representation, the bivector can be written as a single
column:

.. topic:: Representation of rotations as a single column of bivectors

   .. math::

      \begin{equation}
      R =
      \begin{bmatrix}
        + a \; ∂_y ∧ ∂_z \\
        + b \; ∂_z ∧ ∂_x \\
        + c \; ∂_x ∧ ∂_y \\
      \end{bmatrix}
      \end{equation}

Or with a row/column matrix notation:

.. math::

   \begin{equation}
   R =
   \begin{bmatrix}
                      & + c \; ∂_x ∧ ∂_y &                  \\
                      &                  & + a \; ∂_y ∧ ∂_z \\
     + b \; ∂_z ∧ ∂_x &                  &                  \\
   \end{bmatrix}
   \end{equation}

The anti-symmetric property of the wedge product :math:`\partial_i \wedge
\partial_j = - \partial_j \wedge \partial_i` permit to split the terms:

.. math::

   \begin{equation}
   A ∂_i ∧ ∂_j = \frac{1}{2} (A ∂_i ∧ ∂_j - A ∂_j ∧ ∂_i)
   \end{equation}

With a column/row representation, we obtain:

.. math::

   \begin{equation}
   R
   = \frac{1}{2}
   \begin{bmatrix}
                       & + c ∂_x ∧ ∂_y & - b \; ∂_x ∧ ∂_z \\
      - c \; ∂_y ∧ ∂_x &               & + a \; ∂_y ∧ ∂_z \\
      + b \; ∂_z ∧ ∂_x & - a ∂_z ∧ ∂_y &                  \\
   \end{bmatrix}
   \end{equation}

With a row/column representation, we obtain:

.. topic:: The matrix representation of rotations

   .. math::

      \begin{equation}
      R = \frac{1}{2}
      \begin{bmatrix}
                          & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
         + c \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
         - b \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &               \\
      \end{bmatrix}
      \end{equation}

The doubly contravariant rotation object at hand can only act on covectors. To
fall back to matrix multiplication, we need a mixed tensor that takes as input
vectors and we thus must flatten one of the components.

.. }}}

Flattening the First Index
--------------------------

.. {{{

Flattering of the first kind refers to the flattening of the first component of
the doubly contravariant rotation :math:`R`.  In this section, we transform the
:math:`R` to the mixed tensor:

.. math::

   \begin{equation}
   R^{♭♯} =
   \{
                       & - c \; dx^y ∧ ∂_x & + b \; dx^z ∧ ∂_x \\
     + c \; dx^x ∧ ∂_y &                   & - a \; dx^z ∧ ∂_y \\
     - b \; dx^x ∧ ∂_z & + a \; dx^y ∧ ∂_z &                   \\
   \}
   \end{equation}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   The expression at hand is double contravariant and must be flattend in the
   first index:

   .. math::

      \begin{equation}
      R^{♭♯} = (R^{♯♯})^{♭♯}
      \end{equation}

   Expand the rotation to its matrix form:

   .. math::

      \begin{equation}
      R^{♭♯} = \frac{1}{2}
      \begin{bmatrix}
                          & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
        + c  \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
        - b  \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &                  \\
      \end{bmatrix}^{♭♯}
      \end{equation}

   Distribute the musical operators:

   .. math::

      \begin{equation}
      R^{♭♯} = \frac{1}{2}
      \begin{bmatrix}
                                & - c \; (∂_y ∧ ∂_x)^{♭♯} & + b \; (∂_z ∧ ∂_x)^{♭♯} \\
        + c \; (∂_x ∧ ∂_y)^{♭♯} &                         & - a \; (∂_z ∧ ∂_y)^{♭♯} \\
        - b \; (∂_x ∧ ∂_z)^{♭♯} & + a \; (∂_y ∧ ∂_z)^{♭♯} &                      \\
      \end{bmatrix}
      \end{equation}

   Apply the musical operators:

   .. math::

      \begin{equation}
      R^{♭♯} = \frac{1}{2}
      \begin{bmatrix}
                          & - c \; dx^y ∧ ∂_x & + b \; dx^z ∧ ∂_x \\
        + c \; dx^x ∧ ∂_y &                   & - a \; dx^z ∧ ∂_y \\
        - b \; dx^x ∧ ∂_z & + a \; dx^y ∧ ∂_z &                   \\
      \end{bmatrix}
      \end{equation}

   .. }}}

.. }}}

Flattening the Second Index
---------------------------

.. {{{

The *second kind* refers to the flatting of the second tensor component. The
results of this section may be obvious to the point the reader wonders why
detailed calculation steps are given. However in Minkowski space and generally
when considering mixed metric signatures, this is not the case anymore. Hence
every step is detailed, which may be helpfull to fallback to when considering
rotations in Minkowski space. The contravariant/covariant rotation is:

.. math::

   \begin{equation}
   R^{♯♭} =
   \{
                       & - c \; ∂_y ∧ dx^x & + b \; ∂_z ∧ dx^x \\
     + c \; ∂_x ∧ dx^y &                   & - a \; ∂_z ∧ dx^y \\
     - b \; ∂_x ∧ dx^z & + a \; ∂_y ∧ dx^z &                   \\
   \}
   \end{equation}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   .. math::

      \begin{align}
      R^{♯♭}
      &= (R^{♯♯})^{♯♭} \\
      &= \frac{1}{2} \{
                         & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
        + c \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
        - b \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &                  \\
      \}^{♯♭} \\
      &= \frac{1}{2} \{
                                & - c \; (∂_y ∧ ∂_x)^{♯♭} & + b \; (∂_z ∧ ∂_x)^{♯♭} \\
        + c \; (∂_x ∧ ∂_y)^{♯♭} &                         & - a \; (∂_z ∧ ∂_y)^{♯♭} \\
        - b \; (∂_x ∧ ∂_z)^{♯♭} & + a \; (∂_y ∧ ∂_z)^{♯♭} &                         \\
      \} \\
      &= \frac{1}{2} \{
                          & - c \; ∂_y ∧ dx^x & + b \; ∂_z ∧ dx^x \\
        + c \; ∂_x ∧ dx^y &                   & - a \; ∂_z ∧ dx^y \\
        - b \; ∂_x ∧ dx^z & + a \; ∂_y ∧ dx^z &                   \\
      \}
      \end{align}

   .. }}}

Expanding the wedge product to its tensor form and simplifying, we find the
explicit expression of the mixed wedge products.

.. math::

   \begin{array}{}
   (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x ⊗ dx^y - ∂_y ⊗ dx^x \\
   (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y ⊗ dx^z - ∂_z ⊗ dx^y \\
   (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z ⊗ dx^x - ∂_x ⊗ dx^z \\
   \end{array}

.. admonition:: All calculation steps
   :class: dropdown

   Expand the wedge product into tensor products

   .. math::

      \begin{array}{}
      (∂_x ∧ ∂_y)^{♯♭} &=& (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♯♭} \\
      (∂_y ∧ ∂_z)^{♯♭} &=& (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♯♭} \\
      (∂_z ∧ ∂_x)^{♯♭} &=& (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♯♭} \\
      \end{array}

   Distribute the musical operators:

   .. math::

      \begin{array}{}
      (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_x^♭ \\
      (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_y^♭ \\
      (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_z^♭ \\
      \end{array}

   Apply the musical operators:

   .. math::

      \begin{array}{}
      (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x ⊗ η_{yi} dx^i - ∂_y ⊗ η_{xi}dx^i \\
      (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y ⊗ η_{zi} dx^i - ∂_z ⊗ η_{yi}dx^i \\
      (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z ⊗ η_{xi} dx^i - ∂_x ⊗ η_{zi}dx^i \\
      \end{array}

   Take out the metric components:

   .. math::

      \begin{array}{}
      (∂_x ∧ ∂_y)^{♯♭} &=& η_{yi} ∂_x ⊗ dx^i - η_{xi} ∂_y ⊗ dx^i \\
      (∂_y ∧ ∂_z)^{♯♭} &=& η_{zi} ∂_y ⊗ dx^i - η_{yi} ∂_z ⊗ dx^i \\
      (∂_z ∧ ∂_x)^{♯♭} &=& η_{xi} ∂_z ⊗ dx^i - η_{zi} ∂_x ⊗ dx^i \\
      \end{array}

   Identify the non-zero terms:

   .. math::

      \begin{array}{}
      (∂_x ∧ ∂_y)^{♯♭} &=& η_{yy} ∂_x ⊗ dx^y - η_{xx} ∂_y ⊗ dx^x \\
      (∂_y ∧ ∂_z)^{♯♭} &=& η_{zz} ∂_y ⊗ dx^z - η_{yy} ∂_z ⊗ dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &=& η_{xx} ∂_z ⊗ dx^x - η_{zz} ∂_x ⊗ dx^z \\
      \end{array}

   Apply numerical values

   .. math::

      \begin{array}{}
      (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x ⊗ dx^y - ∂_y ⊗ dx^x \\
      (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y ⊗ dx^z - ∂_z ⊗ dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z ⊗ dx^x - ∂_x ⊗ dx^z \\
      \end{array}

From the explicit calculation of the basis elements, we observe the following
properties:

================== ================================ ==========================
Basis element      Expression                       Row/column matrix symmetry
================== ================================ ==========================
:math:`∂_x ∧ dx^y` :math:`∂_x ⊗ dx^y - ∂_y ⊗ dx^x`  Antisymetric
:math:`∂_y ∧ dx^z` :math:`∂_x ⊗ dx^z - ∂_z ⊗ dx^y`  Antisymetric
:math:`∂_z ∧ dx^x` :math:`∂_x ⊗ dx^x - ∂_x ⊗ dx^z`  Antisymetric
================== ================================ ==========================

.. }}}

The :math:`\mathfrak{so}(3)` Rotation Group
-------------------------------------------

.. {{{

Whether as a transpose or not, we identify the :math:`\mathfrak{so}(3)`
matrices as well as get a first hint that we are about to identify the
electromagnetic tensor. Choosing the implicit basis :math:`\mathbf{e}_i \wedge
\mathbf{e}_j` in a row major representation, we obtain:

.. math::

   \begin{align}
   R
   &= \frac{1}{2}
   \begin{bmatrix}
          & - c & + b \\
      + c &     & - a \\
      - b & + a &     \\
   \end{bmatrix} \\
   &=
   a
   \begin{bmatrix}
       0 &  0 &  0 \\
       0 &  0 & -1 \\
       0 & +1 &  0 \\
   \end{bmatrix}
   + b
   \begin{bmatrix}
       0 &  0 & +1 \\
       0 &  0 &  0 \\
      -1 &  0 &  0 \\
   \end{bmatrix}
   + c
   \begin{bmatrix}
       0 & -1 &  0 \\
      +1 &  0 &  0 \\
       0 &  0 &  0 \\
   \end{bmatrix}
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

   \begin{equation}
   ⋆R = ⋆(a \; ∂_y ∧ ∂_z + b \; ∂_z ∧ ∂_x + c \; ∂_x ∧ ∂_y) \\
   \end{equation}

Distribute the Hodge star:

.. math::

   \begin{equation}
   ⋆R = a ⋆(∂_y ∧ ∂_z) + b ⋆(∂_z ∧ ∂_x) + c ⋆(∂_x ∧ ∂_y) \\
   \end{equation}

Identify the cross product:

.. math::

   \begin{equation}
   ⋆R = a \; ∂_x + b \; ∂_y + c \; ∂_z
   \end{equation}

That is, the Hodge star of the rotation ∂_xpressed as a linear comibination of
bivectors is exactly a rotation in terms of cross products in the Hodge dual
space:

.. math::

   \begin{equation}
   ⋆R = a \; ∂_y ⨯ ∂_z + b \; ∂_z ⨯ ∂_x + c \; ∂_x ⨯ ∂_y
   \end{equation}

We could have written a covector in the same explicit manner. This notation is
very conveniant when performing calculations in Cartan's framework as it
permits to identify and organize terms for practical calculations by falling
back to regular matrix multiplication.

.. }}}
