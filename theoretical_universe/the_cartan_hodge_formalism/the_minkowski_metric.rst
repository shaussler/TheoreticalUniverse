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

   η = \begin{bmatrix}
       + 1 &  0 &  0 &  0 \\
         0 & -1 &  0 &  0 \\
         0 &  0 & -1 &  0 \\
         0 &  0 &  0 & -1 \\
   \end{bmatrix}

With :ref:`musical notation <musical_isomorphisms>` and :ref:`free matrix
representation <the_free_matrix_representation>`, we explicitely write the
metric tensor together with its basis:

.. math::

   \eta^{♯♯} = \begin{bmatrix}
       + ∂_t ⊗ ∂_t &             &             &             \\
                   & - ∂_x ⊗ ∂_x &             &             \\
                   &             & - ∂_y ⊗ ∂_y &             \\
                   &             &             & - ∂_z ⊗ ∂_z \\
   \end{bmatrix}

Simply put and much more compactly:

.. math::

   \eta^{♯♯} = \begin{bmatrix}
       + ∂_t ⊗ ∂_t \\
       - ∂_x ⊗ ∂_x \\
       - ∂_y ⊗ ∂_y \\
       - ∂_z ⊗ ∂_z \\
   \end{bmatrix}

Equivalently and with the same procedure and arguments, we express the doubly
covariant metric tensor with:

.. math::

   \eta^{♭♭} = \begin{bmatrix}
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
