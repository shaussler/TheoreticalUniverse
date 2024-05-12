.. Theoretical Universe (c) by Stéphane Haussler

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
   translations.rst
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

.. math:: (df)^{♯} = \mathbf{∇} f

.. rubric:: Divergence

.. math:: ⋆ d ⋆ F^♭ = \mathbf{∇} \cdot \mathbf{F}

.. rubric:: Curl

.. math:: (⋆(dF^♭))^♯ = ∇^♯ ⨯ F^♯

.. rubric:: Laplacian

.. math:: ⋆ d ⋆ d f = \mathbf{∇}^2 f

Of Rotations in Spacetime
-------------------------

I investigate the exterior derivative of :ref:`rotations expressed in
differential form <rotations_in_minkowski_space>`, employing :ref:`the
Cartan-Hodge formalism <the_cartan_hodge_formalism>` within the context of
Minkowski spacetime. I demonstrate in :ref:`Of Maxwell Equations and Rotations
<of_maxwell_equations_and_rotations>` that a twist in spacetime leads to the
equations governing electromagnetism. Readers well versed in the formulation of
electromagnetism may already recognize the Faraday tensor, its dual, and the
Maxwell equations.

.. rubric:: Hodge Dual of the Exterior Derivative of Rotations in Differential
   Form

.. math::

   ⋆ (dR^{♭♭}) = \left[ \begin{alignedat}{1}
     ( &         & - ∂_x d & - ∂_y e & - ∂_z f & \: ) \; dt \\
     ( & - ∂_t d &         & - ∂_y c & + ∂_z b & \: ) \; dx \\
     ( & - ∂_t e & + ∂_x c &         & - ∂_z a & \: ) \; dy \\
     ( & - ∂_t f & - ∂_x b & + ∂_y a &         & \: ) \; dz \\
   \end{alignedat} \right]

.. rubric:: Exterior Derivative of the Hodge Dual of Rotations in Differential
   Form

.. math::

   d( ⋆ R^{♭♭} ) = \left[ \begin{alignedat}{1}
     ( &         &+ ∂_x a & + ∂_y b & + ∂_z c & \: ) \; dx ∧ dy ∧ dz \\
     ( & + ∂_t a &        & - ∂_y f & + ∂_z e & \: ) \; dt ∧ dy ∧ dz \\
     ( & + ∂_t b &+ ∂_x f &         & - ∂_z d & \: ) \; dt ∧ dz ∧ dx \\
     ( & + ∂_t c &- ∂_x e & + ∂_y d &         & \: ) \; dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

.. rubric:: Laplace-De Rham on Rotations in Differential Form

In Minkowski space, the Laplace-De Rham operator is :math:`d ⋆ d ⋆ + ⋆ d ⋆ d`.
Applied to a rotation in spacetime, we obtain the wave equations:

.. math::

   (d ⋆ d ⋆ + ⋆ d ⋆ d) \left[ \begin{aligned}
     - & a \; dt ∧ dx \\
     - & b \; dt ∧ dy \\
     - & c \; dt ∧ dz \\
       & d \; dy ∧ dz \\
       & e \; dz ∧ dx \\
       & f \; dx ∧ dy \\
   \end{aligned} \right]
   &= \left[ \begin{alignedat}{1}
     ( & - ∂_t^2 a & + ∂_x^2 a & + ∂_y^2 a & + ∂_z^2 a & \: ) \; dt∧dx \\
     ( & - ∂_t^2 b & + ∂_x^2 b & + ∂_y^2 b & + ∂_z^2 b & \: ) \; dt∧dy \\
     ( & - ∂_t^2 c & + ∂_x^2 c & + ∂_y^2 c & + ∂_z^2 c & \: ) \; dt∧dz \\
     ( & + ∂_t^2 d & - ∂_x^2 d & - ∂_y^2 d & - ∂_z^2 d & \: ) \; dy∧dz \\
     ( & + ∂_t^2 f & - ∂_x^2 f & - ∂_y^2 f & - ∂_z^2 f & \: ) \; dx∧dy \\
     ( & + ∂_t^2 e & - ∂_x^2 e & - ∂_y^2 e & - ∂_z^2 e & \: ) \; dz∧dx \\
   \end{alignedat} \right]
