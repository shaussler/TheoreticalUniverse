.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _of_maxwell_equations_and_rotations:

Of Maxwell Equations and Rotations
==================================

.. rst-class:: custom-author

   by Stéphane Haussler

This article elucidates the direct relashionship between :ref:`rotations in
differential form` and the :ref:`equations of Mr. Maxwell <the ordered
equations>`. In a previous articles, I utilized :ref:`the Cartan-Hodge
formalism` to obtain :ref:`the exterior derivative of rotations in spacetime`.
Through identification, we will establish that the equations governing
electromagnetism exactly are spacetime rotations to which is applied the
exterior derivative. We thus interpret electromagnetism as a twist in spacetime.
The present line of reasoning and derivation may feel more intuitive compared to
the conventional approach of retroactively proving that expressing the
electromagnetic tensor in a certain manner as a combination of 2-forms, followed
by applying the Hodge operator and the exterior product, leads back to Maxwell's
equations.

The mathematical expressions obtained are the well-recognized expressions of the
differential geometric formulation of Maxwell's equations. I finally further
slightly improve on the conventional notation to combine the expressions into a
single equation.

The Equations of Mr. Maxwell
----------------------------

.. {{{

In a previous article, I present :ref:`the Maxwell equations of 1865 <deriving
the Faraday tensor from the 1865 Maxwell equations>` expressed with modern
notations, and reoredered with the benefit of hindsight:

.. rubric:: Inhomogenous Maxwell equations

.. math::

   \begin{alignedat}{1}
                & + ∂_x \E^x & + ∂_y \E^y & + ∂_z \E^z & = & + μ_0 c ρ \\
     + ∂_t \E^x &            & - ∂_y  B^z & + ∂_z  B^y & = & - μ_0 J^x \\
     + ∂_t \E^y & + ∂_x  B^z &            & - ∂_z  B^x & = & - μ_0 J^y \\
     + ∂_t \E^z & - ∂_x  B^y & + ∂_y  B^x &            & = & - μ_0 J^z \\
   \end{alignedat}

.. rubric:: Homogenous Maxwell equations

.. math::

   \begin{alignedat}{1}
                & + ∂_x  B^x & + ∂_y  B^y & + ∂_z  B^z & = 0 \\
     + ∂_t  B^x &            & + ∂_y \E^z & - ∂_z \E^y & = 0 \\
     + ∂_t  B^y & - ∂_x \E^z &            & + ∂_z \E^x & = 0 \\
     + ∂_t  B^z & + ∂_x \E^y & - ∂_y \E^x &            & = 0 \\
   \end{alignedat}

.. }}}

The Exterior Derivative of Rotations
------------------------------------

.. {{{

In a :ref:`previous article <rotations_in_minkowski_space>`, I investigate
spacetime rotations in differential form and demonstrate that rotations can be
expressed as:

.. math::
   R^{♭♭} = \left[ \begin{aligned}
     - &a \; dt ∧ dx \\
     - &b \; dt ∧ dy \\
     - &c \; dt ∧ dz \\
       &d \; dy ∧ dz \\
       &e \; dz ∧ dx \\
       &f \; dx ∧ dy \\
   \end{aligned} \right]

In a :ref:`subsequent article
<the_exterior_derivative_of_rotations_in_spacetime>`, I systematically calculate
the exterior derivative of that rotation, as well as the exterior derivative of
the Hodge dual.

.. rubric:: Exterior Derivative of the Hodge Dual of Rotations in Differential
   Form

.. math::

   d( ⋆ R^{♭♭} ) = \left[ \begin{alignedat}{1}
     (&         & + ∂_x a & + ∂_y b & + ∂_z c \:&) \; dx ∧ dy ∧ dz \\
     (& + ∂_t a &         & - ∂_y f & + ∂_z e \:&) \; dt ∧ dy ∧ dz \\
     (& + ∂_t b & + ∂_x f &         & - ∂_z d \:&) \; dt ∧ dz ∧ dx \\
     (& + ∂_t c & - ∂_x e & + ∂_y d &         \:&) \; dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

.. rubric:: Hodge Dual of the Exterior Derivative of Rotations in Differential
   Form

.. math::

   ⋆ (dR^{♭♭}) = \left[ \begin{alignedat}{1}
     (&       \;   & - ∂_x \; d & - ∂_y \; e & - ∂_z \; f \:&) \; dt \\
     (& - ∂_t \; d &       \;   & - ∂_y \; c & + ∂_z \; b \:&) \; dx \\
     (& - ∂_t \; e & + ∂_x \; c &       \;   & - ∂_z \; a \:&) \; dy \\
     (& - ∂_t \; f & - ∂_x \; b & + ∂_y \; a &       \;   \:&) \; dz \\
   \end{alignedat} \right]

.. }}}

Identifying the Equations of Mr. Maxwell
----------------------------------------

.. {{{

We identifiy the components of the electric and magnetic fields:

.. math::

   \begin{matrix}
     \E^x = a \\
     \E^y = b \\
     \E^z = c \\
      B^x = d \\
      B^y = e \\
      B^z = f \\
   \end{matrix}

The doubly covariant Faraday tensor is identified as:

.. math::
   F^{♭♭} = \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right]

We conclude electromagnetism is a twist in spacetime. The Maxwell equations are:

.. topic:: Inhomogenous Maxwell Equations

   .. math::

      d ⋆ \left[ \begin{aligned}
        - & \E^x \; dt ∧ dx \\
        - & \E^y \; dt ∧ dy \\
        - & \E^z \; dt ∧ dz \\
          &  B^x \; dy ∧ dz \\
          &  B^y \; dz ∧ dx \\
          &  B^z \; dx ∧ dy \\
      \end{aligned} \right]
      = \begin{bmatrix}
        + μ_0 c ρ \; dx ∧ dy ∧ dz\\
        - μ_0 J^x \; dt ∧ dy ∧ dz\\
        - μ_0 J^y \; dt ∧ dz ∧ dx\\
        - μ_0 J^z \; dt ∧ dx ∧ dy\\
      \end{bmatrix}

.. topic:: Homogenous Maxwell Equations

   .. math::

      ⋆ d \left[ \begin{aligned}
        - & \E^x \; dt ∧ dx \\
        - & \E^y \; dt ∧ dy \\
        - & \E^z \; dt ∧ dz \\
          &  B^x \; dy ∧ dz \\
          &  B^y \; dz ∧ dx \\
          &  B^z \; dx ∧ dy \\
      \end{aligned} \right]
      = 0

Thus we fall back to `the conventional expression of Maxwell equations in
differential form:
<https://en.m.wikipedia.org/wiki/Mathematical_descriptions_of_the_electromagnetic_field#Differential_forms_approach>`_

.. math::
   \begin{matrix}
       d⋆ \mathbf{F} &=& \mathbf{J} \\
       d  \mathbf{F} &=& 0          \\
   \end{matrix}

Most interestingly, since :math:`⋆dF` is a 1-form and :math:`d⋆F` result is a
3-form, we can merge the inhomogenous and homogenous equations.

.. math::

   d ⋆ \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right] - ⋆ d \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right] = \begin{bmatrix}
       + μ_0 c ρ \; dx ∧ dy ∧ dz\\
       - μ_0 J^x \; dt ∧ dy ∧ dz\\
       - μ_0 J^y \; dt ∧ dz ∧ dx\\
       - μ_0 J^z \; dt ∧ dx ∧ dy\\
   \end{bmatrix}

.. note::

   An equation containing 3-forms and 2-forms cannot be reduced. For example, the
   following equation cannot be simplified:

   .. math:: a \; dx ∧ dy + b \; dx ∧ dy ∧ dz = c \; dx ∧ dy

   Surfaces and volumes certainly are different objects which can however be
   written in the same equation using the :math:`+` symbol, just that these
   objects certainly cannot be *added*. Similar examples are adding real and the
   imaginary parts of imaginary numbers, or bivectors and trivectors in Clifford
   algebra. Hence with the exemplary equation above, we necessarily have:

   .. math::

      a &= c \\
      b &= 0 \\

   This is how we can write the Maxwell equations via differential forms to a
   single equation.

.. topic:: The Maxwell Equations in Differential Form

   .. math::

      (d ⋆ - ⋆ d ) \left[ \begin{aligned}
        \E^x \; dt ∧ dx \\
        \E^y \; dt ∧ dy \\
        \E^z \; dt ∧ dz \\
         B^x \; dy ∧ dz \\
         B^y \; dz ∧ dx \\
         B^z \; dx ∧ dy \\
      \end{aligned} \right] = \left[ \begin{aligned}
        + μ_0 c ρ \; dx ∧ dy ∧ dz\\
        - μ_0 J^x \; dt ∧ dy ∧ dz\\
        - μ_0 J^y \; dt ∧ dz ∧ dx\\
        - μ_0 J^z \; dt ∧ dx ∧ dy\\
      \end{aligned} \right]

Or with a shorthand:

.. topic:: The Maxwell Equations in Differential Form

   .. math:: (d ⋆ - ⋆ d) \; F^{♭♭} = J^{♭♭♭}

.. note::

   Flipping the sign of :math:`⋆ d` is also valid.

.. }}}
