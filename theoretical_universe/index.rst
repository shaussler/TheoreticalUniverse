.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Theoretical Universe
====================

.. rst-class:: custom-title

   Maxwell Field Equations via Differential Forms

.. rst-class:: custom-author

   by Stéphane Haussler

Within these pages, you will find a systematic analysis and demonstration of
the formulation of electromagnetism expressed via differential forms. Some of
the content of these articles, although certainly not *new*, may offer insights
not be widely known. I present the details of all calculations to give the
reader a chance to follow and find mistakes. If you are aware of freely
available resources I should cite, open an issue and I will include a
reference. If you find errors, don't hesitate to directly provide corrections
by sending a merge request to `the Theoretical Universe Github repository
<https://github.com/shaussler/TheoreticalUniverse/>`_.

I point out the article :ref:`faraday tensor derivation` for its simplicity.
This derivation is straightforward and self-contained, requiring only knowledge
of vector calculus and matrix multiplication.

Subsequent articles assumes you, the reader, have a working understanding of
`tensor calculus <https://en.m.wikipedia.org/wiki/Tensor_calculus>`_, the
concept of vector/covector duality `differential forms
<https://en.m.wikipedia.org/wiki/Differential_form>`_, `musicality
<https://en.m.wikipedia.org/wiki/Musical_isomorphism>`_, `the exterior product
<https://en.m.wikipedia.org/wiki/Exterior_algebra>`_ and `hodge duality
<https://en.m.wikipedia.org/wiki/Hodge_star_operator>`_. I gather all these
*tools* into what I call the :ref:`The Cartan-Hodge Formalism`. There you will
find a personal overview of these concepts, which can be used as review
material, though certainly not as primary learning material. I also introduce
:ref:`the free matrix representation <The Free Matrix Representation>`, which I
hope the prospective reader will find obvious and usefull for performing actual
computations. For those looking to learn about differential forms, `I loved the
excellent video serie by Michael Penn
<https://youtube.com/playlist?list=PL22w63XsKjqzQZtDZO_9s2HEMRJnaOTX7&si=4dDrAZ-oKa1rI7B8>`_.

At the heart of this work lie three articles:

* :ref:`Rotations in Minkowski Space`.
* :ref:`The Exterior Derivative of Rotations in Spacetime`
* :ref:`Maxwell's Equations via Differential Forms`

In the first article, differential forms are presented as a simple yet
powerfull concept for representing rotations and generalizing them to
four-dimensional Minkowski spacetime. The connection to regular matrix
multiplication is explained, along with its relation to the Lie algebra of the
Lorentz Group :math:`\mathfrak{so}(1,3)`. The second article explores how to
perform a twist in spacetime, essentially applying a derivation operator to a
rotation. There, the exterior derivative of rotations in spacetime is
systematically analyzed. The final article links the exterior derivative of
rotations to Maxwell's equations by identification, revealing that we are
dealing with a twist in spacetime. This provides a comprehensive and coherent
demonstration of how Maxwell's equations emerge from the framework of
differential forms and electromagnetism is reduced to a single equation.

This serie was originally envisioned as a collection of short, standalone
articles. However, it has expanded beyond my initial expectation and evolved
into something more comprehensive.

.. topic:: Maxwell Equations in the Cartan-Hodge Formalism

   .. math::

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

   Where :math:`d` is the exterior derivative, :math:`⋆` the Hodge star, and
   :math:`∧` the exterior product. :math:`\E^x`, :math:`\E^y` and :math:`\E^z`
   are the components of the electric field divided by the speed of light
   :math:`c`, and :math:`B^x`, :math:`B^y`, :math:`B^z` the components of the
   magnetic field. The term on the right hand side is the four-current, with
   :math:`μ_0` the permeability of free space, :math:`ρ` the volume charge
   density, and :math:`J^x`, :math:`J^y`, :math:`J^z` the components of the
   conventional current density.

.. rubric:: :ref:`The Cartan-Hodge Formalism`

This section defines the mathematical objects used in this work. There is argued
the best notation to express basis vectors are partial derivatives :math:`∂_μ`.
This in turns permits to express basis covectors as differentials :math:`d^μ`.
Recalled is the use of the musical sharp :math:`♯` operator to transform
covectors to vectors, and flat :math:`♭` to transform vectors to covectors. The
concept of the Hodge dual is detailed. Finally, I introduce the concept of free
matrix representation, which I hope readers will find very obvious.

I encapsulate these concepts in what I name the Cartan-Hodge formalism. This
comprehensive framework facilitates the systematic analysis of rotation
representation in differential form and a thorough examination of differential
operators within this context.

.. rubric:: :ref:`Rotations in Differential Form`

This section is a systematic analyis of the representation of rotations in three
dimensions and in spacetime. Rotations are expressed as linear combinations of
basis rotations in each planes. The expressions as double covariant tensors,
double contravariant tensors, and mixed tensors are derived. Symmetries are
systematically analyzed. In this section, we get the first insight about the
deep connection between the electromagnetism and rotations in spacetime.

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   licence.rst
   contribute.rst
   resources.rst
   the_cartan_hodge_formalism/index.rst
   rotations/index.rst
   differential_operators/index.rst
   faraday_tensor/index.rst
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
