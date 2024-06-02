.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

The Field Equations
===================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: Under construction

.. ifconfig:: draft in ('yes')

   .. warning:: Draft content

   In this serie of articles, I translate the Field Equations of Mr. Einstein in
   the Cartan-Hodge Formalism.

   The Rieman Curvature Tensor
   ---------------------------

   https://en.m.wikipedia.org/wiki/Curvature_form

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

