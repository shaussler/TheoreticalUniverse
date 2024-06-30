.. Theoretical Universe (c) by Stéphane Haussler

.. theoretical universe is licensed under a creative commons attribution 4.0
.. international license. you should have received a copy of the license along
.. with this work. if not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _the_free_matrix_representation:
.. _the free matrix representation:

The Free Matrix Representation
==============================

.. rst-class:: custom-author

   by Stéphane Haussler

I hope the reader will find the *free matrix representation* obvious. In free
matrix representation, everything in a matrix is expressed with its basis
vectors, basis bivectors, basis volumes, and can be reordered at will. The
matrix bracket :math:`[]` act as an opertor adding a :math:`+` sign between
elements.

Vectors
-------

.. {{{

For example, a vector :math:`v^♯` can be expressed with an implicit
basis as:

.. math::

   v^♯ = \begin{bmatrix}
     a \\
     b \\
     c \\
   \end{bmatrix}

Which means that a :math:`+` sign can be added anywhere in the matrix and the
expression written in the standard form:

.. math::

   v^♯ = a \; ∂_x + b \; ∂_y + c \; ∂_x

The free matrix representation proposses to write the basis explicitely in the
matrix, and order the terms as needed to organize and simplify calculations:

.. math::

   v^♯ = \begin{bmatrix}
     a \; ∂_x \\
     b \; ∂_y \\
     c \; ∂_z \\
   \end{bmatrix}

Practically, applygin a one-form :math:`ω^♭ = e dx + f dy + g dz` to the 
vector :math:`v^♯` result in:

.. math::

   w^♭ (v^♯) &= \begin{bmatrix} e \; dx & f \; dy & g \; dz \end{bmatrix}
   \begin{bmatrix}
     a \; ∂_x \\
     b \; ∂_y \\
     c \; ∂_z \\
   \end{bmatrix} \\
   w^♭ (v^♯) &= \begin{bmatrix}
     e \; dx \left[ a \; ∂_x + b \; ∂_y + c \; ∂_z \right] \\
     f \; dy \left[ a \; ∂_x + b \; ∂_y + c \; ∂_z \right] \\
     g \; dz \left[ a \; ∂_x + b \; ∂_y + c \; ∂_z \right] \\
   \end{bmatrix}

Distributing all terms and using the fact that :math:`dx^i ∂_j = δ^i_j`, we
obtain the rules for covector/vector multiplication, the dot product:

.. math::

   w^♭ (v^♯) = e\;a + f\;b +g\;c

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

Matrix Multiplication
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
notation is very conveniant when performing calculations in the Cartan-Hodge
formalism as it permits to identify and organize terms for practical
calculations, and if needed fall back to regular matrix multiplication.

.. }}}
