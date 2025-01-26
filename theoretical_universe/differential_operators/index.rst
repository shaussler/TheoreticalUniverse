.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _differential_operators_in_differential_form:

Differential operators expressed as exterior derivatives
========================================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   differential_operators.rst
   the_exterior_derivative_of_functions.rst
   the_exterior_derivative_of_translations.rst
   the_exterior_derivative_of_rotations.rst
   the_exterior_derivative_of_3volume_forms.rst
   the_exterior_derivative_of_4volume_forms.rst

.. {{{

The following pages systematically explore the application of the exterior
derivative in both Euclidean space and Minkowski spacetime. Traditional
differential operators from vector calculus are reinterpreted using the
language of differential forms, musical operators, and the Hodge dual. These
operations are then generalized and systematically applied in Minkowski
spacetime. A central focus lies in the analysis of 2-forms, as the primary
objective of this work is to highlight the profound connection between
electromagnetism and rotations.

.. }}}

Exterior derivative in 3-dimensional Euclidean space
----------------------------------------------------

.. {{{

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

.. }}}

Exterior derivative in Minkowski space
--------------------------------------

.. {{{

At the heart of this work lies the exploration of the exterior derivative
applied to :ref:`rotations expressed in differential form <Rotations in
Minkowski Space>`, employing :ref:`the Cartan-Hodge formalism <the Cartan-Hodge
formalism>`, and within the context of Minkowski spacetime. I identify in a
further article :ref:`Of Maxwell Equations and Rotations` that a twist in
spacetime leads to the equations governing electromagnetism. Readers well
versed in the formulation of electromagnetism will readily recognize the
Faraday tensor, its dual, and the Maxwell equations.

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

The differential operator available is the exterior derivative :math:`d`. Since
:math:`d d F = 0`, to avoid obtaining zero, the Hodge star operator :math:`⋆`
must be applied before any further application of the exterior derivative.
Consequently, all differential operators are formed as combinations of the
exterior derivative and the Hodge star operator.

Observe that the number of distinct differential operators is inherently
limited. The non-zero combinations are at most :math:`d ⋆ d ⋆` and :math:`⋆ d ⋆
d`. With these, we can systematically compute all differential operators for
the most general form in Minkowski space.

.. }}}

0--forms --- Functions
''''''''''''''''''''''

.. {{{

----

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

.. }}}

1--forms --- Translations
'''''''''''''''''''''''''

.. {{{

----

.. math::

   ⋆ \left[ \begin{alignedat}{2}
         & A^t & dt \\
       - & A^x & dx \\
       - & A^y & dy \\
       - & A^z & dz \\
   \end{alignedat} \right]
   = \left[ \begin{alignedat}{2}
         & A^t & dx ∧ dy ∧ dz \\
       - & A^x & dt ∧ dy ∧ dz \\
       - & A^y & dt ∧ dz ∧ dx \\
       - & A^z & dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

----

.. math::

   d \left[ \begin{alignedat}{2}
         & A^t & dt \\
       - & A^x & dx \\
       - & A^y & dy \\
       - & A^z & dz \\
   \end{alignedat} \right]
   = \left[ \begin{alignedat}{1}
       ( & - & ∂_t A^x & - & ∂_x A^t) & \; dt ∧ dx \\
       ( & - & ∂_t A^y & - & ∂_y A^t) & \; dt ∧ dy \\
       ( & - & ∂_t A^z & - & ∂_z A^t) & \; dt ∧ dz \\
       ( & - & ∂_y A^z & + & ∂_z A^y) & \; dy ∧ dz \\
       ( & - & ∂_z A^x & + & ∂_x A^z) & \; dz ∧ dx \\
       ( & - & ∂_x A^y & + & ∂_y A^x) & \; dx ∧ dy \\
   \end{alignedat} \right]

----

.. math::

   d⋆ \left[ \begin{alignedat}{2}
         & A^t & dt \\
       - & A^x & dx \\
       - & A^y & dy \\
       - & A^z & dz \\
   \end{alignedat} \right]
   = \left( ∂_t A^t + ∂_x A^x + ∂_y A^y + ∂_z A^z \right) \; dt ∧ dx ∧ dy ∧ dz

----

.. math::

   ⋆d \left[ \begin{alignedat}{2}
         & A^t & dt \\
       - & A^x & dx \\
       - & A^y & dy \\
       - & A^z & dz \\
   \end{alignedat} \right]
   = \left[ \begin{alignedat}{4}
       (+ & ∂_z A^y & - & ∂_y A^z & ) & \; dt ∧ dx \\
       (+ & ∂_x A^z & - & ∂_z A^x & ) & \; dt ∧ dy \\
       (+ & ∂_y A^x & - & ∂_x A^y & ) & \; dt ∧ dz \\
       (+ & ∂_x A^t & + & ∂_t A^x & ) & \; dy ∧ dz \\
       (+ & ∂_y A^t & + & ∂_t A^y & ) & \; dz ∧ dx \\
       (+ & ∂_z A^t & + & ∂_t A^z & ) & \; dx ∧ dy \\
   \end{alignedat} \right]

----

.. math::

   d ⋆ d⋆ - ⋆ d ⋆ d \left[ \begin{alignedat}{2}
         & A^t & dt \\
       - & A^x & dx \\
       - & A^y & dy \\
       - & A^z & dz \\
   \end{alignedat} \right]
   = \left[ \begin{alignedat}{7}
     ( &             & - ∂_x^2 A^t & - ∂_y^2 A^t & - ∂_z^2 A^t & ) \; dt \\
     ( & - ∂_t^2 A^x &             & + ∂_y^2 A^x & + ∂_z^2 A^x & ) \; dx \\
     ( & - ∂_t^2 A^y & + ∂_x^2 A^y &             & + ∂_z^2 A^y & ) \; dy \\
     ( & - ∂_t^2 A^z & + ∂_x^2 A^z & + ∂_y^2 A^z &             & ) \; dz \\
  \end{alignedat} \right]

.. }}}

2--forms --- Rotations
''''''''''''''''''''''

.. {{{

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
       & (           & + ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z & ) \; dx ∧ dy ∧ dz \\
       & ( + ∂_t Q^x &           & - ∂_y R^z & + ∂_z R^y & ) \; dt ∧ dy ∧ dz \\
       & ( + ∂_t Q^y & + ∂_x R^z &           & - ∂_z R^x & ) \; dt ∧ dz ∧ dx \\
       & ( + ∂_t Q^z & - ∂_x R^y & + ∂_y R^x &           & ) \; dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

----

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
       & (           & - ∂_x R^x & - ∂_y R^y & - ∂_z R^z & ) \; dt \\
       & ( - ∂_t R^x &           & - ∂_y Q^z & + ∂_z Q^y & ) \; dx \\
       & ( - ∂_t R^y & + ∂_x Q^z &           & - ∂_z Q^x & ) \; dy \\
       & ( - ∂_t R^z & - ∂_x Q^y & + ∂_y Q^x &           & ) \; dz \\
   \end{alignedat} \right]

----

.. math::

   ( d ⋆ d ⋆ - ⋆ d ⋆ d ) \left[ \begin{aligned}
       - & Q^x \; dt ∧ dx \\
       - & Q^y \; dt ∧ dy \\
       - & Q^z \; dt ∧ dz \\
         & R^x \; dy ∧ dz \\
         & R^y \; dz ∧ dx \\
         & R^z \; dx ∧ dy \\
   \end{aligned} \right]
   &= \left[ \begin{alignedat}{5}
       & ( + ∂_t^2 Q^x & - ∂_x^2 Q^x & - ∂_y^2 Q^x & - ∂_z^2 Q^x & \: ) \; dt∧dx \\
       & ( + ∂_t^2 Q^y & - ∂_x^2 Q^y & - ∂_y^2 Q^y & - ∂_z^2 Q^y & \: ) \; dt∧dy \\
       & ( + ∂_t^2 Q^z & - ∂_x^2 Q^z & - ∂_y^2 Q^z & - ∂_z^2 Q^z & \: ) \; dt∧dz \\
       & ( - ∂_t^2 R^x & + ∂_x^2 R^x & + ∂_y^2 R^x & + ∂_z^2 R^x & \: ) \; dy∧dz \\
       & ( - ∂_t^2 R^y & + ∂_x^2 R^y & + ∂_y^2 R^y & + ∂_z^2 R^y & \: ) \; dz∧dx \\
       & ( - ∂_t^2 R^z & + ∂_x^2 R^z & + ∂_y^2 R^z & + ∂_z^2 R^z & \: ) \; dx∧dy \\
   \end{alignedat} \right]

.. }}}

3--forms --- Volumes
''''''''''''''''''''

4--forms --- Hyper--volumes
'''''''''''''''''''''''''''
