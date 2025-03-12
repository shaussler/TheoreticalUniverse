.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _calculating the hodge dual:

Calculating the Hodge dual
==========================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: Draft

In this page, I present a straightforward algorithmic way to calculate the
inner product between k--vectors (respectively k--forms). The dicussion in the
article :ref:`Hodge duality` for k--vectors provides geometric intuition. Here,
I offer an alternative to compute the inner product of k--forms, as well as the
Hodge dual of k--forms in a trivial algorithmic manner using the interior
product :math:`⌟`. My use of the interior product :math:`⌟` my be non-standard.
I have not investigated whether the procedure described below is known or
established. It certainly works as I intuitively expect it should. You may then
just consider it a usefull trick to efficiently determine the inner product
between k--forms, or the Hodge dual of k-forms.

Inner product on k--froms
-------------------------

To establish a common foundation, recall that the inner product of k--vectors
is equal to that of k--forms. For basis vectors and covectors, the inner
product is the metric. In flat spacetime, this yields the Minkowski metric :math:`η`:

.. math::

   ∂_μ · ∂_ν = dx^μ · dx^ν = η^{μν} = η_{μν}

Considering basis vectors, dual covectors are defined as:

.. math::

   dx^μ \left( ∂_ν \right) = δ^μ_ν

In this sense, 1--forms *measure* vectors, and the measure of a basis vector
:math:`∂_ν` through it corresponding basis covector :math:`dx^μ` is one. The
inner product, denoted with :math:`·` or :math:`\braket{|}`, measures the                                                                             shadow of one vector onto another.

The standard interior product is an operation between a vector and a form. It
consist of rearanging the form to bring the corresponding covector to the
front, and applying the vector to that front slot. This operation transforms a
k--form to a (k-1)--form. For example:

.. math::

   \newcommand{\⌟}{\:⌟\:}
   ∂_y \⌟ dx ∧ dy ∧ dz = ∂_y \⌟ (- dy ∧ dx ∧ dz) = - dy \left( ∂_y \right) ∧ dx ∧ dz = - dx ∧ dz

Here, we have applied the basis vector :math:`∂_ν` to the basis form
:math:`dx^μ`.

We equate the interior product to the dot product for a vector pair to the
interior product :math:`⌟`:

.. math::

   \newcommand{\⌟}{\:⌟\:}
   ∂_ν \⌟ ∂_μ  = ∂_μ  · ∂_ν  = η_{μν}

For covectors:

.. math::

   \newcommand{\⌟}{\:⌟\:}
   dx^ν \⌟ dx^μ = dx^μ · dx^ν = η^{μν} \\

The interior product of a vector can be applied to a general k--vector. For a
basis vector acting on a basis 2--vector, we bring the corresponding basis
1--vector to the front and apply the vector to the first slot:

.. math::

   \newcommand{\⌟}{\:⌟\:}
   dt \⌟ dx ∧ dt &= dt \⌟ \left( - dt ∧ dx \right) \\
                 &= - ( dt · dt ) \; dx \\
                 &= - dx

Simmilarly, the interior product of a basis vector can be taken with a
3--vector or a 4--vector. This provides a straightforward algorithmic approach                                                                        to calculate the inner product with no thinking involved:

.. math::

   \newcommand{\⌟}{\:⌟\:}
   (dt ∧ dx) · (dt ∧ dx) &= dx \⌟ dt \⌟ dt ∧ dx \\
                         &= dx \⌟ (dt · dt) ∧ dx \\
                         &= dx \⌟ dx \\
                         &= dx · dx \\
                         &= -1

Hodge dual of k--forms
----------------------

In the article :ref:`Hodge duality`, the inclusion of the inner product to
determine the Hodge dual of k--forms is explained. Here I present how to
directly determine the Hodge dual. The Hodge dual can be determined directly by
taking the interior product :math:`⌟` with the pseudo-scalar. In Minkowski
space, the pseudo-scalar is :math:`dt ∧ dx ∧ dy ∧ dz`.

For example, the Hodge dual of :math:`dx ∧ dy` is:

.. math::

   \newcommand{\⌟}{\:⌟\:}
   ⋆ dx ∧ dy & = (dx ∧ dy) \⌟ dt ∧ dx ∧ dy ∧ dz \\
             & = dy \⌟ dx \⌟ (- dx ∧ dt ∧ dy ∧ dz) \\
             & = dy \⌟ dx \⌟ (+ dx ∧ dy ∧ dt ∧ dz) \\
             & = dy \⌟ (dx · dx) \: dy ∧ dt ∧ dz \\
             & = - dy \⌟ dy ∧ dt ∧ dz \\
             & = - (dy · dy) \: dt ∧ dz \\
             & = dt ∧ dz \\

Euclidean space
---------------

Inner product
'''''''''''''

Hodge duals
'''''''''''

Minkowski space
---------------

Inner product
'''''''''''''

We can systematicall apply the procedure to obtain the same result as above:

.. rubric:: 1--forms

.. math::

   \newcommand{\⌟}{\:⌟\:}
   \begin{alignedat}{5}
       dt · dt &=& dt &\⌟& dt & = +1 \\
       dx · dt &=& dx &\⌟& dx & = -1 \\
       dy · dt &=& dy &\⌟& dy & = -1 \\
       dz · dt &=& dz &\⌟& dz & = -1 \\
   \end{alignedat}

.. rubric:: 2--forms

.. math::

   \newcommand{\⌟}{\:⌟\:}
   \newcommand{\·}{\:·\:}
   \begin{alignedat}{5}
       (& dt ∧ dx &) \· (& dt ∧ dx &) =& dx &\⌟& dt &\⌟& dt ∧ dx &= + dx &\⌟& dx &= -1 \\
       (& dt ∧ dy &) \· (& dt ∧ dy &) =& dy &\⌟& dt &\⌟& dt ∧ dy &= + dy &\⌟& dy &= -1 \\
       (& dt ∧ dy &) \· (& dt ∧ dz &) =& dz &\⌟& dt &\⌟& dt ∧ dz &= + dz &\⌟& dz &= -1 \\
       (& dy ∧ dz &) \· (& dy ∧ dz &) =& dz &\⌟& dy &\⌟& dy ∧ dz &= - dz &\⌟& dz &= +1 \\
       (& dz ∧ dx &) \· (& dz ∧ dx &) =& dx &\⌟& dz &\⌟& dz ∧ dx &= - dx &\⌟& dx &= +1 \\                                                                    (& dx ∧ dy &) \· (& dx ∧ dy &) =& dy &\⌟& dx &\⌟& dx ∧ dy &= - dy &\⌟& dy &= +1 \\
   \end{alignedat}

.. rubric:: 3--forms

.. math::

   \newcommand{\⌟}{\:⌟\:}
   \newcommand{\·}{\:·\:}
   \small
   \begin{alignedat}{5}
       (& dx ∧ dy ∧ dz &) \· (& dx ∧ dy ∧ dz &) =& dz \⌟ dy \⌟ dx \⌟ dx ∧ dy ∧ dz &=& - dz \⌟ dy \⌟ dy ∧ dz &= + dz \⌟ d = -1 \\
       (& dt ∧ dy ∧ dz &) \· (& dt ∧ dy ∧ dz &) =& dz \⌟ dy \⌟ dt \⌟ dt ∧ dy ∧ dz &=& + dz \⌟ dy \⌟ dy ∧ dz &= - dz \⌟ d = +1 \\
       (& dt ∧ dz ∧ dx &) \· (& dt ∧ dz ∧ dx &) =& dx \⌟ dz \⌟ dt \⌟ dt ∧ dz ∧ dx &=& + dx \⌟ dz \⌟ dz ∧ dx &= - dx \⌟ d = +1 \\                             (& dt ∧ dx ∧ dy &) \· (& dt ∧ dx ∧ dy &) =& dy \⌟ dx \⌟ dt \⌟ dt ∧ dx ∧ dy &=& + dy \⌟ dx \⌟ dx ∧ dy &= - dy \⌟ d = +1 \\
   \end{alignedat}

.. rubric:: 4--forms

.. math::

   \newcommand{\⌟}{\:⌟\:}
   \newcommand{\·}{\:·\:}
   (dt ∧ dx ∧ dy ∧ dz) \· (dt ∧ dx ∧ dy ∧ dz) &= dz \⌟ dy \⌟ dx \⌟ dt \⌟ dt ∧ dx ∧ dy ∧ dz \\
                                             &= dz \⌟ dy \⌟ dx \⌟ dx ∧ dy ∧ dz \\
                                             &= -1 dz \⌟ dy \⌟ ∧ dy ∧ dz \\
                                             &= +1 dz \⌟ ∧ dz \\
                                             &= -1

Hodge duals
'''''''''''

.. rubric:: 1-forms

.. math::

   ⋆& dt &= dx ∧ dy ∧ dz \\
   ⋆& dx &= dt ∧ dy ∧ dz \\
   ⋆& dy &= dt ∧ dz ∧ dx \\
   ⋆& dz &= dt ∧ dx ∧ dy \\

.. admonition:: Calculations
   :class: dropdown, toggle-shown

   .. rubric:: Take the inner product with the pseudoscalar

   .. math::

      \newcommand{\⌟}{\:⌟\:}
      ⋆& dt &= dt &\⌟ dt ∧ dx ∧ dy ∧ dz \\
      ⋆& dx &= dx &\⌟ dt ∧ dx ∧ dy ∧ dz \\
      ⋆& dy &= dy &\⌟ dt ∧ dx ∧ dy ∧ dz \\
      ⋆& dz &= dz &\⌟ dt ∧ dx ∧ dy ∧ dz \\

   .. rubric:: Reorder

   .. math::

      \newcommand{\⌟}{\:⌟\:}
      ⋆& dt &= + dt &\⌟ dt ∧ dx ∧ dy ∧ dz \\
      ⋆& dx &= - dx &\⌟ dx ∧ dt ∧ dy ∧ dz \\
      ⋆& dy &= - dy &\⌟ dy ∧ dt ∧ dz ∧ dx \\
      ⋆& dz &= - dz &\⌟ dz ∧ dt ∧ dx ∧ dy \\

   .. rubric:: Apply the interior product

   .. math::

      \newcommand{\.}{\:.\:}
      ⋆& dt &= + (& dt &\·& dt &) \: & dx ∧ dy ∧ dz \\
      ⋆& dx &= - (& dx &\·& dx &) \: & dt ∧ dy ∧ dz \\
      ⋆& dy &= - (& dy &\·& dy &) \: & dt ∧ dz ∧ dx \\
      ⋆& dz &= - (& dz &\·& dz &) \: & dt ∧ dx ∧ dy \\

   .. rubric:: Apply numerical values and conclude

   .. math::

      ⋆& dt &= dx ∧ dy ∧ dz \\
      ⋆& dx &= dt ∧ dy ∧ dz \\
      ⋆& dy &= dt ∧ dz ∧ dx \\
      ⋆& dz &= dt ∧ dx ∧ dy \\

.. rubric:: 2-forms

.. math::

   \begin{alignedat}{2}
   ⋆ dt ∧ dx &= \\
   ⋆ dt ∧ dy &= \\
   ⋆ dt ∧ dz &= \\
   ⋆ dy ∧ dz &= \\
   ⋆ dz ∧ dx &= \\
   ⋆ dx ∧ dy &= \\
   \end{alignedat}

.. rubric:: 3-forms

.. math::

   ⋆ dx ∧ dy ∧ dz &=  \\
   ⋆ dt ∧ dy ∧ dz &=  \\
   ⋆ dt ∧ dz ∧ dx &=  \\
   ⋆ dt ∧ dx ∧ dy &=  \\

.. rubric:: 4-forms

.. math::

   ⋆ dt ∧ dx ∧ dy ∧ dz =

.. }}}
