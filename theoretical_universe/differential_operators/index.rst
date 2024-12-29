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
   the_exterior_derivative_of_functions.rst
   the_exterior_derivative_of_translations.rst
   the_exterior_derivative_of_rotations.rst
   the_exterior_derivative_of_volume_forms.rst

The following pages systematically explore the application of the exterior
derivative in both Euclidean space and Minkowski spacetime. Traditional
differential operators from vector calculus are reinterpreted using the language
of differential forms, musical operators, and the Hodge dual. These operations
are then generalized and systematically applied in Minkowski spacetime. A
central focus lies in the analysis of 2-forms, as the primary objective of this
work is to highlight the profound connection between electromagnetism and
rotations.

Differential operators in Euclidean space
-----------------------------------------

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

Differential operators in Minkowski Spacetime
---------------------------------------------

At the heart of this work lies the exploration of the exterior derivative
applied to :ref:`rotations expressed in differential form <Rotations in
Minkowski Space>`, employing :ref:`the Cartan-Hodge formalism <the Cartan-Hodge
formalism>`, and within the context of Minkowski spacetime. I identify in a
further article :ref:`Of Maxwell Equations and Rotations` that a twist in
spacetime leads to the equations governing electromagnetism. Readers well versed
in the formulation of electromagnetism will readily recognize the Faraday
tensor, its dual, and the Maxwell equations.

The most generic possible form in Minkowski space is:

.. math::
   f
   + \left[ \begin{alignedat}{1}
       & A^t dt                \\
       & A^x dx                \\
       & A^y dy                \\
       & A^z dz                \\
   \end{alignedat} \right]
   + \left[ \begin{alignedat}{1}
       & Q^x dt ∧ dx           \\
       & Q^y dt ∧ dy           \\
       & Q^z dt ∧ dz           \\
       & R^x dy ∧ dz           \\
       & R^y dz ∧ dx           \\
       & R^z dx ∧ dy           \\
   \end{alignedat} \right]
   + \left[ \begin{alignedat}{1}
       & D^t dx ∧ dy ∧ dz      \\
       & D^x dt ∧ dy ∧ dz      \\
       & D^y dt ∧ dz ∧ dx      \\
       & D^z dt ∧ dy ∧ dz      \\
   \end{alignedat} \right]
   + G   dt ∧ dx ∧ dy ∧ dz

The primal differential operator available is the exterior derivative
:math:`d`. Since :math:`d d F = 0`, to avoid obtaining zero, the Hodge star
operator :math:`⋆` must be applied before any further application of the
exterior derivative. Consequently, all differential operators are formed as
combinations of the exterior derivative and the Hodge star operator.

Observe that the number of distinct differential operators is inherently
limited. The non-zero combinations are at most :math:`d ⋆ d ⋆` and :math:`⋆ d ⋆
d`. With these, we can systematically compute all differential operators for
the most general form in Minkowski space.

.. rubric:: Exterior derivative of functions in spacetime

.. math::

   ⋆ f = - \; f \; dt ∧ dx ∧ dy ∧ dz

----

.. math::

   d f = ∂_t f dt + ∂_x f dx + ∂_y f dy + ∂_z f dz

----

.. math::

   d ⋆ f = 0

----

.. math::

   ⋆ d f = \left[ \begin{aligned}
       ∂_t f dx ∧ dy ∧ dz \\
       ∂_x f dt ∧ dy ∧ dz \\
       ∂_y f dt ∧ dz ∧ dx \\
       ∂_z f dt ∧ dx ∧ dy \\
   \end{aligned} \right]

----

.. math::

   ⋆ d ⋆ f = 0

----

.. math::

   d ⋆ d f = (∂_t^2 - ∂_x^2 - ∂_y^2 - ∂_z^2) \; f \; dz ∧ dt ∧ dx ∧ dy

----

.. rubric:: Exterior derivative of rotations in spacetime

.. math::

   ⋆ d \left[ \begin{aligned}
     - & Q^x\; dt ∧ dx \\
     - & Q^y\; dt ∧ dy \\
     - & Q^z\; dt ∧ dz \\
       & R^x\; dy ∧ dz \\
       & R^y\; dz ∧ dx \\
       & R^z\; dx ∧ dy \\
   \end{aligned} \right]
   = \left[ \begin{alignedat}{5}
     ( &         & - ∂_x R^x & - ∂_y R^y & - ∂_z R^z & \: ) \; dt \\
     ( & - ∂_t R^x &         & - ∂_y Q^z & + ∂_z Q^y & \: ) \; dx \\
     ( & - ∂_t R^y & + ∂_x Q^z &         & - ∂_z Q^x & \: ) \; dy \\
     ( & - ∂_t R^z & - ∂_x Q^y & + ∂_y Q^x &         & \: ) \; dz \\
   \end{alignedat} \right]

----

.. math::

   d ⋆ \left[ \begin{aligned}
     - & Q^x \; dt ∧ dx \\
     - & Q^y \; dt ∧ dy \\
     - & Q^z \; dt ∧ dz \\
       & R^x \; dy ∧ dz \\
       & R^y \; dz ∧ dx \\
       & R^z \; dx ∧ dy \\
   \end{aligned} \right]
   = \left[ \begin{alignedat}{5}
     ( &           &+ ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z & \: ) \; dx ∧ dy ∧ dz \\
     ( & + ∂_t Q^x &          & - ∂_y R^z & + ∂_z R^y & \: ) \; dt ∧ dy ∧ dz \\
     ( & + ∂_t Q^y &+ ∂_x R^z &           & - ∂_z R^x & \: ) \; dt ∧ dz ∧ dx \\
     ( & + ∂_t Q^z &- ∂_x R^y & + ∂_y R^x &           & \: ) \; dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

----

.. math::

   (d ⋆ d ⋆ + ⋆ d ⋆ d) \left[ \begin{aligned}
     - & Q^x \; dt ∧ dx \\
     - & Q^y \; dt ∧ dy \\
     - & Q^z \; dt ∧ dz \\
       & R^x \; dy ∧ dz \\
       & R^y \; dz ∧ dx \\
       & R^z \; dx ∧ dy \\
   \end{aligned} \right]
   &= \left[ \begin{alignedat}{5}
     ( & - ∂_t^2 Q^x & + ∂_x^2 Q^x & + ∂_y^2 Q^x & + ∂_z^2 Q^x & \: ) \; dt∧dx \\
     ( & - ∂_t^2 Q^y & + ∂_x^2 Q^y & + ∂_y^2 Q^y & + ∂_z^2 Q^y & \: ) \; dt∧dy \\
     ( & - ∂_t^2 Q^z & + ∂_x^2 Q^z & + ∂_y^2 Q^z & + ∂_z^2 Q^z & \: ) \; dt∧dz \\
     ( & + ∂_t^2 R^x & - ∂_x^2 R^x & - ∂_y^2 R^x & - ∂_z^2 R^x & \: ) \; dy∧dz \\
     ( & + ∂_t^2 R^y & - ∂_x^2 R^y & - ∂_y^2 R^y & - ∂_z^2 R^y & \: ) \; dz∧dx \\
     ( & + ∂_t^2 R^z & - ∂_x^2 R^z & - ∂_y^2 R^z & - ∂_z^2 R^z & \: ) \; dx∧dy \\
   \end{alignedat} \right]
