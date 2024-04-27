.. Theoretical Universe (c) by Stéphane Haussler
.. 
.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _differential_operators_in_differential_form:

Differential Operators in Differential Form
===========================================

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   differential_operators.rst
   the_exterior_derivative_of_rotations.rst

Summary
-------

Differential Operators
----------------------

The exterior derivative permits to express and generalize all differential
operators. In this serie of articles, I systematically translate the
differential operators in the :ref:`Cartan-Hodge formalism
<the_cartan_hodge_formalism>` to obtain:

.. rubric:: Gradiant

.. math::

   (df)^{♯} = \mathbf{∇} f

.. rubric:: Divergence

.. math::

   ⋆ d ⋆ F^♭ = \mathbf{∇} \cdot \mathbf{F}

.. rubric:: Curl

.. math::

   (⋆(dF^♭))^♯ = ∇^♯ ⨯ F^♯

.. rubric:: Laplacian

.. math::

   ⋆ d ⋆ d f = \mathbf{∇}^2 f

The Exterior Derivative of Rotations in Spacetime
-------------------------------------------------

I investigate the exterior derivative of :ref:`rotations expressed in
differential form <rotations_in_minkowski_space>`, employing :ref:`the
Cartan-Hodge formalism <the_cartan_hodge_formalism>` within the context of
Minkowski spacetime. I demonstrate in :ref:`Of Maxwell Equations and Rotations
<of_maxwell_equations_and_rotations>` that a twist in spacetime leads to the
equations governing electromagnetism. Readers well versed in the formulation of
electromagnetism may already recognize the Faraday tensor, its dual, and the
Maxwell equations.

.. rubric:: Hodge Dual of the Exterior Derivative of Rotations in Differential Form

.. math::

   \newcommand{\_}{\phantom{∂_m m}}

   ⋆ (dR^{♭♭}) = \begin{bmatrix}
       ( \_      & - ∂_x d & - ∂_y e & - ∂_z f \, ) \; dt \\
       ( - ∂_t d & \_      & - ∂_y c & + ∂_z b \, ) \; dx \\
       ( - ∂_t e & + ∂_x c & \_      & - ∂_z a \, ) \; dy \\
       ( - ∂_t f & - ∂_x b & + ∂_y a & \_      \, ) \; dz \\
   \end{bmatrix}

.. rubric:: Exterior Derivative of the Hodge Dual of Rotations in Differential Form

.. math::

   \newcommand{\_}{\phantom{∂_m m}}

   d( ⋆ R^{♭♭} ) = \begin{bmatrix}
       ( \_      &+ ∂_x a & + ∂_y b & + ∂_z c \, ) \; dx ∧ dy ∧ dz \\
       ( + ∂_t a &\_      & - ∂_y f & + ∂_z e \, ) \; dt ∧ dy ∧ dz \\
       ( + ∂_t b &+ ∂_x f & \_      & - ∂_z d \, ) \; dt ∧ dz ∧ dx \\
       ( + ∂_t c &- ∂_x e & + ∂_y d & \_      \, ) \; dt ∧ dx ∧ dy \\
   \end{bmatrix}
