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
of the Hodge dual <hodge_dual:The Hodge Dual>`. With respect to wording, I
interchangeably use the words *oriented surface*, *bivector* and
*pseudo-vectors* as they are :ref:`the same objects <hodge_dual:Pseudo vectors
and pseudo scalars>`, albeit named in different contexts.

.. toctree::
   :maxdepth: 2

   differential_rotations_3d.rst
   differential_rotations_4d.rst

TL;DR
-----

.. rubric:: Rotations are bivectors

Any rotation in Minkowksi space is represented by a linear combination of the
basis bivectors:

.. math::

   \begin{equation}
   B^{♯♯}
   = \{
     F^{tx} \; ∂_t ∧ ∂_x \\
     F^{ty} \; ∂_t ∧ ∂_y \\
     F^{tz} \; ∂_t ∧ ∂_z \\
     F^{xy} \; ∂_x ∧ ∂_y \\
     F^{yz} \; ∂_y ∧ ∂_z \\
     F^{zx} \; ∂_z ∧ ∂_x \\
   \}
   \end{equation}

.. rubric:: Rotations can be order in row-major matrices

Using the antisymetric properties of the wedege product :math:`\wedge`, we
trivially obtain the following representation for a rotation:

.. math::

   \begin{align}
   B^{\sharp\sharp}
   &= \frac{1}{2}
   \{
                         & + F^{tx} ∂_t ∧ ∂_x & + F^{ty} ∂_t ∧ ∂_y & + F^{tz} ∂_t ∧ ∂_z \\
       - F^{tx} ∂_ ∧ ∂_t &                    & + F^{xy} ∂_x ∧ ∂_y & - F^{zx} ∂_x ∧ ∂_z \\
       - F^{ty} ∂_ ∧ ∂_t & - F^{xy} ∂_y ∧ ∂_x &                    & + F^{yz} ∂_y ∧ ∂_z \\
       - F^{tz} ∂_ ∧ ∂_t & + F^{zx} ∂_z ∧ ∂_x & - F^{yz} ∂_z ∧ ∂_y &                    \\
   \}
   \end{align}

.. rubric:: The components of the Rank(1,1) wedge product can be symmetric in
   Minkowski space

Expressing the one time contravariant and one time covartiant wedge product
:math:`\wedge` in term of tensor products :math:`\otimes`, we obtain for the
basis elements:

.. warning::

   Typo. Correction needed

================== ============ =================================
Basis element      Symmetry     Expression
================== ============ =================================
:math:`∂_t ∧ dx^x` Symetric     :math:`+ dx^t ⊗ ∂_x + dx^x ⊗ ∂_t`
:math:`∂_t ∧ dx^y` Symetric     :math:`+ dx^t ⊗ ∂_y + dx^y ⊗ ∂_t`
:math:`∂_t ∧ dx^z` Symetric     :math:`+ dx^t ⊗ ∂_z + dx^z ⊗ ∂_t`
:math:`∂_x ∧ dx^y` Antisymetric :math:`+ dx^x ⊗ ∂_y - dx^y ⊗ ∂_x`
:math:`∂_y ∧ dx^z` Antisymetric :math:`+ dx^y ⊗ ∂_z - dx^z ⊗ ∂_y`
:math:`∂_z ∧ dx^x` Antisymetric :math:`+ dx^z ⊗ ∂_x - dx^x ⊗ ∂_z`
================== ============ =================================

.. rubric:: Rotations in Minkowski space match exactly the Faraday tensor

The row-major free matrix representation of any rotation in Minkowski space,
expressed in a contravariant/coveriant form is:

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \{
                         & - F^{tx} ∂_t ∧ dx^x & - F^{ty} ∂_t ∧ dx^y & - F^{tz} ∂_t ∧ dx^z \\
     - F^{tx} ∂_x ∧ dx^t &                     & - F^{xy} ∂_x ∧ dx^y & + F^{zx} ∂_x ∧ dx^z \\
     - F^{ty} ∂_y ∧ dx^t & + F^{xy} ∂_y ∧ dx^x &                     & - F^{yz} ∂_y ∧ dx^z \\
     - F^{tz} ∂_z ∧ dx^t & - F^{zx} ∂_z ∧ dx^x & + F^{yz} ∂_z ∧ dx^y &                     \\
   \}
   \end{align}

The electromagnetic field tensor :math:`F` is:

.. math::

   F^{♯♭} =
   \frac{1}{2}
   \begin{bmatrix}
           & + \Ex & + \Ey & + \Ez \\
     + \Ex &       & + \Bz & - \By \\
     + \Ey & - \Bz &       & + \Bx \\
     + \Ez & + \By & - \Bx &       \\
   \end{bmatrix}

.. rubric:: Rotations in Cartan's formalism trivially match the Lie Algegra :math:`\mathfrak{so}(1,3)` of the Lorentz group


one. two.
