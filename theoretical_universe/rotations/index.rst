.. _rotations_in_differential_form:

Rotations in Differential Form
==============================

.. rst-class:: custom-author

   by Stéphane Haussler

In these articles, I express rotations in Cartan's formalism and improve on the
notation with the free matrix representation. Anti-symmetries pop out of the
Hodge star operator when ordering the differential forms into matrices, which
exactly correspond to :math:`\mathfrak{so}(3)` and :math:`\mathfrak{so}(1,3)`
matrices. Lastly, unexpectedly, we come accross the electromagnetic field
tensor.

The content in this articles might not be wildely known as I have not found my
observations mentioned anywhere. Feel free to open an issue and I will include
a reference if you are aware of one. If you find mistakes, don't hesitate to
open an issue or directly provide corrections by sending a merge request to my
`Github repository <https://github.com/shaussler/TheoreticalUniverse/>`_.

I assume the reader posses a strong grasp of vector calculus as well as working
understanding of differential forms, the wedge product, and :ref:`the concept
of the Hodge dual <hodge_duality>`. With respect to wording, I interchangeably
use the words *oriented surface*, *bivector* as they are :ref:`the same objects
<pseudo_vectors_and_pseudo_scalars>`, albeit named in different contexts.

.. rubric:: Rotations are Linear Combinations of Bivectors

Any rotation in 4-dimensional Minkowksi space is represented by a linear
combination of the 6 independent planes of rotation. These are represented with
6 basis bivectors:

.. math::

   \begin{equation}
   R^{♯♯}
   = \{
     a \; ∂_t ∧ ∂_x \\
     b \; ∂_t ∧ ∂_y \\
     c \; ∂_t ∧ ∂_z \\
     d \; ∂_y ∧ ∂_z \\
     e \; ∂_z ∧ ∂_x \\
     f \; ∂_x ∧ ∂_y \\
   \}
   \end{equation}

.. rubric:: Rotation Ordered in Row-major Matrice

Using the antisymetric properties of the wedege product :math:`∧`, we trivially
obtain the following representation for a rotation:

.. math::

   \begin{equation}
   R^{♯♯} = \frac{1}{2}
   \begin{bmatrix}
                      & + a \; ∂_t ∧ ∂_x & + b \; ∂_t ∧ ∂_y & + c \; ∂_t ∧ ∂_z \\
     - a \; ∂_x ∧ ∂_t &                  & + f \; ∂_x ∧ ∂_y & - e \; ∂_x ∧ ∂_z \\
     - b \; ∂_y ∧ ∂_t & - f \; ∂_y ∧ ∂_x &                  & + d \; ∂_y ∧ ∂_z \\
     - c \; ∂_z ∧ ∂_t & + e \; ∂_z ∧ ∂_x & - d \; ∂_z ∧ ∂_y &                  \\
   \end{bmatrix}
   \end{equation}

.. rubric:: The Time Components of Mixed Wedge Product in Spacetimme are
   Symmetric

Expressing the one time contravariant and one time covariant wedge product
:math:`∧` in term of tensor products :math:`⊗`, we obtain for the basis
elements:

============ ================== ================================= ================== =================================
Symmetry     ♭♯ basis element   Tensor expression                 ♯♭ basis element   Tensor expression
============ ================== ================================= ================== =================================
Symetric     :math:`dx^t ∧ ∂_x` :math:`+ dx^t ⊗ ∂_x + dx^x ⊗ ∂_t` :math:`∂_t ∧ dx^x` :math:`+ ∂_t ⊗ dx^x + ∂_x ⊗ dx^t`
Symetric     :math:`dx^t ∧ ∂_y` :math:`+ dx^t ⊗ ∂_y + dx^y ⊗ ∂_t` :math:`∂_t ∧ dx^y` :math:`+ ∂_t ⊗ dx^y + ∂_y ⊗ dx^t`
Symetric     :math:`dx^t ∧ ∂_z` :math:`+ dx^t ⊗ ∂_z + dx^z ⊗ ∂_t` :math:`∂_t ∧ dx^z` :math:`+ ∂_t ⊗ dx^z + ∂_z ⊗ dx^t`
Antisymetric :math:`dx^x ∧ ∂_y` :math:`+ dx^x ⊗ ∂_y - dx^y ⊗ ∂_x` :math:`∂_x ∧ dx^y` :math:`+ ∂_x ⊗ dx^y - ∂_y ⊗ dx^x`
Antisymetric :math:`dx^y ∧ ∂_z` :math:`+ dx^y ⊗ ∂_z - dx^z ⊗ ∂_y` :math:`∂_y ∧ dx^z` :math:`+ ∂_y ⊗ dx^z - ∂_z ⊗ dx^y`
Antisymetric :math:`dx^z ∧ ∂_x` :math:`+ dx^z ⊗ ∂_x - dx^x ⊗ ∂_z` :math:`∂_z ∧ dx^x` :math:`+ ∂_z ⊗ dx^x - ∂_x ⊗ dx^z`
============ ================== ================================= ================== =================================

.. rubric:: Rotations in Spacetime Match Exactly the Form of the Faraday Tensor

The row-major free matrix representation of any rotation in Minkowski space,
expressed in a mixed form:

.. math::

   \begin{align}
   R^{♭♯}
   &= \frac{1}{2}
   \begin{bmatrix}
                       & + a \; dx^t ∧ ∂_x & + b \; dx^t ∧ ∂_y & + c \; dx^t ∧ ∂_z \\
     + a \; dx^x ∧ ∂_t &                   & + f \; dx^x ∧ ∂_y & - e \; dx^x ∧ ∂_z \\
     + b \; dx^y ∧ ∂_t & - f \; dx^y ∧ ∂_x &                   & + d \; dx^y ∧ ∂_z \\
     + c \; dx^z ∧ ∂_t & + e \; dx^z ∧ ∂_x & - d \; dx^z ∧ ∂_y &                   \\
   \end{bmatrix}
   \end{align}

For comparison, the :ref:`electromagnetic field tensor
<the_tensor_of_mr_faraday>` :math:`F` is:

.. math::

   \begin{equation}
   F^{♯♭} = \frac{1}{2}
   \begin{bmatrix}
           & + \Ex & + \Ey & + \Ez \\
     + \Ex &       & + \Bz & - \By \\
     + \Ey & - \Bz &       & + \Bx \\
     + \Ez & + \By & - \Bx &       \\
   \end{bmatrix}
   \end{equation}

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

   rotations_in_3_dimensions.rst
   rotations_in_minkowski_space.rst
