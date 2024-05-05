Experiment
==========


Testing keys

.. warning::

   Gathering thoughts together and experimenting.

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

Representing Contractions
=========================

.. {{{

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

.. }}}


Differential as a covector
==========================

.. {{{

The differential of a function is:

.. math::

   \begin{equation}
   df = dx \frac{∂f}{∂x} + dy \frac{∂f}{∂y} + dz \frac{∂f}{∂z}
   \end{equation}

That we rewrite with 

.. math::

   \begin{equation}
   df = dx \frac{∂}{∂x} f + dy \frac{∂}{∂y} f + dz \frac{∂}{∂z} f
   \end{equation}

Considering :math:`f(x, y, z)=x`:

.. math::

   \begin{equation}
   dx = dx \frac{∂}{∂x} x + dy \frac{∂}{∂y} x + dz \frac{∂}{∂z} x
   \end{equation}

And thus:

.. math::

   \begin{equation}
   dφ(x) = dx \frac{∂}{∂x} φ(x)
   \end{equation}

.. math::

   \begin{equation}
   dφ(x) = α dx
   \end{equation}

Taking the taylor serie of :math:`φ(x)`:

.. math::

   \begin{equation}
   φ(x) = φ(a) + x \frac{∂}{∂x} φ(x) + ...
   \end{equation}

We get:

.. math::

   \begin{equation}
   dφ(x) = dx \frac{∂}{∂x} [φ(a) + x \frac{∂}{∂x} φ(x)]
   \end{equation}

Then

.. math::

   \begin{equation}
   dφ(x) = dx \frac{∂}{∂x} [x α]
   \end{equation}

.. math::

   \begin{equation}
   dx = dx \frac{∂}{∂x} x
   \end{equation}

.. math::

   \begin{equation}
   dx \frac{∂}{∂x} = 1
   \end{equation}

.. math::

   \begin{equation}
   dx \frac{∂}{∂y} = 0
   \end{equation}

.. math::

   \begin{equation}
   dx \frac{∂}{∂z} = 0
   \end{equation}


.. math::

   \begin{equation}
   dx^i ∂_j = δ^i_j
   \end{equation}

.. }}}

Field Equations
===============

In this serie of articles, I translate the Field Equations of Mr. Einstein in
the Cartan-Hodge Formalism.

The Field Equations of Mr. Einstein
-----------------------------------

.. {{{

.. math::

   G_{μν} + Λ g_{μν} = κ T_{μν}

.. math::

   R_{μν} - \frac{1}{2} R g_{μν} + Λ g_{μν} = κ T_{μν}

.. math::

   dx ⊗ dy = \frac{1}{2} (dx ⊗ dy + dy ⊗ dx) + \frac{1}{2} (dx ⊗ dy - dy ⊗ dx)

.. }}}

Defining Symmetries
-------------------

.. {{{

The symmetric and antisymmetric parts are:

.. math::

   \begin{matrix}
   dx ∨ dy = (dx ⊗ dy + dy ⊗ dx) \\
   dx ∧ dy = (dx ⊗ dy - dy ⊗ dx) \\
   \end{matrix}

.. }}}

The Stress-Energy Tensor
------------------------

.. {{{

.. math::

   T^{♭♭} = \begin{bmatrix}
   T_g \; dt ∨ dt & T_a \; dt ∨ dx & T_b \; dt ∨ dy & T_c \; dt ∨ dz \\
                  & T_h \; dx ∨ dx & T_f \; dx ∨ dy & T_e \; dx ∨ dz \\
                  &                & T_i \; dy ∨ dy & T_d \; dy ∨ dz \\
                  &                &                & T_j \; dz ∨ dz \\
   \end{bmatrix}

.. math::

   T^{♭♭} = \begin{bmatrix}
   T_g \; dt ∨ dt & T_a \; dt ∨ dx \\
   T_h \; dx ∨ dx & T_b \; dt ∨ dy \\
   T_i \; dy ∨ dy & T_c \; dt ∨ dz \\
   T_j \; dz ∨ dz & T_d \; dy ∨ dz \\
                  & T_e \; dz ∨ dx \\
                  & T_f \; dx ∨ dy \\
   \end{bmatrix}

.. }}}

The Field Equations in Differential Form
----------------------------------------

.. {{{

.. math::

   \begin{bmatrix}
   R_g \; dt ∨ dt & R_a \; dt ∨ dx \\
   R_h \; dx ∨ dx & R_b \; dt ∨ dy \\
   R_i \; dy ∨ dy & R_c \; dt ∨ dz \\
   R_j \; dz ∨ dz & R_d \; dy ∨ dz \\
                  & R_e \; dz ∨ dx \\
                  & R_f \; dx ∨ dy \\
   \end{bmatrix}
   + (Λ  - \frac{1}{2} R) \begin{bmatrix}
   g_g \; dt ∨ dt & g_a \; dt ∨ dx \\
   g_h \; dx ∨ dx & g_b \; dt ∨ dy \\
   g_i \; dy ∨ dy & g_c \; dt ∨ dz \\
   g_j \; dz ∨ dz & g_d \; dy ∨ dz \\
                  & g_e \; dz ∨ dx \\
                  & g_f \; dx ∨ dy \\
   \end{bmatrix}
   = κ \begin{bmatrix}
   T_g \; dt ∨ dt & T_a \; dt ∨ dx \\
   T_h \; dx ∨ dx & T_b \; dt ∨ dy \\
   T_i \; dy ∨ dy & T_c \; dt ∨ dz \\
   T_j \; dz ∨ dz & T_d \; dy ∨ dz \\
                  & T_e \; dz ∨ dx \\
                  & T_f \; dx ∨ dy \\
   \end{bmatrix}

.. }}}
