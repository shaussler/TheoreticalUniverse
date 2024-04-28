.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _the_cartan_hodge_formalism:

The Cartan-Hodge Formalism
==========================

.. rst-class:: custom-author

   by Stéphane Haussler

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents

   basis_vectors.rst
   musicality.rst
   hodge_duality.rst
   the_free_matrix_representation.rst
   the_exterior_derivative.rst
   the_minkowski_metric.rst

Summary
-------

In this serie of articles, I introduce the Cartan-Hodge formalism, which bundles
the notions of *tensor calculus*, *musical operators*, the *Hodge duality*, the
*free matrix representation* into a unified framework for performing
calculations and highlighting symmetries. Practical computations follow clear
and concise rules, with each step presented in a compact and comprehensible
manner. I assume the reader possesses a solid understanding of vector and tensor
calculus, as well as a working familiarity with differential forms.

.. rubric:: Basis Vectors and Covectors

The euclidean basis vectors are traditionally noted :math:`\mathbf{e}_x`,
:math:`\mathbf{e}_y`, and :math:`\mathbf{e}_z`. It can be demonstrated that the
basis vectors are the partial derivatives:

.. math::

   \mathbf{e}_i = ∂_i

Any vector can  be expressed as a linear combination of the basis vectors as

.. math::

   a \; ∂_x + b \; ∂_y + c \; ∂_z

Noticing that the differential applied to the basis vectors result in the
Kronecker :math:`δ`:

.. math::

   dx^i (∂_j) = δ^i_j

Therefore the dual basis covectors are:

.. math::

   \mathbf{e}^i = dx^i

And a covariant dual covector is expressed as linear combination of the basis
covectors:

.. math::

   a \; dx + b \; dy + c \; dz

.. rubric:: Musical Operators

With the musical flat :math:`♭` and sharp :math:`♯` symbols, covectors and
vectors are explicetely declared. For example, a contravariant three-vector is
declared with the sharp operator :math:`♯` as:

.. math::

   V^♯ = a \; ∂_x + b \; ∂_y + c \; ∂_z

The musical flat :math:`♭` and sharp :math:`♯` symbols are further utilzed as
operators to convert vectors to covectors and vice versa. For example, a
three-vector with euclidean metric :math:`δ` is flattend to a three-covector
with:

.. math::

   V^{♭} &= (V^♯)^♭                                                         \\
         &= a \; ∂_x^♭ + b \; ∂_y^♭ + c \; ∂_z^♭                            \\
         &= a \; δ_{xi} \; dx^i + b \; δ_{yi} \; dx^i + c \; δ_{zi} \; dx^i \\
         &= a \; dx + b \; dy + c \; dz                                     \\

.. rubric:: The Free Matrix Representation

With the *free matrix representation*, the vectors can be ordered into arbitray
matrix, while keeping the tensor basis is explicitly included. A vector can the
be expressed explicitly as:

.. math::

   V^♯ = \begin{bmatrix} a \; ∂_x \\ b \; ∂_y \\ c \; ∂_z \end{bmatrix}

But the representation can be freely modified the best facilitate calculations,
as the brackets acts as an operator :math:`\begin{bmatrix}\end{bmatrix}` adding
elements. As an example, the following representation of a vector is also valid:

.. math::

   V^♯ = \begin{bmatrix} a \; ∂_x & b \; ∂_y & c \; ∂_z \end{bmatrix}

.. rubric:: Hodge Duality

The Hodge duality assumes a central role, transitioning tensors between spaces
and their dual complements. Additionally, I introduce the free matrix notation
to streamline calculations, often allowing a straightforward return to matrix
multiplication.
