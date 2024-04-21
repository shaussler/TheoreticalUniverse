.. Theoretical Universe (c) by Stéphane Haussler
.. 
.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _of_maxwell_equations_and_rotations:

Of Maxwell Equations and Rotations
==================================

.. rst-class:: custom-author

   by Stéphane Haussler

This article investigates the connection between :ref:`rotations
<rotations_in_differential_form>`, the :ref:`exterior derivative of rotations
<the_exterior_derivative_of_rotations>`, and the equations of Mr. Maxwell. I
utilize :ref:`the Cartan-Hodge's formalism <the_cartan_hodge_formalism>` in
Minkowski space-time. I demonstrate that applying the exterior derivative to
rotations yields the equations governing electromagnetism. These expressions
reveal Maxwell equations are a twist in the fabric of spacetime.

The content in this articles might not be wildely known as I have not found my
observations mentioned anywhere. Feel free to open an issue and I will include
a reference if you are aware of one. If you find mistakes, don't hesitate to
open an issue or directly provide corrections by sending a merge request to my
`Github repository <https://github.com/shaussler/TheoreticalUniverse/>`_.

The Equations of Mr. Maxwell
----------------------------

.. {{{

In a previous article, I :ref:`derive from the 1865 Maxwell equations the
following expressions <the_ordered_equations>`:

.. rubric:: Inhomogenous Maxwell equations

.. math::

   \begin{equation}
   \newcommand{\E}{\tilde{E}}
   \begin{matrix}
                & + ∂_x \E^x & + ∂_y \E^y & + ∂_z \E^z & = & + μ_0 c ρ \\
     + ∂_t \E^x &            & - ∂_y  B^z & + ∂_z  B^y & = & - μ_0 J^x \\
     + ∂_t \E^y & + ∂_x  B^z &            & - ∂_z  B^x & = & - μ_0 J^y \\
     + ∂_t \E^z & - ∂_x  B^y & + ∂_y  B^x &            & = & - μ_0 J^z \\
   \end{matrix}
   \end{equation}

.. rubric:: Homogenous Maxwell equations

.. math::

   \begin{equation}
   \begin{matrix} \newcommand{\E}{\tilde{E}}
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

In previous articles, I investigate :ref:`rotations in differential form
<rotations_in_minkowski_space>` as well as :ref:`the exterior derivatives of
rotations <the_exterior_derivative_of_rotations>`. I demonstrated that
rotations are expressed as:

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

Taking the exterior derivative of the rotation above represent a twist in the
counterclockwise direction, since :ref:`this is how I oriented space
<orientation_of_space>` from :math:`\mathbf{e}_x` to :math:`\mathbf{e}_y` to
:math:`\mathbf{e}_z`. The exterior derivative can be applied to either the
rotation, or its :ref:`Hodge dual <hodge_duality>`:

.. rubric:: The Exterior Derivative of the Hodge Dual of a Rotation

.. math::

   \begin{equation}
   \newcommand{\_}{\phantom{∂_m m}} % Phantom for alignment
   ⋆d(⋆R^{♭♭})
   =
   \begin{bmatrix}
   (   \_    & - ∂_x a & - ∂_y b & - ∂_z c ) ⋆ dt \\
   ( - ∂_t a &   \_    & + ∂_y f & - ∂_z e ) ⋆ dx \\
   ( - ∂_t b & - ∂_x f &   \_    & + ∂_z d ) ⋆ dy \\
   ( - ∂_t c & + ∂_x e & - ∂_y d &   \_    ) ⋆ dz \\
   \end{bmatrix}
   \end{equation}

.. rubric:: The Exterior Derivative of a Rotation

.. math::

   \begin{equation}\
   \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
   ⋆(dR^{♭♭}) =
   \begin{bmatrix}
     ( \; \phan   & - ∂_x d & - ∂_y e & - ∂_z f \; ) \; dt \\
     ( \; - ∂_t d & \phan   & - ∂_y c & + ∂_z b \; ) \; dx \\
     ( \; - ∂_t e & + ∂_x c & \phan   & - ∂_z a \; ) \; dy \\
     ( \; - ∂_t f & - ∂_x b & + ∂_y a & \phan   \; ) \; dz \\
   \end{bmatrix}
   \end{equation}

.. }}}

Identifying the Equations of Mr. Maxwell
----------------------------------------

The equations of Mr. Maxwell and obtained for the exterior derivative are
exactly the same, up to a sign which depends on our convention for orienting
space and was chosen counterclock-wise. To flip the convention to clock-wise,
we flip the sign:

.. math::

   \begin{equation}
   \newcommand{\E}{\tilde{E}}
   \begin{matrix}
   a → -a \\
   b → -b \\
   c → -c \\
   d → -d \\
   e → -e \\
   f → -f \\
   \end{matrix}
   \end{equation}

And idenfiy the components of the electric and magnetic fields:

.. math::

   \begin{equation}
   \newcommand{\E}{\tilde{E}}
   \begin{matrix}
   \E^x = a \\
   \E^y = b \\
   \E^z = c \\
    B^x = d \\
    B^y = e \\
    B^z = f \\
   \end{matrix}
   \end{equation}

We conclude electromagnetism is a twist in the fabric of spacetime. The Maxwell
equations are:

.. topic:: Inhomogenous Maxwell Equations

   .. math::

      \begin{equation}
      \newcommand{\E}{\tilde{E}}
      ⋆ d ⋆ \begin{bmatrix}
          \E^x \; dx ∧ dt \\
          \E^y \; dy ∧ dt \\
          \E^z \; dz ∧ dt \\
           B^x \; dy ∧ dz \\
           B^y \; dz ∧ dx \\
           B^z \; dx ∧ dy \\
      \end{bmatrix}
      = \begin{bmatrix}
          + μ_0 c ρ \; dt \\
          - μ_0 J^x \; dx \\
          - μ_0 J^y \; dy \\
          - μ_0 J^z \; dz \\
      \end{bmatrix}
      \end{equation}

.. topic:: Homogenous Maxwell Equations

   .. math::

      \begin{equation}
      \newcommand{\E}{\tilde{E}}
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

What we learned
---------------

First, note that we fall back to `the conventional expression of Maxwell
equations in differential form:
<https://en.m.wikipedia.org/wiki/Mathematical_descriptions_of_the_electromagnetic_field#Differential_forms_approach>`_

.. math::

   \begin{equation}
   \begin{matrix}
   d⋆ \mathbf{F} &= \mathbf{J} \\
   d \mathbf{F}  &= 0          \\
   \end{matrix}
   \end{equation}

I would like to think the :ref:`Cartan-Hodge formalism
<the_cartan_hodge_formalism>` result in a more precise description and
interpretation of the mathematical objects by the use of the musical sharp
:math:`♯` and flat :math:`♭` operators. The true nature of the Faraday tensor
by the use of the wedge :math:`∧` product and the exact link to rotations in
spacetime are fully apparent. The expressions above are certainly known. I am
however not aware of a complete derivation from Maxwell equations towards their
expression in differential form. Instead, I have only seen backward
demonstrations where the differential form expression is shown to be equivalent
to Maxwell's equation.

.. }}}

