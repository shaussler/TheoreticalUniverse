.. Theoretical Universe (c) by Stéphane Haussler
.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _of_maxwell_equations_and_rotations:

Of Maxwell Equations and Rotations
==================================

.. rst-class:: custom-author

   by Stéphane Haussler

This article investigates the connection between :ref:`rotations <rotations_in_differential_form>`, the :ref:`exterior
derivative of rotations <the_exterior_derivative_of_rotations_in_spacetime>`, and the equations of Mr. Maxwell. I
utilize :ref:`the Cartan-Hodge's formalism <the_cartan_hodge_formalism>` in Minkowski space-time. I demonstrate that
applying the exterior derivative to rotations yields the equations governing electromagnetism. These expressions reveal
Maxwell equations are a twist in spacetime.

While the concept might not be novel, I have not yet encountered some of my observations elsewhere. If you are aware of
relevant references, feel free to open an issue and I will include them. I you identify any errors, you can either open
an issue, or directly submit corrections via a merge request to my GitHub repository: `Theoretical Universe
<https://github.com/shaussler/TheoreticalUniverse/>`_.

The Equations of Mr. Maxwell
----------------------------

.. {{{

In a :ref:`previous article <the_ordered_equations>`, I derive from the 1865 Maxwell equations the following
expressions:

.. rubric:: Inhomogenous Maxwell equations

.. math::

   \begin{equation} \newcommand{\E}{\tilde{E}}
       \begin{matrix}
                      & + ∂_x \E^x & + ∂_y \E^y & + ∂_z \E^z & = & + μ_0 c ρ \\
           + ∂_t \E^x &            & - ∂_y  B^z & + ∂_z  B^y & = & - μ_0 J^x \\
           + ∂_t \E^y & + ∂_x  B^z &            & - ∂_z  B^x & = & - μ_0 J^y \\
           + ∂_t \E^z & - ∂_x  B^y & + ∂_y  B^x &            & = & - μ_0 J^z \\
       \end{matrix}
   \end{equation}

.. rubric:: Homogenous Maxwell equations

.. math::

   \begin{equation} \newcommand{\E}{\tilde{E}}
       \begin{matrix} 
                      & + ∂_x  B^x & + ∂_y  B^y & + ∂_z  B^z & = & 0 \\
           + ∂_t  B^x &            & + ∂_y \E^z & - ∂_z \E^y & = & 0 \\
           + ∂_t  B^y & - ∂_x \E^z &            & + ∂_z \E^x & = & 0 \\
           + ∂_t  B^z & + ∂_x \E^y & - ∂_y \E^x &            & = & 0 \\
       \end{matrix}
   \end{equation}

.. }}}

The Exterior Derivative of Rotations
------------------------------------

.. {{{

In a :ref:`previous article <rotations_in_minkowski_space>`, I investigate spacetime rotations in differential form and
demonstrate that rotations can be expressed as:

.. math::

   \begin{equation}
   R^{♭♭} =
   \begin{bmatrix}
     a \; dx ∧ dt \\
     b \; dy ∧ dt \\
     c \; dz ∧ dt \\
     d \; dy ∧ dz \\
     e \; dz ∧ dx \\
     f \; dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

In a :ref:`subsequent article <the_exterior_derivative_of_rotations_in_spacetime>`, I systematically calculate the
exterior derivative of that rotation, as well as the exterior derivative of the Hodge dual.

.. rubric:: Exterior Derivative of the Hodge Dual of Rotations in Differential Form

.. math::

   \begin{equation} \newcommand{\_}{\phantom{∂_m m}}
       d( ⋆ R^{♭♭} ) = \begin{bmatrix}
           ( \_      &+ ∂_x a & + ∂_y b & + ∂_z c \, ) \; dx ∧ dy ∧ dz \\
           ( + ∂_t a &\_      & - ∂_y f & + ∂_z e \, ) \; dt ∧ dy ∧ dz \\
           ( + ∂_t b &+ ∂_x f & \_      & - ∂_z d \, ) \; dt ∧ dz ∧ dx \\
           ( + ∂_t c &- ∂_x e & + ∂_y d & \_      \, ) \; dt ∧ dx ∧ dy \\
       \end{bmatrix}
   \end{equation}

.. rubric:: Hodge Dual of the Exterior Derivative of Rotations in Differential Form

.. math::

   \begin{equation}\
       \newcommand{\_}{\phantom{∂_m m}}
       ⋆ (dR^{♭♭}) = \begin{bmatrix}
           ( \_      & - ∂_x d & - ∂_y e & - ∂_z f \, ) \; dt \\
           ( - ∂_t d & \_      & - ∂_y c & + ∂_z b \, ) \; dx \\
           ( - ∂_t e & + ∂_x c & \_      & - ∂_z a \, ) \; dy \\
           ( - ∂_t f & - ∂_x b & + ∂_y a & \_      \, ) \; dz \\
       \end{bmatrix}
   \end{equation}

.. }}}

Identifying the Equations of Mr. Maxwell
----------------------------------------

.. {{{

We identifiy the components of the electric and magnetic fields:

.. math::

   \begin{equation} \newcommand{\E}{\tilde{E}}
       \begin{matrix}
           \E^x = a \\
           \E^y = b \\
           \E^z = c \\
            B^x = d \\
            B^y = e \\
            B^z = f \\
       \end{matrix}
   \end{equation}

The doubly covariant Faraday tensor is identified as:

.. math::

   F^{♭♭} = \begin{equation} \newcommand{\E}{\tilde{E}}
   \begin{bmatrix}
       \E^x \; dx ∧ dt \\
       \E^y \; dy ∧ dt \\
       \E^z \; dz ∧ dt \\
        B^x \; dy ∧ dz \\
        B^y \; dz ∧ dx \\
        B^z \; dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

We conclude electromagnetism is a twist in spacetime. The Maxwell equations are:

.. topic:: Inhomogenous Maxwell Equations

   .. math::

      \begin{equation} \newcommand{\E}{\tilde{E}}
      d ⋆ \begin{bmatrix}
          \E^x \; dx ∧ dt \\
          \E^y \; dy ∧ dt \\
          \E^z \; dz ∧ dt \\
           B^x \; dy ∧ dz \\
           B^y \; dz ∧ dx \\
           B^z \; dx ∧ dy \\
      \end{bmatrix}
      = \begin{bmatrix}
          + μ_0 c ρ \; dx ∧ dy ∧ dz\\
          - μ_0 J^x \; dt ∧ dy ∧ dz\\
          - μ_0 J^y \; dt ∧ dz ∧ dx\\
          - μ_0 J^z \; dt ∧ dx ∧ dy\\
      \end{bmatrix}
      \end{equation}

.. topic:: Homogenous Maxwell Equations

   .. math::

      \begin{equation} \newcommand{\E}{\tilde{E}}
      ⋆ d \begin{bmatrix}
          \E^x \; dx ∧ dt \\
          \E^y \; dy ∧ dt \\
          \E^z \; dz ∧ dt \\
           B^x \; dy ∧ dz \\
           B^y \; dz ∧ dx \\
           B^z \; dx ∧ dy \\
      \end{bmatrix}
      = 0
      \end{equation}

Thus we fall back to `the conventional expression of Maxwell equations in differential form:
<https://en.m.wikipedia.org/wiki/Mathematical_descriptions_of_the_electromagnetic_field#Differential_forms_approach>`_

.. math::

   \begin{equation}
       \begin{matrix}
           d⋆ \mathbf{F} &=& \mathbf{J} \\
           d \mathbf{F}  &=& 0          \\
       \end{matrix}
   \end{equation}


Most interestingly, since :math:`⋆dF` is a 1-form and :math:`d*F` result is a 3-form, we can merge the inhomogenous and
homogenous equations:

.. math::

   \begin{equation}
   \newcommand{\E}{\tilde{E}}
   d ⋆ \begin{bmatrix}
       \E^x \; dx ∧ dt \\
       \E^y \; dy ∧ dt \\
       \E^z \; dz ∧ dt \\
        B^x \; dy ∧ dz \\
        B^y \; dz ∧ dx \\
        B^z \; dx ∧ dy \\
   \end{bmatrix}
   -
   ⋆ d \begin{bmatrix}
       \E^x \; dx ∧ dt \\
       \E^y \; dy ∧ dt \\
       \E^z \; dz ∧ dt \\
        B^x \; dy ∧ dz \\
        B^y \; dz ∧ dx \\
        B^z \; dx ∧ dy \\
  \end{bmatrix}
   = \begin{bmatrix}
       + μ_0 c ρ \; dx ∧ dy ∧ dz\\
       - μ_0 J^x \; dt ∧ dy ∧ dz\\
       - μ_0 J^y \; dt ∧ dz ∧ dx\\
       - μ_0 J^z \; dt ∧ dx ∧ dy\\
   \end{bmatrix}
   \end{equation}

.. topic:: The Maxwell Equations in Differential Form

   .. math::

      \begin{equation}
      \newcommand{\E}{\tilde{E}}
      (d ⋆ - ⋆ d ) \begin{bmatrix}
          \E^x \; dx ∧ dt \\
          \E^y \; dy ∧ dt \\
          \E^z \; dz ∧ dt \\
           B^x \; dy ∧ dz \\
           B^y \; dz ∧ dx \\
           B^z \; dx ∧ dy \\
      \end{bmatrix}
      = \begin{bmatrix}
          + μ_0 c ρ \; dx ∧ dy ∧ dz\\
          - μ_0 J^x \; dt ∧ dy ∧ dz\\
          - μ_0 J^y \; dt ∧ dz ∧ dx\\
          - μ_0 J^z \; dt ∧ dx ∧ dy\\
      \end{bmatrix}
      \end{equation}

Or with a shorthand:

.. topic:: The Maxwell Equations in Differential Form

   .. math::
   
      \begin{equation}
      (d ⋆ - ⋆ d) \; F = J
      \end{equation}

.. note::

   Flipping the sign of :math:`⋆ d` is also a valid solution.

.. }}}
