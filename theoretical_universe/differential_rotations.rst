Rotations in the Cartan-Hodge Formalism
=======================================

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
of the Hodge dual <formalism_hodge_dual:Hodge Duality>`. With respect to
wording, I interchangeably use the words *oriented surface*, *bivector* as they
are :ref:`the same objects <formalism_hodge_dual:Pseudo vectors and pseudo
scalars>`, albeit named in different contexts.

TL;DR Too long; didn't read
---------------------------

.. rubric:: Rotations are bivectors

Any rotation in 3 dimensional or Minkowksi space is represented by a linear
combination of the basis bivectors:

.. math::

   \begin{equation}
   R^{♯♯}
   = \{
     a \; ∂_t ∧ ∂_x \\
     b \; ∂_t ∧ ∂_y \\
     c \; ∂_t ∧ ∂_z \\
     d \; ∂_x ∧ ∂_y \\
     e \; ∂_y ∧ ∂_z \\
     f \; ∂_z ∧ ∂_x \\
   \}
   \end{equation}

.. rubric:: Rotations can be order in row-major matrices

Using the antisymetric properties of the wedege product :math:`∧`, we trivially
obtain the following representation for a rotation:

.. math::

   \begin{equation}
   R^{♯♯} = \frac{1}{2}
   \begin{bmatrix}
                     & + a \; ∂_t ∧ ∂_x & + b \; ∂_t ∧ ∂_y & + c \; ∂_t ∧ ∂_z \\
     - a \; ∂_ ∧ ∂_t &                  & + d \; ∂_x ∧ ∂_y & - f \; ∂_x ∧ ∂_z \\
     - b \; ∂_ ∧ ∂_t & - d \; ∂_y ∧ ∂_x &                  & + e \; ∂_y ∧ ∂_z \\
     - c \; ∂_ ∧ ∂_t & + f \; ∂_z ∧ ∂_x & - e \; ∂_z ∧ ∂_y &                  \\
   \end{bmatrix}
   \end{equation}

.. rubric:: The components of mixed wedge product can be symmetric in Minkowski
   space

Expressing the one time contravariant and one time covartiant wedge product
:math:`\wedge` in term of tensor products :math:`\otimes`, we obtain for the
basis elements:

================== ============ =================================
Basis element      Symmetry     Expression
================== ============ =================================
:math:`dx^t ∧ ∂_x` Symetric     :math:`+ dx^t ⊗ ∂_x + dx^x ⊗ ∂_t`
:math:`dx^t ∧ ∂_y` Symetric     :math:`+ dx^t ⊗ ∂_y + dx^y ⊗ ∂_t`
:math:`dx^t ∧ ∂_z` Symetric     :math:`+ dx^t ⊗ ∂_z + dx^z ⊗ ∂_t`
:math:`dx^x ∧ ∂_y` Antisymetric :math:`+ dx^x ⊗ ∂_y - dx^y ⊗ ∂_x`
:math:`dx^y ∧ ∂_z` Antisymetric :math:`+ dx^y ⊗ ∂_z - dx^z ⊗ ∂_y`
:math:`dx^z ∧ ∂_x` Antisymetric :math:`+ dx^z ⊗ ∂_x - dx^x ⊗ ∂_z`
:math:`∂_t ∧ dx^x` Symetric     :math:`+ ∂_t ⊗ dx^x + ∂_x ⊗ dx^t`
:math:`∂_t ∧ dx^y` Symetric     :math:`+ ∂_t ⊗ dx^y + ∂_y ⊗ dx^t`
:math:`∂_t ∧ dx^z` Symetric     :math:`+ ∂_t ⊗ dx^z + ∂_z ⊗ dx^t`
:math:`∂_x ∧ dx^y` Antisymetric :math:`+ ∂_x ⊗ dx^y - ∂_y ⊗ dx^x`
:math:`∂_y ∧ dx^z` Antisymetric :math:`+ ∂_y ⊗ dx^z - ∂_z ⊗ dx^y`
:math:`∂_z ∧ dx^x` Antisymetric :math:`+ ∂_z ⊗ dx^x - ∂_x ⊗ dx^z`
================== ============ =================================

.. rubric:: Rotations in Minkowski space match exactly the Faraday tensor

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

The electromagnetic field tensor :math:`F` is:

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

.. rubric:: Rotations in Cartan's formalism trivially match the Lie Algegra of the Lorentz group

one. two.

.. toctree::
   :maxdepth: 2

   differential_rotations_3d.rst
   differential_rotations_4d.rst
