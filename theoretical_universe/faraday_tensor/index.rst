The Electromagnetic Field Tensor
================================

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   of_maxwell_equations_and_rotations.rst
   all_electromagnetic_field_tensors.rst

.. rubric:: Of Maxwell Equations and Rotations in Spacetime

In this serie of articles, we finally conclude on the formalism of electromagnetism in differential form. From the
stystematic analysis of the :ref:`exterior derivative of rotations in differential forms
<the_exterior_derivative_of_rotations_in_spacetime>`, we determine that electromagnetism is a twist in spacetime.

.. topic:: Maxwell Equations in Differential Form

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

.. topic:: Condensed Version of the Maxwell Equations in Differential Form

   .. math::
   
      \begin{equation}
      (d ⋆ - ⋆ d) \; F = J
      \end{equation}

I believe the :ref:`Cartan-Hodge formalism <the_cartan_hodge_formalism>` offers a more refined, precise, and intuitive
description and interpretation of the mathematical entities under consideration. It unveils the true essence of the
Faraday tensor and establishes a clear connection to rotations in spacetime. While many of the expressions mentioned are
undoubtedly familiar, I haven't come across a comprehensive derivation from Maxwell's equations to their differential
form representation. Typically, I've encountered reverse demonstrations where the equivalence between the two forms is
demonstrated. Additionally, I haven't yet come across the condensed form of Maxwell's equations in the form :math:`(d⋆ =
⋆d) F = J`.

.. rubric:: All Electromagentic Field Tensors

Systematic caculation of all electromagnetic field tensor and hodge dual forms:

* the doubly covariant form
* the doubly contravariant from
* the mixed froms

.. warning::

   Under construction
