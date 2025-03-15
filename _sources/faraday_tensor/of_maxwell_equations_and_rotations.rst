.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _of_maxwell_equations_and_rotations:
.. _of maxwell equations and rotations:
.. _Maxwell's Equations via Differential Forms:

Deriving the Faraday 2-form from the 1865 Maxwell's equations
=============================================================

.. rst-class:: custom-title

   The Connection to Rotations

.. rst-class:: custom-author

   by Stéphane Haussler

The present page presents a derivation of the geometric differential
formulation of electromagnetism, emphasizing the direct connection between
Maxwell's equations and :ref:`rotations in differential form <rotations in
differential form>`. The mathematical expressions are based on previous
investigations, where I utilize :ref:`the Cartan-Hodge formalism <the
cartan-hodge formalism>` to calculate :ref:`the exterior derivative of
rotations in spacetime <the exterior derivative of rotations in spacetime>`.
Through a straightforward identification process, we will see that the
equations governing electromagnetism are, in fact, spacetime rotations with the
exterior derivative applied. In layman's terms, we can think of
electromagnetism as a twist in spacetime.

My approach should feel more intuitive than the conventional method where the
electromagnetic 2-form as well as the Maxwell's equations in geometric
differential form are given upfront, and equivalence to the vector formulation
proven backward. For an example of the standard proof, see `a nonetheless great
video by Michael Penn <https://www.youtube.com/watch?v=YQoiR-HEUqk&t=3s>`_. The
mathematical expressions obtained in this section correspond to `the
well-recognized differential geometric formulation of Maxwell's equations
<https://en.m.wikipedia.org/wiki/Mathematical_descriptions_of_the_electromagnetic_field#Differential_forms_approach>`_,
where :math:`\mathbf{F}` is the field 2-form and :math:`\mathbf{J}` the current
3-form.

.. math::

   d\:\mathbf{F} = 0 \\
   d⋆ \mathbf{F} = \mathbf{J}

Unless explicitly mentioned otherwise, I use :ref:`the Cartan-Hodge formalism`,
which permits to be explicit about the nature of the mathematical objects
involved by using musical notation. The electromagnetic field 2-form
:math:`\mathbf{F}` is written :math:`F^{♭♭}`, the current 3-form :math:`J^{♭♭♭}`
and the Hodge dual current 1-form :math:`J^♭`.

The Equations of Mr. Maxwell
----------------------------

.. {{{

In the article :ref:`Deriving the Faraday Tensor from the 1865 Maxwell
Equations`, I reordered and re-expressed the original Maxwell's equations with
modern notation. We use this form as the basis for formulating the
electromagnetic field equations using geometric differential forms.

.. rubric:: Inhomogenous Maxwell equations

*Gauss’s Law* and *Ampère’s Circuital Law* are gathered:

.. math::
   :label: M1

   \begin{alignedat}{5}
                & + ∂_x \E^x & + ∂_y \E^y & + ∂_z \E^z & = & + μ_0 c ρ \\
     + ∂_t \E^x &            & - ∂_y  B^z & + ∂_z  B^y & = & - μ_0 J^x \\
     + ∂_t \E^y & + ∂_x  B^z &            & - ∂_z  B^x & = & - μ_0 J^y \\
     + ∂_t \E^z & - ∂_x  B^y & + ∂_y  B^x &            & = & - μ_0 J^z \\
   \end{alignedat}

.. rubric:: Homogenous Maxwell equations

Similarly, *Gauss’s Law for Magnetism* and *Faraday’s Law of Induction* are also
be formulated in this manner:

.. math::
   :label: M2

   \begin{alignedat}{4}
                & + ∂_x  B^x & + ∂_y  B^y & + ∂_z  B^z & = 0 \\
     + ∂_t  B^x &            & + ∂_y \E^z & - ∂_z \E^y & = 0 \\
     + ∂_t  B^y & - ∂_x \E^z &            & + ∂_z \E^x & = 0 \\
     + ∂_t  B^z & + ∂_x \E^y & - ∂_y \E^x &            & = 0 \\
   \end{alignedat}

.. }}}

The Exterior Derivative of Rotations
------------------------------------

.. {{{

In the article :ref:`Rotations in Minkowski Space`, I investigate spacetime
rotations in differential form and demonstrate that rotations can be expressed
as:

.. math::
   R^{♭♭} = \left[ \begin{aligned}
     - &a \; dt ∧ dx \\
     - &b \; dt ∧ dy \\
     - &c \; dt ∧ dz \\
       &d \; dy ∧ dz \\
       &e \; dz ∧ dx \\
       &f \; dx ∧ dy \\
   \end{aligned} \right]

In the subsequent article :ref:`The Exterior Derivative of Rotations in
Spacetime`, I systematically calculate the exterior derivative of arbitrary
rotations and their Hodge dual, obtaining the following expressions:

.. rubric:: Exterior derivative of the Hodge dual of rotations in differential
   form

.. math::
   :label: dR1

   d ⋆ R^{♭♭} = \left[ \begin{alignedat}{5}
     (&         & + ∂_x a & + ∂_y b & + ∂_z c \:&) \; dx ∧ dy ∧ dz \\
     (& + ∂_t a &         & - ∂_y f & + ∂_z e \:&) \; dt ∧ dy ∧ dz \\
     (& + ∂_t b & + ∂_x f &         & - ∂_z d \:&) \; dt ∧ dz ∧ dx \\
     (& + ∂_t c & - ∂_x e & + ∂_y d &         \:&) \; dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

.. rubric:: Hodge dual of the exterior derivative of rotations in differential
   form

.. math::
   :label: dR2

   ⋆\:d\:R^{♭♭} = \left[ \begin{alignedat}{5}
     (&       \;   & - ∂_x \; d & - ∂_y \; e & - ∂_z \; f \:&) \; dt \\
     (& - ∂_t \; d &       \;   & - ∂_y \; c & + ∂_z \; b \:&) \; dx \\
     (& - ∂_t \; e & + ∂_x \; c &       \;   & - ∂_z \; a \:&) \; dy \\
     (& - ∂_t \; f & - ∂_x \; b & + ∂_y \; a &       \;   \:&) \; dz \\
   \end{alignedat} \right]

.. }}}

Identifying the Equations of Mr. Maxwell
----------------------------------------

.. {{{

From equations :eq:`M1` and :eq:`dR1`, identifiying the components of the
electric field :math:`\tilde{E}^i=E^i/c` and magnetic field :math:`B^i` is
trivial:

.. math::

   \begin{matrix}
     \E^x = a & B^x = d \\
     \E^y = b & B^y = e \\
     \E^z = c & B^z = f \\
   \end{matrix}

We could have equally used equations :eq:`M2` and :eq:`dR1` for the
identification. There, the sign of :eq:`M2` can be flipped as needed. The doubly
covariant Faraday tensor :math:`F^{♭♭}` is identified as an arbitrary rotation
:math:`R^{♭♭}` in Minkowski spacetime:

.. rubric:: The doubly covariant Faraday 2-form as a rotation in spacetime

.. math::

   R^{♭♭} = F^{♭♭} = \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right]

Maxwell equations are therefore obtained by applying the exterior derivative to
that rotation with :math:`d F^{♭♭}` and its Hodge dual :math:`d ⋆ F^{♭♭}`.

.. rubric:: Inhomogenous Maxwell equations via differential forms

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

.. rubric:: Homogenous Maxwell equations via differential forms

.. math::

   ⋆\:d \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right]
   = 0

Thus and as advertised in the introduction, we fall back to the well-known
expression of Maxwell equations in differential form where :math:`\mathbf{F}` is
the field 2-form and :math:`\mathbf{J}` is the current 3-form.

.. math::

   d\:\mathbf{F} &= 0          \\
   d⋆ \mathbf{F} &= \mathbf{J} \\

.. }}}

A Single Equation
-----------------

.. {{{

With the explicit component form of the Cartan-Hodge formalism, it may now be
obvious that since :math:`⋆\:d\:F` is a 1-form and :math:`d⋆F` a 3-form, we can
unambiguously merge inhomogeneous and homogeneous equations [note2]_.

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

.. rubric:: Maxwell's Equations in Differential Form

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

.. topic:: Maxwell equations

   .. math:: (d ⋆ + ⋆ d) \; F^{♭♭} = J^{♭♭♭}

Maxwell's equations are interpreted as a twist in spacetime, with a strength
proportional to the 4-current.

.. admonition:: Proof using the *standard* notation
   :class: dropdown

   Using the standard notation, we get to the same result:

   .. math::

      ⋆ \: d \: \mathbf{F} + d⋆\mathbf{F} = \mathbf{J}

   Since :math:`d\:\mathbf{F}` is a 3-form, its Hodge dual
   :math:`⋆\:d\:\mathbf{F}` is a 1-form. We can thus rewrite the homogenous
   equation as acting on 1-forms, and the inhomogeneous equations as acting on
   3-forms:

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
   reduced to a single equation involving both 3-forms and 1-forms:

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
