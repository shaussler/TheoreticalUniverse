.. _the_minkowski_metric:

The Minkowski Metric
====================

We choose the metric signature :math:`(+, -, -, -)`. The only non-zero
components are the diagonal elements. The doubly contravariant and doubley
covariant Minkowski metric tensors are often (and unfortunately) represented in
matrix notation with the same object:

.. math::

   η =
   \begin{bmatrix}
     + 1 &  0 &  0 &  0 \\
       0 & -1 &  0 &  0 \\
       0 &  0 & -1 &  0 \\
       0 &  0 &  0 & -1 \\
   \end{bmatrix}

With :ref:`musical notation <musical_isomorphisms>` and :ref:`free matrix
representation <the_free_matrix_representation>`, we explicitely write the
metric tensor together with its basis:

.. math::

   \begin{equation}
   \eta^{♯♯} =
   \begin{bmatrix}
     + ∂_t ⊗ ∂_t &             &             &             \\
                 & - ∂_x ⊗ ∂_x &             &             \\
                 &             & - ∂_y ⊗ ∂_y &             \\
                 &             &             & - ∂_z ⊗ ∂_z \\
   \end{bmatrix}
   \end{equation}

Simply put and much more compactly:

.. math::

   \begin{equation}
   \eta^{♯♯} =
   \begin{bmatrix}
     + ∂_t ⊗ ∂_t \\
     - ∂_x ⊗ ∂_x \\
     - ∂_y ⊗ ∂_y \\
     - ∂_z ⊗ ∂_z \\
   \end{bmatrix}
   \end{equation}

Equivalently and with the same procedure and arguments, we express the doubly
covariant metric tensor with:

.. math::

   \begin{equation}
   \eta^{♭♭} =
   \begin{bmatrix}
     + dx^t ⊗ dx^t \\
     - dx^x ⊗ dx^x \\
     - dx^y ⊗ dx^y \\
     - dx^z ⊗ dx^z \\
   \end{bmatrix}
   \end{equation}

.. rubric:: Applying the metric to a vectors and covectors

We can flatten a basis vector with the flat operator :math:`♭`:

.. math::

   \begin{equation}
   (∂_μ)^♭ = η_{μν} dx^ν
   \end{equation}

Or sharpen a basis covector with the flat operator :math:`♯`:

.. math::

   \begin{equation}
   (dx^μ)^♭ = η^{μν} ∂_ν
   \end{equation}

.. rubric:: Applying the metric to wedge products of vectors and covectors

The indices of the wedge product can be sharpened or flattend at will:

.. math::

   \begin{equation}
   (∂_μ ∧ ∂_ν)^{♭♯} = η_{γμ} dx^γ ∧ ∂_ν
   \end{equation}

.. math::

   \begin{equation}
   (∂_μ ∧ ∂_ν)^{♯♭} = η_{γν} ∂_μ ∧ dx^γ
   \end{equation}

.. math::

   \begin{equation}
   (∂_μ ∧ ∂_ν)^{♭♭} = η_{δμ} η_{γν} dx^δ ∧ dx^γ
   \end{equation}

.. rubric:: Applying the metric to tensor products of vectors and covectors

The indices of the tensor product can be sharpened or flattend at will:

.. math::

   \begin{equation}
   (∂_μ ⊗ ∂_ν)^{♭♯} = η_{γμ} dx^γ ⊗ ∂_ν
   \end{equation}

.. math::

   \begin{equation}
   (∂_μ ⊗ ∂_ν)^{♯♭} = η_{γν} ∂_μ ⊗ dx^γ
   \end{equation}

.. math::

   \begin{equation}
   (∂_μ ⊗ ∂_ν)^{♭♭} = η_{δμ} η_{γν} dx^δ ⊗ dx^γ
   \end{equation}

.. warning:: Experimenting with notation to represent contraction

   .. math::
   
      \begin{equation}
      \begin{bmatrix} a \; ∂_t & b \; ∂_x & c \; ∂_y & d \; ∂_z \end{bmatrix}
      \begin{bmatrix}
        + dx^t ⊗ dx^t \\
        - dx^x ⊗ dx^x \\
        - dx^y ⊗ dx^y \\
        - dx^z ⊗ dx^z \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        + a \braket{∂_t|dx^t ⊗ dx^t} \\
        + b \braket{∂_x|dx^x ⊗ dx^x} \\
        + c \braket{∂_y|dx^y ⊗ dx^y} \\
        + d \braket{∂_z|dx^z ⊗ dx^z} \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        + a \braket{∂_t|dx^t} dx^t \\
        + b \braket{∂_x|dx^x} dx^x \\
        + c \braket{∂_y|dx^y} dx^y \\
        + d \braket{∂_z|dx^z} dx^z \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        + a dx^t \\
        - b dx^x \\
        - c dx^y \\
        - d dx^z \\
      \end{bmatrix}
      \end{equation}

