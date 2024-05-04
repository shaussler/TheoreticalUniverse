.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _musical_isomorphisms:

Musicality
==========

.. rst-class:: custom-author

   by Stéphane Haussler

Musical Declaration
-------------------

Traditionally, a vector would be noted with a bold font as :math:`\mathbf{V}`,
or with an arrow symbol :math:`\overrightarrow{V}`. These notations precludes
the advent of tensor calculus and the discovery of the dual covectors, thus
leaving no notation for these dual objects. The abstract index notation of Ricci
calculus brings some improvement, with three-vectors expressed as :math:`v^i`,
and the dual covectors expressed with lower indices as :math:`v_i`. With the
musical flat :math:`♭` and sharp :math:`♯` symbols, covectors and vectors are
explicetely declared. For example, a contravariant three-vector is declared with
the sharp symbol :math:`♯`:

.. topic:: Musical Vector Notation

   .. math:: V^♯

Whereas the dual covariant three-covector is declared with the flat symbol
:math:`♭`:

.. topic:: Musical Covector Notation

   .. math:: V^♭

Musical Operations
------------------

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

The vector field :math:`\mathbf{F}` is noted with the musical isomorphism
:math:`\sharp` as :math:`F^\sharp`, which either declare :math:`F` is a vector,
or transform a covector to a vector. The flat operator :math:`\flat` brings a
vector to a covector.

.. math::

   \mathbf{F}=F^\sharp=(F^\sharp)^\sharp=(F^\flat)^\sharp = v^i \mathbf{e}_i
