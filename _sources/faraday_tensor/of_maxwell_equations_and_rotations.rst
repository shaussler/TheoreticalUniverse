.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _of_maxwell_equations_and_rotations:
.. _of maxwell equations and rotations:
.. _Maxwell's Equations via Differential Forms:
.. _Deriving the Faraday 2--form from the 1865 Maxwell's equations:

Deriving the Faraday 2--form from the 1865 Maxwell's equations
==============================================================

.. rst-class:: custom-title

   The connection to rotations

.. rst-class:: custom-author

   by Stéphane Haussler

.. {{{

This page presents the geometric differential formulation of electromagnetism,
emphasizing the direct connection between Maxwell's equations and
:ref:`rotations expressed with differential form <rotations in differential
form>`. By calculating :ref:`the exterior derivative these rotations in
spacetime <the exterior derivative of rotations in spacetime>` and
straightforward identification, we will see that the equations governing
electromagnetism are, in fact, spacetime rotations with the exterior derivative
applied. In layman's terms, we can think of electromagnetism as a torque over
all possible 6 planes of rotations in 4--dimensional spacetime.

I hope my approach will feel more intuitive than the conventional method where
the electromagnetic 2-form as well as the Maxwell's equations in geometric
differential form are given upfront, and equivalence to the vector formulation
proven backward. For an example of the standard proof, see `a nonetheless great
video by Michael Penn <https://www.youtube.com/watch?v=YQoiR-HEUqk&t=3s>`_. The
mathematical expressions obtained in this section correspond to `the
well-recognized differential geometric formulation of Maxwell's equations
<https://en.m.wikipedia.org/wiki/Mathematical_descriptions_of_the_electromagnetic_field#Differential_forms_approach>`_,
where :math:`\mathbf{F}` is the field 2--form and :math:`\mathbf{J}` the
current 3--form.

.. math::

   d\:\mathbf{F} = 0 \\
   d⋆ \mathbf{F} = \mathbf{J}

Unless explicitly stated otherwise, I explicitely indicate the nature of the
mathematical objects involved using musical notation. The electromagnetic field
2--form :math:`\mathbf{F}` is written with a double musical flat
:math:`F^{♭♭}`, the current 3--form with a triple musical flat :math:`J^{♭♭♭}`,
and the Hodge dual current 1--form with a single musical flat :math:`J^♭`.

This argumentation in this page proceeds as follows: First, I reordered
Maxwell's equations to align with their original formulation, using modern
notation. This reorered form will serve the foundation for expressing the
electromagnetic field equations in terms of geometric differential forms. Next,
I represent a generic rotation in spacetime to which I apply the exterior
derivative. Finally, I identified Maxwell's equations with the exterior
derivative of this spacetime rotation.

The discussion assumes a solid understanding of the exterior derivative
:math:`d`, Élie Caretan's differential forms, as well as :ref:`Hodge duality
<hodge duality>`. This page is self-contained and can be read independently of
other content on this site.

.. include:: faraday_tensor_derivation.rst
   :start-after: _vector_formulation_of_mr_heaviside:
   :end-before: _the_tensor_of_mr_faraday:

We now link the ordered Maxwell equations to the exterior derivative of
rotations in spacetime. For this, we first express a generic rotation as a
linear combination of bivectors, flatten to a 2--form, and calculate the
exterior derivative.

.. }}}

Rotations in differential forms
-------------------------------

.. {{{

.. include:: ../rotations/rotations_in_minkowski_space.rst
   :start-after: _inc_begin_♯♯_rotations:
   :end-before: _inc_end_♯♯_rotations:

.. include:: ../rotations/rotations_in_minkowski_space.rst
   :start-after: _inc_begin_♭♭_rotations:
   :end-before: _inc_end_♭♭_rotations:

.. }}}

The exterior derivative of rotations
------------------------------------

.. {{{

In the article :ref:`Differential operators expressed as exterior derivatives`,
I systematically compute the exterior derivative of all possible k--forms in
both 3D Euclidean space and 4D spacetime with the Minkowski metric. The
motivation for these systematic calculations is that all differential operators
acting on fields (such as the gradient and the laplacian) or vector fields
(such as the divergence and the curl) can be expressed using combinations of
the Hodge star operator :math:`⋆` and the exterior derivative :math:`d`.

Since the combinations of these two operators are finite, this approach allows
for the calculation of all conceivable differential operators, which are
generalized within the framework of exterior calculus. Specifically, we derive
expressions for the exterior derivative of rotations and the exterior
derivative of their Hodge duals the following:

.. rubric:: Hodge dual of rotations

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_⋆R♭♭:
   :end-before: _inc_end_⋆R♭♭:

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_calc_⋆R♭♭:
   :end-before: _inc_end_calc_⋆R♭♭:

.. rubric:: Exterior derivative of the Hodge dual of rotations

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_d⋆R♭♭:
   :end-before: _inc_end_d⋆R♭♭:

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_calc_d⋆R♭♭:
   :end-before: _inc_end_calc_d⋆R♭♭:

.. rubric:: Exterior derivative of rotations

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_dR♭♭:
   :end-before: _inc_end_dR♭♭:

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_calc_dR♭♭:
   :end-before: _inc_end_calc_dR♭♭:

.. rubric:: Hodge dual of the exterior derivative of rotations

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_⋆dR♭♭:
   :end-before: _inc_end_⋆dR♭♭:

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_calc_⋆dR♭♭:
   :end-before: _inc_end_calc_⋆dR♭♭:

.. }}}

Identifying the Faraday 2--form
-------------------------------

.. {{{

To summarize the results and observations thus far, an arbitrary rotation in
Minkowski space is represented by a 2--form:

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_R♭♭:
   :end-before: _inc_end_R♭♭:

By applying the exterior derivative :math:`d` to this rotation or to its Hodge
dual (effectively calculating a torque), we obtain:

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_d⋆R♭♭:
   :end-before: _inc_end_d⋆R♭♭:

.. include:: ../differential_operators/minkowski-space/2-forms.rst
   :start-after: _inc_begin_⋆dR♭♭:
   :end-before: _inc_end_⋆dR♭♭:

We have also reordered the 1865 Maxwell equations to:

.. rubric:: Inhomogenous equations

.. include:: ./faraday_tensor_derivation.rst
   :start-after: _inc_beg_ordered_inhomogenous_equations:
   :end-before: _inc_end_ordered_inhomogenous_equations:

.. rubric:: Homogenous equations

.. include:: ./faraday_tensor_derivation.rst
   :start-after: _inc_beg_ordered_homogenous_equations:
   :end-before: _inc_end_ordered_homogenous_equations:

.. rubric:: Identification

Identifiying the components of the electric field :math:`\tilde{E}^i=E^i/c` and
the magnetic field :math:`B^i` is straightforward:

.. math::

   \begin{matrix}
       \E^x = R^x \\
       \E^y = R^y \\
       \E^z = R^z \\
        B^x = Q^x \\
        B^y = Q^y \\
        B^z = Q^z \\
   \end{matrix}

The Faraday 2--form :math:`F^{♭♭}` is a rotation in Minkowski spacetime.

.. math::

   F^{♭♭} = \left[ \begin{aligned}
       - & \E^x \; dt ∧ dx \\
       - & \E^y \; dt ∧ dy \\
       - & \E^z \; dt ∧ dz \\
         &  B^x \; dy ∧ dz \\
         &  B^y \; dz ∧ dx \\
         &  B^z \; dx ∧ dy \\
   \end{aligned} \right]

Maxwell's equations are obtained by applying the exterior derivative, both
directly :math:`dF^{♭♭}` and to its Hodge dual :math:`d⋆F^{♭♭}`:

.. rubric:: Inhomogenous Maxwell equations

.. math::

   d\:⋆ \left[ \begin{aligned}
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

.. rubric:: Homogenous Maxwell equations

.. math::

   d \left[ \begin{aligned}
       - & \E^x \; dt ∧ dx \\
       - & \E^y \; dt ∧ dy \\
       - & \E^z \; dt ∧ dz \\
         &  B^x \; dy ∧ dz \\
         &  B^y \; dz ∧ dx \\
         &  B^z \; dx ∧ dy \\
   \end{aligned} \right]
   = 0

We have flipped the sign of the ordered homegenous Maxwell equations to our
conveniance to ensure the correct overall sign. With our explicit notation,
using a double musical flat ♭♭ to identify 2--forms, and a single musical flat
♭ to identify 1--forms, we have:

.. math::

   d\:F^{♭♭} &= 0   \\
   d⋆ F^{♭♭} &= J^♭ \\

As advertised in the introduction and using the implicit notation of the
wikipedia article, we fall back to the `well-recognized differential geometric
formulation of Maxwell's equations
<https://en.m.wikipedia.org/wiki/Mathematical_descriptions_of_the_electromagnetic_field#Differential_forms_approach>`_,
where :math:`\mathbf{F}` is the field 2--form and :math:`\mathbf{J}` is the
current 3--form.

.. math::

   d\:\mathbf{F} &= 0          \\
   d⋆ \mathbf{F} &= \mathbf{J} \\

.. }}}

A single equation
-----------------

.. {{{

Adding a further Hodge star to the Homogenous equations is equally valid and we
can equally write :math:`d\:F^{♭♭} = 0` or :math:`⋆d\:F^{♭♭}=0`. With our
explicit notation using double or single musical flats to idenfity 1--forms (♭)
and 2--forms (♭♭), and since :math:`⋆\:d\:F` is a 1--form and :math:`d⋆F` a
3--form, we notice that we can unambiguously merge inhomogeneous and
homogeneous equations into a single equation [note2]_:

.. math::

   d ⋆ \left[ \begin{aligned}
       - & \E^x \; dt ∧ dx \\
       - & \E^y \; dt ∧ dy \\
       - & \E^z \; dt ∧ dz \\
         &  B^x \; dy ∧ dz \\
         &  B^y \; dz ∧ dx \\
         &  B^z \; dx ∧ dy \\
   \end{aligned} \right] + ⋆\:d \left[ \begin{aligned}
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

.. rubric:: Maxwell's equations in differential form

.. math::

   (d ⋆ + ⋆ d ) \left[ \begin{aligned}
       - & \E^x \; dt ∧ dx \\
       - & \E^y \; dt ∧ dy \\
       - & \E^z \; dt ∧ dz \\
         &  B^x \; dy ∧ dz \\
         &  B^y \; dz ∧ dx \\
         &  B^z \; dx ∧ dy \\
   \end{aligned} \right] = \left[ \begin{aligned}
       + μ_0 c ρ \; dx ∧ dy ∧ dz\\
       - μ_0 J^x \; dt ∧ dy ∧ dz\\
       - μ_0 J^y \; dt ∧ dz ∧ dx\\
       - μ_0 J^z \; dt ∧ dx ∧ dy\\
   \end{aligned} \right]

With a shorthand :math:`F^{♭♭}` for the electromagnetic field 2-form and
:math:`J^{♭♭♭}` for the current 3-form, we conclude with the compact form
[note3]_:

.. topic:: Maxwell's equations

   .. math:: (d ⋆ + ⋆ d) \; F^{♭♭} = J^{♭♭♭}

Maxwell's equations are interpreted as a twist in spacetime, with a strength
proportional to the 4-current.

.. admonition:: Reducing to a single equation using the *wikipedia* notation
   :class: dropdown

   Using the *wikipedia* notation, we arrive at the same result. However the
   lack of an explicit distinction between 1--forms and 2--forms is unfortunate
   as it makes it harder to see the reduction to a single equation.

   .. math::

      ⋆ \: d \: \mathbf{F} + d⋆\mathbf{F} = \mathbf{J}

   Since :math:`d\:\mathbf{F}` is a 3--form, its Hodge dual
   :math:`⋆\:d\:\mathbf{F}` is a 1--form. We can thus rewrite the homogenous
   equation as acting on 1--forms, and the inhomogeneous equations as acting on
   3--forms:

   .. math::

      \begin{alignedat}{2}
      ⋆ \: d \: \mathbf{F} &= 0          & \qquad\text{1-forms} \\
      d⋆\mathbf{F}         &= \mathbf{J} & \qquad\text{3-forms} \\
      \end{alignedat}

   Expanding the right hand side of both equations for the argument, we have:

   .. math::

      ⋆ \: d \: \mathbf{F} =& \: 0\:dt + 0\:dx + 0\:dy + 0\:dz                                             \\
      d⋆\mathbf{F}         =& \: \mu_0 ρ dx∧dy∧dz - μ_0 J^x dt∧dy∧dz - μ_0 J^y dt∧dz∧dx - μ_0 J^z dt∧dx∧dy \\

   Therefore, the differential geometric formulation can be unambiguously
   reduced to a single equation involving both 3--forms and 1--forms:

   .. math::

      ⋆ \: d \: \mathbf{F} + d⋆\mathbf{F} = \mathbf{J}

.. }}}

Notes
-----

.. {{{

.. [note2] An equation containing 3-forms and 2-forms indeed cannot be reduced.
   For example, the following equation: :math:`a \; dx ∧ dy + b \; dx ∧ dy ∧ dz
   = c \; dx ∧ dy` cannot be simplified. Surface 2-forms and volume 3-forms are
   distinct objects, but they can be represented in the same equation using the
   :math:`+` symbol, even though they cannot actually be added together. Similar
   examples include combining the real and imaginary parts of complex numbers,
   or adding bivectors and trivectors in Clifford algebra. With the exemplary
   equation above, we thus necessarily have :math:`a = c` as well as :math:`b =
   0`. This is how we can write the Maxwell equations via differential forms
   into a single equation.

.. [note3] Flipping the sign of :math:`⋆ d` is equally valid.

.. }}}
