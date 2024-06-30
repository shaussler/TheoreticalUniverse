The Electromagnetic Field Tensor
================================

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   faraday_tensor_derivation.rst
   of_maxwell_equations_and_rotations.rst
   all_electromagnetic_field_tensors.rst

My aim with these pages is to improve upon other sources by providing a clear
and natural derivation of the Faraday tensor as an electromagnetic 2-form,
along with the expression of Maxwell's equations via geometric differential
forms. I seek to clarify the connection of the Faraday tensor to rotations in
Minkowski spacetime.

I could not find a truly satisfying derivation of Maxwell's equations in
differential form. Typically, the standard approach assumes the final equations
as well as the electromagnetic Faraday 2-form, and then proving their
equivalence to Maxwell's equations in the widespread vector formulation of
Heaviside. In contrast, I begin by expressing rotations in Minkowski spacetime
as 2-forms. I then systematically compute the exterior derivative of rotations
to explore the expression of twists in Minkowski spacetime. This procedure
naturally leads to the emergence of the Faraday tensor. By utilizing the
exterior derivative :math:`d` and the Hodge dual :math:`⋆`, we will derive the
theory of electromagnetism into a single equation:

.. math:: (d ⋆ - ⋆ d) \; F^{♭♭} = J^{♭♭♭}

Where the Faraday tensor :math:`F` will be identified as a generic rotation in
4-dimensional spacetime and expressed as a 2-form :math:`F^{♭♭}`. The 4-current
:math:`J` is expressed as a 3-form :math:`F^{♭♭♭}` and represents the amount of
torque. Expanding in component form, we obtain a set of equations which can be
used for actual computations:

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

Where the wedge symbol :math:`∧` denotes the exterior product,
:math:`\tilde{E}^i` the electric field components divided by the speed of light
:math:`c`, and :math:`B^i` are the magnetic field components. :math:`μ_0` is
the `vacuum permeability
<https://en.m.wikipedia.org/wiki/Vacuum_permeability>`_ and :math:`c ρ` and
:math:`J^i` are the components of the `four-current
<https://en.m.wikipedia.org/wiki/Four-current>`_.

Maxwell's equations are rooted in experimental observations. Except for
Maxwell's modification to Ampère's circuital law, these equations are
mathematical expressions of empirical data, and can thus be considered
established experimental facts. We approach rotations in differential forms
from a purely mathematical and systematic perspective. An attentive reader will
immediately recognize the presence of the equations governing electromagnetism.
The conclusion will be a straightforward process of identifying components.

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
