.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Exterior Derivative of Volume Forms in Spacetime
================================================

.. rst-class:: custom-author

   by Stéphane Haussler

This article is part of a series of systematic calculations of combinations of
the Hodge star operator and the exterior derivative.

Here, we perform these calculations for a 4-form. A generic 4-form is denoted
:math:`F^{♭♭♭♭} = \; f \; dt ∧ dx ∧ dy ∧ dz`.

:math:`⋆F^{♭♭♭♭}`
-----------------

.. {{{

Applying the Hodge operator results directly in:

.. math::

   ⋆ F^{♭♭♭♭} = - f

.. }}}

:math:`dF^{♭♭♭♭}`
-----------------

.. {{{

Applying the exterior derivative results directly in:

.. math::

   d F^{♭♭♭♭} = 0

.. }}}

:math:`d⋆F^{♭♭♭♭}`
------------------

.. {{{

Applying the exterior derivative results directly in:

.. math::

   d ⋆ F^{♭♭♭♭} = - ∂_t f dt - ∂_x f dx - ∂_y f dy - ∂_z f dz

.. }}}

:math:`⋆dF^{♭♭♭♭}`
------------------

.. {{{

Applying the Hodge star results directly in:

.. math::

   ⋆ d F^{♭♭♭♭} = 0

.. }}}

:math:`⋆d⋆F^{♭♭♭♭}`
-------------------

.. {{{

Applying the Hodge star results directly in:

.. math::

   ⋆ d ⋆ F^{♭♭♭♭} = \left[ \begin{aligned}
       - ∂_t f dx ∧ dy ∧ dz \\
       - ∂_x f dt ∧ dy ∧ dz \\
       - ∂_y f dt ∧ dz ∧ dx \\
       - ∂_z f dt ∧ dx ∧ dy \\
   \end{aligned} \right]

.. }}}

:math:`d⋆dF^{♭♭♭♭}`
-------------------

.. {{{

Applying the exterior derivative results directly in:

.. math::

   d ⋆ d F^{♭♭♭♭} = 0

.. }}}
