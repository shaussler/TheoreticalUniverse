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

Assumption
----------

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
