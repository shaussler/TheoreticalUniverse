.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _differential_operators_in_differential_form:

Differential Operators in Differential Form
===========================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   differential_operators.rst
   the_exterior_derivative_of_rotations.rst

The following pages systematically explore the application of the exterior
derivative in both Euclidean space and Minkowski spacetime. Traditional
differential operators from vector calculus are reinterpreted using the language
of differential forms, musical operators, and the Hodge dual. These operations
are then generalized and systematically applied in Minkowski spacetime. A
central focus lies in the analysis of 2-forms, as the primary objective of this
work is to highlight the profound connection between electromagnetism and
rotations.

Differential Operators
----------------------

All standard differential operators commonly encountered in vector calculus are
expressed in the framework of differential forms, musicality, and Hodge duality:

.. rubric:: Gradiant

.. math:: (df)^♯ = \mathbf{∇} f

.. rubric:: Divergence

.. math:: ⋆ d ⋆ F^♭ = \mathbf{∇} \cdot \mathbf{F}

.. rubric:: Curl

.. math:: (⋆(dF^♭))^♯ = ∇^♯ ⨯ F^♯

.. rubric:: Laplacian

.. math:: ⋆ d ⋆ d f = \mathbf{∇}^2 f

Rotations in Minkowski Spacetime
--------------------------------

At the heart of this work lies the exploration of the exterior derivative
applied to :ref:`rotations expressed in differential form <Rotations in
Minkowski Space>`, employing :ref:`the Cartan-Hodge formalism <the Cartan-Hodge
formalism>`, and within the context of Minkowski spacetime. I identify in a
further article :ref:`Of Maxwell Equations and Rotations` that a twist in
spacetime leads to the equations governing electromagnetism. Readers well versed
in the formulation of electromagnetism will readily recognize the Faraday
tensor, its dual, and the Maxwell equations. The Laplace-De Rham operator
results in wave equations.

.. rubric:: Hodge Dual of the Exterior Derivative of Rotations in Differential
   Form

.. math::

   ⋆ (dR^{♭♭}) = \left[ \begin{alignedat}{5}
     ( &         & - ∂_x d & - ∂_y e & - ∂_z f & \: ) \; dt \\
     ( & - ∂_t d &         & - ∂_y c & + ∂_z b & \: ) \; dx \\
     ( & - ∂_t e & + ∂_x c &         & - ∂_z a & \: ) \; dy \\
     ( & - ∂_t f & - ∂_x b & + ∂_y a &         & \: ) \; dz \\
   \end{alignedat} \right]

.. rubric:: Exterior Derivative of the Hodge Dual of Rotations in Differential
   Form

.. math::

   d( ⋆ R^{♭♭} ) = \left[ \begin{alignedat}{5}
     ( &         &+ ∂_x a & + ∂_y b & + ∂_z c & \: ) \; dx ∧ dy ∧ dz \\
     ( & + ∂_t a &        & - ∂_y f & + ∂_z e & \: ) \; dt ∧ dy ∧ dz \\
     ( & + ∂_t b &+ ∂_x f &         & - ∂_z d & \: ) \; dt ∧ dz ∧ dx \\
     ( & + ∂_t c &- ∂_x e & + ∂_y d &         & \: ) \; dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

.. rubric:: Laplace-De Rham on Rotations in Differential Form

.. math::

   (d ⋆ d ⋆ + ⋆ d ⋆ d) \left[ \begin{aligned}
     - & a \; dt ∧ dx \\
     - & b \; dt ∧ dy \\
     - & c \; dt ∧ dz \\
       & d \; dy ∧ dz \\
       & e \; dz ∧ dx \\
       & f \; dx ∧ dy \\
   \end{aligned} \right]
   &= \left[ \begin{alignedat}{5}
     ( & - ∂_t^2 a & + ∂_x^2 a & + ∂_y^2 a & + ∂_z^2 a & \: ) \; dt∧dx \\
     ( & - ∂_t^2 b & + ∂_x^2 b & + ∂_y^2 b & + ∂_z^2 b & \: ) \; dt∧dy \\
     ( & - ∂_t^2 c & + ∂_x^2 c & + ∂_y^2 c & + ∂_z^2 c & \: ) \; dt∧dz \\
     ( & + ∂_t^2 d & - ∂_x^2 d & - ∂_y^2 d & - ∂_z^2 d & \: ) \; dy∧dz \\
     ( & + ∂_t^2 f & - ∂_x^2 f & - ∂_y^2 f & - ∂_z^2 f & \: ) \; dx∧dy \\
     ( & + ∂_t^2 e & - ∂_x^2 e & - ∂_y^2 e & - ∂_z^2 e & \: ) \; dz∧dx \\
   \end{alignedat} \right]
