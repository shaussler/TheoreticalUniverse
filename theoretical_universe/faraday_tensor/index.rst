The Electromagnetic Field Tensor
================================

In this serie of articles, we finally conclude on the formalism of
electromagnetism in differential form. From the stystematic analysis of the
:ref:`exterior derivative of rotations in differential forms
<the_exterior_derivative_of_rotations>`, we determine that electromagnetism is
a twist in spacetime. The Maxwell equations are expressed as:

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

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents:

   of_maxwell_equations_and_rotations.rst
   all_electromagnetic_field_tensors.rst
