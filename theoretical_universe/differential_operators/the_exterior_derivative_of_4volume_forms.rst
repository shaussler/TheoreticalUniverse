.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Differential operators in Minkowski space on 4-forms (4-volumes)
================================================================

.. rst-class:: custom-author

   by Stéphane Haussler

This article is part of a series of systematic calculations of combinations of
the Hodge star operator and the exterior derivative.

Here, we perform these calculations for a 4-form. A generic 4-form is denoted
:math:`G^{♭♭♭♭} = \; g \; dt ∧ dx ∧ dy ∧ dz`.

:math:`⋆G^{♭♭♭♭}`
-----------------

.. {{{

Applying the Hodge operator results directly in:

.. math::

   ⋆ G^{♭♭♭♭} = - g

.. }}}

:math:`dG^{♭♭♭♭}`
-----------------

.. {{{

Applying the exterior derivative results directly in:

.. math::

   d G^{♭♭♭♭} = 0

.. }}}

:math:`d⋆G^{♭♭♭♭}`
------------------

.. {{{

Applying the exterior derivative results directly in:

.. math::

   d ⋆ G^{♭♭♭♭} = - ∂_t G dt - ∂_x G dx - ∂_y G dy - ∂_z G dz

.. }}}

:math:`⋆dG^{♭♭♭♭}`
------------------

.. {{{

Applying the Hodge star results directly in:

.. math::

   ⋆ d G^{♭♭♭♭} = 0

.. }}}

:math:`⋆d⋆G^{♭♭♭♭}`
-------------------

.. {{{

Applying the Hodge star results directly in:

.. math::

   ⋆ d ⋆ G^{♭♭♭♭} = \left[ \begin{aligned}
       - ∂_t G dx ∧ dy ∧ dz \\
       - ∂_x G dt ∧ dy ∧ dz \\
       - ∂_y G dt ∧ dz ∧ dx \\
       - ∂_z G dt ∧ dx ∧ dy \\
   \end{aligned} \right]

.. }}}

:math:`d⋆dG^{♭♭♭♭}`
-------------------

.. {{{

Applying the exterior derivative results directly in:

.. math::

   d ⋆ d G^{♭♭♭♭} = 0

.. }}}
