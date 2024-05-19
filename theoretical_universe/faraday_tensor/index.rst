The Electromagnetic Field Tensor
================================

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   faraday_tensor_derivation.rst
   of_maxwell_equations_and_rotations.rst
   all_electromagnetic_field_tensors.rst

.. rubric:: Of Maxwell Equations and Rotations in Spacetime

In this serie of articles, we finally conclude on the formalism of
electromagnetism in differential form. From the stystematic analysis of the
:ref:`exterior derivative of rotations in differential forms
<the_exterior_derivative_of_rotations_in_spacetime>`, we determine that
electromagnetism is a twist in spacetime:

.. rubric:: Maxwell Equations in Differential Form

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

This can be written in a compact form as:

.. rubric:: Compact Maxwell Equations in Differential Form

.. math:: (d ⋆ - ⋆ d) \; F^{♭♭} = J^{♭♭♭}

I like to think :ref:`the Cartan-Hodge formalism <the Cartan-Hodge formalism>`
offers a more refined, precise, and intuitive description and interpretation of
the mathematical entities under consideration. It unveils the true essence of
the Faraday tensor and establishes a clear connection to rotations in spacetime.
While many of the expressions mentioned are undoubtedly familiar, I haven't come
across a comprehensive derivation from Maxwell's equations to their differential
form representation. Typically, I've encountered reverse demonstrations where
the equivalence between the two forms is demonstrated.

.. ifconfig:: draft in ('yes')

   .. warning:: Draft content

   .. rubric:: The Wave Equation

   .. rubric:: All Electromagentic Field Tensors

   Systematic caculation of all electromagnetic field tensor and hodge dual forms:

   * the doubly covariant form
   * the doubly contravariant from
   * the mixed froms
