.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

0--forms (functions) in Minkowski space
=======================================

.. rst-class:: custom-author

   by Stéphane Haussler

This article is part of a series of systematic calculations of combinations of
the Hodge star operator and the exterior derivative.

Here, we perform these calculations for a function. A generic scalar field is
denoted :math:`f`.

:math:`⋆f`
----------

.. {{{

Applying the Hodge star results directly in:

.. math::

   ⋆ f = - f dt ∧ dx ∧ dy ∧ dz

.. }}}

:math:`df`
----------

.. {{{

Applying the exterior derivative results directly in:

.. math::

   d f = ∂_t f dt + ∂_x f dx + ∂_y f dy + ∂_z f dz

.. }}}

:math:`d⋆f`
-----------

.. {{{

Applying the exterior derivative results directly in:

.. math::

   d ⋆ f = 0

.. }}}

:math:`⋆df`
-----------

.. {{{

Applying the Hodge star results directly in:

.. math::

   ⋆ d f = \left[ \begin{aligned}
       ∂_t f dx ∧ dy ∧ dz \\
       ∂_x f dt ∧ dy ∧ dz \\
       ∂_y f dt ∧ dz ∧ dx \\
       ∂_z f dt ∧ dx ∧ dy \\
   \end{aligned} \right]

.. }}}

:math:`⋆d⋆f`
------------

.. {{{

Applying the Hodge star results directly in:

.. math::

   ⋆ d ⋆ f = 0

.. }}}

:math:`d⋆df`
------------

.. {{{

.. math::

   d ⋆ d f = (∂_t^2 - ∂_x^2 - ∂_y^2 - ∂_z^2) f \; dz ∧ dt ∧ dx ∧ dy

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the exterior derivative

   .. math::

      d ⋆ d f = d \left[ \begin{aligned}
          ∂_t f dx ∧ dy ∧ dz \\
          ∂_x f dt ∧ dy ∧ dz \\
          ∂_y f dt ∧ dz ∧ dx \\
          ∂_z f dt ∧ dx ∧ dy \\
      \end{aligned} \right]

   .. rubric:: Expand the exterior derivative

   .. math::

      d ⋆ d f = \left[ \begin{aligned}
          ∂_t ∂_t f dt ∧ dx ∧ dy ∧ dz \\
          ∂_x ∂_x f dx ∧ dt ∧ dy ∧ dz \\
          ∂_y ∂_y f dy ∧ dt ∧ dz ∧ dx \\
          ∂_z ∂_z f dz ∧ dt ∧ dx ∧ dy \\
      \end{aligned} \right]

   .. rubric:: Simplify and conclude

   .. math::

      d ⋆ d f = (∂_t^2 - ∂_x^2 - ∂_y^2 - ∂_z^2) f \; dz ∧ dt ∧ dx ∧ dy

   .. }}}

.. }}}
