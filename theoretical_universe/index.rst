.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Theoretical Universe
====================

This serie was initially conceived as a set of short, independent articles.
However, it has expanded beyond my initial expectation. It all begins with the
derivation of the electromagnetic field tensor from Maxwell's equations of
1865, a process straightforward for those with a grasp of vector calculus and
matrix multiplication.

My exploration extended to Riemannian manifolds, differential forms, and the
exterior derivative. I delved into musical isomorphisms and the Hodge dual,
encapsulating these concepts in what I term :ref:`the Cartan-Hodge formalism
<the_cartan_hodge_formalism>`. This comprehensive framework facilitated a
systematic analysis of rotation representation in differential form and a
thorough examination of differential operators within this context. Notably, I
dissected the exterior derivative of rotations, leading to the understanding
that it precisely mirrors Maxwell's equations, offering a fully coherent
demonstration of the formulation of Maxwell's equations in differential form:

.. topic:: Maxwell Equations in the Cartan-Hodge Formalism

   .. math::

      \newcommand{\E}{\tilde{E}}
      (d ⋆ - ⋆ d ) \begin{bmatrix}
          \E^x \; dx ∧ dt \\ \E^y \; dy ∧ dt \\ \E^z \; dz ∧ dt \\
           B^x \; dy ∧ dz \\  B^y \; dz ∧ dx \\  B^z \; dx ∧ dy \\
      \end{bmatrix}
      = \begin{bmatrix}
          + μ_0 c ρ \; dx ∧ dy ∧ dz\\
          - μ_0 J^x \; dt ∧ dy ∧ dz\\
          - μ_0 J^y \; dt ∧ dz ∧ dx\\
          - μ_0 J^z \; dt ∧ dx ∧ dy\\
      \end{bmatrix}

   :math:`d` is the exterior derivative, :math:`⋆` the Hodge star operator and
   :math:`∧` the wedge product.

Some of the content of these articles, although certainly not *new*, may offer
insights which may not be widely known. I present the details of all
calculations to give the reader a chance to follow or find mistakes. If you are
aware of freely available resources I should cite, open an issue and I will
include a reference. If you find mistakes, don't hesitate to directly provide
corrections by sending a merge request to `the Theoretical Universe Github
repository <https://github.com/shaussler/TheoreticalUniverse/>`_.

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   licence.rst
   contribute.rst
   the_cartan_hodge_formalism/index.rst
   rotations/index.rst
   differential_operators/index.rst
   faraday_tensor/index.rst
   field_equations/index.rst
   miscellaneous/index.rst

LINKS:

.. table::
   :align: left

   ============= =======================================================

   ============= =======================================================
   Documentation https://shaussler.github.io/TheoreticalUniverse
   Repository    https://github.com/shaussler/TheoreticalUniverse
   Issues        https://github.com/shaussler/TheoreticalUniverse/issues
   ============= =======================================================
