.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Rotations in Euclidean space
============================

.. rst-class:: custom-author

   by Stéphane Haussler

On this page, I systematically explore the representation of infinitesimal
rotations in 3-dimensional Euclidean space using the language of differential
forms. We establish the relation to matrix multiplication rules, as well as the
direct relation to the cross product. In preparation for the analysis of
rotations in 4-dimensional Minkowski spacetime, we determine the symmetries of
the exterior product in mixed form, which, in this case, are found to be
trivial.

Free matrix representation of rotations
---------------------------------------

.. {{{

:ref:`the free matrix representation` is intuitive when using a bivector basis,
since the elements can be organized and re-ordered at will. With three
dimensions, rotations are possible on the three planes and can be expressed as
a linear combinations the three basis bivectors:

.. math::

   R^{♯♯} = a \; ∂_y ∧ ∂_z + b \; ∂_z ∧ ∂_x + c \; ∂_x ∧ ∂_y

We can rewrite as a single column:

.. topic:: Representation of rotations as a single column of bivectors

   .. math::

      R^{♯♯} = \begin{bmatrix}
        a \; ∂_y ∧ ∂_z \\
        b \; ∂_z ∧ ∂_x \\
        c \; ∂_x ∧ ∂_y \\
      \end{bmatrix}

We could also represent the rotation with a row/column notation:

.. math::

   R^{♯♯} = \left[ \begin{alignedat}{2}
                    & c \; ∂_x ∧ ∂_y &                \\
                    &                & a \; ∂_y ∧ ∂_z \\
     b \; ∂_z ∧ ∂_x &                &                \\
   \end{alignedat} \right]

However there is a more natural representation. The exterior product is
anti-symmetric :math:`∂_i ∧ ∂_j = - ∂_j ∧ ∂_i` and strictly equivalent to
:math:`∂_i ∧ ∂_j = \frac{1}{2} (∂_i ∧ ∂_j - ∂_j ∧ ∂_i)`, which permits to
rewrite:

.. math::

   R^{♯♯} = \begin{bmatrix}
     a \; ∂_y ∧ ∂_z \\
     b \; ∂_z ∧ ∂_x \\
     c \; ∂_x ∧ ∂_y \\
   \end{bmatrix} =
   \begin{bmatrix}
     a \; ∂_y ∧ ∂_z - a \; ∂_z ∧ ∂_y \\
     b \; ∂_z ∧ ∂_x - b \; ∂_x ∧ ∂_z \\
     c \; ∂_x ∧ ∂_y - c \; ∂_y ∧ ∂_x \\
   \end{bmatrix}

With a row/column representation, we obtain a fully anti-symmetric and doubly
contravariant representation:

.. topic:: The doubly contravariant row/column representation of rotations

   .. math::

      R^{♯♯} = \frac{1}{2} \begin{bmatrix}
                       & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
      + c \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
      - b \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &               \\
      \end{bmatrix}

The doubly contravariant rotation obtained exclusively operates on covectors.
Falling back to matrix multiplication rules requires a mixed tensor that takes
a vector as input, and output a vector as output. Specifically, we need to
flatten the first component in oder to obtain the :math:`♯♭` tensor
representation, which corresponds exactly to the matrix representation commonly
encountered in linear algebra.

.. }}}

.. _♭♯ representation:

:math:`♭♯` representation
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

   .. rubric:: Take the doubly contravariant row/column representation

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

   .. rubric:: Apply the musical operators, using the euclidean metric

   .. math::

      R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                               & - c \; δ_{yi} dx^i ∧ ∂_x & + b \; δ_{zi} dx^i ∧ ∂_x \\
      + c \; δ_{xi} dx^i ∧ ∂_y &                          & - a \; δ_{zi} dx^i ∧ ∂_y \\
      - b \; δ_{xi} dx^i ∧ ∂_z & + a \; δ_{yi} dx^i ∧ ∂_z &                          \\
      \end{bmatrix}

   .. rubric:: Identify the non-zero components and conclude

   .. math::

      R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                      & - c \; dy ∧ ∂_x & + b \; dz ∧ ∂_x \\
      + c \; dx ∧ ∂_y &                 & - a \; dz ∧ ∂_y \\
      - b \; dx ∧ ∂_z & + a \; dy ∧ ∂_z &                 \\
      \end{bmatrix}

   .. }}}

Expanding the exterior product to its tensor form and simplifying, we find the
explicit expression in terms of tensor products :math:`⊗`:

.. math::

   (∂_x ∧ ∂_y)^{♭♯} &= dx ⊗ ∂_y - dy ⊗ ∂_x \\
   (∂_y ∧ ∂_z)^{♭♯} &= dy ⊗ ∂_z - dz ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♭♯} &= dz ⊗ ∂_x - dx ⊗ ∂_z \\

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Expand the exterior product into tensor products

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♭♯} \\
      (∂_y ∧ ∂_z)^{♭♯} &= (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♭♯} \\
      (∂_z ∧ ∂_x)^{♭♯} &= (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♭♯} \\

   .. rubric:: Distribute the musical operators

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= ∂_x^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_x^♯ \\
      (∂_y ∧ ∂_z)^{♭♯} &= ∂_y^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_y^♯ \\
      (∂_z ∧ ∂_x)^{♭♯} &= ∂_z^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_z^♯ \\

   .. rubric:: Apply musical operators using the Euclidean metric:

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= δ_{xi} dx^i ⊗ ∂_y - δ_{yi} dx^i ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &= δ_{yi} dx^i ⊗ ∂_z - δ_{zi} dx^i ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= δ_{zi} dx^i ⊗ ∂_x - δ_{xi} dx^i ⊗ ∂_z \\

   .. rubric:: Identify the non-zero terms

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= δ_{xx} dx ⊗ ∂_y - δ_{yy} dy ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &= δ_{yy} dy ⊗ ∂_z - δ_{zz} dz ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= δ_{zz} dz ⊗ ∂_x - δ_{xx} dx ⊗ ∂_z \\

   .. rubric:: Conclude

   .. math::

      (∂_x ∧ ∂_y)^{♭♯} &= dx ⊗ ∂_y - dy ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &= dy ⊗ ∂_z - dz ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= dz ⊗ ∂_x - dx ⊗ ∂_z \\

   .. }}}

.. }}}

:math:`♯♭` representation
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

Symmetries of the mixed exterior product
----------------------------------------

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

The :math:`\mathfrak{so}(3)` rotation group
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
   &= a \left[ \begin{alignedat}{4}
     \; 0 & \;   & 0 & \;  & 0 \\
     \; 0 & \;   & 0 & \;- & 1 \\
     \; 0 & \; + & 1 & \;  & 0 \\
   \end{alignedat} \right]
   + b \left[ \begin{alignedat}{4}
       & 0 & \quad 0 & \; + & 1 \\
       & 0 & \quad 0 & \;   & 0 \\
     - & 1 & \quad 0 & \;   & 0 \\
   \end{alignedat} \right]
   + c \left[ \begin{alignedat}{4}
       & 0 & - & 1 & \quad 0 \\
     + & 1 &   & 0 & \quad 0 \\
       & 0 &   & 0 & \quad 0 \\
   \end{alignedat} \right]
   \end{align}

Which is `a regular choice for the basis
<https://en.m.wikipedia.org/wiki/3D_rotation_group>`_ of the
:math:`\mathfrak{so}(3)` group.

.. }}}

The cross product
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

