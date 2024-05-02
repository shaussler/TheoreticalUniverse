.. _the_free_matrix_representation:

The Free Matrix Representation
==============================

.. rst-class:: custom-author

   by Stéphane Haussler

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

Which means that a :math:`+` sign can be added anywhere in the matrix and the
expression written in the standard form:

.. math::

   v = a \; ∂_x + b \; ∂_y + c \; ∂_x

This is powerfull when using a pseudo-vector or pseudo-scalar basis, since the
elements of the matrix can be re-ordered at will.

.. math::

   \frac{1}{2}\begin{bmatrix}
                             & + a^{xy} \; ∂_x ∧ ∂_y & - a^{zx} \; ∂_x ∧ ∂_z \\
       - a^{xy} \; ∂_y ∧ ∂_x &                       & + a^{yz} \; ∂_y ∧ ∂_z \\
       + a^{zx} \; ∂_z ∧ ∂_x & - a^{yz} \; ∂_z ∧ ∂_y &                       \\
   \end{bmatrix}
   = \begin{bmatrix}
       + a^{yz} \; ∂_y ∧ ∂_z \\
       + a^{zx} \; ∂_z ∧ ∂_x \\
       + a^{xy} \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

The transpose can be taken if it permits to use the usual rules of matrix
multiplication:

.. math::

   \frac{1}{2} \begin{bmatrix}
                             & - a^{xy} \; ∂_y ∧ ∂_x & + a^{zx} \; ∂_z ∧ ∂_x \\
       + a^{xy} \; ∂_x ∧ ∂_y &                       & - a^{yz} \; ∂_z ∧ ∂_y \\
       - a^{zx} \; ∂_x ∧ ∂_z & + a^{yz} \; ∂_y ∧ ∂_z &                       \\
   \end{bmatrix}

All above matrix representations can writen as a sum:

.. math::

   a^{yz} \; ∂_y ∧ ∂_z +
   a^{zx} \; ∂_z ∧ ∂_x +
   a^{xy} \; ∂_x ∧ ∂_y

We could have written a covector in the same explicit manner. This notation is
very conveniant when performing calculations in Cartan's framework as it
permits to identify and organize terms for practical calculations, and if
needed fall back to regular matrix multiplication.
