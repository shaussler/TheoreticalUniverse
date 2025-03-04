.. _rotations_in_differential_form:
.. _rotations in differential form:

Rotations in differential form
==============================

.. rst-class:: custom-author

   by Stéphane Haussler

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents

   rotations_in_3_dimensions.rst
   rotations_in_minkowski_space.rst

In the following pages, I systematically express infinitesimal rotations in
both 3-dimensional Euclidean and Minkowski space. The ultimate purpose is to
establish the relation of the electromagnetic field to infinitesimal rotations
in spacetime.

The components of these infinitesimal rotations, expressed as differential
2-forms, will be arranged into matrices. The anti-symmetries will be explicit,
emerging the exterior product :math:`∧`. I will demonstrate the exact relation
to :math:`\mathfrak{so}(3)` and :math:`\mathfrak{so}(1,3)` matrices.

I assume the reader understands tensor calculus and the exterior product
:math:`∧`, as well as familiarity with :ref:`Hodge duality <hodge duality>`.

.. rubric:: Rotations are Linear Combinations of Bivectors

Any rotation in 3-dimensional Euclidean space is represented by a linear
combination of the 3 independent planes of rotation. These are represented with
3 basis bivectors:

.. math::

   R^{♯♯} = \begin{bmatrix}
       R^{x} \; ∂_y ∧ ∂_z \\
       R^{y} \; ∂_z ∧ ∂_x \\
       R^{z} \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

Any rotation in 4-dimensional Minkowksi space is represented by a linear
combination of the 6 independent planes of rotation. These are represented with
6 basis bivectors:

.. math::

   R^{♯♯}= \begin{bmatrix}
       Q^{x} \; ∂_t ∧ ∂_x \\
       Q^{y} \; ∂_t ∧ ∂_y \\
       Q^{z} \; ∂_t ∧ ∂_z \\
       R^{x} \; ∂_y ∧ ∂_z \\
       R^{y} \; ∂_z ∧ ∂_x \\
       R^{z} \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

Equivalently, rotations in spacetime can be represented by linear combinations
of 6 basis bicovectors:

.. math::

   R^{♭♭} = \left[ \begin{aligned}
       - & Q^{x} \; dt ∧ dx \\
       - & Q^{y} \; dt ∧ dy \\
       - & Q^{z} \; dt ∧ dz \\
         & R^{x} \; dy ∧ dz \\
         & R^{y} \; dz ∧ dx \\
         & R^{z} \; dx ∧ dy \\
   \end{aligned} \right]

.. rubric:: Matrice Representation of the Mixed Exterior Product

The row-major free matrix representation of any rotation in Minkowski space,
expressed in a mixed form is:

.. math::

   R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                     & + a \; dt ∧ ∂_x & + b \; dt ∧ ∂_y & + c \; dt ∧ ∂_z \\
     + a \; dx ∧ ∂_t &                 & + f \; dx ∧ ∂_y & - e \; dx ∧ ∂_z \\
     + b \; dy ∧ ∂_t & - f \; dy ∧ ∂_x &                 & + d \; dy ∧ ∂_z \\
     + c \; dz ∧ ∂_t & + e \; dz ∧ ∂_x & - d \; dz ∧ ∂_y &                 \\
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
