The Electromagnetic Field Tensor
================================

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   faraday_tensor_derivation.rst
   of_maxwell_equations_and_rotations.rst
   all_electromagnetic_field_tensors.rst

My goal with these pages is to improve upon other sources by offering a
natural, precise, and intuitive derivation of the Faraday tensor expressed as
an electromagnetic 2-form, along with the equations governing electormagnetism
in differential form. I aim to clarify the essence of the Faraday tensor and
establish the connection to rotations in Minkowski spacetime. While many of
these expressions will be familiar to the reader acquainted with the Faraday
2-form, I have not encountered a comprehensive derivation of Maxwell's
equations in their differential form representation. Typically, the standard
approach takes the final equations and the electromagnetic 2-form as given,
demonstrating their equivalence with Maxwell's equations in the standard vector
formulation proposed by Mr. Heaviside. In contrast, I start by defining
rotations in Minkowski spacetime and show how they can be written as 2-forms. I
then calculate the exterior derivative, exploring how to twist spacetime, and
naturally derive the Faraday tensor and Maxwell's equations in a form
equivalent to the original 1865 formulation. This approach provides a deep
connection between spacetime twists and electromagnetism.

Through a systematic analysis of rotations, we will establish that
electromagnetism is essentially a twist in spacetime. By utilizing the exterior
derivative :math:`d` and the Hodge dual :math:`⋆`, we will derive the theory of
electromagnetism into a single equation:

.. math:: (d ⋆ - ⋆ d) \; F^{♭♭} = J^{♭♭♭}

Where the Faraday tensor :math:`F` is expressed as a 2-form :math:`F^{♭♭}`, and
the 4-current :math:`J` is expressed as a 3-form :math:`F^{♭♭♭}`. Expanding in
component form we obtain a set of equations which can be used for actual
computations:

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

This allows for a systematic analysis of the exterior derivative applied to
rotations. In layman's terms, we examine how to apply a rotational force, or
torque, to twist spacetime.

.. rubric:: :ref:`Deriving the Faraday Tensor from the 1865 Maxwell's Equations`

We revisit the original expression of Maxwell's equations, moving away from the
now-standard vector form proposed by Mr. Heaviside, and drawing significant
inspiration from the work of Mr. Minkowski.

.. rubric:: :ref:`Maxwell's Equations via Differential Forms`

This is the core of our analysis, where everything falls into place in the most
straightforward manner. From the expressions derived while studying rotations
in differential forms, Maxwell's equations naturally emerge, allowing us to
identify the fundamental equations governing electromagnetism.

.. rubric:: :ref:`All Electromagnetic Field Tensors`

Here, we systematically calculate all representations of the Faraday tensor:
the doubly covariant form, the doubly contravariant form, both mixed forms, as
well as the Hodge duals of all these quantities. I hope this will clarify the
expression of all Faraday tensors using metric signature :math:`(+,-,-,-)`
(Please let me know if you find mistakes!).
