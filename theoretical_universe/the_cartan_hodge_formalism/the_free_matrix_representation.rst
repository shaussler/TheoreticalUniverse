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

.. warning:: Under construction

Vectors
-------

.. {{{

I hope the reader will find the *free matrix representation* obvious.
Everything in a matrix is expressed with its basis vectors and can be reordered
at will. For example, a vector is can expressed with an implicit basis as:

.. math::

   v = \begin{bmatrix}
       a \\
       b \\
       c \\
   \end{bmatrix}

I merely propose to write the basis explicitely in the matrix:

.. math::

   v = \begin{bmatrix}
       a \; ∂_x \\
       b \; ∂_y \\
       c \; ∂_x \\
   \end{bmatrix}

.. }}}

Bivectors
---------

.. {{{

Which means that a :math:`+` sign can be added anywhere in the matrix and the
expression written in the standard form:

.. math::

   v = a \; ∂_x + b \; ∂_y + c \; ∂_x

This is powerfull when using a pseudo-vector or pseudo-scalar basis, since the
elements of the matrix can be re-ordered at will.

.. math::

   R^{♯♯} = \begin{bmatrix}
     a \; ∂_y ∧ ∂_z \\
     b \; ∂_z ∧ ∂_x \\
     c \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

.. math::

   R^{♯♯} = \frac{1}{2} \begin{bmatrix}
                    & - c \; ∂_y ∧ ∂_x & + b \; ∂_z ∧ ∂_x \\
   + c \; ∂_x ∧ ∂_y &                  & - a \; ∂_z ∧ ∂_y \\
   - b \; ∂_x ∧ ∂_z & + a \; ∂_y ∧ ∂_z &               \\
   \end{bmatrix}

.. }}}

The Rules of Matrix Multiplication
----------------------------------

.. {{{

The transpose can be taken if it permits to use the usual rules of matrix
multiplication:

.. math::

   R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                   & - c \; dy ∧ ∂_x & + b \; dz ∧ ∂_x \\
   + c \; dx ∧ ∂_y &                 & - a \; dz ∧ ∂_y \\
   - b \; dx ∧ ∂_z & + a \; dy ∧ ∂_z &                 \\
   \end{bmatrix}

All above matrix representations can writen as a sum:

.. math::

   a \; ∂_y ∧ ∂_z +
   b \; ∂_z ∧ ∂_x +
   c \; ∂_x ∧ ∂_y

We could have written a covector in the same explicit manner. This notation is
very conveniant when performing calculations in Cartan's framework as it
permits to identify and organize terms for practical calculations, and if
needed fall back to regular matrix multiplication.

.. }}}

.. ifconfig:: draft in ('yes')

   .. warning:: Draft

   Representing Contractions
   -------------------------

   .. {{{

   .. math::

      \begin{equation}
      \begin{bmatrix} a \; ∂_t & b \; ∂_x & c \; ∂_y & d \; ∂_z \end{bmatrix}
      \begin{bmatrix}
        + dx^t ⊗ dx^t \\
        - dx^x ⊗ dx^x \\
        - dx^y ⊗ dx^y \\
        - dx^z ⊗ dx^z \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        + a \braket{∂_t|dx^t ⊗ dx^t} \\
        + b \braket{∂_x|dx^x ⊗ dx^x} \\
        + c \braket{∂_y|dx^y ⊗ dx^y} \\
        + d \braket{∂_z|dx^z ⊗ dx^z} \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        + a \braket{∂_t|dx^t} dx^t \\
        + b \braket{∂_x|dx^x} dx^x \\
        + c \braket{∂_y|dx^y} dx^y \\
        + d \braket{∂_z|dx^z} dx^z \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        + a dx^t \\
        - b dx^x \\
        - c dx^y \\
        - d dx^z \\
      \end{bmatrix}
      \end{equation}

   .. }}}
