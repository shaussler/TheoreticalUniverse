.. _rotations_in_differential_form:
.. _rotations in differential form:

Rotations in Differential Form
==============================

.. rst-class:: custom-author

   by Stéphane Haussler

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents

   rotations_in_3_dimensions.rst
   rotations_in_minkowski_space.rst

In the following pages, I express rotations in 3-dimensional Euclidean as well
as in 4-dimensional Minkowski space, utilizing :ref:`the Cartan-Hodge
formalism`. Anti-symmetries emerge from the Hodge star operator when arranging
the differential forms into matrices, which exactly correspond to
:math:`\mathfrak{so}(3)` and :math:`\mathfrak{so}(1,3)` matrices. Finally, we
establish the identification of the electromagnetic field tensor.

.. rubric:: Rotations are Linear Combinations of Bivectors

Any rotation in 3-dimensional Euclidean space is represented by a linear
combination of the 3 independent planes of rotation. These are represented with
3 basis bivectors:

.. math::

   R^{♯♯} = \begin{bmatrix}
     a \; ∂_y ∧ ∂_z \\
     b \; ∂_z ∧ ∂_x \\
     c \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

Any rotation in 4-dimensional Minkowksi space is represented by a linear
combination of the 6 independent planes of rotation. These are represented with
6 basis bivectors:

.. math::

   R^{♯♯}= \begin{bmatrix}
     a \; ∂_t ∧ ∂_x \\
     b \; ∂_t ∧ ∂_y \\
     c \; ∂_t ∧ ∂_z \\
     d \; ∂_y ∧ ∂_z \\
     e \; ∂_z ∧ ∂_x \\
     f \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

Equivalently, rotations in spacetime can be represented by linear combinations
of 6 basis bicovectors:

.. math::

   R^{♭♭} = \left[ \begin{aligned}
     - & a \; dt ∧ dx \\
     - & b \; dt ∧ dy \\
     - & c \; dt ∧ dz \\
       & d \; dy ∧ dz \\
       & e \; dz ∧ dx \\
       & f \; dx ∧ dy \\
   \end{aligned} \right]

.. rubric:: Matrice Representation of the Mixed Exterior Product

The row-major free matrix representation of any rotation in Minkowski space,
expressed in a mixed form is:

.. math::

   R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                       & + a \; dx^t ∧ ∂_x & + b \; dx^t ∧ ∂_y & + c \; dx^t ∧ ∂_z \\
     + a \; dx^x ∧ ∂_t &                   & + f \; dx^x ∧ ∂_y & - e \; dx^x ∧ ∂_z \\
     + b \; dx^y ∧ ∂_t & - f \; dx^y ∧ ∂_x &                   & + d \; dx^y ∧ ∂_z \\
     + c \; dx^z ∧ ∂_t & + e \; dx^z ∧ ∂_x & - d \; dx^z ∧ ∂_y &                   \\
   \end{bmatrix}

Readers well versed in the tensor formulations of electromagnetism will
recognise the mixed form of the :ref:`electromagnetic field tensor
<the_tensor_of_mr_faraday>`.

.. rubric:: Symmetries of the Mixed Exterior Product in Minkowski Space

Expressing the mixed exterior product :math:`∧` in term of tensor products
:math:`⊗`, we demonstrate that the mixed exterior product is not fully
antisymmetric in Minkowski space. However, the total number of symmetries is
equal. We obtain:

============ =============================
Symmetry     Basis elements
============ =============================
Symetric     :math:`dt ∧ ∂_x = + dx ∧ ∂_t`
Symetric     :math:`dt ∧ ∂_y = + dy ∧ ∂_t`
Symetric     :math:`dt ∧ ∂_z = + dz ∧ ∂_t`
Antisymetric :math:`dy ∧ ∂_z = - dz ∧ ∂_y`
Antisymetric :math:`dz ∧ ∂_x = - dx ∧ ∂_z`
Antisymetric :math:`dx ∧ ∂_y = - dy ∧ ∂_x`
============ =============================
