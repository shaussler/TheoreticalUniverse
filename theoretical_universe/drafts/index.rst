Drafts
======

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents:

   the_cartan_hodge_formalism/index.rst
   field_equations/index.rst

Rotations in Minkowski Space
----------------------------

:math:`SO(1,3)`
'''''''''''''''

.. warning:: Draft content

.. math:: R^{i}{}_j \; ∂_i ∧ dx^j

.. math:: \exp(X) = I + X + \frac{1}{2} X^2 + \frac{1}{6} X^3


.. math::

   R^{♯♭} = \begin{bmatrix}
     - a \; ∂_t ∧ dx \\
     - b \; ∂_t ∧ dy \\
     - c \; ∂_t ∧ dz \\
     - d \; ∂_y ∧ dz \\
     - e \; ∂_z ∧ dx \\
     - f \; ∂_x ∧ dy \\
   \end{bmatrix}

.. math::

   R^{♯♭} v^♯ = \begin{bmatrix}
     - a \; ∂_t ∧ dx \\
     - b \; ∂_t ∧ dy \\
     - c \; ∂_t ∧ dz \\
     - d \; ∂_y ∧ dz \\
     - e \; ∂_z ∧ dx \\
     - f \; ∂_x ∧ dy \\
   \end{bmatrix}
   \begin{bmatrix}
   t ∂_t \\
   x ∂_x \\
   y ∂_y \\
   z ∂_z \\
   \end{bmatrix}
   = \begin{bmatrix}
   -a\\
   \\
   \\
   \\
   \end{bmatrix}

This is a little bit of a problem because :math:`∂_t ∧ dx` is symmetric and one
should have a look at the tensor expression of the wedged expression.

.. math::

   \frac{1}{2} \begin{bmatrix}
                     & - a \; ∂_t ∧ dx & - b \; ∂_t ∧ dy & - c \; ∂_t ∧ dz \\
     - a \; ∂_x ∧ dt &                 & - f \; ∂_x ∧ dy & + e \; ∂_x ∧ dz \\
     - b \; ∂_y ∧ dt & + f \; ∂_y ∧ dx &                 & - d \; ∂_y ∧ dz \\
     - c \; ∂_z ∧ dt & - e \; ∂_z ∧ dx & + d \; ∂_z ∧ dy &                 \\
   \end{bmatrix}
   \begin{bmatrix}
   t ∂_t \\
   x ∂_x \\
   y ∂_y \\
   z ∂_z \\
   \end{bmatrix}

Using alternating forms:

.. math:: R^{♯♯} R^{♭♭} v^♯
.. math:: R^{♭♭} R^{♯♯} R^{♭♭} v^♯

.. math::

   R^{♯♯} = \begin{bmatrix}
     a \; ∂_t ∧ ∂_x \\
     b \; ∂_t ∧ ∂_y \\
     c \; ∂_t ∧ ∂_z \\
     d \; ∂_y ∧ ∂_z \\
     e \; ∂_z ∧ ∂_x \\
     f \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

.. math::

   R^{♭♭} = \left[ \begin{aligned}
     - & a \; dt ∧ dx \\
     - & b \; dt ∧ dy \\
     - & c \; dt ∧ dz \\
       & d \; dy ∧ dz \\
       & e \; dz ∧ dx \\
       & f \; dx ∧ dy \\
   \end{aligned} \right]

.. math::

   R^{♭♭} v^♯ = \left[ \begin{aligned}
     - & a \; dt ∧ dx \\
     - & b \; dt ∧ dy \\
     - & c \; dt ∧ dz \\
       & d \; dy ∧ dz \\
       & e \; dz ∧ dx \\
       & f \; dx ∧ dy \\
   \end{aligned} \right]
   \begin{bmatrix}
     t ∂_t \\
     x ∂_x \\
     y ∂_y \\
     z ∂_z \\
   \end{bmatrix}

.. math::

   R^{♭♭} v^♯ &= \begin{bmatrix}
     a \: \left( - dt ⊗ dx + dx \otimes dt \right) \\
     b \: \left( - dt ⊗ dy + dy \otimes dt \right) \\
     c \: \left( - dt ⊗ dz + dz \otimes dt \right) \\
     d \: \left( + dy ⊗ dz - dz \otimes dy \right) \\
     e \: \left( + dz ⊗ dx - dx \otimes dz \right) \\
     f \: \left( + dx ⊗ dy - dy \otimes dx \right) \\
   \end{bmatrix}
   \begin{bmatrix}
     t \: ∂_t \\
     x \: ∂_x \\
     y \: ∂_y \\
     z \: ∂_z \\
   \end{bmatrix}
   = \begin{bmatrix}
    + a t dx + b t dy + c t dz \\
    - a x dt + e x dz - f x dy \\
    - b y dt + f y dx - d y dz \\
    - c z dt + d z dy - e z dx \\
   \end{bmatrix} \\
   &= \begin{bmatrix}
             & + a t dx & + b t dy & + c t dz \\
    - a x dt &          & - f x dy & + e x dz \\
    - b y dt & + f y dx &          & - d y dz \\
    - c z dt & - e z dx & + d z dy &          \\
   \end{bmatrix} \\
   &= \left[ \begin{alignedat}{1}
     ( &   &     & - & a x & - & b y & - & c z & ) \: dt \\
     ( & + & a t &   &     & + & f y & - & e z & ) \: dx \\
     ( & + & b t & - & f x &   &     & + & d z & ) \: dy \\
     ( & + & c t & + & e x & - & d y &   &     & ) \: dz \\
   \end{alignedat} \right]

Squaring:

.. math::

   R^{♭♭} (R^{♭♭} v^♯)^♯ &= \begin{bmatrix}
     a \: \left( - dt ⊗ dx + dx \otimes dt \right) \\
     b \: \left( - dt ⊗ dy + dy \otimes dt \right) \\
     c \: \left( - dt ⊗ dz + dz \otimes dt \right) \\
     d \: \left( + dy ⊗ dz - dz \otimes dy \right) \\
     e \: \left( + dz ⊗ dx - dx \otimes dz \right) \\
     f \: \left( + dx ⊗ dy - dy \otimes dx \right) \\
   \end{bmatrix}
   \left[ \begin{alignedat}{1}
     ( &   &     & - & a x & - & b y & - & c z & ) \: dt \\
     ( & + & a t &   &     & + & f y & - & e z & ) \: dx \\
     ( & + & b t & - & f x &   &     & + & d z & ) \: dy \\
     ( & + & c t & + & e x & - & d y &   &     & ) \: dz \\
   \end{alignedat} \right]^♯

.. math::

   R^{♭♭} (R^{♭♭} v^♯)^♯ &= \begin{bmatrix}
     a \: \left( - dt ⊗ dx + dx \otimes dt \right) \\
     b \: \left( - dt ⊗ dy + dy \otimes dt \right) \\
     c \: \left( - dt ⊗ dz + dz \otimes dt \right) \\
     d \: \left( + dy ⊗ dz - dz \otimes dy \right) \\
     e \: \left( + dz ⊗ dx - dx \otimes dz \right) \\
     f \: \left( + dx ⊗ dy - dy \otimes dx \right) \\
   \end{bmatrix}
   \left[ \begin{alignedat}{1}
     ( &   &     & - & a x & - & b y & - & c z & ) \: ∂_t \\
     ( & - & a t &   &     & - & f y & + & e z & ) \: ∂_x \\
     ( & - & b t & + & f x &   &     & - & d z & ) \: ∂_y \\
     ( & - & c t & - & e x & + & d y &   &     & ) \: ∂_z \\
   \end{alignedat} \right] \\
   &= \left[ \begin{alignedat}{1}
     (         - a a x - a b y - a c z ) \: dx \\
     (         - b a x - b b y - b c z ) \: dy \\
     (         - c a x - c b y - c c z ) \: dz \\
     ( + a a t         + a f y - a e z ) \: dt \\
     ( - e a t         - e f y + e e z ) \: dz \\
     ( + f a t         + f f y - f e z ) \: dy \\
     ( - b t + f x           - d z   ) \: ∂_y \\
     ( - c t - e x +   d y           ) \: ∂_z \\
   \end{alignedat} \right]





