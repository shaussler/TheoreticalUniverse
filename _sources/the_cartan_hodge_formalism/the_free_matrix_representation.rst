.. Theoretical Universe (c) by Stéphane Haussler

.. theoretical universe is licensed under a creative commons attribution 4.0
.. international license. you should have received a copy of the license along
.. with this work. if not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _the_free_matrix_representation:
.. _the free matrix representation:

Free matrix representation
==========================

.. rst-class:: custom-author

   by Stéphane Haussler

I hope the reader will find the *free matrix representation* intuitive. In this
representation, each matrix element is expressed using its basis vectors, basis
bivectors, and basis volumes, and can be reordered freely. The matrix brackets
:math:`[]` function as an operator, adding a :math:`+` sign between the
elements within the brackets.

Vectors
-------

.. {{{

A vector :math:`v^♯` with components :math:`a`, :math:`b`, and :math:`c`  will
most often expressed using implicit basis vectors in column form:

.. math::

   v^♯ = \begin{bmatrix}
     a \\
     b \\
     c \\
   \end{bmatrix}

A *plus* sign :math:`+` can be added to all elements multiplied by their respective
basis vectors :math:`∂_x`, :math:`∂_y`, and :math:`∂_z`:

.. math::

   v^♯ = a \, ∂_x + b \, ∂_y + c \, ∂_x

The free matrix representation proposes explicitely writing the basis in the
matrix, and order the terms as needed to organize and simplify calculations:

.. math::

   v^♯ = \begin{bmatrix}
     a \, ∂_x \\
     b \, ∂_y \\
     c \, ∂_z \\
   \end{bmatrix}

Concretely, applying a 1-form :math:`ω^♭ = e \, dx + f \, dy + g \, dz` to the
vector :math:`v^♯` result in:

.. math::

   w^♭ (v^♯) = \begin{bmatrix} e \; dx & f \; dy & g \; dz \end{bmatrix}
   \begin{bmatrix}
     a \, ∂_x \\
     b \, ∂_y \\
     c \, ∂_z \\
   \end{bmatrix}

Since the vector and covector bases are explicitely written, we can fully
reorganize the matrices and represent both the covector :math:`ω^♭` and the
vector :math:`v^♯` as column matrices. The reader will likely notice that, in
this common case, the standard notation is more convenient. However, this may
not hold true for more complex situations.

.. math::

   w^♭ (v^♯) = \begin{bmatrix}
     e \; dx \\
     f \; dy \\
     g \; dz \\
   \end{bmatrix}
   \begin{bmatrix}
     a \, ∂_x \\
     b \, ∂_y \\
     c \, ∂_z \\
   \end{bmatrix}

Distribute :math:`v^♯` to each basis covectors :math:`dx^i`:

.. math::

   w^♭ (v^♯) = \begin{bmatrix}
     e \, dx \left( a \, ∂_x + b \, ∂_y + c \, ∂_z \right) \\
     f \, dy \left( a \, ∂_x + b \, ∂_y + c \, ∂_z \right) \\
     g \, dz \left( a \, ∂_x + b \, ∂_y + c \, ∂_z \right) \\
   \end{bmatrix}

Distribute each basis vectors :math:`∂_i` to each basis covectors :math:`dx^i`:

.. math::

   w^♭ (v^♯) = \begin{bmatrix}
     e \, a \, dx ∂_x + e \, b \, dx ∂_y + e \, c \, dx ∂_z \\
     f \, a \, dy ∂_x + f \, b \, dy ∂_y + f \, c \, dy ∂_z \\
     g \, a \, dz ∂_x + g \, b \, dz ∂_y + g \, c \, dz ∂_z \\
   \end{bmatrix}

With :math:`dx^i ∂_j = δ^i_j`, most terms cancel and we obtain:

.. math::

   w^♭ (v^♯) = \begin{bmatrix}
     e \, a \, dx ∂_x \\
     f \, b \, dy ∂_y \\
     g \, c \, dz ∂_z \\
   \end{bmatrix}
   = \begin{bmatrix}
     e \, a \\
     f \, b \\
     g \, c \\
   \end{bmatrix}

In other words we obtain the rules for the dot product, as we certainly
expected:

.. math::

   w^♭ (v^♯) = e\;a + f\;b +g\;c

The calculations above are provided in exhaustive detail to illustrate a key
point. By incorporating basis vectors and basis covectors into their matrix
representation, we can organize and simplify calculations. This is achieved by
arranging the components of covectors into rows and the components of vectors
into columns, allowing us to follow matrix multiplication rules. While the
result is straightforward in this example, the approach remains valid and
effective even for more complex cases involving doubly covariant tensors.

.. }}}

Bivectors
---------

.. {{{

This is powerfull when using a pseudo-vector or pseudo-scalar basis, since the
elements of the matrix can be re-ordered at will. For example, if we consider
a linear combination of two forms in Euclidean space, we can write:

.. math::

   R^{♯♯} = \begin{bmatrix}
     a \; ∂_y ∧ ∂_z \\
     b \; ∂_z ∧ ∂_x \\
     c \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

But also, since :math:`∂_i ∧ ∂_j = - ∂_j ∧ ∂_i`:

.. math::

   R^{♯♯} = \frac{1}{2} \begin{bmatrix}
     a \; ∂_y ∧ ∂_z  - a \; ∂_z ∧ ∂_y \\
     b \; ∂_z ∧ ∂_x  - b \; ∂_x ∧ ∂_z \\
     c \; ∂_x ∧ ∂_y  - c \; ∂_y ∧ ∂_x \\
   \end{bmatrix}

Which can be reordered into an arbitray matrix, for example using a row/column
matrix representation:

.. math::

   R^{♯♯} = \frac{1}{2} \begin{bmatrix}
                      & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
     + c \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
     - b \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &               \\
   \end{bmatrix}

All above matrix representations merely mean:

.. math::

   R^{♯♯} a \; ∂_y ∧ ∂_z + b \; ∂_z ∧ ∂_x + c \; ∂_x ∧ ∂_y

.. }}}

Matrix multiplication
---------------------

.. {{{

We consider now the :math:`♭♯` representation of :math:`R` because this object
takes in a vector, and outputs a vector. See :ref:`here <♭♯ representation>`
for a detailed calculation. The core of this section is to point out that we
can order :math:`R^{♭♯}` using the `row-major convention
<https://en.m.wikipedia.org/wiki/Row-_and_column-major_order>`_:

.. math::

   R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                     & - c \; dy ∧ ∂_x & + b \; dz ∧ ∂_x \\
     + c \; dx ∧ ∂_y &                 & - a \; dz ∧ ∂_y \\
     - b \; dx ∧ ∂_z & + a \; dy ∧ ∂_z &                 \\
   \end{bmatrix}

We fall back to Matrix multiplication rules. Consider a vector :math:`v^♯ = v^x
∂_x + v^y ∂_y + v^z ∂_z`, to which is applied the :math:`R^{♭♯}` matrix. We
fully expand and distribute each component to prove that indeed, we could have
followed matrix multiplication rules, using an implicit basis.

Apply the rotation matrix :math:`R^{♭♯}` to the vector :math:`v^♯`

.. math::

   R^{♭♯} v^♯ = \frac{1}{2} \begin{bmatrix}
                     & - c \; dy ∧ ∂_x & + b \; dz ∧ ∂_x \\
     + c \; dx ∧ ∂_y &                 & - a \; dz ∧ ∂_y \\
     - b \; dx ∧ ∂_z & + a \; dy ∧ ∂_z &                 \\
   \end{bmatrix}
   \begin{bmatrix} v^x ∂_x \\ v^y ∂_y \\ v^z ∂_z \\ \end{bmatrix}

Fully expand and distribute the vector :math:`v^♯` to each element of the
matrix:

.. math::

   R^{♭♯} v^♯ = \frac{1}{2} \begin{bmatrix}
                                                   & - c \; dy (v^x ∂_x + v^y ∂_y + v^z ∂_z) ∧ ∂_x & + b \; dz (v^x ∂_x + v^y ∂_y + v^z ∂_z) ∧ ∂_x \\
     + c \; dx (v^x ∂_x + v^y ∂_y + v^z ∂_z) ∧ ∂_y &                                               & - a \; dz (v^x ∂_x + v^y ∂_y + v^z ∂_z) ∧ ∂_y \\
     - b \; dx (v^x ∂_x + v^y ∂_y + v^z ∂_z) ∧ ∂_z & + a \; dy (v^x ∂_x + v^y ∂_y + v^z ∂_z) ∧ ∂_z &                                               \\
   \end{bmatrix}

Apply the differential to the partial derivatives :math:`dx^i ∂_j = δ^i_j`:

.. math::

   R^{♭♯} v^♯ = \frac{1}{2} \begin{bmatrix}
                    & - c \; v^y ∂_x & + b \; v^z ∂_x \\
     + c \; v^x ∂_y &                & - a \; v^z ∂_y \\
     - b \; v^x ∂_z & + a \; v^y ∂_z &                \\
   \end{bmatrix}

Reorder into a column vector:

.. math::

   R^{♭♯} v^♯ = \frac{1}{2} \begin{bmatrix}
     (- c \; v^y + b \; v^z) ∂_x \\
     (+ c \; v^x - a \; v^z) ∂_y \\
     (- b \; v^x + a \; v^y) ∂_z \\
   \end{bmatrix}

Indeed, we arrive at the result we would have obtained using matrix
multiplication rules. This clarifies and justifies matrix multiplication rules,
as well as provide a way to organize tensors of any rank into matrices in order
to facilitate practical calculations. This comes at the cost of having to
explicitely write the basis, which arguably improves on readability and is more
explicit. We could have written a covector in the same explicit manner. This
notation is very convenient when performing calculations in the Cartan-Hodge
formalism as it permits to identify and organize terms for practical
calculations, and if needed fall back to regular matrix multiplication.

.. }}}
