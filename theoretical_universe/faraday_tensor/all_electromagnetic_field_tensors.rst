.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _All Electromagnetic Field Tensors:

All Electromagnetic Field Tensors
=================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. {{{

In this section, I systematically derive all representations of the Faraday
tensor :math:`F` and its Hodge dual with metric signature :math:`(+,-,-,-)`. I
cannot imagine there is no sign error in the calculations below. The Hodge dual
:math:`⋆\:F` is also noted :math:`G`. We take as a starting  point the
electromagnetic field 2-form derivated in the article :ref:`Maxwell's Equations
via Differential Forms`:

.. math::

   F^{♭♭} = \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right]

All the expressions of the Faraday Tensor :math:`F` are the same object viewed
from a different perspective. All :math:`F` objects are strictly equivalent,
whether it is called a 2-form or a tensor, and a matter of convention.

.. }}}

:math:`F^{♭♭}`
--------------

.. {{{

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

.. }}}

:math:`F^{♭♯}`
--------------

.. {{{

The starting point is the twice flattened Faraday tensor :math:`F^{♭♭}` to
which we apply the ♭♯ operator :math:`F^{♭♯}=\left(F^{♭♭}\right)^{♭♯}` and
obtain:

.. math::

   F^{♭♯} = \left[ \begin{aligned}
       & \E^x \; dt ∧ ∂_x \\
       & \E^y \; dt ∧ ∂_y \\
       & \E^z \; dt ∧ ∂_z \\
     - &  B^x \; dy ∧ ∂_z \\
     - &  B^y \; dz ∧ ∂_x \\
     - &  B^z \; dx ∧ ∂_y \\
   \end{aligned} \right]

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

   .. rubric:: Distribute the flat ♭ and sharp ♯ operators

   .. math::

      F^{♭♯} = \left(F^{♭♭}\right)^{♭♯} = \left[ \begin{aligned}
        - & \E^x \; dt ∧ dx \\
        - & \E^y \; dt ∧ dy \\
        - & \E^z \; dt ∧ dz \\
          &  B^x \; dy ∧ dz \\
          &  B^y \; dz ∧ dx \\
          &  B^z \; dx ∧ dy \\
      \end{aligned} \right]^{♭♯}
      = \left[ \begin{aligned}
        - & \E^x \; dt^♭ ∧ dx^♯ \\
        - & \E^y \; dt^♭ ∧ dy^♯ \\
        - & \E^z \; dt^♭ ∧ dz^♯ \\
          &  B^x \; dy^♭ ∧ dz^♯ \\
          &  B^y \; dz^♭ ∧ dx^♯ \\
          &  B^z \; dx^♭ ∧ dy^♯ \\
      \end{aligned} \right]

   .. rubric:: Expand the sharpened basis covectors

   The :math:`dx^μ` terms are already flattened, and applying the flattening
   operator twice does not modify these terms: :math:`(dx^μ)^♭=dx^μ`. The sharpened terms
   are expanded with the metric: :math:`(dx^ν)^♯ = η_{νμ} ∂_μ`.

   .. math::

      F^{♭♯} = \left[ \begin{aligned}
        - & \E^x \; dt ∧ η^{xμ} ∂_μ \\
        - & \E^y \; dt ∧ η^{yμ} ∂_μ \\
        - & \E^z \; dt ∧ η^{zμ} ∂_μ \\
          &  B^x \; dy ∧ η^{zμ} ∂_μ \\
          &  B^y \; dz ∧ η^{xμ} ∂_μ \\
          &  B^z \; dx ∧ η^{yμ} ∂_μ \\
      \end{aligned} \right]

   .. rubric:: Identify the non-zero terms

   .. math::

      F^{♭♯} = \left[ \begin{aligned}
        - & \E^x \; dt ∧ η^{xx} ∂_x \\
        - & \E^y \; dt ∧ η^{yy} ∂_y \\
        - & \E^z \; dt ∧ η^{zz} ∂_z \\
          &  B^x \; dy ∧ η^{zz} ∂_z \\
          &  B^y \; dz ∧ η^{xx} ∂_x \\
          &  B^z \; dx ∧ η^{yy} ∂_y \\
      \end{aligned} \right]

   .. rubric:: Apply numerical values

   .. math::

      F^{♭♯} = \left[ \begin{aligned}
        - & \E^x \; dt ∧ (-1) ∂_x \\
        - & \E^y \; dt ∧ (-1) ∂_y \\
        - & \E^z \; dt ∧ (-1) ∂_z \\
          &  B^x \; dy ∧ (-1) ∂_z \\
          &  B^y \; dz ∧ (-1) ∂_x \\
          &  B^z \; dx ∧ (-1) ∂_y \\
      \end{aligned} \right] = \left[ \begin{aligned}
          & \E^x \; dt ∧ ∂_x \\
          & \E^y \; dt ∧ ∂_y \\
          & \E^z \; dt ∧ ∂_z \\
        - &  B^x \; dy ∧ ∂_z \\
        - &  B^y \; dz ∧ ∂_x \\
        - &  B^z \; dx ∧ ∂_y \\
      \end{aligned} \right]

   .. }}}

We derive the row/column representation of the :math:`F^{♭♯}` Faraday tensor:

.. math::

   F^{♭♯} = \frac{1}{2} \left[ \begin{aligned}
                          & + \E^x \; dt ∧ ∂_x & + \E^y \; dt ∧ ∂_y & + \E^z \; dt ∧ ∂_z \\
       + \E^x \; dx ∧ ∂_t &                    & -  B^z \; dx ∧ ∂_y & +  B^y \; dx ∧ ∂_z \\
       + \E^y \; dy ∧ ∂_t & +  B^z \; dy ∧ ∂_x &                    & -  B^x \; dy ∧ ∂_z \\
       + \E^z \; dz ∧ ∂_t & -  B^y \; dz ∧ ∂_x & +  B^x \; dz ∧ ∂_y &                    \\
   \end{aligned} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   In this version of the calculation, we expand to matrix form using the
   :ref:`symmetries of the mixed exterior product in Minkowski
   <symmetries_of_the_flat_sharp_mixed_exterior_product>`:

   ============ =============================
   Symmetry     Basis elements
   ============ =============================
   Symetric     :math:`dt ∧ ∂_x = + dx ∧ ∂_t`
   Symetric     :math:`dt ∧ ∂_y = + dy ∧ ∂_t`
   Symetric     :math:`dt ∧ ∂_z = + dz ∧ ∂_t`
   Antisymetric :math:`dy ∧ ∂_z = - dz ∧ ∂_y`
   Antisymetric :math:`dz ∧ ∂_x = - dx ∧ ∂_z`
   Antisymetric :math:`dx ∧ ∂_y = - dy ∧ ∂_x`
   ============ =============================

   .. rubric:: Expand using symmetries

   .. math::

      F^{♭♯} = \left[ \begin{aligned}
            & \E^x \; dt ∧ ∂_x \\
            & \E^y \; dt ∧ ∂_y \\
            & \E^z \; dt ∧ ∂_z \\
          - &  B^x \; dy ∧ ∂_z \\
          - &  B^y \; dz ∧ ∂_x \\
          - &  B^z \; dx ∧ ∂_y \\
      \end{aligned} \right] = \left[ \begin{aligned}
            & \E^x \; \frac{1}{2} \left( dt ∧ ∂_x + dx ∧ ∂_t \right) \\
            & \E^y \; \frac{1}{2} \left( dt ∧ ∂_y + dy ∧ ∂_t \right) \\
            & \E^z \; \frac{1}{2} \left( dt ∧ ∂_z + dz ∧ ∂_t \right) \\
          - &  B^x \; \frac{1}{2} \left( dy ∧ ∂_z - dz ∧ ∂_y \right) \\
          - &  B^y \; \frac{1}{2} \left( dz ∧ ∂_x - dx ∧ ∂_z \right) \\
          - &  B^z \; \frac{1}{2} \left( dx ∧ ∂_y - dy ∧ ∂_x \right) \\
      \end{aligned} \right]

   .. rubric:: Reorder

   .. math::

      F^{♭♯} = \frac{1}{2} \left[ \begin{aligned}
          + \E^x \; dt ∧ ∂_x + \E^x \; dx ∧ ∂_t \\
          + \E^y \; dt ∧ ∂_y + \E^y \; dy ∧ ∂_t \\
          + \E^z \; dt ∧ ∂_z + \E^z \; dz ∧ ∂_t \\
          -  B^x \; dy ∧ ∂_z +  B^x \; dz ∧ ∂_y \\
          -  B^y \; dz ∧ ∂_x +  B^y \; dx ∧ ∂_z \\
          -  B^z \; dx ∧ ∂_y +  B^z \; dy ∧ ∂_x \\
      \end{aligned} \right]

   .. rubric:: Reorder in row/column convention

   .. math::

      F^{♭♯} = \frac{1}{2} \left[ \begin{aligned}
                             & + \E^x \; dt ∧ ∂_x & + \E^y \; dt ∧ ∂_y & + \E^z \; dt ∧ ∂_z \\
          + \E^x \; dx ∧ ∂_t &                    & -  B^z \; dx ∧ ∂_y & +  B^y \; dx ∧ ∂_z \\
          + \E^y \; dy ∧ ∂_t & +  B^z \; dy ∧ ∂_x &                    & -  B^x \; dy ∧ ∂_z \\
          + \E^z \; dz ∧ ∂_t & -  B^y \; dz ∧ ∂_x & +  B^x \; dz ∧ ∂_y &                    \\
      \end{aligned} \right]

   .. }}}

With implicit bivector basis, we have :

.. math::

   F_μ{}^ν = \begin{bmatrix}
              & + \E^x & + \E^y & + \E^z \\
       + \E^x &        & -  B^z & +  B^y \\
       + \E^y & +  B^z &        & -  B^x \\
       + \E^z & -  B^y & +  B^x &        \\
   \end{bmatrix}

Where the mixed electromagnetic field is related to the covariant-contravariant
Faraday tensor through:

.. math::

   F^{♭♯} = \frac{1}{2} \: F_μ{}^ν \: dx^μ ∧ ∂_ν

.. }}}

:math:`F^{♯♯}`
--------------

The starting point is the twice flattened Faraday tensor :math:`F^{♭♭}` to
which we apply the ♭♯ operator :math:`F^{♭♯}=\left(F^{♭♭}\right)^{♭♯}` and
obtain:

.. math::

   F^{♯♯} = \left[ \begin{aligned}
       \E^x \; ∂_t ∧ ∂_x \\
       \E^y \; ∂_t ∧ ∂_y \\
       \E^z \; ∂_t ∧ ∂_z \\
        B^x \; ∂_y ∧ ∂_z \\
        B^y \; ∂_z ∧ ∂_x \\
        B^z \; ∂_x ∧ ∂_y \\
   \end{aligned} \right]

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

   .. rubric:: Apply the musical sharp-sharp ♯♯ operator

   .. math::

      F^{♯♯} = \left(F^{♭♭} \right)^{♯♯}
      = \left[ \begin{aligned}
          - & \E^x \; dt ∧ dx \\
          - & \E^y \; dt ∧ dy \\
          - & \E^z \; dt ∧ dz \\
            &  B^x \; dy ∧ dz \\
            &  B^y \; dz ∧ dx \\
            &  B^z \; dx ∧ dy \\
      \end{aligned} \right]^{♯♯}

   .. rubric:: Distribute the musical operators

   .. math::

      F^{♯♯} = \left[ \begin{aligned}
          - & \E^x \; (dt ∧ dx)^{♯♯} \\
          - & \E^y \; (dt ∧ dy)^{♯♯} \\
          - & \E^z \; (dt ∧ dz)^{♯♯} \\
            &  B^x \; (dy ∧ dz)^{♯♯} \\
            &  B^y \; (dz ∧ dx)^{♯♯} \\
            &  B^z \; (dx ∧ dy)^{♯♯} \\
      \end{aligned} \right]

   .. rubric:: Distribute the musical operators

   .. math::

      F^{♯♯} = \left[ \begin{aligned}
          - & \E^x \; dt^♯ ∧ dx^♯ \\
          - & \E^y \; dt^♯ ∧ dy^♯ \\
          - & \E^z \; dt^♯ ∧ dz^♯ \\
            &  B^x \; dy^♯ ∧ dz^♯ \\
            &  B^y \; dz^♯ ∧ dx^♯ \\
            &  B^z \; dx^♯ ∧ dy^♯ \\
      \end{aligned} \right]

   .. rubric:: Apply

   .. math::

      F^{♯♯} = \left[ \begin{aligned}
          - & \E^x \; η^{tμ} ∂_μ ∧ η^{xμ} ∂_μ \\
          - & \E^y \; η^{tμ} ∂_μ ∧ η^{yμ} ∂_μ \\
          - & \E^z \; η^{tμ} ∂_μ ∧ η^{zμ} ∂_μ \\
            &  B^x \; η^{yμ} ∂_μ ∧ η^{zμ} ∂_μ \\
            &  B^y \; η^{zμ} ∂_μ ∧ η^{xμ} ∂_μ \\
            &  B^z \; η^{xμ} ∂_μ ∧ η^{yμ} ∂_μ \\
      \end{aligned} \right]

   .. rubric:: Identify non-zero terms

   .. math::

      F^{♯♯} = \left[ \begin{aligned}
          - & \E^x \; η^{tt} ∂_t ∧ η^{xx} ∂_x \\
          - & \E^y \; η^{tt} ∂_t ∧ η^{yy} ∂_y \\
          - & \E^z \; η^{tt} ∂_t ∧ η^{zz} ∂_z \\
            &  B^x \; η^{yy} ∂_y ∧ η^{zz} ∂_z \\
            &  B^y \; η^{zz} ∂_z ∧ η^{xx} ∂_x \\
            &  B^z \; η^{xx} ∂_x ∧ η^{yy} ∂_y \\
      \end{aligned} \right]

   .. rubric:: Apply numerical values

   .. math::

      F^{♯♯} = \left[ \begin{aligned}
          - & \E^x \; (+1) ∂_t ∧ (-1) ∂_x \\
          - & \E^y \; (+1) ∂_t ∧ (-1) ∂_y \\
          - & \E^z \; (+1) ∂_t ∧ (-1) ∂_z \\
            &  B^x \; (-1) ∂_y ∧ (-1) ∂_z \\
            &  B^y \; (-1) ∂_z ∧ (-1) ∂_x \\
            &  B^z \; (-1) ∂_x ∧ (-1) ∂_y \\
      \end{aligned} \right]

   .. rubric:: Conclude

   .. math::

      F^{♯♯} = \left[ \begin{aligned}
          \E^x \; ∂_t ∧ ∂_x \\
          \E^y \; ∂_t ∧ ∂_y \\
          \E^z \; ∂_t ∧ ∂_z \\
           B^x \; ∂_y ∧ ∂_z \\
           B^y \; ∂_z ∧ ∂_x \\
           B^z \; ∂_x ∧ ∂_y \\
      \end{aligned} \right]

   .. }}}

We derive the row/column representation of the :math:`F^{♭♯}` Faraday tensor:

.. math::

   F^{♯♯} = \frac{1}{2} \begin{bmatrix}
                         & - \E^x \; ∂_x ∧ ∂_t & - \E^y \; ∂_y ∧ ∂_t & - \E^z \; ∂_z ∧ ∂_t \\
       \E^x \; ∂_t ∧ ∂_x &                     & -  B^z \; ∂_y ∧ ∂_x & +  B^y \; ∂_z ∧ ∂_x \\
       \E^y \; ∂_t ∧ ∂_y & + B^z \; ∂_x ∧ ∂_y  &                     & -  B^x \; ∂_z ∧ ∂_y \\
       \E^z \; ∂_t ∧ ∂_z & -  B^y \; ∂_x ∧ ∂_z & +  B^x \; ∂_y ∧ ∂_z &                     \\
   \end{bmatrix}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Start from

   .. math::

      F^{♯♯} = \left[ \begin{aligned}
          \E^x \; ∂_t ∧ ∂_x \\
          \E^y \; ∂_t ∧ ∂_y \\
          \E^z \; ∂_t ∧ ∂_z \\
           B^x \; ∂_y ∧ ∂_z \\
           B^y \; ∂_z ∧ ∂_x \\
           B^z \; ∂_x ∧ ∂_y \\
      \end{aligned} \right]

   .. rubric:: Apply the symmetries of the exterior product

   .. math::

      F^{♯♯} = \left[ \begin{aligned}
          \E^x \; \frac{1}{2} & (∂_t ∧ ∂_x - ∂_x ∧ ∂_t) \\
          \E^y \; \frac{1}{2} & (∂_t ∧ ∂_y - ∂_y ∧ ∂_t) \\
          \E^z \; \frac{1}{2} & (∂_t ∧ ∂_z - ∂_z ∧ ∂_t) \\
           B^x \; \frac{1}{2} & (∂_y ∧ ∂_z - ∂_z ∧ ∂_y) \\
           B^y \; \frac{1}{2} & (∂_z ∧ ∂_x - ∂_x ∧ ∂_z) \\
           B^z \; \frac{1}{2} & (∂_x ∧ ∂_y - ∂_y ∧ ∂_x) \\
      \end{aligned} \right]

   .. rubric:: Reorder

   .. math::

      F^{♯♯} = \frac{1}{2} \left[ \begin{aligned}
          \E^x \; ∂_t ∧ ∂_x & - \E^x \; ∂_x ∧ ∂_t \\
          \E^y \; ∂_t ∧ ∂_y & - \E^y \; ∂_y ∧ ∂_t \\
          \E^z \; ∂_t ∧ ∂_z & - \E^z \; ∂_z ∧ ∂_t \\
           B^x \; ∂_y ∧ ∂_z & -  B^x \; ∂_z ∧ ∂_y \\
           B^y \; ∂_z ∧ ∂_x & -  B^y \; ∂_x ∧ ∂_z \\
           B^z \; ∂_x ∧ ∂_y & -  B^z \; ∂_y ∧ ∂_x \\
      \end{aligned} \right]

   .. rubric:: Reorder and conclude

   .. math::

      F^{♯♯} = \frac{1}{2} \begin{bmatrix}
                            & - \E^x \; ∂_x ∧ ∂_t & - \E^y \; ∂_y ∧ ∂_t & - \E^z \; ∂_z ∧ ∂_t \\
          \E^x \; ∂_t ∧ ∂_x &                     & -  B^z \; ∂_y ∧ ∂_x & +  B^y \; ∂_z ∧ ∂_x \\
          \E^y \; ∂_t ∧ ∂_y & + B^z \; ∂_x ∧ ∂_y  &                     & -  B^x \; ∂_z ∧ ∂_y \\
          \E^z \; ∂_t ∧ ∂_z & -  B^y \; ∂_x ∧ ∂_z & +  B^x \; ∂_y ∧ ∂_z &                     \\
      \end{bmatrix}

   .. }}}

Where the electromagnetic field is related to the doubly contravariant Faraday
tensor through:

.. math::

   F^{♯♯} = \frac{1}{2} \: F^{μν} \: ∂_μ ∧ ∂_ν

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

     G^{♭♭} = \left[ \begin{alignedat}{2}
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
