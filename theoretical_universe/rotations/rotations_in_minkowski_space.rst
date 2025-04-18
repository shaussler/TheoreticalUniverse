.. Theoretical Universe (c) by Stéphane Haussler

.. theoretical universe is licensed under a creative commons attribution 4.0
.. international license. you should have received a copy of the license along
.. with this work. if not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _Rotations in Minkowski Space:

Rotations in Minkowski space
============================

.. rst-class:: custom-author

   by Stéphane Haussler

On this page, I systematically explore the geometric differential
representation of infinitesimal rotations in Minkowski spacetime. Rotations are
first expressed as linear combination of rotation planes in terms of bivectors.
The dual differential 2--forms are then derived, as well as the mixed ♯♭ and ♭♯
representation. We work out the Lie algebra of the Lorentz group as well as the
full matrix representation of rotations. The mixed wedge products are fully
expressed in terms of tensor products and their symmetries highlighted.

The :math:`♯♯` rotation tensor
------------------------------

.. {{{

.. _inc_begin_♯♯_rotations:

General rotations can be expressed as linear combinations of rotations in each
planes. For Minkowski space with 4 directions :math:`∂_t`, :math:`∂_x`,
:math:`∂_y` and :math:`∂_t`, this result in 6 planes of rotations. Each plance
is expressed as the exterior product :math:`∧` of basis vectors as :math:`∂_μ ∧
∂_ν`. Rotations in spacetime are expresssed as linear combination of basis
rotations in the six available planes of rotations.

.. topic:: Rotations in Minkowski space

   .. math::

      R^{♯♯} = \begin{bmatrix}
          Q^x \; ∂_t ∧ ∂_x \\
          Q^y \; ∂_t ∧ ∂_y \\
          Q^z \; ∂_t ∧ ∂_z \\
          R^x \; ∂_y ∧ ∂_z \\
          R^y \; ∂_z ∧ ∂_x \\
          R^z \; ∂_x ∧ ∂_y \\
      \end{bmatrix}

.. _inc_end_♯♯_rotations:

The sharp symbol :math:`\sharp` indicates that the components are doubly
contravariant tensor components. Using the antisymmetric property of the
exterior product :math:`∂_μ ∧ ∂_ν = - ∂_ν ∧ ∂_μ`, all terms can be rewritten as
:math:`∂_μ ∧ ∂_ν = \frac{1}{2}( ∂_μ ∧ ∂_ν - ∂_ν ∧ ∂_μ)`:

.. math::

   R^{♯♯} = \begin{bmatrix}
      Q^x \; \frac{1}{2} (∂_t ∧ ∂_x - ∂_x ∧ ∂_t) \\
      Q^y \; \frac{1}{2} (∂_t ∧ ∂_y - ∂_y ∧ ∂_t) \\
      Q^z \; \frac{1}{2} (∂_t ∧ ∂_z - ∂_z ∧ ∂_t) \\
      R^x \; \frac{1}{2} (∂_y ∧ ∂_z - ∂_z ∧ ∂_y) \\
      R^y \; \frac{1}{2} (∂_z ∧ ∂_x - ∂_x ∧ ∂_z) \\
      R^z \; \frac{1}{2} (∂_x ∧ ∂_y - ∂_y ∧ ∂_x) \\
   \end{bmatrix}

With minor rearangement, we get:

.. math::

   R^{♯♯} = \frac{1}{2} \begin{bmatrix}
       Q^x \; ∂_t ∧ ∂_x - Q^x \; ∂_x ∧ ∂_t) \\
       Q^y \; ∂_t ∧ ∂_y - Q^y \; ∂_y ∧ ∂_t) \\
       Q^z \; ∂_t ∧ ∂_z - Q^z \; ∂_z ∧ ∂_t) \\
       R^x \; ∂_y ∧ ∂_z - R^x \; ∂_z ∧ ∂_y) \\
       R^y \; ∂_z ∧ ∂_x - R^y \; ∂_x ∧ ∂_z) \\
       R^z \; ∂_x ∧ ∂_y - R^z \; ∂_y ∧ ∂_x) \\
   \end{bmatrix}

The free matrix representation permits to state the obvious, in that we can
rewrite the rotation above utilizing a row/column matrix representation:

.. topic:: The doubly contravariant rotation in matrix form

   .. math::

      R^{♯♯}= \frac{1}{2} \begin{bmatrix}
                             & + Q^x \; ∂_t ∧ ∂_x & + Q^y \; ∂_t ∧ ∂_y & + Q^z \; ∂_t ∧ ∂_z \\
          - Q^x \; ∂_x ∧ ∂_t &                    & + R^z \; ∂_x ∧ ∂_y & - R^y \; ∂_x ∧ ∂_z \\
          - Q^y \; ∂_y ∧ ∂_t & - R^z \; ∂_y ∧ ∂_x &                    & + R^x \; ∂_y ∧ ∂_z \\
          - Q^z \; ∂_z ∧ ∂_t & + R^y \; ∂_z ∧ ∂_x & - R^x \; ∂_z ∧ ∂_y &                    \\
      \end{bmatrix}

.. }}}

The :math:`♭♭` rotation tensor
------------------------------

.. {{{

.. _inc_begin_♭♭_rotations:

Using the Minkowski metric :math:`η`, we flatten a basis vector with the flat
operator :math:`♭`:

.. math::

   (∂_μ)^♭ = η_{μν} dx^ν

Likewise any index of the doubly contravariant exterior product can be
flattened:

.. math::

   \begin{matrix}
       (∂_μ ∧ ∂_ν)^{♭♯} &= η_{γμ} dx^γ ∧ ∂_ν         \\
       (∂_μ ∧ ∂_ν)^{♯♭} &= η_{γν} ∂_μ ∧ dx^γ         \\
       (∂_μ ∧ ∂_ν)^{♭♭} &= η_{δμ} η_{γν} dx^δ ∧ dx^γ \\
   \end{matrix}

To obtain the doubly covariant representation of rotations in spacetime, we
apply the flat operators :math:`♭♭` to each components :math:`R^{♭♭} =
(R^{♯♯})^{♭♭}`:

.. topic:: Doubly covariant representation of rotations in Minkowski space

   .. math::

      R^{♭♭} = \left[ \begin{aligned}
          - & Q^x \; dt ∧ dx \\
          - & Q^y \; dt ∧ dy \\
          - & Q^z \; dt ∧ dz \\
            & R^x \; dy ∧ dz \\
            & R^y \; dz ∧ dx \\
            & R^z \; dx ∧ dy \\
      \end{aligned} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the flat operators

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; ∂_t ∧ ∂_x \\
          Q^y \; ∂_t ∧ ∂_y \\
          Q^z \; ∂_t ∧ ∂_z \\
          R^x \; ∂_y ∧ ∂_z \\
          R^y \; ∂_z ∧ ∂_x \\
          R^z \; ∂_x ∧ ∂_y \\
      \end{bmatrix}^{♭♭}

   .. rubric:: Distribute the musical operators

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; ∂_t^♭ ∧ ∂_x^♭ \\
          Q^y \; ∂_t^♭ ∧ ∂_y^♭ \\
          Q^z \; ∂_t^♭ ∧ ∂_z^♭ \\
          R^x \; ∂_y^♭ ∧ ∂_z^♭ \\
          R^y \; ∂_z^♭ ∧ ∂_x^♭ \\
          R^z \; ∂_x^♭ ∧ ∂_y^♭ \\
      \end{bmatrix}

   .. rubric:: Expand

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; η_{tμ} d^xμ ∧ η_{xμ} dx^μ \\
          Q^y \; η_{tμ} d^xμ ∧ η_{yμ} dx^μ \\
          Q^z \; η_{tμ} d^xμ ∧ η_{zμ} dx^μ \\
          R^x \; η_{yμ} d^xμ ∧ η_{zμ} dx^μ \\
          R^y \; η_{zμ} d^xμ ∧ η_{xμ} dx^μ \\
          R^z \; η_{xμ} d^xμ ∧ η_{yμ} dx^μ \\
      \end{bmatrix}

   .. rubric:: Identify non-zero terms

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; η_{tt} dt ∧ η_{xx} dx \\
          Q^y \; η_{tt} dt ∧ η_{yy} dy \\
          Q^z \; η_{tt} dt ∧ η_{zz} dz \\
          R^x \; η_{yy} dy ∧ η_{zz} dz \\
          R^y \; η_{zz} dz ∧ η_{xx} dx \\
          R^z \; η_{xx} dx ∧ η_{yy} dy \\
      \end{bmatrix}

   .. rubric:: Apply numerical values

   .. math::

      R^{♭♭} = \left[ \begin{aligned}
          - & Q^x \; dt ∧ dx \\
          - & Q^y \; dt ∧ dy \\
          - & Q^z \; dt ∧ dz \\
            & R^x \; dy ∧ dz \\
            & R^y \; dz ∧ dx \\
            & R^z \; dx ∧ dy \\
      \end{aligned} \right]

   .. }}}

.. _inc_end_♭♭_rotations:

.. }}}

The :math:`♭♯` rotation tensor
------------------------------

.. {{{

In this section, I flattne the first component using the :ref:`free matrix
representation <the_free_matrix_representation>`. The mixed tensor is obtained
by applying the flatternig operator :math:`\flat`:

.. math::

   R^{♭♯} = \begin{bmatrix}
       Q^x \; ∂_t ∧ ∂_x \\
       Q^y \; ∂_t ∧ ∂_y \\
       Q^z \; ∂_t ∧ ∂_z \\
       R^x \; ∂_y ∧ ∂_z \\
       R^y \; ∂_z ∧ ∂_x \\
       R^z \; ∂_x ∧ ∂_y \\
   \end{bmatrix}^{♭♯}
   = \begin{bmatrix}
       + Q^x \; dx^x ∧ ∂_t \\
       + Q^y \; dx^y ∧ ∂_t \\
       + Q^z \; dx^z ∧ ∂_t \\
       - R^x \; dx^z ∧ ∂_y \\
       - R^y \; dx^x ∧ ∂_z \\
       - R^z \; dx^y ∧ ∂_x \\
   \end{bmatrix}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the musical operators

   .. math::

      B^{♭♯} = \begin{bmatrix}
          Q^x \; ∂_t ∧ ∂_x \\
          Q^y \; ∂_t ∧ ∂_y \\
          Q^z \; ∂_t ∧ ∂_z \\
          R^x \; ∂_y ∧ ∂_z \\
          R^y \; ∂_z ∧ ∂_x \\
          R^z \; ∂_x ∧ ∂_y \\
      \end{bmatrix}^{♭♯}

   .. rubric:: Distribute the musical operators to each matrix elements

   .. math::

      B^{♭♯} = \begin{bmatrix}
          Q^x \; (∂_t ∧ ∂_x)^{♭♯} \\
          Q^y \; (∂_t ∧ ∂_y)^{♭♯} \\
          Q^z \; (∂_t ∧ ∂_z)^{♭♯} \\
          R^x \; (∂_y ∧ ∂_z)^{♭♯} \\
          R^y \; (∂_z ∧ ∂_x)^{♭♯} \\
          R^z \; (∂_x ∧ ∂_y)^{♭♯} \\
      \end{bmatrix}

   .. rubric:: Distribute the musical operators

   .. math::

      B^{♭♯} = \begin{bmatrix}
          Q^x \; (∂_t^♭ ∧ ∂_x^♯) \\
          Q^y \; (∂_t^♭ ∧ ∂_y^♯) \\
          Q^z \; (∂_t^♭ ∧ ∂_z^♯) \\
          R^x \; (∂_y^♭ ∧ ∂_z^♯) \\
          R^y \; (∂_z^♭ ∧ ∂_x^♯) \\
          R^z \; (∂_x^♭ ∧ ∂_y^♯) \\
      \end{bmatrix}

   .. rubric:: Apply the musical operators

   .. math::

      B^{♭♯} = \begin{bmatrix}
          Q^x \; η_{tγ} dx^γ ∧ ∂_x^♯ \\
          Q^y \; η_{tγ} dx^γ ∧ ∂_y^♯ \\
          Q^z \; η_{tγ} dx^γ ∧ ∂_z^♯ \\
          R^x \; η_{yγ} dx^γ ∧ ∂_z^♯ \\
          R^y \; η_{zγ} dx^γ ∧ ∂_x^♯ \\
          R^z \; η_{xγ} dx^γ ∧ ∂_y^♯ \\
      \end{bmatrix}

   .. rubric:: Identify the non-zero terms of the Minkowski metric

   .. math::

      B^{♭♯} = \begin{bmatrix}
          Q^x \; η_{tt} dx^t ∧ ∂_x \\
          Q^y \; η_{tt} dx^t ∧ ∂_y \\
          Q^z \; η_{tt} dx^t ∧ ∂_z \\
          R^x \; η_{yy} dx^y ∧ ∂_z \\
          R^y \; η_{zz} dx^z ∧ ∂_x \\
          R^z \; η_{xx} dx^x ∧ ∂_y \\
      \end{bmatrix}

   .. rubric:: Use the numerical values of the Minkowski metric

   .. math::

      B^{♭♯} = \begin{bmatrix}
          + Q^x \; dx^t ∧ ∂_x \\
          + Q^y \; dx^t ∧ ∂_y \\
          + Q^z \; dx^t ∧ ∂_z \\
          - R^x \; dx^y ∧ ∂_z \\
          - R^y \; dx^z ∧ ∂_x \\
          - R^z \; dx^x ∧ ∂_y \\
      \end{bmatrix}

   .. }}}

Taking into account the symetric property of :math:`dx^t ∧ ∂_x`, :math:`dx^t ∧
∂_y`, and :math:`dx^t ∧ ∂_z`, as well the antisymetric property of :math:`dx^x
∧ ∂_y`, :math:`dx^y ∧ ∂_z`, and :math:`dx^z ∧ ∂_x` demonstrated above, this
results in:

.. math::

   R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                           & + Q^x \; dx^t ∧ ∂_x & + Q^y \; dx^t ∧ ∂_y & + Q^z \; dx^t ∧ ∂_z \\
       + Q^x \; dx^x ∧ ∂_t &                     & + R^z \; dx^x ∧ ∂_y & - R^y \; dx^x ∧ ∂_z \\
       + Q^y \; dx^y ∧ ∂_t & - R^z \; dx^y ∧ ∂_x &                     & + R^x \; dx^y ∧ ∂_z \\
       + Q^z \; dx^z ∧ ∂_t & + R^y \; dx^z ∧ ∂_x & - R^x \; dx^z ∧ ∂_y &                     \\
   \end{bmatrix}

.. }}}

The :math:`♯♭` rotation tensor
------------------------------

.. {{{

In this section, I raise the indice using the free matrix notaion. The mixed
tensor is obtained by applying the flatternig operator :math:`\flat`:

.. math::

   R^{♯♭} = \begin{bmatrix}
       Q^x \; ∂_t ∧ ∂_x \\
       Q^y \; ∂_t ∧ ∂_y \\
       Q^z \; ∂_t ∧ ∂_z \\
       R^x \; ∂_y ∧ ∂_z \\
       R^y \; ∂_z ∧ ∂_x \\
       R^z \; ∂_x ∧ ∂_y \\
   \end{bmatrix}^{♯♭}
   = \begin{bmatrix}
       - Q^x \; ∂_t ∧ dx \\
       - Q^y \; ∂_t ∧ dy \\
       - Q^z \; ∂_t ∧ dz \\
       - R^x \; ∂_y ∧ dz \\
       - R^y \; ∂_z ∧ dx \\
       - R^z \; ∂_x ∧ dy \\
   \end{bmatrix}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the musical operators

   .. math::

      B^{♯♭} = \begin{bmatrix}
          Q^x \; ∂_t ∧ ∂_x \\
          Q^y \; ∂_t ∧ ∂_y \\
          Q^z \; ∂_t ∧ ∂_z \\
          R^x \; ∂_y ∧ ∂_z \\
          R^y \; ∂_z ∧ ∂_x \\
          R^z \; ∂_x ∧ ∂_y \\
      \end{bmatrix}^{♯♭}

   .. rubric:: Distribute the musical operators to each matrix elements

   .. math::

      B^{♯♭} = \begin{bmatrix}
          Q^x \; (∂_t ∧ ∂_x)^{♯♭} \\
          Q^y \; (∂_t ∧ ∂_y)^{♯♭} \\
          Q^z \; (∂_t ∧ ∂_z)^{♯♭} \\
          R^x \; (∂_y ∧ ∂_z)^{♯♭} \\
          R^y \; (∂_z ∧ ∂_x)^{♯♭} \\
          R^z \; (∂_x ∧ ∂_y)^{♯♭} \\
      \end{bmatrix}

   .. rubric:: Distribute the musical operators

   .. math::

      B^{♯♭} = \begin{bmatrix}
          Q^x \; (∂_t^♯ ∧ ∂_x^♭) \\
          Q^y \; (∂_t^♯ ∧ ∂_y^♭) \\
          Q^z \; (∂_t^♯ ∧ ∂_z^♭) \\
          R^x \; (∂_y^♯ ∧ ∂_z^♭) \\
          R^y \; (∂_z^♯ ∧ ∂_x^♭) \\
          R^z \; (∂_x^♯ ∧ ∂_y^♭) \\
      \end{bmatrix}

   .. rubric:: Apply and expand

   .. math::

      B^{♯♭} = \begin{bmatrix}
          Q^x \; ∂_t ∧ η_{xγ} dx^γ \\
          Q^y \; ∂_t ∧ η_{yγ} dx^γ \\
          Q^z \; ∂_t ∧ η_{zγ} dx^γ \\
          R^x \; ∂_y ∧ η_{zγ} dx^γ \\
          R^y \; ∂_z ∧ η_{xγ} dx^γ \\
          R^z \; ∂_x ∧ η_{yγ} dx^γ \\
      \end{bmatrix}

   .. rubric:: The metric tensor can be taken out due to mulilinearity

   .. math::

      B^{♯♭} = \begin{bmatrix}
          Q^x \; η_{xγ} ∂_t ∧ dx^γ \\
          Q^y \; η_{yγ} ∂_t ∧ dx^γ \\
          Q^z \; η_{zγ} ∂_t ∧ dx^γ \\
          R^x \; η_{zγ} ∂_y ∧ dx^γ \\
          R^y \; η_{xγ} ∂_z ∧ dx^γ \\
          R^z \; η_{yγ} ∂_x ∧ dx^γ \\
      \end{bmatrix}

   .. rubric:: Most terms of the Minkowski metric are zero

   .. math::

      R^{♯♭} = \begin{bmatrix}
          Q^x \; η_{xx} ∂_t ∧ dx \\
          Q^y \; η_{yy} ∂_t ∧ dy \\
          Q^z \; η_{zz} ∂_t ∧ dz \\
          R^x \; η_{zz} ∂_y ∧ dz \\
          R^y \; η_{xx} ∂_z ∧ dx \\
          R^z \; η_{yy} ∂_x ∧ dy \\
      \end{bmatrix}

   .. rubric:: Use the numerical values of the Minkowski metric

   .. math::

      R^{♯♭} = \begin{bmatrix}
          - Q^x \; ∂_t ∧ dx \\
          - Q^y \; ∂_t ∧ dy \\
          - Q^z \; ∂_t ∧ dz \\
          - R^x \; ∂_y ∧ dz \\
          - R^y \; ∂_z ∧ dx \\
          - R^z \; ∂_x ∧ dy \\
      \end{bmatrix}

   .. }}}

Taking into account the symetric property of :math:`∂_t ∧ dx^x`, :math:`∂_t ∧
dx^y`, and :math:`∂_t ∧ dx^z`, as well the antisymetric property of :math:`∂_x ∧
dx^y`, :math:`∂_ey ∧ dx^z`, and :math:`∂_z ∧ dx^x` demonstrated above, this
results in:

.. math::

   R^{♯♭} = \frac{1}{2} \begin{bmatrix}
                         & - Q^x \; ∂_t ∧ dx & - Q^y \; ∂_t ∧ dy & - Q^z \; ∂_t ∧ dz \\
       - Q^x \; ∂_x ∧ dt &                   & - R^z \; ∂_x ∧ dy & + R^y \; ∂_x ∧ dz \\
       - Q^y \; ∂_y ∧ dt & + R^z \; ∂_y ∧ dx &                   & - R^x \; ∂_y ∧ dz \\
       - Q^z \; ∂_z ∧ dt & - R^y \; ∂_z ∧ dx & + R^x \; ∂_z ∧ dy &                   \\
   \end{bmatrix}

.. }}}

Symmetries of rotations in :math:`♭♯` form
------------------------------------------

.. {{{

The purpose here is to determine the symmetries of the mixed exterior product.
Calculations are tedious, but permit to verify that everything works as it
should as the quantities are encountered when :ref:`deriving the Faraday tensor
from the 1865 Maxwell equations`. The discussion is often avoided, but it is
nice to settle it. This is important when performing matrix multiplications
since per convention, matrices are :math:`♯♭` tensors organized in tables
following the row-column convention. This is not critical when using :ref:`the
free matrix representation`, but permits to fall back to this familiar
framework.

Applying the :math:`♭♯` operators to flatten the first index of each basis
bivectors, we obtain:

.. math::

   \begin{alignedat}{4}
       (∂_t ∧ ∂_x)^{♭♯} =& + dt ∧ ∂_x &\qquad& (∂_x ∧ ∂_t)^{♭♯} =& - dx ∧ ∂_t \\
       (∂_t ∧ ∂_y)^{♭♯} =& + dt ∧ ∂_y &\qquad& (∂_y ∧ ∂_t)^{♭♯} =& - dy ∧ ∂_t \\
       (∂_t ∧ ∂_z)^{♭♯} =& + dt ∧ ∂_z &\qquad& (∂_z ∧ ∂_t)^{♭♯} =& - dz ∧ ∂_t \\
       (∂_y ∧ ∂_z)^{♭♯} =& - dy ∧ ∂_z &\qquad& (∂_y ∧ ∂_x)^{♭♯} =& - dy ∧ ∂_x \\
       (∂_z ∧ ∂_x)^{♭♯} =& - dz ∧ ∂_x &\qquad& (∂_z ∧ ∂_y)^{♭♯} =& - dz ∧ ∂_y \\
       (∂_x ∧ ∂_y)^{♭♯} =& - dx ∧ ∂_y &\qquad& (∂_x ∧ ∂_z)^{♭♯} =& - dx ∧ ∂_z \\
   \end{alignedat}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Distribute musical operators

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♭♯} &= (∂_t^♭ ∧ ∂_x^♯) &\qquad& (∂_x ∧ ∂_t)^{♭♯} &=& (∂_x^♭ ∧ ∂_t^♯) \\
          (∂_t ∧ ∂_y)^{♭♯} &= (∂_t^♭ ∧ ∂_y^♯) &\qquad& (∂_y ∧ ∂_t)^{♭♯} &=& (∂_y^♭ ∧ ∂_t^♯) \\
          (∂_t ∧ ∂_z)^{♭♯} &= (∂_t^♭ ∧ ∂_z^♯) &\qquad& (∂_z ∧ ∂_t)^{♭♯} &=& (∂_z^♭ ∧ ∂_t^♯) \\
          (∂_x ∧ ∂_y)^{♭♯} &= (∂_x^♭ ∧ ∂_y^♯) &\qquad& (∂_y ∧ ∂_x)^{♭♯} &=& (∂_y^♭ ∧ ∂_x^♯) \\
          (∂_y ∧ ∂_z)^{♭♯} &= (∂_y^♭ ∧ ∂_z^♯) &\qquad& (∂_z ∧ ∂_y)^{♭♯} &=& (∂_z^♭ ∧ ∂_y^♯) \\
          (∂_z ∧ ∂_x)^{♭♯} &= (∂_z^♭ ∧ ∂_x^♯) &\qquad& (∂_x ∧ ∂_z)^{♭♯} &=& (∂_x^♭ ∧ ∂_z^♯) \\
      \end{alignedat}

   .. rubric:: Apply musical operators

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♭♯} &= η_{tγ} dx^γ ∧ ∂_x &\qquad& (∂_x ∧ ∂_t)^{♭♯} &=& η_{xγ} dx^γ ∧ ∂_t \\
          (∂_t ∧ ∂_y)^{♭♯} &= η_{tγ} dx^γ ∧ ∂_y &\qquad& (∂_y ∧ ∂_t)^{♭♯} &=& η_{yγ} dx^γ ∧ ∂_t \\
          (∂_t ∧ ∂_z)^{♭♯} &= η_{tγ} dx^γ ∧ ∂_z &\qquad& (∂_z ∧ ∂_t)^{♭♯} &=& η_{zγ} dx^γ ∧ ∂_t \\
          (∂_x ∧ ∂_y)^{♭♯} &= η_{xγ} dx^γ ∧ ∂_y &\qquad& (∂_y ∧ ∂_x)^{♭♯} &=& η_{yγ} dx^γ ∧ ∂_x \\
          (∂_y ∧ ∂_z)^{♭♯} &= η_{yγ} dx^γ ∧ ∂_z &\qquad& (∂_z ∧ ∂_y)^{♭♯} &=& η_{zγ} dx^γ ∧ ∂_y \\
          (∂_z ∧ ∂_x)^{♭♯} &= η_{zγ} dx^γ ∧ ∂_x &\qquad& (∂_x ∧ ∂_z)^{♭♯} &=& η_{xγ} dx^γ ∧ ∂_z \\
      \end{alignedat}

   .. rubric:: Identify non-zero elements

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♭♯} &= η_{tt} dx^t ∧ ∂_x &\qquad& (∂_x ∧ ∂_t)^{♭♯} &=& η_{xx} dx^x ∧ ∂_t \\
          (∂_t ∧ ∂_y)^{♭♯} &= η_{tt} dx^t ∧ ∂_y &\qquad& (∂_y ∧ ∂_t)^{♭♯} &=& η_{yy} dx^y ∧ ∂_t \\
          (∂_t ∧ ∂_z)^{♭♯} &= η_{tt} dx^t ∧ ∂_z &\qquad& (∂_z ∧ ∂_t)^{♭♯} &=& η_{zz} dx^z ∧ ∂_t \\
          (∂_x ∧ ∂_y)^{♭♯} &= η_{xx} dx^x ∧ ∂_y &\qquad& (∂_y ∧ ∂_x)^{♭♯} &=& η_{yy} dx^y ∧ ∂_x \\
          (∂_y ∧ ∂_z)^{♭♯} &= η_{yy} dx^y ∧ ∂_z &\qquad& (∂_z ∧ ∂_y)^{♭♯} &=& η_{zz} dx^z ∧ ∂_y \\
          (∂_z ∧ ∂_x)^{♭♯} &= η_{zz} dx^z ∧ ∂_x &\qquad& (∂_x ∧ ∂_z)^{♭♯} &=& η_{xx} dx^x ∧ ∂_z \\
      \end{alignedat}

   .. rubric:: Apply numerical values

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♭♯} &= + dt ∧ ∂_x &\qquad& (∂_x ∧ ∂_t)^{♭♯} &=& - dx ∧ ∂_t \\
          (∂_t ∧ ∂_y)^{♭♯} &= + dt ∧ ∂_y &\qquad& (∂_y ∧ ∂_t)^{♭♯} &=& - dy ∧ ∂_t \\
          (∂_t ∧ ∂_z)^{♭♯} &= + dt ∧ ∂_z &\qquad& (∂_z ∧ ∂_t)^{♭♯} &=& - dz ∧ ∂_t \\
          (∂_x ∧ ∂_y)^{♭♯} &= - dx ∧ ∂_y &\qquad& (∂_y ∧ ∂_x)^{♭♯} &=& - dy ∧ ∂_x \\
          (∂_y ∧ ∂_z)^{♭♯} &= - dy ∧ ∂_z &\qquad& (∂_z ∧ ∂_y)^{♭♯} &=& - dz ∧ ∂_y \\
          (∂_z ∧ ∂_x)^{♭♯} &= - dz ∧ ∂_x &\qquad& (∂_x ∧ ∂_z)^{♭♯} &=& - dx ∧ ∂_z \\
      \end{alignedat}

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{alignedat}{8}
       (∂_t ∧ ∂_x)^{♭♯} =& + dt ⊗ ∂_x &+& dx ⊗ ∂_t &\qquad& (∂_x ∧ ∂_t)^{♭♯} =& - dx ⊗ ∂_t &-& dt ⊗ ∂_x \\
       (∂_t ∧ ∂_y)^{♭♯} =& + dt ⊗ ∂_y &+& dy ⊗ ∂_t &\qquad& (∂_y ∧ ∂_t)^{♭♯} =& - dy ⊗ ∂_t &-& dt ⊗ ∂_y \\
       (∂_t ∧ ∂_z)^{♭♯} =& + dt ⊗ ∂_z &+& dz ⊗ ∂_t &\qquad& (∂_z ∧ ∂_t)^{♭♯} =& - dz ⊗ ∂_t &-& dt ⊗ ∂_z \\
       (∂_y ∧ ∂_z)^{♭♯} =& - dy ⊗ ∂_z &+& dz ⊗ ∂_y &\qquad& (∂_z ∧ ∂_y)^{♭♯} =& - dz ⊗ ∂_y &+& dy ⊗ ∂_z \\
       (∂_z ∧ ∂_x)^{♭♯} =& - dz ⊗ ∂_x &+& dx ⊗ ∂_z &\qquad& (∂_x ∧ ∂_z)^{♭♯} =& - dx ⊗ ∂_z &+& dz ⊗ ∂_x \\
       (∂_x ∧ ∂_y)^{♭♯} =& - dx ⊗ ∂_y &+& dy ⊗ ∂_x &\qquad& (∂_y ∧ ∂_x)^{♭♯} =& - dy ⊗ ∂_x &+& dx ⊗ ∂_y \\
   \end{alignedat}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Expand exterior products to their tensor expressions

   .. math::

      \begin{alignedat}{7}
          (∂_t ∧ ∂_x)^{♭♯} =& (∂_t ⊗ ∂_x &-& ∂_x ⊗ ∂_t)^{♭♯} &\qquad& (∂_x ∧ ∂_t)^{♭♯} &=& (∂_x ⊗ ∂_t &-& ∂_t ⊗ ∂_x)^{♭♯} \\
          (∂_t ∧ ∂_y)^{♭♯} =& (∂_t ⊗ ∂_y &-& ∂_y ⊗ ∂_t)^{♭♯} &\qquad& (∂_y ∧ ∂_t)^{♭♯} &=& (∂_y ⊗ ∂_t &-& ∂_t ⊗ ∂_y)^{♭♯} \\
          (∂_t ∧ ∂_z)^{♭♯} =& (∂_t ⊗ ∂_z &-& ∂_z ⊗ ∂_t)^{♭♯} &\qquad& (∂_z ∧ ∂_t)^{♭♯} &=& (∂_z ⊗ ∂_t &-& ∂_t ⊗ ∂_z)^{♭♯} \\
          (∂_y ∧ ∂_z)^{♭♯} =& (∂_y ⊗ ∂_z &-& ∂_z ⊗ ∂_y)^{♭♯} &\qquad& (∂_z ∧ ∂_y)^{♭♯} &=& (∂_z ⊗ ∂_y &-& ∂_y ⊗ ∂_z)^{♭♯} \\
          (∂_z ∧ ∂_x)^{♭♯} =& (∂_z ⊗ ∂_x &-& ∂_x ⊗ ∂_z)^{♭♯} &\qquad& (∂_x ∧ ∂_z)^{♭♯} &=& (∂_x ⊗ ∂_z &-& ∂_z ⊗ ∂_x)^{♭♯} \\
          (∂_x ∧ ∂_y)^{♭♯} =& (∂_x ⊗ ∂_y &-& ∂_y ⊗ ∂_x)^{♭♯} &\qquad& (∂_y ∧ ∂_x)^{♭♯} &=& (∂_y ⊗ ∂_x &-& ∂_x ⊗ ∂_y)^{♭♯} \\
      \end{alignedat}

   .. rubric:: Distribute musical operators

   .. math::

      \begin{alignedat}{7}
          (∂_t ∧ ∂_x)^{♭♯} =& ∂_t^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_t^♯ &\qquad& (∂_x ∧ ∂_t)^{♭♯} &=& ∂_x^♭ ⊗ ∂_t^♯ - ∂_t^♭ ⊗ ∂_x^♯ \\
          (∂_t ∧ ∂_y)^{♭♯} =& ∂_t^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_t^♯ &\qquad& (∂_y ∧ ∂_t)^{♭♯} &=& ∂_y^♭ ⊗ ∂_t^♯ - ∂_t^♭ ⊗ ∂_y^♯ \\
          (∂_t ∧ ∂_z)^{♭♯} =& ∂_t^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_t^♯ &\qquad& (∂_z ∧ ∂_t)^{♭♯} &=& ∂_z^♭ ⊗ ∂_t^♯ - ∂_t^♭ ⊗ ∂_z^♯ \\
          (∂_y ∧ ∂_z)^{♭♯} =& ∂_y^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_y^♯ &\qquad& (∂_z ∧ ∂_y)^{♭♯} &=& ∂_z^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_z^♯ \\
          (∂_z ∧ ∂_x)^{♭♯} =& ∂_z^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_z^♯ &\qquad& (∂_x ∧ ∂_z)^{♭♯} &=& ∂_x^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_x^♯ \\
          (∂_x ∧ ∂_y)^{♭♯} =& ∂_x^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_x^♯ &\qquad& (∂_y ∧ ∂_x)^{♭♯} &=& ∂_y^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_y^♯ \\
      \end{alignedat}

   .. rubric:: Apply musical operators

   .. math::

      \begin{alignedat}{7}
          (∂_t ∧ ∂_x)^{♭♯} &= η_{tγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_t &\qquad& (∂_x ∧ ∂_t)^{♭♯} &=& η_{xγ} dx^γ ⊗ ∂_t - η_{tγ} dx^γ ⊗ ∂_x \\
          (∂_t ∧ ∂_y)^{♭♯} &= η_{tγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_t &\qquad& (∂_y ∧ ∂_t)^{♭♯} &=& η_{yγ} dx^γ ⊗ ∂_t - η_{tγ} dx^γ ⊗ ∂_y \\
          (∂_t ∧ ∂_z)^{♭♯} &= η_{tγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_t &\qquad& (∂_z ∧ ∂_t)^{♭♯} &=& η_{zγ} dx^γ ⊗ ∂_t - η_{tγ} dx^γ ⊗ ∂_z \\
          (∂_y ∧ ∂_z)^{♭♯} &= η_{yγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_y &\qquad& (∂_z ∧ ∂_y)^{♭♯} &=& η_{zγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_z \\
          (∂_z ∧ ∂_x)^{♭♯} &= η_{zγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_z &\qquad& (∂_x ∧ ∂_z)^{♭♯} &=& η_{xγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_x \\
          (∂_x ∧ ∂_y)^{♭♯} &= η_{xγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_x &\qquad& (∂_y ∧ ∂_x)^{♭♯} &=& η_{yγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_y \\
      \end{alignedat}

   .. rubric:: Identify non-zero metric elements

   .. math::

      \begin{alignedat}{7}
          (∂_t ∧ ∂_x)^{♭♯} &= η_{tt} dx^t ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_t &\qquad& (∂_x ∧ ∂_t)^{♭♯} &=& η_{xx} dx^x ⊗ ∂_t - η_{tt} dx^t ⊗ ∂_x \\
          (∂_t ∧ ∂_y)^{♭♯} &= η_{tt} dx^t ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_t &\qquad& (∂_y ∧ ∂_t)^{♭♯} &=& η_{yy} dx^y ⊗ ∂_t - η_{tt} dx^t ⊗ ∂_y \\
          (∂_t ∧ ∂_z)^{♭♯} &= η_{tt} dx^t ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_t &\qquad& (∂_z ∧ ∂_t)^{♭♯} &=& η_{zz} dx^z ⊗ ∂_t - η_{tt} dx^t ⊗ ∂_z \\
          (∂_y ∧ ∂_z)^{♭♯} &= η_{yy} dx^y ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_y &\qquad& (∂_z ∧ ∂_y)^{♭♯} &=& η_{zz} dx^z ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_z \\
          (∂_z ∧ ∂_x)^{♭♯} &= η_{zz} dx^z ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_z &\qquad& (∂_x ∧ ∂_z)^{♭♯} &=& η_{xx} dx^x ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_x \\
          (∂_x ∧ ∂_y)^{♭♯} &= η_{xx} dx^x ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_x &\qquad& (∂_y ∧ ∂_x)^{♭♯} &=& η_{yy} dx^y ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_y \\
      \end{alignedat}

   .. rubric:: Apply numerical values

   .. math::

      \begin{alignedat}{6}
          (∂_t ∧ ∂_x)^{♭♯} & = + dt ⊗ ∂_x & + dx ⊗ ∂_t & \qquad & (∂_x ∧ ∂_t)^{♭♯} & = & - dx ⊗ ∂_t &-& dt ⊗ ∂_x \\
          (∂_t ∧ ∂_y)^{♭♯} & = + dt ⊗ ∂_y & + dy ⊗ ∂_t & \qquad & (∂_y ∧ ∂_t)^{♭♯} & = & - dy ⊗ ∂_t &-& dt ⊗ ∂_y \\
          (∂_t ∧ ∂_z)^{♭♯} & = + dt ⊗ ∂_z & + dz ⊗ ∂_t & \qquad & (∂_z ∧ ∂_t)^{♭♯} & = & - dz ⊗ ∂_t &-& dt ⊗ ∂_z \\
          (∂_y ∧ ∂_z)^{♭♯} & = - dy ⊗ ∂_z & + dz ⊗ ∂_y & \qquad & (∂_z ∧ ∂_y)^{♭♯} & = & - dz ⊗ ∂_y &+& dy ⊗ ∂_z \\
          (∂_z ∧ ∂_x)^{♭♯} & = - dz ⊗ ∂_x & + dx ⊗ ∂_z & \qquad & (∂_x ∧ ∂_z)^{♭♯} & = & - dx ⊗ ∂_z &+& dz ⊗ ∂_x \\
          (∂_x ∧ ∂_y)^{♭♯} & = - dx ⊗ ∂_y & + dy ⊗ ∂_x & \qquad & (∂_y ∧ ∂_x)^{♭♯} & = & - dy ⊗ ∂_x &+& dx ⊗ ∂_y \\
      \end{alignedat}

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{alignedat}{9}
       dt ∧ ∂_x = & + dt ⊗ ∂_x & + & dx ⊗ ∂_t & \qquad & dx ∧ ∂_t & = & + dt ⊗ ∂_x & + & dx ⊗ ∂_t \\
       dt ∧ ∂_y = & + dt ⊗ ∂_y & + & dy ⊗ ∂_t & \qquad & dy ∧ ∂_t & = & + dt ⊗ ∂_y & + & dy ⊗ ∂_t \\
       dt ∧ ∂_z = & + dt ⊗ ∂_z & + & dz ⊗ ∂_t & \qquad & dz ∧ ∂_t & = & + dt ⊗ ∂_z & + & dz ⊗ ∂_t \\
       dy ∧ ∂_z = & + dy ⊗ ∂_z & - & dz ⊗ ∂_y & \qquad & dz ∧ ∂_y & = & - dy ⊗ ∂_z & + & dz ⊗ ∂_y \\
       dz ∧ ∂_x = & + dz ⊗ ∂_x & - & dx ⊗ ∂_z & \qquad & dx ∧ ∂_z & = & - dz ⊗ ∂_x & + & dx ⊗ ∂_z \\
       dx ∧ ∂_y = & + dx ⊗ ∂_y & - & dy ⊗ ∂_x & \qquad & dy ∧ ∂_x & = & - dx ⊗ ∂_y & + & dy ⊗ ∂_x \\
   \end{alignedat}

Taken together, we get:

.. _symmetries_of_the_flat_sharp_mixed_exterior_product:

.. topic:: Symmetries of the :math:`♭♯` mixed exterior product

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

.. }}}

Symmetries of rotations in :math:`♯♭` form
------------------------------------------

.. {{{

The calculations in this section repeat the calculations of the previous
sections. The results servers as a test with respect to the former calculations
as the results should be fully consistent. We show this is indeed the case. We
apply the :math:`♯♭` operators to flatten the second index of each basis
bivectors and obtain:

.. math::

   \begin{alignedat}{5}
       (∂_t ∧ ∂_x)^{♯♭} & = - ∂_t ∧ dx & \qquad & (∂_x ∧ ∂_t)^{♯♭} & = & + ∂_x ∧ dt \\
       (∂_t ∧ ∂_y)^{♯♭} & = - ∂_t ∧ dy & \qquad & (∂_y ∧ ∂_t)^{♯♭} & = & + ∂_y ∧ dt \\
       (∂_t ∧ ∂_z)^{♯♭} & = - ∂_t ∧ dz & \qquad & (∂_z ∧ ∂_t)^{♯♭} & = & + ∂_z ∧ dt \\
       (∂_y ∧ ∂_z)^{♯♭} & = - ∂_y ∧ dz & \qquad & (∂_z ∧ ∂_y)^{♯♭} & = & - ∂_z ∧ dy \\
       (∂_z ∧ ∂_x)^{♯♭} & = - ∂_z ∧ dx & \qquad & (∂_x ∧ ∂_z)^{♯♭} & = & - ∂_x ∧ dz \\
       (∂_x ∧ ∂_y)^{♯♭} & = - ∂_x ∧ dy & \qquad & (∂_y ∧ ∂_x)^{♯♭} & = & - ∂_y ∧ dx \\
   \end{alignedat}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Distribute the musical operators

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= ∂_t^♯ ∧ ∂_x^♭ &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& ∂_x^♯ ∧ ∂_t^♭ \\
          (∂_t ∧ ∂_y)^{♯♭} &= ∂_t^♯ ∧ ∂_y^♭ &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& ∂_y^♯ ∧ ∂_t^♭ \\
          (∂_t ∧ ∂_z)^{♯♭} &= ∂_t^♯ ∧ ∂_z^♭ &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& ∂_z^♯ ∧ ∂_t^♭ \\
          (∂_y ∧ ∂_z)^{♯♭} &= ∂_y^♯ ∧ ∂_z^♭ &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& ∂_z^♯ ∧ ∂_y^♭ \\
          (∂_z ∧ ∂_x)^{♯♭} &= ∂_z^♯ ∧ ∂_x^♭ &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& ∂_x^♯ ∧ ∂_z^♭ \\
          (∂_x ∧ ∂_y)^{♯♭} &= ∂_x^♯ ∧ ∂_y^♭ &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& ∂_y^♯ ∧ ∂_x^♭ \\
      \end{alignedat}

   .. rubric:: Apply the musical operators

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= ∂_t ∧ η_{xγ} dx^γ &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& ∂_x ∧ η_{γt} dx^γ \\
          (∂_t ∧ ∂_y)^{♯♭} &= ∂_t ∧ η_{yγ} dx^γ &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& ∂_y ∧ η_{γt} dx^γ \\
          (∂_t ∧ ∂_z)^{♯♭} &= ∂_t ∧ η_{zγ} dx^γ &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& ∂_z ∧ η_{γt} dx^γ \\
          (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ∧ η_{zγ} dx^γ &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& ∂_z ∧ η_{γy} dx^γ \\
          (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ∧ η_{xγ} dx^γ &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& ∂_x ∧ η_{γz} dx^γ \\
          (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ∧ η_{yγ} dx^γ &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& ∂_y ∧ η_{γx} dx^γ \\
      \end{alignedat}

   .. rubric:: Identify the non-zero metric components:

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= η_{xx} ∂_t ∧ dx^x &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& ∂_x ∧ η_{tt} dt \\
          (∂_t ∧ ∂_y)^{♯♭} &= η_{yy} ∂_t ∧ dx^y &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& ∂_y ∧ η_{tt} dt \\
          (∂_t ∧ ∂_z)^{♯♭} &= η_{zz} ∂_t ∧ dx^z &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& ∂_z ∧ η_{tt} dt \\
          (∂_y ∧ ∂_z)^{♯♭} &= η_{zz} ∂_y ∧ dx^z &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& ∂_z ∧ η_{yy} dy \\
          (∂_z ∧ ∂_x)^{♯♭} &= η_{xx} ∂_z ∧ dx^x &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& ∂_x ∧ η_{zz} dz \\
          (∂_x ∧ ∂_y)^{♯♭} &= η_{yy} ∂_x ∧ dx^y &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& ∂_y ∧ η_{xx} dx \\
      \end{alignedat}

   .. rubric:: Simplify

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= η_{xx} ∂_t ∧ dx &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& η_{tt} ∂_x ∧ dt \\
          (∂_t ∧ ∂_y)^{♯♭} &= η_{yy} ∂_t ∧ dy &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& η_{tt} ∂_y ∧ dt \\
          (∂_t ∧ ∂_z)^{♯♭} &= η_{zz} ∂_t ∧ dz &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& η_{tt} ∂_z ∧ dt \\
          (∂_y ∧ ∂_z)^{♯♭} &= η_{zz} ∂_y ∧ dz &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& η_{yy} ∂_z ∧ dy \\
          (∂_z ∧ ∂_x)^{♯♭} &= η_{xx} ∂_z ∧ dx &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& η_{zz} ∂_x ∧ dz \\
          (∂_x ∧ ∂_y)^{♯♭} &= η_{yy} ∂_x ∧ dy &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& η_{xx} ∂_y ∧ dx \\
      \end{alignedat}

   .. rubric:: Apply numerical values:

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} & = - ∂_t ∧ dx & \qquad & (∂_x ∧ ∂_t)^{♯♭} & = & + ∂_x ∧ dt \\
          (∂_t ∧ ∂_y)^{♯♭} & = - ∂_t ∧ dy & \qquad & (∂_y ∧ ∂_t)^{♯♭} & = & + ∂_y ∧ dt \\
          (∂_t ∧ ∂_z)^{♯♭} & = - ∂_t ∧ dz & \qquad & (∂_z ∧ ∂_t)^{♯♭} & = & + ∂_z ∧ dt \\
          (∂_y ∧ ∂_z)^{♯♭} & = - ∂_y ∧ dz & \qquad & (∂_z ∧ ∂_y)^{♯♭} & = & - ∂_z ∧ dy \\
          (∂_z ∧ ∂_x)^{♯♭} & = - ∂_z ∧ dx & \qquad & (∂_x ∧ ∂_z)^{♯♭} & = & - ∂_x ∧ dz \\
          (∂_x ∧ ∂_y)^{♯♭} & = - ∂_x ∧ dy & \qquad & (∂_y ∧ ∂_x)^{♯♭} & = & - ∂_y ∧ dx \\
      \end{alignedat}

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{alignedat}{5}
       (∂_t ∧ ∂_x)^{♯♭} & = - ∂_t ⊗ dx - ∂_x ⊗ dt & \qquad & (∂_x ∧ ∂_t)^{♯♭} & = & + ∂_x ⊗ dt + ∂_t ⊗ dx \\
       (∂_t ∧ ∂_y)^{♯♭} & = - ∂_t ⊗ dy - ∂_y ⊗ dt & \qquad & (∂_y ∧ ∂_t)^{♯♭} & = & + ∂_y ⊗ dt + ∂_t ⊗ dy \\
       (∂_t ∧ ∂_z)^{♯♭} & = - ∂_t ⊗ dz - ∂_z ⊗ dt & \qquad & (∂_z ∧ ∂_t)^{♯♭} & = & + ∂_z ⊗ dt + ∂_t ⊗ dz \\
       (∂_y ∧ ∂_z)^{♯♭} & = - ∂_y ⊗ dz + ∂_z ⊗ dy & \qquad & (∂_z ∧ ∂_y)^{♯♭} & = & - ∂_z ⊗ dy + ∂_y ⊗ dz \\
       (∂_z ∧ ∂_x)^{♯♭} & = - ∂_z ⊗ dx + ∂_x ⊗ dz & \qquad & (∂_x ∧ ∂_z)^{♯♭} & = & - ∂_x ⊗ dz + ∂_z ⊗ dx \\
       (∂_x ∧ ∂_y)^{♯♭} & = - ∂_x ⊗ dy + ∂_y ⊗ dx & \qquad & (∂_y ∧ ∂_x)^{♯♭} & = & - ∂_y ⊗ dx + ∂_x ⊗ dy \\
   \end{alignedat}

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Expand in terms of tensor product

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= (∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t)^{♯♭} &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& (∂_x ⊗ ∂_t - ∂_t ⊗ ∂_x)^{♯♭} \\
          (∂_t ∧ ∂_y)^{♯♭} &= (∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t)^{♯♭} &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& (∂_y ⊗ ∂_t - ∂_t ⊗ ∂_y)^{♯♭} \\
          (∂_t ∧ ∂_z)^{♯♭} &= (∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t)^{♯♭} &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& (∂_z ⊗ ∂_t - ∂_t ⊗ ∂_z)^{♯♭} \\
          (∂_y ∧ ∂_z)^{♯♭} &= (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♯♭} &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& (∂_z ⊗ ∂_y - ∂_y ⊗ ∂_z)^{♯♭} \\
          (∂_z ∧ ∂_x)^{♯♭} &= (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♯♭} &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& (∂_x ⊗ ∂_z - ∂_z ⊗ ∂_x)^{♯♭} \\
          (∂_x ∧ ∂_y)^{♯♭} &= (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♯♭} &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& (∂_y ⊗ ∂_x - ∂_x ⊗ ∂_y)^{♯♭} \\
      \end{alignedat}

   .. rubric:: Distribute the musical operators

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= ∂_t^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_t^♭ &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& ∂_x^♯ ⊗ ∂_t^♭ - ∂_t^♯ ⊗ ∂_x^♭ \\
          (∂_t ∧ ∂_y)^{♯♭} &= ∂_t^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_t^♭ &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& ∂_y^♯ ⊗ ∂_t^♭ - ∂_t^♯ ⊗ ∂_y^♭ \\
          (∂_t ∧ ∂_z)^{♯♭} &= ∂_t^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_t^♭ &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& ∂_z^♯ ⊗ ∂_t^♭ - ∂_t^♯ ⊗ ∂_z^♭ \\
          (∂_y ∧ ∂_z)^{♯♭} &= ∂_y^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_y^♭ &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& ∂_z^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_z^♭ \\
          (∂_z ∧ ∂_x)^{♯♭} &= ∂_z^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_z^♭ &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& ∂_x^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_x^♭ \\
          (∂_x ∧ ∂_y)^{♯♭} &= ∂_x^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_x^♭ &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& ∂_y^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_y^♭ \\
      \end{alignedat}

   .. rubric:: Apply musical operators

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= ∂_t ⊗ η_{xγ} dx^γ - η_{tγ} ∂_x ⊗ dx^γ &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& ∂_x ⊗ η_{γt} dx^γ - ∂_t ⊗ η_{γx} dx^γ \\
          (∂_t ∧ ∂_y)^{♯♭} &= ∂_t ⊗ η_{yγ} dx^γ - η_{tγ} ∂_y ⊗ dx^γ &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& ∂_y ⊗ η_{γt} dx^γ - ∂_t ⊗ η_{γy} dx^γ \\
          (∂_t ∧ ∂_z)^{♯♭} &= ∂_t ⊗ η_{zγ} dx^γ - η_{tγ} ∂_z ⊗ dx^γ &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& ∂_z ⊗ η_{γt} dx^γ - ∂_t ⊗ η_{γz} dx^γ \\
          (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ⊗ η_{zγ} dx^γ - η_{yγ} ∂_z ⊗ dx^γ &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& ∂_z ⊗ η_{γy} dx^γ - ∂_y ⊗ η_{γz} dx^γ \\
          (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ⊗ η_{xγ} dx^γ - η_{zγ} ∂_x ⊗ dx^γ &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& ∂_x ⊗ η_{γz} dx^γ - ∂_z ⊗ η_{γx} dx^γ \\
          (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ⊗ η_{yγ} dx^γ - η_{xγ} ∂_y ⊗ dx^γ &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& ∂_y ⊗ η_{γx} dx^γ - ∂_x ⊗ η_{γy} dx^γ \\
      \end{alignedat}

   .. rubric:: Identify the non-zero components

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= ∂_t ⊗ η_{xx} dx - ∂_x ⊗ η_{tt} dt &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& ∂_x ⊗ η_{tt} dt - ∂_t ⊗ η_{xx} dx \\
          (∂_t ∧ ∂_y)^{♯♭} &= ∂_t ⊗ η_{yy} dy - ∂_y ⊗ η_{tt} dt &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& ∂_y ⊗ η_{tt} dt - ∂_t ⊗ η_{yy} dy \\
          (∂_t ∧ ∂_z)^{♯♭} &= ∂_t ⊗ η_{zz} dz - ∂_z ⊗ η_{tt} dt &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& ∂_z ⊗ η_{tt} dt - ∂_t ⊗ η_{zz} dz \\
          (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ⊗ η_{zz} dz - ∂_z ⊗ η_{yy} dy &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& ∂_z ⊗ η_{yy} dy - ∂_y ⊗ η_{zz} dz \\
          (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ⊗ η_{xx} dx - ∂_x ⊗ η_{zz} dz &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& ∂_x ⊗ η_{zz} dz - ∂_z ⊗ η_{xx} dx \\
          (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ⊗ η_{yy} dy - ∂_y ⊗ η_{xx} dx &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& ∂_y ⊗ η_{xx} dx - ∂_x ⊗ η_{yy} dy \\
      \end{alignedat}

   .. rubric:: Apply numerical values

   .. math::

      \begin{alignedat}{5}
          (∂_t ∧ ∂_x)^{♯♭} &= - ∂_t ⊗ dx - ∂_x ⊗ dt &\qquad& (∂_x ∧ ∂_t)^{♯♭} &=& + ∂_x ⊗ dt + ∂_t ⊗ dx \\
          (∂_t ∧ ∂_y)^{♯♭} &= - ∂_t ⊗ dy - ∂_y ⊗ dt &\qquad& (∂_y ∧ ∂_t)^{♯♭} &=& + ∂_y ⊗ dt + ∂_t ⊗ dy \\
          (∂_t ∧ ∂_z)^{♯♭} &= - ∂_t ⊗ dz - ∂_z ⊗ dt &\qquad& (∂_z ∧ ∂_t)^{♯♭} &=& + ∂_z ⊗ dt + ∂_t ⊗ dz \\
          (∂_y ∧ ∂_z)^{♯♭} &= - ∂_y ⊗ dz + ∂_z ⊗ dy &\qquad& (∂_z ∧ ∂_y)^{♯♭} &=& - ∂_z ⊗ dy + ∂_y ⊗ dz \\
          (∂_z ∧ ∂_x)^{♯♭} &= - ∂_z ⊗ dx + ∂_x ⊗ dz &\qquad& (∂_x ∧ ∂_z)^{♯♭} &=& - ∂_x ⊗ dz + ∂_z ⊗ dx \\
          (∂_x ∧ ∂_y)^{♯♭} &= - ∂_x ⊗ dy + ∂_y ⊗ dx &\qquad& (∂_y ∧ ∂_x)^{♯♭} &=& - ∂_y ⊗ dx + ∂_x ⊗ dy \\
      \end{alignedat}

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{alignedat}{4}
       ∂_t ∧ dx & = + ∂_t ⊗ dx + ∂_x ⊗ dt & \qquad & ∂_x ∧ dt & = + ∂_x ⊗ dt + ∂_t ⊗ dx \\
       ∂_t ∧ dy & = + ∂_t ⊗ dy + ∂_y ⊗ dt & \qquad & ∂_y ∧ dt & = + ∂_y ⊗ dt + ∂_t ⊗ dy \\
       ∂_t ∧ dz & = + ∂_t ⊗ dz + ∂_z ⊗ dt & \qquad & ∂_z ∧ dt & = + ∂_z ⊗ dt + ∂_t ⊗ dz \\
       ∂_y ∧ dz & = + ∂_y ⊗ dz - ∂_z ⊗ dy & \qquad & ∂_z ∧ dy & = + ∂_z ⊗ dy - ∂_y ⊗ dz \\
       ∂_z ∧ dx & = + ∂_z ⊗ dx - ∂_x ⊗ dz & \qquad & ∂_x ∧ dz & = + ∂_x ⊗ dz - ∂_z ⊗ dx \\
       ∂_x ∧ dy & = + ∂_x ⊗ dy - ∂_y ⊗ dx & \qquad & ∂_y ∧ dx & = + ∂_y ⊗ dx - ∂_x ⊗ dy \\
   \end{alignedat}

Taken together, we get the result consistent with the symmetries obtained for
the :math:`♭♯`, thus strongly suggesting the results regarding the symmetries of
the mixeed exterior product are correct.

.. _symmetries_of_the_sharp_flat_mixed_exterior_product:

.. topic:: Symmetries of the :math:`♯♭` mixed exterior product

   ============ =============================
   Symmetry     Basis elements
   ============ =============================
   Symetric     :math:`∂_t ∧ dx = + ∂_x ∧ dt`
   Symetric     :math:`∂_t ∧ dy = + ∂_y ∧ dt`
   Symetric     :math:`∂_t ∧ dz = + ∂_z ∧ dt`
   Antisymetric :math:`∂_y ∧ dz = - ∂_z ∧ dy`
   Antisymetric :math:`∂_z ∧ dx = - ∂_x ∧ dz`
   Antisymetric :math:`∂_x ∧ dy = - ∂_y ∧ dx`
   ============ =============================

.. }}}

:math:`\mathfrak{so}(1,3)` Lie algebra of the Lorentz group
-----------------------------------------------------------

.. {{{

Matrices are organized in column of vectors and therefore type :math:`♯♭`
tensors, written :math:`M_μ{}^ν` in abstract index notation. The objects can
take vectors :math:`v^ν` as input and output transformed vectors :math:`M_γ{}^ν
\: v^γ`.

.. math::

   M = \begin{pmatrix}
   \vdots & \vdots & \vdots & \vdots \\
   v_0^ν & v_1^ν & v_2^ν & v_3^{ν}   \\
   \vdots & \vdots & \vdots & \vdots \\
   \end{pmatrix}

The type :math:`♯♭` row/column matrix representation of rotations is:

.. math::

   R^{♭♯} = \frac{1}{2} \begin{bmatrix}
                         & + Q^x \: dt ∧ ∂_x & + Q^y \: dt ∧ ∂_y & + Q^z \: dt ∧ ∂_z \\
       + Q^x \: dx ∧ ∂_t &                   & + R^z \: dx ∧ ∂_y & - R^y \: dx ∧ ∂_z \\
       + Q^y \: dy ∧ ∂_t & - R^z \: dy ∧ ∂_x &                   & + R^x \: dy ∧ ∂_z \\
       + Q^z \: dz ∧ ∂_t & + R^y \: dz ∧ ∂_x & - R^x \: dz ∧ ∂_y &                   \\
   \end{bmatrix}

Taking out the basis bivectors from :ref:`the free matrix representation`, we
trivially obtain the representation of the `Lorentz group
<https://en.m.wikipedia.org/wiki/Lorentz_group#Lie_algebra>`_, as well as the
interpretation as a rotation in spacetime:

.. math::

   R^{♭♯} = \frac{1}{2} \begin{bmatrix}
             & + Q^x & + Q^y & + Q^z \\
       + Q^x &       & + R^z & - R^y \\
       + Q^y & - R^z &       & + R^x \\
       + Q^z & + R^y & - R^x &       \\
   \end{bmatrix}

.. }}}
