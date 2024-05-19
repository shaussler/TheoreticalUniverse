The Electromagnetic Field Tensor
================================

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   faraday_tensor_derivation.rst
   of_maxwell_equations_and_rotations.rst
   all_electromagnetic_field_tensors.rst

In this serie of articles, I conclude on the formalism of electromagnetism in
differential form. From the stystematic analysis of :ref:`the exterior
derivative of rotations <The Exterior Derivative of Rotations in Spacetime>`, we
determine that electromagnetism is a twist in spacetime expressed with the
exterior derivative :math:`d` and the Hodge dual :math:`⋆`. The Equations of Mr.
Maxwell written in Differential Form are:

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

This can be written compactly in one line as:

.. math:: (d ⋆ - ⋆ d) \; F^{♭♭} = J^{♭♭♭}

Where :math:`F` is the Faraday tensor expressed as a 2-form, and :math:`J` is
the 4-current expressed as a 3-form. :math:`\tilde{E}^i` are the electric field
components divided by the speed of light :math:`c`, and :math:`B^i` are the
magnetic field components. :math:`μ_0` is the `vacuum permeability
<https://en.m.wikipedia.org/wiki/Vacuum_permeability>`_ and :math:`c ρ` and
:math:`J^i` are the component of the `four-current
<https://en.m.wikipedia.org/wiki/Four-current>`_.

To double-check the results, I direct you to `Michael Penn's video on Maxwell's
equations via differential forms
<https://www.youtube.com/watch?v=YQoiR-HEUqk>`_. These pages, I hope, improve
upon other sources by offering a natural, precise and intuitive derivation of
the Faraday tensor written as an electromagnetic 2-form. I hope to clarify the
essence of the Faraday tensor and establish a clear connection to rotations in
spacetime. While many of these expressions are undoubtedly familiar to many, I
have not come across a comprehensive derivation of Maxwell's equations in their
differential form representation. Typically, the equivalence with the widespread
and now standard vector formulation of Mr. Heaviside is demonstrated in reverse.
The standard approach take the final equations as well as the eletromagnetic
2-form as a given, and then demonstrate the equivalence with Maxwell equations
in the standard vector formulation. In contrastg, I begin by defining rotations
in Minkowski spacetime and demonstrate how they can be written as 2-forms. I
then calculate the exterior derivative, essentially exploring how to *twist*
spacetime, and naturally *find* the Faraday tensor and the equations of Mr
Maxwell in a form equivalent to the original 1865 formulation. This provides a
deep connection between twists in spacetime and electromagnetism.

.. ifconfig:: draft in ('yes')

   .. warning:: Draft content

   .. rubric:: The Wave Equation

   .. rubric:: All Electromagentic Field Tensors

   Systematic caculation of all electromagnetic field tensor and hodge dual forms:

   * the doubly covariant form
   * the doubly contravariant from
   * the mixed froms
