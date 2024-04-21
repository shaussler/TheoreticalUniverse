Experiment
==========

.. warning::

   Gathering thoughts together and experimenting.

On the Minkowski Metric
-----------------------

.. rubric:: Second in Frame of First

.. math::

   \begin{equation}
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
   \end{equation}

.. math::

   \begin{equation}
   P^{♯♯} =
   \begin{bmatrix}
     + a \; ∂_y ∧ ∂_z \\
     + b \; ∂_z ∧ ∂_x \\
     + c \; ∂_x ∧ ∂_y \\
   \end{bmatrix}
   , \;
   P^{♭♭} =
   \begin{bmatrix}
     + a \; dy ∧ dz \\
     + b \; dz ∧ dx \\
     + c \; dx ∧ dy \\
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

Assume:

.. math::

   \begin{equation}
   \begin{matrix}
   u = c \; x \\
   v = c \; y \\
   w = c \; z \\
   \end{matrix}
   \end{equation}

.. math::

   \begin{equation}
   Q^{♯♯} =
   \begin{bmatrix}
     + d \; ∂_v ∧ ∂_w \\
     + e \; ∂_w ∧ ∂_u \\
     + f \; ∂_u ∧ ∂_v \\
   \end{bmatrix}
   Q^{♭♭} =
   \begin{bmatrix}
     + d \; dv ∧ dw \\
     + e \; dw ∧ du \\
     + f \; du ∧ dv \\
   \end{bmatrix}
   \end{equation}

Notation to Represent Contraction
---------------------------------

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
