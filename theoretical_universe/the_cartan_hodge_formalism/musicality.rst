.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _musicality:

Musicality
==========

.. rst-class:: custom-author

   by Stéphane Haussler

.. rubric:: Musical declarations

Traditionally, vectors are noted with a bold font as :math:`\mathbf{V}`, or with
an arrow symbol :math:`\overrightarrow{V}`. These notations precludes the advent
of tensor calculus and the discovery of the dual covectors, thus leaving no
notation for these dual objects. The abstract index notation of Ricci calculus
brings some improvement, with three-vectors expressed as :math:`v^i`, and the
dual covectors expressed with lower indices as :math:`v_i`. With the musical
flat :math:`♭` and sharp :math:`♯` symbols, covectors and vectors are explicitly
declared. For example, a contravariant three-vector is noted with the sharp
symbol :math:`♯`:

.. math:: V^♯

Whereas the dual covariant three-covector is declared with the flat symbol
:math:`♭`:

.. math:: V^♭

.. rubric:: Musical operations

Considering a vector in 3 dimensional Euclidean space expressed as a linear
combination of the basis vectors :math:`∂_i`:

.. math::

   V^♯ = a \; ∂_x + b \; ∂_y + c \; ∂_z

The musical flat :math:`♭` symbol is further utilized as an operator converting
vectors to covectors. For example, the three-vector :math:`V^♯` is flattend to a
three-covector using the Euclidean metric :math:`δ` with:

.. math::

   V^♭ &= (V^♯)^♭                                                         \\
       &= a \; ∂_x^♭ + b \; ∂_y^♭ + c \; ∂_z^♭                            \\
       &= a \; δ_{xi} \; dx^i + b \; δ_{yi} \; dx^i + c \; δ_{zi} \; dx^i \\
       &= a \; δ_{xx} \; dx^x + b \; δ_{yy} \; dx^y + c \; δ_{zz} \; dx^z \\
       &= a \; dx + b \; dy + c \; dz                                     \\

Likewise, the musical sharp :math:`♯` is utilized as an operatro converting
covectors to vecotrs. For example, the three-covector :math:`V^♭` is sharpened
to a three-vector using:

.. math::

   V^♯ &= (V^♭)^♯                                                      \\
       &= a \; dx^♯ + b \; dy^♯ + c \; dz^♯                             \\
       &= a \; δ_{xi} \; ∂_i + b \; δ_{yi} \; ∂_i + c \; δ_{zi} \; ∂_i \\
       &= a \; δ_{xx} \; ∂_x + b \; δ_{yy} \; ∂_y + c \; δ_{zz} \; ∂_z \\
       &= a \; ∂_x + b \; ∂_y + c \; ∂_z                               \\

The notation can be further utilzed to raise or lower the indices of a tensor T
of any rank. For example, a doubly contravariant tensor in Minkowski space
:math:`T^{♯♯}`, also noted :math:`T^{μν}` in abstract index notation is lowered
using the metric component :math:`η_{μν}` with:

.. math::

   T^{♭♯} &= (T^{♯♯})^{♭♯} \\
          &= T^{μν} \; (∂_μ ⊗ ∂_ν)^{♭♯} \\
          &= T^{μν} \; ∂_μ^♭ ⊗ ∂_ν^♯ \\
          &= T^{μν} \; η_{μγ} \; dx^{γ} ⊗ ∂_ν

Compared to Ricci calculus, musicality serves as a mean to clearly articulate
the tensor basis alongside its components. Those familiar with abstract index
notation may initially perceive the musical notation with explicit tensor bases
as merely introducing additional symbols. However, the practical utility of
this notation becomes evident when conducting real calculations with all
elements of the Cartan-Hodge formalism.
