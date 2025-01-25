.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _the_cartan_hodge_formalism:
.. _the Cartan-Hodge formalism:

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
   the_minkowski_metric.rst

This part introduces the Cartan-Hodge formalism, which bundles the notions of
*tensor calculus*, *musical operators*, *Hodge duality*, *exterior derivative*,
and the *free matrix representation* into a comprehensive framework of notation
and mathematical tools. Practical computations follow clear and concise rules,
with each step presented in a compact and comprehensible manner. The objective
is also to depart from the abstract index notation of tensor calculus,
eliminate the need for the Levi-Civita symbol, and expand tensor equations to
their component from, all while adhering to standard and widespread notations.

This is not a comprehensive introduction into these subjects, but recalls basic
definitions and properties necessary to perform calculations. I assume the
reader possesses a solid understanding of vector and tensor calculus, as well
as a working familiarity with Cartan's differential forms and the exterior
derivative.

I also here highlight and point out :ref:`the article on Hodge duality <hodge
duality>` can be read as a self-contained article and may be of interest to the
reader on its own.

Basis vectors
-------------

.. {{{

The Euclidean basis vectors are traditionally noted :math:`\mathbf{e}_x`,
:math:`\mathbf{e}_y`, and :math:`\mathbf{e}_z`. It can be demonstrated that the
basis vectors are the partial derivatives:

.. math:: \mathbf{e}_i = ∂_i

Any vector can  be expressed as a linear combination of the basis vectors as:

.. math:: a \; ∂_x + b \; ∂_y + c \; ∂_z

The differential applied to the basis vectors results in the Kronecker
:math:`δ`:

.. math:: dx^i (∂_j) = δ^i_j

Therefore the dual basis covectors are:

.. math::

   \mathbf{e}^i = dx^i

And a covariant dual covector is expressed as linear combination of the basis
covectors:

.. math:: a \; dx + b \; dy + c \; dz

.. }}}

Musicality
----------

.. {{{

With the musical flat :math:`♭` and sharp :math:`♯` symbols, covectors and
vectors are explicetely declared. For example, a contravariant three-vector is
declared with the sharp operator :math:`♯` as:

.. math:: V^♯ = a \; ∂_x + b \; ∂_y + c \; ∂_z

The musical flat :math:`♭` and sharp :math:`♯` symbols are further utilzed as
operators converting vectors to covectors and vice versa. For example, a
three-vector with euclidean metric :math:`δ` is flattend to a three-covector
with:

.. math::

   V^{♭} &= (V^♯)^♭                                                         \\
         &= a \; ∂_x^♭ + b \; ∂_y^♭ + c \; ∂_z^♭                            \\
         &= a \; δ_{xi} \; dx^i + b \; δ_{yi} \; dx^i + c \; δ_{zi} \; dx^i \\
         &= a \; dx + b \; dy + c \; dz                                     \\

.. }}}

The free matrix representation
------------------------------

.. {{{

With the *free matrix representation*, vectors can be ordered into arbitray
matrix, while keeping the tensor basis is explicitly included. A vector can the
be expressed explicitly as:

.. math::

   V^♯ = \begin{bmatrix}
     a \; ∂_x \\
     b \; ∂_y \\
     c \; ∂_z \\
   \end{bmatrix}

The representation can be freely modified to best facilitate calculations, with
the brackets acting as an operator :math:`\begin{bmatrix}\end{bmatrix}` adding
elements together. As an example, the following row representation of a vector is
also valid in the free matrix representation:

.. math::

   V^♯ = \begin{bmatrix} a \; ∂_x & b \; ∂_y & c \; ∂_z \end{bmatrix}

.. }}}

Hodge duality
-------------

Inner product of k-forms in Minkowski space
'''''''''''''''''''''''''''''''''''''''''''

.. {{{

The inner product of k-forms in Minkowski space are calculated for the basis
vectors, bivectors, trivectors and quadvectors and summarized here in table
form.

----

.. math::

   \begin{array}{c|rrrr}
           & ∂_t & ∂_x & ∂_y & ∂_z \\
       \hline
       ∂_t & +1  &  0  &  0  &  0  \\
       ∂_x &  0  & -1  &  0  &  0  \\
       ∂_y &  0  &  0  & -1  &  0  \\
       ∂_z &  0  &  0  &  0  & -1  \\
   \end{array}

----

.. math::

   \begin{array}{c|rrrrrr}
             & ∂_t ∧ ∂_x & ∂_t ∧ ∂_y & ∂_t ∧ ∂_z & ∂_y ∧ ∂_z & ∂_z ∧ ∂_x & ∂_x ∧ ∂_y \\
             \hline
   ∂_t ∧ ∂_x & -1        &  0        &  0        &   0       &  0        &  0        \\
   ∂_t ∧ ∂_y &  0        & -1        &  0        &   0       &  0        &  0        \\
   ∂_t ∧ ∂_z &  0        &  0        & -1        &   0       &  0        &  0        \\
   ∂_y ∧ ∂_z &  0        &  0        &  0        &  +1       &  0        &  0        \\
   ∂_z ∧ ∂_x &  0        &  0        &  0        &   0       & +1        &  0        \\
   ∂_x ∧ ∂_y &  0        &  0        &  0        &   0       &  0        & +1        \\
   \end{array}

----

.. math::

   \begin{array}{c|rrrr}
                   & ∂_x ∧ ∂_y ∧ ∂_z & ∂_t ∧ ∂_y ∧ ∂_z & ∂_t ∧ ∂_z ∧ ∂_x & ∂_t ∧ ∂_x ∧ ∂_y \\
                   \hline
   ∂_x ∧ ∂_y ∧ ∂_z & -1              &  0              &   0             &   0             \\
   ∂_t ∧ ∂_y ∧ ∂_z &  0              & +1              &   0             &   0             \\
   ∂_t ∧ ∂_z ∧ ∂_x &  0              &  0              &  +1             &   0             \\
   ∂_t ∧ ∂_x ∧ ∂_y &  0              &  0              &   0             &  +1             \\
   \end{array}

----

.. math::

   \begin{array}{c|c}
                             & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\
       \hline
       ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z &                    -1 \\
   \end{array}


----

.. }}}

.. _hodge dual tables:

Hodge dual tables
'''''''''''''''''

.. {{{

The Hodge duality assumes a central role, transitioning tensors between spaces
and their dual complements.

.. math::

   ⋆ dt & = dx ∧ dy ∧ dz \\
   ⋆ dx & = dt ∧ dy ∧ dz \\
   ⋆ dy & = dt ∧ dz ∧ dx \\
   ⋆ dz & = dt ∧ dx ∧ dy \\

----

.. math::

   \begin{alignedat}{2}
   ⋆ dt ∧ dx &= -& dy ∧ dz \\
   ⋆ dt ∧ dy &= -& dz ∧ dx \\
   ⋆ dt ∧ dz &= -& dx ∧ dy \\
   ⋆ dy ∧ dz &=  & dt ∧ dx \\
   ⋆ dz ∧ dx &=  & dt ∧ dy \\
   ⋆ dx ∧ dy &=  & dt ∧ dz \\
   \end{alignedat}

----

.. math::

   ⋆ dx ∧ dy ∧ dz &= dt \\
   ⋆ dt ∧ dy ∧ dz &= dx \\
   ⋆ dt ∧ dz ∧ dx &= dy \\
   ⋆ dt ∧ dx ∧ dy &= dz \\

----

.. math::

   ⋆ dt ∧ dx ∧ dy ∧ dz = - 1

.. }}}
