.. _the_minkowski_metric:

The Minkowski Metric
====================

.. rst-class:: custom-author

   by Stéphane Haussler

We choose the metric signature :math:`(+, -, -, -)`. The only non-zero
components are the diagonal elements. The doubly contravariant and doubley
covariant Minkowski metric tensors are often (and unfortunately) represented in
matrix notation with the same object:

.. math::

   η = \left[ \begin{alignedat}{1}
     + & 1 \quad&   & 0 \quad &  & 0 \quad  &   & 0 \\
       & 0 \quad& - & 1 \quad &  & 0 \quad  &   & 0 \\
       & 0 \quad&   & 0 \quad & -& 1 \quad  &   & 0 \\
       & 0 \quad&   & 0 \quad &  & 0 \quad  & - & 1 \\
   \end{alignedat} \right]

Using :ref:`musical <Musicality>` and :ref:`free matrix notation <The Free
Matrix Representation>`, we explicitely write the metric tensor together with
its basis:

.. math::

   η^{♯♯} = \left[ \begin{alignedat}{1}
     + ∂_t ⊗ ∂_t &             &             &             \\
                 & - ∂_x ⊗ ∂_x &             &             \\
                 &             & - ∂_y ⊗ ∂_y &             \\
                 &             &             & - ∂_z ⊗ ∂_z \\
   \end{alignedat} \right]

Which can be reduced to the much more compact form:

.. math::

   η^{♯♯} = \begin{bmatrix}
     + ∂_t ⊗ ∂_t \\
     - ∂_x ⊗ ∂_x \\
     - ∂_y ⊗ ∂_y \\
     - ∂_z ⊗ ∂_z \\
   \end{bmatrix}

Equivalently and with the same procedure and arguments, we express the doubly
covariant metric tensor with:

.. math::

   η^{♭♭} = \begin{bmatrix}
     + dx^t ⊗ dx^t \\
     - dx^x ⊗ dx^x \\
     - dx^y ⊗ dx^y \\
     - dx^z ⊗ dx^z \\
   \end{bmatrix}

.. rubric:: Applying the metric to a vectors and covectors

We can flatten a basis vector with the flat operator :math:`♭`:

.. math:: (∂_μ)^♭ = η_{μν} dx^ν

Or sharpen a basis covector with the flat operator :math:`♯`:

.. math:: (dx^μ)^♯ = η^{μν} ∂_ν

.. rubric:: Applying the metric to wedge products of vectors and covectors

The indices of the wedge product can be sharpened or flattend at will:

.. math:: (∂_μ ∧ ∂_ν)^{♭♯} = η_{γμ} dx^γ ∧ ∂_ν

.. math::

   (∂_μ ∧ ∂_ν)^{♯♭} = η_{γν} ∂_μ ∧ dx^γ

.. math::

   (∂_μ ∧ ∂_ν)^{♭♭} = η_{δμ} η_{γν} dx^δ ∧ dx^γ

.. rubric:: Applying the metric to tensor products of vectors and covectors

The indices of the tensor product can be sharpened or flattend at will:

.. math::

   (∂_μ ⊗ ∂_ν)^{♭♯} = η_{γμ} dx^γ ⊗ ∂_ν

.. math::

   (∂_μ ⊗ ∂_ν)^{♯♭} = η_{γν} ∂_μ ⊗ dx^γ

.. math::

   (∂_μ ⊗ ∂_ν)^{♭♭} = η_{δμ} η_{γν} dx^δ ⊗ dx^γ

.. ifconfig:: draft in ('yes')

   .. warning:: Draft content

   Generating the Minkowski Metric
   ===============================

   Tentatively trying to generate a space with mixed metric signature from
   to copies of :math:`\mathbb{R}^3`.

   Setting up the frames
   ---------------------

   .. {{{

   .. rubric:: Second in Frame of First

   .. math::

      p^♯ = \begin{bmatrix}
          x \; ∂_x \\
          y \; ∂_y \\
          z \; ∂_z \\
      \end{bmatrix}
      , \;
      p^♭ = \begin{bmatrix}
          x \; dx \\
          y \; dy \\
          z \; dz \\
      \end{bmatrix}

   .. math::

      \begin{equation}
      p^{♯♯} =
      \begin{bmatrix}
        + a \; ∂_y ∧ ∂_z \\
        + b \; ∂_z ∧ ∂_x \\
        + c \; ∂_x ∧ ∂_y \\
      \end{bmatrix}
      , \;
      p^{♭♭} =
      \begin{bmatrix}
        + a \; dy ∧ dz \\
        + b \; dz ∧ dx \\
        + c \; dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

   .. math::

      \begin{equation}
      p^{♯♯♯} =
      \begin{bmatrix}
        + l \; ∂_x ∧ ∂_y ∧ ∂_z \\
      \end{bmatrix}
      , \;
      p^{♭♭♭} =
      \begin{bmatrix}
        + l \; dx ∧ dy ∧ dz \\
      \end{bmatrix}
      \end{equation}

   .. rubric:: First in Frame of Second

   .. math::

      \begin{equation}
      q^♯ = \begin{bmatrix}
          u \; ∂_u \\
          v \; ∂_v \\
          w \; ∂_w \\
      \end{bmatrix}
      , \;
      q^♭ = \begin{bmatrix}
          u \; du \\
          v \; dv \\
          w \; dw \\
      \end{bmatrix}
      \end{equation}

   .. math::

      \begin{equation}
      q^{♯♯} =
      \begin{bmatrix}
        + d \; ∂_v ∧ ∂_w \\
        + e \; ∂_w ∧ ∂_u \\
        + f \; ∂_u ∧ ∂_v \\
      \end{bmatrix}
      q^{♭♭} =
      \begin{bmatrix}
        + d \; dv ∧ dw \\
        + e \; dw ∧ du \\
        + f \; du ∧ dv \\
      \end{bmatrix}
      \end{equation}

   .. math::

      \begin{equation}
      q^{♯♯♯} =
      \begin{bmatrix}
        + m \; ∂_u ∧ ∂_v ∧ w \\
      \end{bmatrix}
      q^{♭♭♭} =
      \begin{bmatrix}
        + m \; du ∧ dv ∧ dw \\
      \end{bmatrix}
      \end{equation}

   .. }}}

   Assumption
   ----------

   .. {{{

   Rationalizing the assumption that oneself is immobile in ones frame of
   reference, hence only the neighbor is moving. That is:

   * :math:`u=u(x)`
   * :math:`v=u(y)`
   * :math:`w=u(z)`

   For twisting, this is the same.

   .. math::

      \begin{equation}
      \begin{bmatrix}
      u = + c \; x \\
      v = + c \; y \\
      w = + c \; z \\
      \end{bmatrix}
      , \;
      \begin{bmatrix}
      d = - c \; a \\
      e = - c \; b \\
      f = - c \; c \\
      \end{bmatrix}
      , \;
      \begin{bmatrix}
      m = - c \; l \\
      \end{bmatrix}
      \end{equation}

   So now try:

   .. math::

      \begin{equation}
      q^♭ = \begin{bmatrix}
          c^2 x \; dx \\
          c^2 y \; dy \\
          c^2 z \; dz \\
      \end{bmatrix}
      \end{equation}

   .. math::

      \begin{equation}
      q^{♭♭} =
      \begin{bmatrix}
        - c^3 d \; dy ∧ dz \\
        - c^3 e \; dz ∧ dx \\
        - c^3 f \; dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

   .. math::

      \begin{equation}
      q^{♭♭♭} =
      \begin{bmatrix}
        - c^4 l \; dx ∧ dy ∧ dz \\
      \end{bmatrix}
      \end{equation}

   .. }}}
