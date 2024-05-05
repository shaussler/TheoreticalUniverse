.. Theoretical Universe (c) by Stéphane Haussler

.. theoretical universe is licensed under a creative commons attribution 4.0
.. international license. you should have received a copy of the license along
.. with this work. if not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _rotations_in_minkowski_space:
.. _rotations in minkowski space:

Rotations in Minkowski Space
============================

.. rst-class:: custom-author

   by Stéphane Haussler

In this section, we explore rotations in minkowski space. We express rotations
first as linear combination of bivectors, and systematically derive the
expression as:

* linear combination of bicovectors
* doubly contravariant rank 2 tensor
* doubly convariant rank 2 tensor
* mixed tensors of rank (1,1)

We work out the Lie algebra of the Lorentz group and the matrix representation
of rotations. The mixed wedge products are fully expressed in terms of tensor
products and their symmetries highlighted.

The :math:`♯♯` Rotation Tensor
------------------------------

.. {{{

General rotations can be expressed as linear combinations of rotations in each
planes. For Minkowski space with 4 dimensions, this result in 6 planes of
rotations. Each plance is expressed as the wedge product :math:`∧` of basis
vectors as :math:`∂_x ∧ ∂_y`. A rotation in spacetime is represented by the
linear combination of all basis rotations in all six available planes.

.. topic:: Rotations in Minkowski Space

   .. math::

      R^{♯♯} = \begin{bmatrix}
          a \; ∂_t ∧ ∂_x \\
          b \; ∂_t ∧ ∂_y \\
          c \; ∂_t ∧ ∂_z \\
          d \; ∂_y ∧ ∂_z \\
          e \; ∂_z ∧ ∂_x \\
          f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}

The sharp symbol :math:`\sharp` indicates that the components are doubly
contravariant tensor components. Using the antisymmetric property of the wedge
product (:math:`∂_μ ∧ ∂_ν = - ∂_ν ∧ ∂_μ`) all terms can be rewritten as
:math:`∂_μ ∧ ∂_ν = \frac{1}{2}( ∂_μ ∧ ∂_ν - ∂_ν ∧ ∂_μ)`. We get:

.. math::

   R^{♯♯} = \begin{bmatrix}
       a \; \frac{1}{2} (∂_t ∧ ∂_x - ∂_x ∧ ∂_t) \\
       b \; \frac{1}{2} (∂_t ∧ ∂_y - ∂_y ∧ ∂_t) \\
       c \; \frac{1}{2} (∂_t ∧ ∂_z - ∂_z ∧ ∂_t) \\
       d \; \frac{1}{2} (∂_y ∧ ∂_z - ∂_z ∧ ∂_y) \\
       e \; \frac{1}{2} (∂_z ∧ ∂_x - ∂_x ∧ ∂_z) \\
       f \; \frac{1}{2} (∂_x ∧ ∂_y - ∂_y ∧ ∂_x) \\
   \end{bmatrix}
   = \frac{1}{2} \begin{bmatrix}
       a \; ∂_t ∧ ∂_x - a \; ∂_x ∧ ∂_t) \\
       b \; ∂_t ∧ ∂_y - b \; ∂_y ∧ ∂_t) \\
       c \; ∂_t ∧ ∂_z - c \; ∂_z ∧ ∂_t) \\
       d \; ∂_y ∧ ∂_z - d \; ∂_z ∧ ∂_y) \\
       e \; ∂_z ∧ ∂_x - e \; ∂_x ∧ ∂_z) \\
       f \; ∂_x ∧ ∂_y - f \; ∂_y ∧ ∂_x) \\
   \end{bmatrix}

The free matrix representation permits to state the obvious, in that we can
rewrite the rotation with a row/column matrix representation:

.. topic:: The Doubly Contravariant Rotation Matrix

   .. math::

      R^{♯♯}= \frac{1}{2} \begin{bmatrix}
                           & + a \; ∂_t ∧ ∂_x & + b \; ∂_t ∧ ∂_y & + c \; ∂_t ∧ ∂_z \\
          - a \; ∂_x ∧ ∂_t &                  & + f \; ∂_x ∧ ∂_y & - e \; ∂_x ∧ ∂_z \\
          - b \; ∂_y ∧ ∂_t & - f \; ∂_y ∧ ∂_x &                  & + d \; ∂_y ∧ ∂_z \\
          - c \; ∂_z ∧ ∂_t & + e \; ∂_z ∧ ∂_x & - d \; ∂_z ∧ ∂_y &                  \\
      \end{bmatrix}

.. }}}

The :math:`♭♭` Rotation Tensor
------------------------------

.. {{{

Using :ref:`the Minkowski metric <the_minkowski_metric>`, we can flatten a basis
vector with the flat operator :math:`♭`:

.. math::

   (∂_μ)^♭ = η_{μν} dx^ν

And likewise flatten any index of the doubly contravariant wedge product:

.. math::

   \begin{matrix}
       (∂_μ ∧ ∂_ν)^{♭♯} &= η_{γμ} dx^γ ∧ ∂_ν         \\
       (∂_μ ∧ ∂_ν)^{♯♭} &= η_{γν} ∂_μ ∧ dx^γ         \\
       (∂_μ ∧ ∂_ν)^{♭♭} &= η_{δμ} η_{γν} dx^δ ∧ dx^γ \\
   \end{matrix}

To obtain the doubly covariant representation of rotations in spacetime, we
apply the flat operators to each components, :math:`R^{♭♭} = (R^{♯♯})^{♭♭}`:

.. topic:: Doubly Covariant Representation of Rotations in Minkowski Space

   .. math::

      R^{♭♭} = \left[ \begin{aligned}
          - & a \; dt ∧ dx \\
          - & b \; dt ∧ dy \\
          - & c \; dt ∧ dz \\
            & d \; dy ∧ dz \\
            & e \; dz ∧ dx \\
            & f \; dx ∧ dy \\
      \end{aligned} \right]

.. admonition:: Calculation Steps
   :class: dropdown

   .. {{{

   .. math::

      R^{♭♭} = \begin{bmatrix}
          a \; ∂_t ∧ ∂_x \\
          b \; ∂_t ∧ ∂_y \\
          c \; ∂_t ∧ ∂_z \\
          d \; ∂_y ∧ ∂_z \\
          e \; ∂_z ∧ ∂_x \\
          f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}^{♭♭}

   Distribute the flat operators :math:`♭`

   .. math::

      R^{♭♭} = \begin{bmatrix}
          a \; ∂_t^♭ ∧ ∂_x^♭ \\
          b \; ∂_t^♭ ∧ ∂_y^♭ \\
          c \; ∂_t^♭ ∧ ∂_z^♭ \\
          d \; ∂_y^♭ ∧ ∂_z^♭ \\
          e \; ∂_z^♭ ∧ ∂_x^♭ \\
          f \; ∂_x^♭ ∧ ∂_y^♭ \\
      \end{bmatrix}

   Expand:

   .. math::

      R^{♭♭} = \begin{bmatrix}
          a \; η_{tμ} d^μ ∧ η_{xμ} d^μ \\
          b \; η_{tμ} d^μ ∧ η_{yμ} d^μ \\
          c \; η_{tμ} d^μ ∧ η_{zμ} d^μ \\
          d \; η_{yμ} d^μ ∧ η_{zμ} d^μ \\
          e \; η_{zμ} d^μ ∧ η_{xμ} d^μ \\
          f \; η_{xμ} d^μ ∧ η_{yμ} d^μ \\
      \end{bmatrix}

   Identify non-zero terms:

   .. math::

      R^{♭♭} = \begin{bmatrix}
          a \; η_{tt} dt ∧ η_{xx} dx \\
          b \; η_{tt} dt ∧ η_{yy} dy \\
          c \; η_{tt} dt ∧ η_{zz} dz \\
          d \; η_{yy} dy ∧ η_{zz} dz \\
          e \; η_{zz} dz ∧ η_{xx} dx \\
          f \; η_{xx} dx ∧ η_{yy} dy \\
      \end{bmatrix}

   Apply numerical values:

   .. math::

      R^{♭♭} = \left[ \begin{aligned}
          - & a \; dt ∧ dx \\
          - & b \; dt ∧ dy \\
          - & c \; dt ∧ dz \\
            & d \; dy ∧ dz \\
            & e \; dz ∧ dx \\
            & f \; dx ∧ dy \\
      \end{aligned} \right]

   .. }}}

.. }}}

The :math:`♯♭` Rotation Tensor
------------------------------

.. {{{

In this section, I raise the indice using the free matrix notaion. The mixed
tensor is obtained by applying the flatternig operator :math:`\flat`:

.. math::

   B^{♯♭} = \begin{bmatrix}
       a \; ∂_t ∧ ∂_x \\
       b \; ∂_t ∧ ∂_y \\
       c \; ∂_t ∧ ∂_z \\
       d \; ∂_y ∧ ∂_z \\
       e \; ∂_z ∧ ∂_x \\
       f \; ∂_x ∧ ∂_y \\
   \end{bmatrix}^{♯♭}
   = \begin{bmatrix}
       - a \; ∂_t ∧ dx^x \\
       - b \; ∂_t ∧ dx^y \\
       - c \; ∂_t ∧ dx^z \\
       - d \; ∂_y ∧ dx^z \\
       - e \; ∂_z ∧ dx^x \\
       - f \; ∂_x ∧ dx^y \\
   \end{bmatrix}

.. admonition:: Calculation Steps
   :class: dropdown

   .. {{{

   Apply the musical operator :math:`♯♭`

   .. math::

      B^{♯♭} = \begin{bmatrix}
          a \; ∂_t ∧ ∂_x \\
          b \; ∂_t ∧ ∂_y \\
          c \; ∂_t ∧ ∂_z \\
          d \; ∂_y ∧ ∂_z \\
          e \; ∂_z ∧ ∂_x \\
          f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}^{♯♭}

   Distribute the musical operators to each matrix elements:

   .. math::

      B^{♯♭} = \begin{bmatrix}
          a \; (∂_t ∧ ∂_x)^{♯♭} \\
          b \; (∂_t ∧ ∂_y)^{♯♭} \\
          c \; (∂_t ∧ ∂_z)^{♯♭} \\
          d \; (∂_y ∧ ∂_z)^{♯♭} \\
          e \; (∂_z ∧ ∂_x)^{♯♭} \\
          f \; (∂_x ∧ ∂_y)^{♯♭} \\
      \end{bmatrix}

   Distribute the musical operators:

   .. math::

      B^{♯♭} = \begin{bmatrix}
        a \; (∂_t^♯ ∧ ∂_x^♭) \\
        b \; (∂_t^♯ ∧ ∂_y^♭) \\
        c \; (∂_t^♯ ∧ ∂_z^♭) \\
        d \; (∂_y^♯ ∧ ∂_z^♭) \\
        e \; (∂_z^♯ ∧ ∂_x^♭) \\
        f \; (∂_x^♯ ∧ ∂_y^♭) \\
      \end{bmatrix}

   Apply and expand:

   .. math::

      B^{♯♭} = \begin{bmatrix}
        a \; ∂_t ∧ η_{xγ} dx^γ \\
        b \; ∂_t ∧ η_{yγ} dx^γ \\
        c \; ∂_t ∧ η_{zγ} dx^γ \\
        d \; ∂_y ∧ η_{zγ} dx^γ \\
        e \; ∂_z ∧ η_{xγ} dx^γ \\
        f \; ∂_x ∧ η_{yγ} dx^γ \\
      \end{bmatrix}

   The metric tensor can be taken out due to mulilinearity:

   .. math::

      B^{♯♭} = \begin{bmatrix}
          a \; η_{xγ} ∂_t ∧ dx^γ \\
          b \; η_{yγ} ∂_t ∧ dx^γ \\
          c \; η_{zγ} ∂_t ∧ dx^γ \\
          d \; η_{zγ} ∂_y ∧ dx^γ \\
          e \; η_{xγ} ∂_z ∧ dx^γ \\
          f \; η_{yγ} ∂_x ∧ dx^γ \\
      \end{bmatrix}

   Most terms of the Minkowski metric are zero:

   .. math::

      B^{♯♭} = \begin{bmatrix}
          a \; η_{xx} ∂_t ∧ dx^x \\
          b \; η_{yy} ∂_t ∧ dx^y \\
          c \; η_{zz} ∂_t ∧ dx^z \\
          d \; η_{zz} ∂_y ∧ dx^z \\
          e \; η_{xx} ∂_z ∧ dx^x \\
          f \; η_{yy} ∂_x ∧ dx^y \\
      \end{bmatrix}

   Use the numerical values of the Minkowski metric:

   .. math::

      B^{♯♭} = \begin{bmatrix}
        - a \; ∂_t ∧ dx^x \\
        - b \; ∂_t ∧ dx^y \\
        - c \; ∂_t ∧ dx^z \\
        - d \; ∂_y ∧ dx^z \\
        - e \; ∂_z ∧ dx^x \\
        - f \; ∂_x ∧ dx^y \\
      \end{bmatrix}

   .. }}}

Taking into account the symetric property of :math:`∂_t ∧ dx^x`, :math:`∂_t
∧ dx^y`, and :math:`∂_t ∧ dx^z`, as well the antisymetric property of
:math:`∂_x ∧ dx^y`, :math:`∂_ey ∧ dx^z`, and :math:`∂_z ∧ dx^x`
demonstrated above, this results in:

.. math::

   B^{♯♭} = \frac{1}{2} \begin{bmatrix}
                         & - a \; ∂_t ∧ dx^x & - b \; ∂_t ∧ d^y & - c \; ∂_t ∧ dx^z \\
       - a \; ∂_x ∧ dx^t &                   & - f \; ∂_x ∧ d^y & + e \; ∂_x ∧ dx^z \\
       - b \; ∂_y ∧ dx^t & + f \; ∂_y ∧ dx^x &                  & - d \; ∂_y ∧ dx^z \\
       - c \; ∂_z ∧ dx^t & - e \; ∂_z ∧ dx^x & + d \; ∂_z ∧ d^y &                   \\
   \end{bmatrix}

.. }}}

The :math:`♭♯` Rotation Tensor
------------------------------

.. {{{

In this section, I flattne the first component using the :ref:`free matrix
representation <the_free_matrix_representation>`. The mixed tensor is obtained
by applying the flatternig operator :math:`\flat`:

.. math::

   B^{♭♯} = \begin{bmatrix}
       a \; ∂_t ∧ ∂_x \\
       b \; ∂_t ∧ ∂_y \\
       c \; ∂_t ∧ ∂_z \\
       d \; ∂_y ∧ ∂_z \\
       e \; ∂_z ∧ ∂_x \\
       f \; ∂_x ∧ ∂_y \\
   \end{bmatrix}^{♭♯}
   = \begin{bmatrix}
       + a \; dx^x ∧ ∂_t \\
       + b \; dx^y ∧ ∂_t \\
       + c \; dx^z ∧ ∂_t \\
       - d \; dx^z ∧ ∂_y \\
       - e \; dx^x ∧ ∂_z \\
       - f \; dx^y ∧ ∂_x \\
   \end{bmatrix}

.. admonition:: Calculation Steps
   :class: dropdown

   .. {{{

   Apply the musical operator :math:`♭♯`

   .. math::

      B^{♭♯} = \begin{bmatrix}
          a \; ∂_t ∧ ∂_x \\
          b \; ∂_t ∧ ∂_y \\
          c \; ∂_t ∧ ∂_z \\
          d \; ∂_y ∧ ∂_z \\
          e \; ∂_z ∧ ∂_x \\
          f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}^{♭♯}

   Distribute the musical operators to each matrix elements:

   .. math::

      B^{♭♯} = \begin{bmatrix}
        a \; (∂_t ∧ ∂_x)^{♭♯} \\
        b \; (∂_t ∧ ∂_y)^{♭♯} \\
        c \; (∂_t ∧ ∂_z)^{♭♯} \\
        d \; (∂_y ∧ ∂_z)^{♭♯} \\
        e \; (∂_z ∧ ∂_x)^{♭♯} \\
        f \; (∂_x ∧ ∂_y)^{♭♯} \\
      \end{bmatrix}

   Distribute the musical operators:

   .. math::

      B^{♭♯} = \begin{bmatrix}
        a \; (∂_t^♭ ∧ ∂_x^♯) \\
        b \; (∂_t^♭ ∧ ∂_y^♯) \\
        c \; (∂_t^♭ ∧ ∂_z^♯) \\
        d \; (∂_y^♭ ∧ ∂_z^♯) \\
        e \; (∂_z^♭ ∧ ∂_x^♯) \\
        f \; (∂_x^♭ ∧ ∂_y^♯) \\
      \end{bmatrix}

   Apply the musical operators:

   .. math::

      B^{♭♯} = \begin{bmatrix}
        a \; η_{tγ} dx^γ ∧ ∂_x^♯ \\
        b \; η_{tγ} dx^γ ∧ ∂_y^♯ \\
        c \; η_{tγ} dx^γ ∧ ∂_z^♯ \\
        d \; η_{yγ} dx^γ ∧ ∂_z^♯ \\
        e \; η_{zγ} dx^γ ∧ ∂_x^♯ \\
        f \; η_{xγ} dx^γ ∧ ∂_y^♯ \\
      \end{bmatrix}

   Identify the non-zero terms of the Minkowski metric:

   .. math::

      B^{♭♯} = \begin{bmatrix}
        a \; η_{tt} dx^t ∧ ∂_x \\
        b \; η_{tt} dx^t ∧ ∂_y \\
        c \; η_{tt} dx^t ∧ ∂_z \\
        d \; η_{yy} dx^y ∧ ∂_z \\
        e \; η_{zz} dx^z ∧ ∂_x \\
        f \; η_{xx} dx^x ∧ ∂_y \\
      \end{bmatrix}

   Use the numerical values of the Minkowski metric:

   .. math::

      B^{♭♯} = \begin{bmatrix}
        + a \; dx^t ∧ ∂_x \\
        + b \; dx^t ∧ ∂_y \\
        + c \; dx^t ∧ ∂_z \\
        - d \; dx^y ∧ ∂_z \\
        - e \; dx^z ∧ ∂_x \\
        - f \; dx^x ∧ ∂_y \\
      \end{bmatrix}

   .. }}}

Taking into account the symetric property of :math:`dx^t ∧ ∂_x`, :math:`dx^t
∧ ∂_y`, and :math:`dx^t ∧ ∂_z`, as well the antisymetric property of
:math:`dx^x ∧ ∂_y`, :math:`dx^y ∧ ∂_z`, and :math:`dx^z ∧ ∂_x`
demonstrated above, this results in:

.. math::

   B^{♭♯} = \frac{1}{2} \begin{bmatrix}
                         & + a \; dx^t ∧ ∂_x & + b \; dx^t ∧ ∂_y & + c \; dx^t ∧ ∂_z \\
       + a \; dx^x ∧ ∂_t &                   & + f \; dx^x ∧ ∂_y & - e \; dx^x ∧ ∂_z \\
       + b \; dx^y ∧ ∂_t & - f \; dx^y ∧ ∂_x &                   & + d \; dx^y ∧ ∂_z \\
       + c \; dx^z ∧ ∂_t & + e \; dx^z ∧ ∂_x & - d \; dx^z ∧ ∂_y &                   \\
   \end{bmatrix}

.. }}}

The :math:`\mathfrak{so}(1,3)` Lie Algebra of the Lorentz Group
---------------------------------------------------------------

.. {{{

We thus obtain triviall obtain the representation of the `Lorentz group
<https://en.m.wikipedia.org/wiki/Lorentz_group#Lie_algebra>`_.

.. math::

   B^{♯♭}= \frac{1}{2} \begin{bmatrix}
           & + a & + b & + c \\
       + a &     & + d & + f \\
       + b & - d &     & + e \\
       + c & - f & - e &     \\
   \end{bmatrix}

.. }}}

Symmetries of the Mixed Wedge Product
-------------------------------------

.. {{{

.. rubric:: Flattening the First Index

.. {{{

We apply the :math:`♭♯` operators to flatten the first index of each basis
bivectors:

.. math::

   (∂_t ∧ ∂_x)^{♭♯} &= + dx^t ∧ ∂_x \\
   (∂_t ∧ ∂_y)^{♭♯} &= + dx^t ∧ ∂_y \\
   (∂_t ∧ ∂_z)^{♭♯} &= + dx^t ∧ ∂_z \\
   (∂_y ∧ ∂_z)^{♭♯} &= - dx^y ∧ ∂_z \\
   (∂_z ∧ ∂_x)^{♭♯} &= - dx^z ∧ ∂_x \\
   (∂_x ∧ ∂_y)^{♭♯} &= - dx^x ∧ ∂_y \\

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Distribute the musical operators to their respective indices:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= (∂_t^♭ ∧ ∂_x^♯) \\
      (∂_t ∧ ∂_y)^{♭♯} &= (∂_t^♭ ∧ ∂_y^♯) \\
      (∂_t ∧ ∂_z)^{♭♯} &= (∂_t^♭ ∧ ∂_z^♯) \\
      (∂_x ∧ ∂_y)^{♭♯} &= (∂_x^♭ ∧ ∂_y^♯) \\
      (∂_y ∧ ∂_z)^{♭♯} &= (∂_y^♭ ∧ ∂_z^♯) \\
      (∂_z ∧ ∂_x)^{♭♯} &= (∂_z^♭ ∧ ∂_x^♯) \\

   Apply the musical operators:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= η_{tγ} dx^γ ∧ ∂_x \\
      (∂_t ∧ ∂_y)^{♭♯} &= η_{tγ} dx^γ ∧ ∂_y \\
      (∂_t ∧ ∂_z)^{♭♯} &= η_{tγ} dx^γ ∧ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &= η_{xγ} dx^γ ∧ ∂_y \\
      (∂_y ∧ ∂_z)^{♭♯} &= η_{yγ} dx^γ ∧ ∂_z \\
      (∂_z ∧ ∂_x)^{♭♯} &= η_{zγ} dx^γ ∧ ∂_x \\

   Identify the non-zero metric elements:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= η_{tt} dx^t ∧ ∂_x \\
      (∂_t ∧ ∂_y)^{♭♯} &= η_{tt} dx^t ∧ ∂_y \\
      (∂_t ∧ ∂_z)^{♭♯} &= η_{tt} dx^t ∧ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &= η_{xx} dx^x ∧ ∂_y \\
      (∂_y ∧ ∂_z)^{♭♯} &= η_{yy} dx^y ∧ ∂_z \\
      (∂_z ∧ ∂_x)^{♭♯} &= η_{zz} dx^z ∧ ∂_x \\

   Apply the numerical values:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= + dx^t ∧ ∂_x \\
      (∂_t ∧ ∂_y)^{♭♯} &= + dx^t ∧ ∂_y \\
      (∂_t ∧ ∂_z)^{♭♯} &= + dx^t ∧ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &= - dx^x ∧ ∂_y \\
      (∂_y ∧ ∂_z)^{♭♯} &= - dx^y ∧ ∂_z \\
      (∂_z ∧ ∂_x)^{♭♯} &= - dx^z ∧ ∂_x \\

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   (∂_t ∧ ∂_x)^{♭♯} &= + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
   (∂_t ∧ ∂_y)^{♭♯} &= + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
   (∂_t ∧ ∂_z)^{♭♯} &= + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
   (∂_y ∧ ∂_z)^{♭♯} &= - dx^y ⊗ ∂_z + dx^z ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♭♯} &= - dx^z ⊗ ∂_x + dx^x ⊗ ∂_z \\
   (∂_x ∧ ∂_y)^{♭♯} &= - dx^x ⊗ ∂_y + dx^y ⊗ ∂_x \\

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Expand wedge products to their tensor expressions:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= (∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t)^{♭♯} \\
      (∂_t ∧ ∂_y)^{♭♯} &= (∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t)^{♭♯} \\
      (∂_t ∧ ∂_z)^{♭♯} &= (∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t)^{♭♯} \\
      (∂_y ∧ ∂_z)^{♭♯} &= (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♭♯} \\
      (∂_z ∧ ∂_x)^{♭♯} &= (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♭♯} \\
      (∂_x ∧ ∂_y)^{♭♯} &= (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♭♯} \\

   Distribute the musical operators:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= (∂_t^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_t^♯) \\
      (∂_t ∧ ∂_y)^{♭♯} &= (∂_t^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_t^♯) \\
      (∂_t ∧ ∂_z)^{♭♯} &= (∂_t^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_t^♯) \\
      (∂_y ∧ ∂_z)^{♭♯} &= (∂_y^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_y^♯) \\
      (∂_z ∧ ∂_x)^{♭♯} &= (∂_z^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_z^♯) \\
      (∂_x ∧ ∂_y)^{♭♯} &= (∂_x^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_x^♯) \\

   Apply the musical operators:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= η_{tγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &= η_{tγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &= η_{tγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_t \\
      (∂_y ∧ ∂_z)^{♭♯} &= η_{yγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= η_{zγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &= η_{xγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_x \\

   Select non-zero metric elements:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= η_{tt} dx^t ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &= η_{tt} dx^t ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &= η_{tt} dx^t ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_t \\
      (∂_y ∧ ∂_z)^{♭♯} &= η_{yy} dx^y ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= η_{zz} dx^z ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &= η_{xx} dx^x ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_x \\

   Apply numerical values:

   .. math::

      (∂_t ∧ ∂_x)^{♭♯} &= + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &= + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &= + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
      (∂_y ∧ ∂_z)^{♭♯} &= - dx^y ⊗ ∂_z + dx^z ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &= - dx^z ⊗ ∂_x + dx^x ⊗ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &= - dx^x ⊗ ∂_y + dx^y ⊗ ∂_x \\

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   dx^t ∧ ∂_x &= + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
   dx^t ∧ ∂_y &= + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
   dx^t ∧ ∂_z &= + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
   dx^y ∧ ∂_z &= + dx^y ⊗ ∂_z - dx^z ⊗ ∂_y \\
   dx^z ∧ ∂_x &= + dx^z ⊗ ∂_x - dx^x ⊗ ∂_z \\
   dx^x ∧ ∂_y &= + dx^x ⊗ ∂_y - dx^y ⊗ ∂_x \\

.. }}}

.. rubric:: Flattening the Second Index

.. {{{

We apply the :math:`♯♭` operators to flatten the second index of each basis
bivectors and obtain:

.. math::

   (∂_t ∧ ∂_x)^{♯♭} &= - ∂_t ∧ dx^x \\
   (∂_t ∧ ∂_y)^{♯♭} &= - ∂_t ∧ dx^y \\
   (∂_t ∧ ∂_z)^{♯♭} &= - ∂_t ∧ dx^z \\
   (∂_y ∧ ∂_z)^{♯♭} &= - ∂_y ∧ dx^z \\
   (∂_z ∧ ∂_x)^{♯♭} &= - ∂_z ∧ dx^x \\
   (∂_x ∧ ∂_y)^{♯♭} &= - ∂_x ∧ dx^y \\

.. admonition:: All calculation steps
   :class: dropdown

   Distribute the musical operators:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= ∂_t^♯ ∧ ∂_x^♭ \\
      (∂_t ∧ ∂_y)^{♯♭} &= ∂_t^♯ ∧ ∂_y^♭ \\
      (∂_t ∧ ∂_z)^{♯♭} &= ∂_t^♯ ∧ ∂_z^♭ \\
      (∂_y ∧ ∂_z)^{♯♭} &= ∂_y^♯ ∧ ∂_z^♭ \\
      (∂_z ∧ ∂_x)^{♯♭} &= ∂_z^♯ ∧ ∂_x^♭ \\
      (∂_x ∧ ∂_y)^{♯♭} &= ∂_x^♯ ∧ ∂_y^♭ \\

   Apply the musical operators:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= ∂_t ∧ η_{xγ} dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &= ∂_t ∧ η_{yγ} dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &= ∂_t ∧ η_{zγ} dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ∧ η_{zγ} dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ∧ η_{xγ} dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ∧ η_{yγ} dx^γ \\

   Take out the metric components:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= η_{xγ} ∂_t ∧ dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &= η_{yγ} ∂_t ∧ dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &= η_{zγ} ∂_t ∧ dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &= η_{zγ} ∂_y ∧ dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &= η_{xγ} ∂_z ∧ dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &= η_{yγ} ∂_x ∧ dx^γ \\

   Identify the non-zero metric components:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= η_{xx} ∂_t ∧ dx^x \\
      (∂_t ∧ ∂_y)^{♯♭} &= η_{yy} ∂_t ∧ dx^y \\
      (∂_t ∧ ∂_z)^{♯♭} &= η_{zz} ∂_t ∧ dx^z \\
      (∂_y ∧ ∂_z)^{♯♭} &= η_{zz} ∂_y ∧ dx^z \\
      (∂_z ∧ ∂_x)^{♯♭} &= η_{xx} ∂_z ∧ dx^x \\
      (∂_x ∧ ∂_y)^{♯♭} &= η_{yy} ∂_x ∧ dx^y \\

   Apply numerical values:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= - ∂_t ∧ dx^x \\
      (∂_t ∧ ∂_y)^{♯♭} &= - ∂_t ∧ dx^y \\
      (∂_t ∧ ∂_z)^{♯♭} &= - ∂_t ∧ dx^z \\
      (∂_y ∧ ∂_z)^{♯♭} &= - ∂_y ∧ dx^z \\
      (∂_z ∧ ∂_x)^{♯♭} &= - ∂_z ∧ dx^x \\
      (∂_x ∧ ∂_y)^{♯♭} &= - ∂_x ∧ dx^y \\

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   (∂_t ∧ ∂_x)^{♯♭} &= - ∂_t ⊗ dx^x - ∂_x ⊗ dx^t \\
   (∂_t ∧ ∂_y)^{♯♭} &= - ∂_t ⊗ dx^y - ∂_y ⊗ dx^t \\
   (∂_t ∧ ∂_z)^{♯♭} &= - ∂_t ⊗ dx^z - ∂_z ⊗ dx^t \\
   (∂_y ∧ ∂_z)^{♯♭} &= - ∂_y ⊗ dx^z + ∂_z ⊗ dx^y \\
   (∂_z ∧ ∂_x)^{♯♭} &= - ∂_z ⊗ dx^x + ∂_x ⊗ dx^z \\
   (∂_x ∧ ∂_y)^{♯♭} &= - ∂_x ⊗ dx^y + ∂_y ⊗ dx^x \\

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Expand in terms of tensor product:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= (∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t)^{♯♭} \\
      (∂_t ∧ ∂_y)^{♯♭} &= (∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t)^{♯♭} \\
      (∂_t ∧ ∂_z)^{♯♭} &= (∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t)^{♯♭} \\
      (∂_y ∧ ∂_z)^{♯♭} &= (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♯♭} \\
      (∂_z ∧ ∂_x)^{♯♭} &= (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♯♭} \\
      (∂_x ∧ ∂_y)^{♯♭} &= (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♯♭} \\

   Distribute the flattening operator :math:`♭` to the second tensor component:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= (∂_t^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_t^♭) \\
      (∂_t ∧ ∂_y)^{♯♭} &= (∂_t^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_t^♭) \\
      (∂_t ∧ ∂_z)^{♯♭} &= (∂_t^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_t^♭) \\
      (∂_y ∧ ∂_z)^{♯♭} &= (∂_y^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_y^♭) \\
      (∂_z ∧ ∂_x)^{♯♭} &= (∂_z^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_z^♭) \\
      (∂_x ∧ ∂_y)^{♯♭} &= (∂_x^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_x^♭) \\

   Apply and expand:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= ∂_t ⊗ η_{xγ} dx^γ - η_{tγ} ∂_x ⊗ dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &= ∂_t ⊗ η_{yγ} dx^γ - η_{tγ} ∂_y ⊗ dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &= ∂_t ⊗ η_{zγ} dx^γ - η_{tγ} ∂_z ⊗ dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &= ∂_y ⊗ η_{zγ} dx^γ - η_{yγ} ∂_z ⊗ dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &= ∂_z ⊗ η_{xγ} dx^γ - η_{zγ} ∂_x ⊗ dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &= ∂_x ⊗ η_{yγ} dx^γ - η_{xγ} ∂_y ⊗ dx^γ \\

   Due to the linearity of the tensor product, the Minkowski metric components
   can be taken out in front of the expression:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= η_{xγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_x ⊗ dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &= η_{yγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_y ⊗ dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &= η_{zγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_z ⊗ dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &= η_{zγ} ∂_y ⊗ dx^γ - η_{yγ} ∂_z ⊗ dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &= η_{xγ} ∂_z ⊗ dx^γ - η_{zγ} ∂_x ⊗ dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &= η_{yγ} ∂_x ⊗ dx^γ - η_{xγ} ∂_y ⊗ dx^γ \\

   Identify the non-zero metric components:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= η_{xx} ∂_t ⊗ dx^x - η_{tt} ∂_ex ⊗ dx^t \\
      (∂_t ∧ ∂_y)^{♯♭} &= η_{yy} ∂_t ⊗ dx^y - η_{tt} ∂_ey ⊗ dx^t \\
      (∂_t ∧ ∂_z)^{♯♭} &= η_{zz} ∂_t ⊗ dx^z - η_{tt} ∂_ez ⊗ dx^t \\
      (∂_y ∧ ∂_z)^{♯♭} &= η_{zz} ∂_y ⊗ dx^z - η_{yy} ∂_ez ⊗ dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &= η_{xx} ∂_z ⊗ dx^x - η_{zz} ∂_ex ⊗ dx^z \\
      (∂_x ∧ ∂_y)^{♯♭} &= η_{yy} ∂_x ⊗ dx^y - η_{xx} ∂_ey ⊗ dx^x \\

   Apply numerical values:

   .. math::

      (∂_t ∧ ∂_x)^{♯♭} &= - ∂_t ⊗ dx^x - ∂_x ⊗ dx^t \\
      (∂_t ∧ ∂_y)^{♯♭} &= - ∂_t ⊗ dx^y - ∂_y ⊗ dx^t \\
      (∂_t ∧ ∂_z)^{♯♭} &= - ∂_t ⊗ dx^z - ∂_z ⊗ dx^t \\
      (∂_y ∧ ∂_z)^{♯♭} &= - ∂_y ⊗ dx^z + ∂_z ⊗ dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &= - ∂_z ⊗ dx^x + ∂_x ⊗ dx^z \\
      (∂_x ∧ ∂_y)^{♯♭} &= - ∂_x ⊗ dx^y + ∂_y ⊗ dx^x \\

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   ∂_t ∧ dx^x &= + ∂_t ⊗ dx^x + ∂_x ⊗ dx^t \\
   ∂_t ∧ dx^y &= + ∂_t ⊗ dx^y + ∂_y ⊗ dx^t \\
   ∂_t ∧ dx^z &= + ∂_t ⊗ dx^z + ∂_z ⊗ dx^t \\
   ∂_y ∧ dx^z &= + ∂_y ⊗ dx^z - ∂_z ⊗ dx^y \\
   ∂_z ∧ dx^x &= + ∂_z ⊗ dx^x - ∂_x ⊗ dx^z \\
   ∂_x ∧ dx^y &= + ∂_x ⊗ dx^y - ∂_y ⊗ dx^x \\

.. }}}

.. rubric:: Symmetries

.. {{{

From the flattening of the first and second indices, we identified the
expression of the mixed wedge product in terms of tensor products. We conclude
that not all elements of the mixed wedge product in Minkowski space are
antisymmetric. **The elements depending on time are symmetric**.

.. rubric:: Covariant-contravariant basis elements

================== =================================
Basis element      Expression
================== =================================
:math:`dx^t ∧ ∂_x` :math:`+ dx^t ⊗ ∂_x + dx^x ⊗ ∂_t`
:math:`dx^t ∧ ∂_y` :math:`+ dx^t ⊗ ∂_y + dx^y ⊗ ∂_t`
:math:`dx^t ∧ ∂_z` :math:`+ dx^t ⊗ ∂_z + dx^z ⊗ ∂_t`
:math:`dx^y ∧ ∂_z` :math:`+ dx^y ⊗ ∂_z - dx^z ⊗ ∂_y`
:math:`dx^z ∧ ∂_x` :math:`+ dx^z ⊗ ∂_x - dx^x ⊗ ∂_z`
:math:`dx^x ∧ ∂_y` :math:`+ dx^x ⊗ ∂_y - dx^y ⊗ ∂_x`
================== =================================

.. rubric:: Contravariant-covariant basis elements

================== =================================
Basis element      Expression
================== =================================
:math:`∂_t ∧ dx^x` :math:`+ ∂_t ⊗ dx^x + ∂_x ⊗ dx^t`
:math:`∂_t ∧ dx^y` :math:`+ ∂_t ⊗ dx^y + ∂_y ⊗ dx^t`
:math:`∂_t ∧ dx^z` :math:`+ ∂_t ⊗ dx^z + ∂_z ⊗ dx^t`
:math:`∂_y ∧ dx^z` :math:`+ ∂_y ⊗ dx^z - ∂_z ⊗ dx^y`
:math:`∂_z ∧ dx^x` :math:`+ ∂_z ⊗ dx^x - ∂_x ⊗ dx^z`
:math:`∂_x ∧ dx^y` :math:`+ ∂_x ⊗ dx^y - ∂_y ⊗ dx^x`
================== =================================

.. rubric:: Symmetries

Taken together, we get:

============ =================================
Symmetry     Basis elements
============ =================================
Symetric     :math:`dx^t ∧ ∂_x = + ∂_t ∧ dx^x`
Symetric     :math:`dx^t ∧ ∂_y = + ∂_t ∧ dx^y`
Symetric     :math:`dx^t ∧ ∂_z = + ∂_t ∧ dx^z`
Antisymetric :math:`dx^y ∧ ∂_z = - ∂_y ∧ dx^z`
Antisymetric :math:`dx^z ∧ ∂_x = - ∂_z ∧ dx^x`
Antisymetric :math:`dx^x ∧ ∂_y = - ∂_x ∧ dx^y`
============ =================================

.. }}}

.. }}}


