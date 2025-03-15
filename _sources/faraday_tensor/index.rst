.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Covariant formulation of the electromagnetic field
==================================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   faraday_tensor_derivation.rst
   of_maxwell_equations_and_rotations.rst
   2form_vs_tensor.rst
   potential_formulation.rst
   all_electromagnetic_field_forms.rst

Summary
-------

My aim with these pages is to improve upon other sources by providing a clear
and natural derivation of the Faraday tensor as an electromagnetic 2-form,
along with the expression of Maxwell's equations via geometric differential
forms. I seek to clarify the connection of the Faraday tensor to rotations in
Minkowski spacetime.

I could not find a truly satisfying derivation of Maxwell's equations in
differential form. Typically, the standard approach consists in assuming both
the final equations in differential form, as well as the electromagnetic
Faraday 2-form, and then prove the equivalence to Maxwell's equations in the
standard vector form. Here, I start from a mathematical point of view,
expressing rotations in Minkowski spacetime as 2-forms. I then systematically
compute the exterior derivative :math:`d` of these rotations, thereby exploring
how to express twists, or to be more precise torque, in Minkowski spacetime.
This procedure naturally leads to the emergence of the Faraday tensor. By
utilizing the exterior derivative :math:`d` and the Hodge dual :math:`⋆`, we
will derive the theory of electromagnetism into a single equation:

.. math:: (d ⋆ - ⋆ d) \; F^{♭♭} = J^{♭♭♭}

The Faraday tensor :math:`F` will be identified as a generic rotation in
spacetime and expressed as a 2-form :math:`F^{♭♭}`. The 4-current :math:`J` is
expressed as the 3-form :math:`J^{♭♭♭}`, represents the amount of torque
applied. Expanding in component form, we will obtain the following set of
equations:

.. math::

   (d ⋆ - ⋆ d ) \left[ \begin{aligned}
     -& \E^x \; dt ∧ dx \\
     -& \E^y \; dt ∧ dy \\
     -& \E^z \; dt ∧ dz \\
      &  B^x \; dy ∧ dz \\
      &  B^y \; dz ∧ dx \\
      &  B^z \; dx ∧ dy \\
   \end{aligned}\right]
   = \begin{bmatrix}
     + μ_0 c ρ \; dx ∧ dy ∧ dz\\
     - μ_0 J^x \; dt ∧ dy ∧ dz\\
     - μ_0 J^y \; dt ∧ dz ∧ dx\\
     - μ_0 J^z \; dt ∧ dx ∧ dy\\
   \end{bmatrix}

The wedge symbol :math:`∧` denotes the exterior product, :math:`\tilde{E}^i`
the electric field components divided by the speed of light :math:`c`, and
:math:`B^i` the magnetic field components. :math:`μ_0` is the `vacuum
permeability <https://en.m.wikipedia.org/wiki/Vacuum_permeability>`_, and
:math:`c ρ` and :math:`J^i` are the components of the `4-current
<https://en.m.wikipedia.org/wiki/Four-current>`_.

Maxwell's equations are rooted in experimental observations, except for
Maxwell's modification to Ampère's circuital law, which originates from purely
mathematical considerations. These equations mathematically express empirical
data and are established experimental facts. We approach the formulation in
geometric differential form via a systematic mathematical analysis of
rotations. There, the reader will likely immediately recognize the presence of
the equations governing electromagnetism. The conclusion will then consist of a
straightforward identification.

To double-check the results, I recommend `Michael Penn's video on Maxwell's
equations via differential forms
<https://www.youtube.com/watch?v=YQoiR-HEUqk>`_.

.. rubric:: :ref:`Rotations in Differential Form`

Rotations in Euclidean space and Minkowski spacetime are systematically
expressed and analyzed using differential forms.

.. rubric:: :ref:`The Exterior Derivative of Rotations in Spacetime`

We systematically analyse the exterior derivative applied to rotations. In
layman's terms, we examine how to apply a rotational force, or torque, to
express a twist in 4-dimensional spacetime.

.. rubric:: :ref:`Deriving the Faraday Tensor from the 1865 Maxwell's Equations`

We revisit the original expression of Maxwell's equations, moving away from the
now-standard vector form proposed by Mr. Heaviside, and drawing significant
inspiration from the work of Mr. Minkowski.

.. rubric:: :ref:`Maxwell's Equations via Differential Forms`

This is the cornerstone of our analysis, where everything falls into place in
the most straightforward manner. From the expressions derived while studying
rotations in differential forms, Maxwell's equations naturally emerge, allowing
us to identify the fundamental equations governing electromagnetism.

.. rubric:: :ref:`All Electromagnetic Field Tensors`

We systematically calculate all representations of the Faraday tensor: the
doubly covariant form, the doubly contravariant form, both mixed forms, as well
as the Hodge duals of all these quantities. I hope this will clarify the
expression of all Faraday tensors using metric signature :math:`(+,-,-,-)`
(Please let me know if you find mistakes!).
