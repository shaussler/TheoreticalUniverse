.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _All Electromagnetic Field Tensors:

All Electromagnetic Field Tensors
=================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: Under construction

In this section, we derive all possible representations of the Faraday tensor
:math:`F` and its Hodge dual :math:`⋆\:F`, also noted :math:`G`. We take as a
starting  point the electromagnetic field 2-form. For reference, you can find
the derivation in the article :ref:`Maxwell's Equations via Differential Forms`:

.. math::

   F^{♭♭} = \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right] \\

All the expressions of the Faraday Tensor :math:`F` are the same object viewed
from a different perspective. All :math:`F` objects are strictly equivalent,
whether it is called a 2-form or a tensor, and a matter of convention.

:math:`F^{♭♭}`
--------------

The Faraday 2-form is here the starting point as given above. In a columns
representation, it is written as:

.. math::

   F^{♭♭} = \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right] \\

From the Faraday 2-form and noting that 2-forms *are* tensors, we can derive the
row/column representation of the doubly covariant Faraday tensor.

.. math::

   F^{♭♭} = \frac{1}{2} \begin{bmatrix}
                       & + \E^x \; dx ∧ dt & + \E^y \; dy ∧ dt & + \E^z \; dz ∧ dt \\
     - \E^x \; dt ∧ dx &                   & -  B^z \; dy ∧ dx & +  B^y \; dz ∧ dx \\
     - \E^y \; dt ∧ dy & +  B^z \; dx ∧ dy &                   & -  B^x \; dz ∧ dy \\
     - \E^z \; dt ∧ dz & -  B^y \; dx ∧ dz & +  B^x \; dy ∧ dz &                   \\
   \end{bmatrix}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Start from the Faraday 2-form

   .. math::

     F^{♭♭} = \left[ \begin{aligned}
       - & \E^x \; dt ∧ dx \\
       - & \E^y \; dt ∧ dy \\
       - & \E^z \; dt ∧ dz \\
         &  B^x \; dy ∧ dz \\
         &  B^y \; dz ∧ dx \\
         &  B^z \; dx ∧ dy \\
     \end{aligned} \right] \\

   .. rubric:: Duplicate each 2-form

   The following line is so obvious that the prospective reader may be confused.
   I am; indeed; really writing that :math:`A = \frac{1}{2} (A+A)`.

   .. math::

      F^{♭♭} = \frac{1}{2} \begin{bmatrix}
        - \E^x \; dt ∧ dx & - \E^x \; dt ∧ dx \\
        - \E^y \; dt ∧ dy & - \E^y \; dt ∧ dy \\
        - \E^z \; dt ∧ dz & - \E^z \; dt ∧ dz \\
        +  B^x \; dy ∧ dz & +  B^x \; dy ∧ dz \\
        +  B^y \; dz ∧ dx & +  B^y \; dz ∧ dx \\
        +  B^z \; dx ∧ dy & +  B^z \; dx ∧ dy \\
      \end{bmatrix}

   .. rubric:: Flip the exterior product

   The purpose of the above operation was to utilize the antisymmetry of the
   exterior product and flip the signs :math:`dx^μ ∧ dx^ν = -dx^ν ∧ dx^μ` as
   needed.

   .. math::

      F^{♭♭} = \frac{1}{2} \begin{bmatrix}
        - \E^x \; dt ∧ dx & + \E^x \; dx ∧ dt \\
        - \E^y \; dt ∧ dy & + \E^y \; dy ∧ dt \\
        - \E^z \; dt ∧ dz & + \E^z \; dz ∧ dt \\
        +  B^x \; dy ∧ dz & -  B^x \; dz ∧ dy \\
        +  B^y \; dz ∧ dx & -  B^y \; dx ∧ dz \\
        +  B^z \; dx ∧ dy & -  B^z \; dy ∧ dx \\
      \end{bmatrix}

   The purpose of this operation is to switch the representation of the Faraday
   2-Form as a single row of basis 2-Forms, to a row/column representation.

   .. rubric:: Reorder into rows/column representation

   From there, we conclude utilizing the free matrix representation of the
   Cartan-Hodge formalism, reordering the elements into rows and columns.

   .. math::

      F^{♭♭} = \frac{1}{2} \begin{bmatrix}
                          & + \E^x \; dx ∧ dt & + \E^y \; dy ∧ dt & + \E^z \; dz ∧ dt \\
        - \E^x \; dt ∧ dx &                   & -  B^z \; dy ∧ dx & +  B^y \; dz ∧ dx \\
        - \E^y \; dt ∧ dy & +  B^z \; dx ∧ dy &                   & -  B^x \; dz ∧ dy \\
        - \E^z \; dt ∧ dz & -  B^y \; dx ∧ dz & +  B^x \; dy ∧ dz &                   \\
      \end{bmatrix}

   .. }}}

With implicit bivector basis, we have the `standard representation with abstract
index notation <https://en.m.wikipedia.org/wiki/Electromagnetic_tensor>`_

.. math::

   F_{μν} = \begin{bmatrix}
            & + \E^x & + \E^y & + \E^z \\
     - \E^x &        & -  B^z & +  B^y \\
     - \E^y & +  B^z &        & -  B^x \\
     - \E^z & -  B^y & +  B^x &        \\
   \end{bmatrix}

Where the field 2-form is related to the Faraday tensor with:

.. math::

   F^{♭♭} = \frac{1}{2} \: F_{μν} \: dx^μ ∧ dx^ν

For sanity, I refer to Wikipedia for a quick double check of `the link between
the Faraday 2-Form and the Faraday tensor
<https://en.m.wikipedia.org/wiki/Mathematical_descriptions_of_the_electromagnetic_field#Field_2-form>`_.

:math:`F^{♯♯}`
--------------

:math:`F^{♭♯}`
--------------

:math:`F^{♯♭}`
--------------

:math:`G^{♭♭}`
--------------

.. {{{

The Hodge dual :math:`G^{♭♭}` of the Faraday 2-form :math:`F^{♭♭}` is:

.. math:: G^{♭♭} = ⋆ F^{♭♭}

Expanded, we obtain:

.. math::

  G^{♭♭} = \left[ \begin{alignedat}{1}
     B^x \; & dt ∧ dx \\
     B^y \; & dt ∧ dy \\
     B^z \; & dt ∧ dz \\
    \E^x \; & dy ∧ dz \\
    \E^y \; & dz ∧ dx \\
    \E^z \; & dx ∧ dy \\
  \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Start from the Faraday 2-form

   .. math::

     F^{♭♭} = \left[ \begin{aligned}
       - & \E^x \; dt ∧ dx \\
       - & \E^y \; dt ∧ dy \\
       - & \E^z \; dt ∧ dz \\
         &  B^x \; dy ∧ dz \\
         &  B^y \; dz ∧ dx \\
         &  B^z \; dx ∧ dy \\
     \end{aligned} \right]

   .. rubric:: Take the Hodge dual

   .. math::

     G^{♭♭} = ⋆ F^{♭♭} = ⋆ \left[ \begin{aligned}
       - & \E^x \; dt ∧ dx \\
       - & \E^y \; dt ∧ dy \\
       - & \E^z \; dt ∧ dz \\
         &  B^x \; dy ∧ dz \\
         &  B^y \; dz ∧ dx \\
         &  B^z \; dx ∧ dy \\
     \end{aligned} \right]

   .. rubric:: Distribute the Hodge dual operator

   .. math::

     G^{♭♭} = \left[ \begin{aligned}
       - & \E^x \; ⋆ dt ∧ dx \\
       - & \E^y \; ⋆ dt ∧ dy \\
       - & \E^z \; ⋆ dt ∧ dz \\
         &  B^x \; ⋆ dy ∧ dz \\
         &  B^y \; ⋆ dz ∧ dx \\
         &  B^z \; ⋆ dx ∧ dy \\
     \end{aligned} \right]

   .. rubric:: Apply the Hodge dual operator

   You can find the Hodge dual of each bivector basis in Minkowski space
   :ref:`here <Duality in Minkowski Space>`.

   .. math::

     G^{♭♭} = \left[ \begin{alignedat}{1}
       - & \E^x \; (-1) & dy ∧ dz \\
       - & \E^y \; (-1) & dz ∧ dx \\
       - & \E^z \; (-1) & dx ∧ dy \\
         &  B^x \; (+1) & dt ∧ dx \\
         &  B^y \; (+1) & dt ∧ dy \\
         &  B^z \; (+1) & dt ∧ dz \\
     \end{alignedat} \right]

   .. rubric:: Simplify

   .. math::

     G^{♭♭} = \left[ \begin{alignedat}{1}
       \E^x \; & dy ∧ dz \\
       \E^y \; & dz ∧ dx \\
       \E^z \; & dx ∧ dy \\
        B^x \; & dt ∧ dx \\
        B^y \; & dt ∧ dy \\
        B^z \; & dt ∧ dz \\
     \end{alignedat} \right]

   .. rubric:: Reorder

   .. math::

     G^{♭♭} = \left[ \begin{alignedat}{1}
        B^x \; & dt ∧ dx \\
        B^y \; & dt ∧ dy \\
        B^z \; & dt ∧ dz \\
       \E^x \; & dy ∧ dz \\
       \E^y \; & dz ∧ dx \\
       \E^z \; & dx ∧ dy \\
     \end{alignedat} \right]

   .. }}}

From the dual Faraday 2-form and noting that 2-forms are tensors, we can derive
the row/column representation of the doubly covariant dual Faraday tensor.

.. math::

  G^{♭♭} = \begin{bmatrix}
                   & -  B^x \; dx ∧ dt & -  B^y \; dy ∧ dt & -  B^z \; dz ∧ dt \\
    B^x \; dt ∧ dx &                   & - \E^z \; dy ∧ dx & + \E^y \; dz ∧ dx \\
    B^y \; dt ∧ dy & + \E^z \; dx ∧ dy &                   & - \E^x \; dz ∧ dy \\
    B^z \; dt ∧ dz & - \E^y \; dx ∧ dz & + \E^x \; dy ∧ dz &                   \\
  \end{bmatrix}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Begin with the Hodge dual in column form

   .. math::

     G^{♭♭} = \begin{bmatrix}
        B^x \; dt ∧ dx \\
        B^y \; dt ∧ dy \\
        B^z \; dt ∧ dz \\
       \E^x \; dy ∧ dz \\
       \E^y \; dz ∧ dx \\
       \E^z \; dx ∧ dy \\
     \end{bmatrix}

   .. rubric:: Duplicate each 2-form

   The following line is so obvious that the prospective reader may be confused.
   I am; indeed; really writing that :math:`A = \frac{1}{2} (A+A)`.

   .. math::

     G^{♭♭} = \begin{bmatrix}
        B^x \; dt ∧ dx & +  B^x \; dt ∧ dx \\
        B^y \; dt ∧ dy & +  B^y \; dt ∧ dy \\
        B^z \; dt ∧ dz & +  B^z \; dt ∧ dz \\
       \E^x \; dy ∧ dz & + \E^x \; dy ∧ dz \\
       \E^y \; dz ∧ dx & + \E^y \; dz ∧ dx \\
       \E^z \; dx ∧ dy & + \E^z \; dx ∧ dy \\
     \end{bmatrix}

   .. rubric:: Flip the exterior product

   The purpose of the above operation was to utilize the antisymmetry of the
   exterior product and flip the signs :math:`dx^μ ∧ dx^ν = -dx^ν ∧ dx^μ` as
   needed.

   .. math::

     G^{♭♭} = \begin{bmatrix}
        B^x \; dt ∧ dx & -  B^x \; dx ∧ dt \\
        B^y \; dt ∧ dy & -  B^y \; dy ∧ dt \\
        B^z \; dt ∧ dz & -  B^z \; dz ∧ dt \\
       \E^x \; dy ∧ dz & - \E^x \; dz ∧ dy \\
       \E^y \; dz ∧ dx & - \E^y \; dx ∧ dz \\
       \E^z \; dx ∧ dy & - \E^z \; dy ∧ dx \\
     \end{bmatrix}

   The purpose of this operation is to switch the representation of the dual
   Faraday 2-Form as a single row of basis 2-Forms, to a row/column
   representation.

   .. rubric:: Reorder into rows/column representation

   From there, we conclude utilizing the free matrix representation of the
   Cartan-Hodge formalism, reordering the elements into rows and columns.

   .. math::

     G^{♭♭} = \begin{bmatrix}
                      & -  B^x \; dx ∧ dt & -  B^y \; dy ∧ dt & -  B^z \; dz ∧ dt \\
       B^x \; dt ∧ dx &                   & - \E^z \; dy ∧ dx & + \E^y \; dz ∧ dx \\
       B^y \; dt ∧ dy & + \E^z \; dx ∧ dy &                   & - \E^x \; dz ∧ dy \\
       B^z \; dt ∧ dz & - \E^y \; dx ∧ dz & + \E^x \; dy ∧ dz &                   \\
     \end{bmatrix}

   .. }}}

.. }}}


:math:`G^{♯♯}`
--------------

:math:`G^{♭♯}`
--------------

:math:`G^{♯♭}`
--------------
