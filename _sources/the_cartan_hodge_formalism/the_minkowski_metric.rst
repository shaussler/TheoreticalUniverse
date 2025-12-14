.. Theoretical Universe (c) by Stéphane Haussler

.. theoretical universe is licensed under a creative commons attribution 4.0
.. international license. you should have received a copy of the license along
.. with this work. if not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _the_minkowski_metric:

Minkowski metric
================

.. rst-class:: custom-author

   by Stéphane Haussler

.. {{{

The Minkowski metric describes a four-dimensional flat spacetime, in contrast
to the curved spacetime of general relativity. Concretely, the doubly covariant
metric tensor is calculated using the dot product of all basis vectors
:math:`∂_μ \cdot ∂_ν = g_{μν}`. It is described by a matrix where temporal and
spatial components are distinguished by their signs. For flat spacetime the
metric tensor :math:`g` is noted :math:`η`. In that case, the only non-zero
components of the matrix representation are the diagonal elements. The
components are either :math:`+1` for time, or :math:`-1` for space, thereby
using metric signature :math:`(+, -, -, -)`. The metric tensor for
four-dimensional Minkowski space is often represented by the same matrix for
both contravariant and covariant forms:

.. math::

   η = \left[ \begin{alignedat}{6}
       + & 1 \quad&   & 0 \quad &  & 0 \quad  &   & 0 \\
         & 0 \quad& - & 1 \quad &  & 0 \quad  &   & 0 \\
         & 0 \quad&   & 0 \quad & -& 1 \quad  &   & 0 \\
         & 0 \quad&   & 0 \quad &  & 0 \quad  & - & 1 \\
   \end{alignedat} \right]

The drawback of this notation is that the metric tensor is given either in
doubly covariant form :math:`η_{μν}`, or doubly contravariant form
:math:`η^{μν}`, both represented by the same matrix following the `row-major
convention <https://en.m.wikipedia.org/wiki/Row-_and_column-major_order>`_.
This row/column representation does not necessarily adhere to standard matrix
multiplication rules but often does because the non-diagonal elements are zero!
To strictly follow matrix multiplication rules, we need an object that takes in
a contravariant vector :math:`v^{μ}` and outputs a contravariant vector
:math:`v^{μ}`. Concretely, we would need a mixed covariant-contravariant
:math:`η^{μ}{}_{ν}` tensor. Using :ref:`musical notation<Musicality>` and
:ref:`the free matrix representation <The Free Matrix Representation>`, we can
resolve this by explicitly expressing the metric tensor with its basis, making
the zero elements unnecessary:

.. math::

   η^{♯♯} = \left[ \begin{alignedat}{3}
     + ∂_t ⊗ ∂_t &             &             &             \\
                 & - ∂_x ⊗ ∂_x &             &             \\
                 &             & - ∂_y ⊗ ∂_y &             \\
                 &             &             & - ∂_z ⊗ ∂_z \\
   \end{alignedat} \right]

We can then reduce the representation to the much more compact form:

.. math::

   η^{♯♯} = \left[ \begin{alignedat}{3}
       + & \, ∂_t & \, ⊗ & \, ∂_t \\
       - & \, ∂_x & \, ⊗ & \, ∂_x \\
       - & \, ∂_y & \, ⊗ & \, ∂_y \\
       - & \, ∂_z & \, ⊗ & \, ∂_z \\
   \end{alignedat} \right]

Equivalently and with the same procedure, we express the doubly covariant
metric tensor with:

.. math::

   η^{♭♭} = \left[ \begin{alignedat}{3}
       + & \, dt & \, ⊗ & \, dt \\
       - & \, dx & \, ⊗ & \, dx \\
       - & \, dy & \, ⊗ & \, dy \\
       - & \, dz & \, ⊗ & \, dz \\
   \end{alignedat} \right]

.. rubric:: Applying the metric to a vectors and covectors

We can flatten a basis vector with the flat operator :math:`♭`:

.. math:: (∂_μ)^♭ = η_{μν} dx^ν

Or sharpen a basis covector with the flat operator :math:`♯`:

.. math:: (dx^μ)^♯ = η^{μν} ∂_ν

.. rubric:: Applying the metric to exterior product of vectors and covectors

The musicality of exterior products can also be sharpened or flattened. The
steps are:

* Distribute the musical operators.
* Apply the musical operators.
* Use linearity to reorder numerical components to the front of the expressions.

.. math::

   (∂_μ ∧ ∂_ν)^{♭♯} = (∂_μ)^♭ ∧ (∂_ν)^♯
                    = (η_{γμ} dx^γ) ∧ ∂_ν
                    = η_{γμ} dx^γ ∧ ∂_ν

.. math::

   (∂_μ ∧ ∂_ν)^{♯♭} = (∂_μ)^♯ ∧ (∂_μ)^♭
                    = ∂_μ ∧ (η_{γν} dx^γ)\
                    = η_{γν} ∂_μ ∧ dx^γ

.. math::

   (∂_μ ∧ ∂_ν)^{♭♭} = (∂_μ)^♭ ∧ (∂_ν)^♭
                    = (η_{δμ} dx^δ) ∧ (η_{γν} dx^γ)
                    = η_{δμ} η_{γν} dx^δ ∧ dx^γ

.. rubric:: Applying the metric to tensor products of vectors and covectors

Following the same steps as for the exterior product, the musicality of the
tensor product can also be sharpened or flattend:

.. math::

   (∂_μ ⊗ ∂_ν)^{♭♯} = (∂_μ)^♭ ⊗ (∂_ν)^♯
                    = (η_{γμ} dx^γ) ⊗ ∂_ν
                    = η_{γμ} dx^γ ⊗ ∂_ν

.. math::

   (∂_μ ⊗ ∂_ν)^{♯♭} = (∂_μ)^♯ ⊗ (∂_ν)^♭
                    = ∂_μ ⊗ (η_{γν} dx^γ)
                    = η_{γν} ∂_μ ⊗ dx^γ

.. math::

   (∂_μ ⊗ ∂_ν)^{♭♭} = (∂_μ)^♭ ⊗ (∂_ν)^♭
                    = (η_{δμ} dx^δ) ⊗ (η_{γν} dx^γ)
                    = η_{δμ} η_{γν} dx^δ ⊗ dx^γ

.. }}}
