.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _The Exterior Derivative of Rotations in Spacetime:
.. _the exterior derivative or rotations in spacetime:

2--forms (rotations) in Minkowski space
=======================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. {{{

This article investigates the exterior derivative of :ref:`rotations expressed
in differential form <Rotations in Minkowski Space>`. We employ :ref:`the
Cartan-Hodge formalism <the_cartan_hodge_formalism>` within the context of
Minkowski spacetime. Following the systematic calculations presented in this
article, I demonstrate in :ref:`Of Maxwell Equations and Rotations
<of_maxwell_equations_and_rotations>` that a twist in spacetime leads to the
equations governing electromagnetism.

While the concept might not be entirely novel, I have not yet encountered some
of my observations elsewhere. If you are aware of relevant references, feel free
to open an issue and I will include them. I you identify any errors, you can
either open an issue, or directly submit corrections via a merge request to my
GitHub repository: `Theoretical Universe
<https://github.com/shaussler/TheoreticalUniverse/>`_.

.. }}}

Rotations
---------

.. {{{

Rotations in spacetime can occur in six independent planes. Any rotation can be
decomposed into a linear combination of basis rotations within each plane:

.. math::

   R^{♯♯} = \begin{bmatrix}
       Q^x \; ∂_t ∧ ∂_x \\
       Q^y \; ∂_t ∧ ∂_y \\
       Q^z \; ∂_t ∧ ∂_z \\
       R^x \; ∂_y ∧ ∂_z \\
       R^y \; ∂_z ∧ ∂_x \\
       R^z \; ∂_x ∧ ∂_y \\
   \end{bmatrix}

The generic rotation above is doubly contravariant, given in terms of the wedge
product :math:`∧` of vectors corresponding to our physical understanding of
space (and time). By fully flattening, we obtain the associated doubly
covariant differential 2-form representative of the rotation:

.. math::

   R^{♭♭} = \left[ \begin{aligned}
       - & Q^x \; dt ∧ dx \\
       - & Q^y \; dt ∧ dy \\
       - & Q^z \; dt ∧ dz \\
         & R^x \; dy ∧ dz \\
         & R^y \; dz ∧ dx \\
         & R^z \; dx ∧ dy \\
   \end{aligned} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{za

   .. rubric:: Flatten the rotation

   .. math:: R^{♭♭} = (R^{♯♯})^{♭♭}

   .. rubric:: Expand and distribute the flat operator

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; ∂_t^♭ ∧ ∂_x^♭ \\
          Q^y \; ∂_t^♭ ∧ ∂_y^♭ \\
          Q^z \; ∂_t^♭ ∧ ∂_z^♭ \\
          R^x \; ∂_y^♭ ∧ ∂_z^♭ \\
          R^y \; ∂_z^♭ ∧ ∂_x^♭ \\
          R^z \; ∂_x^♭ ∧ ∂_y^♭ \\
      \end{bmatrix}

   .. rubric:: Expand with the Minkowski metric

   .. math::

      R^{♭♭} = \begin{bmatrix}
        Q^x \; η_{αt} \; dx^α ∧ η_{βx} \; dx^β \\
        Q^y \; η_{αt} \; dx^α ∧ η_{βy} \; dx^β \\
        Q^z \; η_{αt} \; dx^α ∧ η_{βz} \; dx^β \\
        R^x \; η_{αy} \; dx^α ∧ η_{βz} \; dx^β \\
        R^y \; η_{αz} \; dx^α ∧ η_{βx} \; dx^β \\
        R^z \; η_{αx} \; dx^α ∧ η_{βy} \; dx^β \\
      \end{bmatrix}

   The exterior product :math:`∧` is bilinear. The Minkowski metric components
   :math:`η`'s can be taken in front of the expression:

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; η_{αt} η_{βx} \; dx^α ∧ dx^β \\
          Q^y \; η_{αt} η_{βy} \; dx^α ∧ dx^β \\
          Q^z \; η_{αt} η_{βz} \; dx^α ∧ dx^β \\
          R^x \; η_{αy} η_{βz} \; dx^α ∧ dx^β \\
          R^y \; η_{αz} η_{βx} \; dx^α ∧ dx^β \\
          R^z \; η_{αx} η_{βy} \; dx^α ∧ dx^β \\
      \end{bmatrix}

   .. rubric:: Identify the non-zero components of the Minkowski metric

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; η_{tt} η_{xx} \; dx^t ∧ dx^x \\
          Q^y \; η_{tt} η_{yy} \; dx^t ∧ dx^y \\
          Q^z \; η_{tt} η_{zz} \; dx^t ∧ dx^z \\
          R^x \; η_{yy} η_{zz} \; dx^y ∧ dx^z \\
          R^y \; η_{zz} η_{xx} \; dx^z ∧ dx^x \\
          R^z \; η_{xx} η_{yy} \; dx^x ∧ dx^y \\
      \end{bmatrix}

   .. rubric:: Rewrite

   For readability, replace the :math:`dx^μ` symbols by their explicit
   expressions:

   .. math::

      dx^t &= dt \\
      dx^x &= dx \\
      dx^y &= dy \\
      dx^z &= dz

   We obtain:

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; η_{tt} η_{xx} \; dt ∧ dx \\
          Q^y \; η_{tt} η_{yy} \; dt ∧ dy \\
          Q^z \; η_{tt} η_{zz} \; dt ∧ dz \\
          R^x \; η_{yy} η_{zz} \; dy ∧ dz \\
          R^y \; η_{zz} η_{xx} \; dz ∧ dx \\
          R^z \; η_{xx} η_{yy} \; dx ∧ dy \\
      \end{bmatrix}

   .. rubric:: Apply the numerical values of the Minkowski metric components

   .. math::

      R^{♭♭} = \begin{bmatrix}
          Q^x \; (+1) (-1) \; dt ∧ dx \\
          Q^y \; (+1) (-1) \; dt ∧ dy \\
          Q^z \; (+1) (-1) \; dt ∧ dz \\
          R^x \; (-1) (-1) \; dy ∧ dz \\
          R^y \; (-1) (-1) \; dz ∧ dx \\
          R^z \; (-1) (-1) \; dx ∧ dy \\
      \end{bmatrix}

   .. rubric:: Conclude

   .. math::

      R^{♭♭} = \left[ \begin{aligned}
          - & Q^x \; dt ∧ dx \\
          - & Q^y \; dt ∧ dy \\
          - & Q^z \; dt ∧ dz \\
            & R^x \; dy ∧ dz \\
            & R^y \; dz ∧ dx \\
            & R^z \; dx ∧ dy \\
      \end{aligned} \right]

   .. }}}

.. }}}

:math:`⋆ R^{♭♭}`
----------------

.. {{{

Applying the Hodge star to the rotation 2-form, we obtain:

.. math::

   ⋆ R^{♭♭} = \left[ \begin{aligned}
       & Q^x \; dy ∧ dz \\
       & Q^y \; dz ∧ dx \\
       & Q^z \; dx ∧ dy \\
       & R^x \; dt ∧ dx \\
       & R^y \; dt ∧ dy \\
       & R^z \; dt ∧ dz \\
   \end{aligned} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the Hodge star by linearity

   .. math::

      ⋆ R^{♭♭} = ⋆ \left[ \begin{aligned}
          - & Q^x \; dt ∧ dx \\
          - & Q^y \; dt ∧ dy \\
          - & Q^z \; dt ∧ dz \\
            & R^x \; dy ∧ dz \\
            & R^y \; dz ∧ dx \\
            & R^z \; dx ∧ dy \\
      \end{aligned} \right]
      = \left[ \begin{aligned}
          - & Q^x \; ⋆ dt ∧ dx \\
          - & Q^y \; ⋆ dt ∧ dy \\
          - & Q^z \; ⋆ dt ∧ dz \\
            & R^x \; ⋆ dy ∧ dz \\
            & R^y \; ⋆ dz ∧ dx \\
            & R^z \; ⋆ dx ∧ dy \\
      \end{aligned} \right]

   .. rubric:: Apply the Hodge star to the basis 2-Forms

   Using the :ref:`tables for the Hodge dual <Hodge dual tables>`:

   .. math::

      ⋆ R^{♭♭} = \left[ \begin{aligned}
          & Q^x \; dy ∧ dz \\
          & Q^y \; dz ∧ dx \\
          & Q^z \; dx ∧ dy \\
          & R^x \; dt ∧ dx \\
          & R^y \; dt ∧ dy \\
          & R^z \; dt ∧ dz \\
      \end{aligned} \right]

   .. }}}

.. }}}

:math:`d R^{♭♭}`
----------------

.. {{{

Apply the exterior derivative to the rotation 2-form, we obtain:

.. math::

   dR^{♭♭} = \left[ \begin{alignedat}{5}
     (&         & + ∂_x R^x & + ∂_y R^y & + ∂_z R^z &\:) \; dx^x ∧ dx^y ∧ dx^z \\
     (& + ∂_t R^x &         & + ∂_y Q^z & - ∂_z Q^y &\:) \; dx^t ∧ dx^y ∧ dx^z \\
     (& + ∂_t R^y & - ∂_x Q^z &         & + ∂_z Q^x &\:) \; dx^t ∧ dx^z ∧ dx^x \\
     (& + ∂_t R^z & + ∂_x Q^y & - ∂_y Q^x &         &\:) \; dx^t ∧ dx^x ∧ dx^y \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Distribute the exterior derivative

   .. math::

      dR^{♭♭} = \begin{bmatrix}
         d( - Q^x \; dt ∧ dx ) \\
         d( - Q^y \; dt ∧ dy ) \\
         d( - Q^z \; dt ∧ dz ) \\
         d( + R^x \; dy ∧ dz ) \\
         d( + R^y \; dz ∧ dx ) \\
         d( + R^z \; dx ∧ dy ) \\
      \end{bmatrix}

   .. rubric:: Apply the exterior derivative

   .. math::

      dR^{♭♭} = \left[ \begin{alignedat}{3}
          ∂_y (- Q^x ) \; & dy ∧ dt ∧ dx & + & ∂_z (- Q^x ) \; & dz ∧ dt ∧ dx \\
          ∂_x (- Q^y ) \; & dx ∧ dt ∧ dy & + & ∂_z (- Q^y ) \; & dz ∧ dt ∧ dy \\
          ∂_x (- Q^z ) \; & dx ∧ dt ∧ dz & + & ∂_y (- Q^z ) \; & dy ∧ dt ∧ dz \\
          ∂_t (+ R^x ) \; & dt ∧ dy ∧ dz & + & ∂_x (+ R^x ) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ R^y ) \; & dt ∧ dz ∧ dx & + & ∂_y (+ R^y ) \; & dy ∧ dz ∧ dx \\
          ∂_t (+ R^z ) \; & dt ∧ dx ∧ dy & + & ∂_z (+ R^z ) \; & dz ∧ dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Reorder the exterior products

   .. math::

      dR^{♭♭} = \left[ \begin{alignedat}{3}
          ∂_y (- Q^x )(+1) \; & dt ∧ dx ∧ dy & + & ∂_z (- Q^x )(-1) \; & dt ∧ dz ∧ dx \\
          ∂_x (- Q^y )(-1) \; & dt ∧ dx ∧ dy & + & ∂_z (- Q^y )(+1) \; & dt ∧ dy ∧ dz \\
          ∂_x (- Q^z )(+1) \; & dt ∧ dz ∧ dx & + & ∂_y (- Q^z )(-1) \; & dt ∧ dy ∧ dz \\
          ∂_t (+ R^x )(+1) \; & dt ∧ dy ∧ dz & + & ∂_x (+ R^x )(+1) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ R^y )(+1) \; & dt ∧ dz ∧ dx & + & ∂_y (+ R^y )(+1) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ R^z )(+1) \; & dt ∧ dx ∧ dy & + & ∂_z (+ R^z )(+1) \; & dx ∧ dy ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Simplify

   .. math::

      dR^{♭♭} = \left[ \begin{alignedat}{3}
          ∂_y (- Q^x ) \; & dt ∧ dx ∧ dy & + & ∂_z (+ Q^x ) \; & dt ∧ dz ∧ dx \\
          ∂_x (+ Q^y ) \; & dt ∧ dx ∧ dy & + & ∂_z (- Q^y ) \; & dt ∧ dy ∧ dz \\
          ∂_x (- Q^z ) \; & dt ∧ dz ∧ dx & + & ∂_y (+ Q^z ) \; & dt ∧ dy ∧ dz \\
          ∂_t (+ R^x ) \; & dt ∧ dy ∧ dz & + & ∂_x (+ R^x ) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ R^y ) \; & dt ∧ dz ∧ dx & + & ∂_y (+ R^y ) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ R^z ) \; & dt ∧ dx ∧ dy & + & ∂_z (+ R^z ) \; & dx ∧ dy ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      dR^{♭♭} = \left[ \begin{alignedat}{5}
        (&         & + ∂_x R^x & + ∂_y R^y & + ∂_z R^z &\:) \; dx^x ∧ dx^y ∧ dx^z \\
        (& + ∂_t R^x &         & + ∂_y Q^z & - ∂_z Q^y &\:) \; dx^t ∧ dx^y ∧ dx^z \\
        (& + ∂_t R^y & - ∂_x Q^z &         & + ∂_z Q^x &\:) \; dx^t ∧ dx^z ∧ dx^x \\
        (& + ∂_t R^z & + ∂_x Q^y & - ∂_y Q^x &         &\:) \; dx^t ∧ dx^x ∧ dx^y \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`d⋆ R^{♭♭}`
-----------------

.. {{{

Applying in sequence the exterior derivative and the Hodge star operator to the
rotation 2-form, we obtain:

.. math::

   d( ⋆ R^{♭♭} ) = \left[ \begin{alignedat}{5}
     (&         & + ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z &\:) \; dx ∧ dy ∧ dz \\
     (& + ∂_t Q^x &         & - ∂_y R^z & + ∂_z R^y &\:) \; dt ∧ dy ∧ dz \\
     (& + ∂_t Q^y & + ∂_x R^z &         & - ∂_z R^x &\:) \; dt ∧ dz ∧ dx \\
     (& + ∂_t Q^z & - ∂_x R^y & + ∂_y R^x &         &\:) \; dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Take the exterior derivative

   .. math::

      d⋆R^{♭♭} = d \begin{bmatrix}
          Q^x \; dy ∧ dz \\
          Q^y \; dz ∧ dx \\
          Q^z \; dx ∧ dy \\
          R^x \; dt ∧ dx \\
          R^y \; dt ∧ dy \\
          R^z \; dt ∧ dz \\
      \end{bmatrix}

   .. rubric:: Distribute the exterior derivative

   .. math::

      d⋆R^{♭♭} = \begin{bmatrix}
          d( Q^x \; dy ∧ dz) \\
          d( Q^y \; dz ∧ dx) \\
          d( Q^z \; dx ∧ dy) \\
          d( R^x \; dt ∧ dx) \\
          d( R^y \; dt ∧ dy) \\
          d( R^z \; dt ∧ dz) \\
      \end{bmatrix}

   .. rubric:: Apply

   .. math::

      d⋆R^{♭♭})= \left[ \begin{alignedat}{5}
          ∂_t (+ Q^x ) \; & dt ∧ dy ∧ dz & + & ∂_x (+ Q^x ) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ Q^y ) \; & dt ∧ dz ∧ dx & + & ∂_y (+ Q^y ) \; & dy ∧ dz ∧ dx \\
          ∂_t (+ Q^z ) \; & dt ∧ dx ∧ dy & + & ∂_z (+ Q^z ) \; & dz ∧ dx ∧ dy \\
          ∂_y (+ R^x ) \; & dy ∧ dt ∧ dx & + & ∂_z (+ R^x ) \; & dz ∧ dt ∧ dx \\
          ∂_x (+ R^y ) \; & dx ∧ dt ∧ dy & + & ∂_z (+ R^y ) \; & dz ∧ dt ∧ dy \\
          ∂_x (+ R^z ) \; & dx ∧ dt ∧ dz & + & ∂_y (+ R^z ) \; & dy ∧ dt ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Reorder

   .. math::

      d⋆R^{♭♭} = \left[ \begin{alignedat}{5}
          ∂_t (+ Q^x )(+1) \; & dt ∧ dy ∧ dz & + & ∂_x (+ Q^x )(+1) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ Q^y )(+1) \; & dt ∧ dz ∧ dx & + & ∂_y (+ Q^y )(+1) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ Q^z )(+1) \; & dt ∧ dx ∧ dy & + & ∂_z (+ Q^z )(+1) \; & dx ∧ dy ∧ dz \\
          ∂_y (+ R^x )(+1) \; & dt ∧ dx ∧ dy & + & ∂_z (+ R^x )(-1) \; & dt ∧ dz ∧ dx \\
          ∂_x (+ R^y )(-1) \; & dt ∧ dx ∧ dy & + & ∂_z (+ R^y )(+1) \; & dt ∧ dy ∧ dz \\
          ∂_x (+ R^z )(+1) \; & dt ∧ dz ∧ dx & + & ∂_y (+ R^z )(-1) \; & dt ∧ dy ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Apply values

   .. math::

      d(⋆R^{♭♭}) = \left[ \begin{alignedat}{5}
          ∂_t (+ Q^x ) \; & dt ∧ dy ∧ dz & + & ∂_x (+ Q^x ) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ Q^y ) \; & dt ∧ dz ∧ dx & + & ∂_y (+ Q^y ) \; & dx ∧ dy ∧ dz \\
          ∂_t (+ Q^z ) \; & dt ∧ dx ∧ dy & + & ∂_z (+ Q^z ) \; & dx ∧ dy ∧ dz \\
          ∂_y (+ R^x ) \; & dt ∧ dx ∧ dy & + & ∂_z (- R^x ) \; & dt ∧ dz ∧ dx \\
          ∂_x (- R^y ) \; & dt ∧ dx ∧ dy & + & ∂_z (+ R^y ) \; & dt ∧ dy ∧ dz \\
          ∂_x (+ R^z ) \; & dt ∧ dz ∧ dx & + & ∂_y (- R^z ) \; & dt ∧ dy ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      d ⋆ R^{♭♭} = \left[ \begin{alignedat}{5}
          (&         & + ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z & \: ) \; & dx ∧ dy ∧ dz \\
          (& + ∂_t Q^x &         & - ∂_y R^z & + ∂_z R^y & \: ) \; & dt ∧ dy ∧ dz \\
          (& + ∂_t Q^y & + ∂_x R^z &         & - ∂_z R^x & \: ) \; & dt ∧ dz ∧ dx \\
          (& + ∂_t Q^z & - ∂_x R^y & + ∂_y R^x &         & \: ) \; & dt ∧ dx ∧ dy \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`⋆d R^{♭♭}`
-----------------

.. {{{

Applying in sequence the Hodge star and the exterior derivative operator
:math:`d` to the rotation 2-form, we obtain:

.. math::

   ⋆ dR^{♭♭} = \left[ \begin{alignedat}{5}
       (&         & - ∂_x R^x & - ∂_y R^y & - ∂_z R^z &\:) \; dt \\
       (& - ∂_t R^x &         & - ∂_y Q^z & + ∂_z Q^y &\:) \; dx \\
       (& - ∂_t R^y & + ∂_x Q^z &         & - ∂_z Q^x &\:) \; dy \\
       (& - ∂_t R^z & - ∂_x Q^y & + ∂_y Q^x &         &\:) \; dz \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the Hodge star

   Apply the Hodge star to :math:`dR^{♭♭}`:

   .. math::

      ⋆dR^{♭♭} = ⋆\left[ \begin{alignedat}{5}
        (&         & + ∂_x R^x & + ∂_y R^y & + ∂_z R^z &\:) \; dx ∧ dy ∧ dz \\
        (& + ∂_t R^x &         & + ∂_y Q^z & - ∂_z Q^y &\:) \; dt ∧ dy ∧ dz \\
        (& + ∂_t R^y & - ∂_x Q^z &         & + ∂_z Q^x &\:) \; dt ∧ dz ∧ dx \\
        (& + ∂_t R^z & + ∂_x Q^y & - ∂_y Q^x &         &\:) \; dt ∧ dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Distribute the Hodge star

   .. math::

      ⋆dR^{♭♭} = \left[ \begin{alignedat}{5}
        (&         & + ∂_x R^x & + ∂_y R^y & + ∂_z R^z &\:) \; ⋆ dx^x ∧ dx^y ∧ dx^z \\
        (& + ∂_t R^x &         & + ∂_y Q^z & - ∂_z Q^y &\:) \; ⋆ dx^t ∧ dx^y ∧ dx^z \\
        (& + ∂_t R^y & - ∂_x Q^z &         & + ∂_z Q^x &\:) \; ⋆ dx^t ∧ dx^z ∧ dx^x \\
        (& + ∂_t R^z & + ∂_x Q^y & - ∂_y Q^x &         &\:) \; ⋆ dx^t ∧ dx^x ∧ dx^y \\
      \end{alignedat} \right]

   .. rubric:: Apply the Hodge star to the basis 1-forms

   Using the :ref:`tables for the Hodge dual <Hodge dual tables>`:

   .. math::

      ⋆dR^{♭♭} = \left[ \begin{alignedat}{5}
        (&         & + ∂_x R^x & + ∂_y R^y & + ∂_z R^z &\:) \; (-dt) \\
        (& + ∂_t R^x &         & + ∂_y Q^z & - ∂_z Q^y &\:) \; (-dx) \\
        (& + ∂_t R^y & - ∂_x Q^z &         & + ∂_z Q^x &\:) \; (-dy) \\
        (& + ∂_t R^z & + ∂_x Q^y & - ∂_y Q^x &         &\:) \; (-dz) \\
      \end{alignedat} \right]

   .. rubric:: Conclude

   .. math::

      ⋆dR^{♭♭} = \left[ \begin{alignedat}{5}
        (&         & - ∂_x R^x & - ∂_y R^y & - ∂_z R^z &\:) \; dt \\
        (& - ∂_t R^x &         & - ∂_y Q^z & + ∂_z Q^y &\:) \; dx \\
        (& - ∂_t R^y & + ∂_x Q^z &         & - ∂_z Q^x &\:) \; dy \\
        (& - ∂_t R^z & - ∂_x Q^y & + ∂_y Q^x &         &\:) \; dz \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`⋆d⋆ R^{♭♭}`
------------------

.. {{{


Applying the Hodge star to :math:`d⋆R^{♭♭}`, we obtain:

.. math::

   ⋆d⋆R^{♭♭} = \left[ \begin{alignedat}{5}
     (&         & + ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z &\:) \; dt \\
     (& + ∂_t Q^x &         & - ∂_y R^z & + ∂_z R^y &\:) \; dx \\
     (& + ∂_t Q^y & + ∂_x R^z &         & - ∂_z R^x &\:) \; dy \\
     (& + ∂_t Q^z & - ∂_x R^y & + ∂_y R^x &         &\:) \; dz \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the Hodge star

   Apply the Hodge star to :math:`d⋆R^{♭♭}`:

   .. math::

      ⋆ d⋆R^{♭♭} = ⋆ \left[ \begin{alignedat}{5}
        (&         & + ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z &\:) \; dx ∧ dy ∧ dz \\
        (& + ∂_t Q^x &         & - ∂_y R^z & + ∂_z R^y &\:) \; dt ∧ dy ∧ dz \\
        (& + ∂_t Q^y & + ∂_x R^z &         & - ∂_z R^x &\:) \; dt ∧ dz ∧ dx \\
        (& + ∂_t Q^z & - ∂_x R^y & + ∂_y R^x &         &\:) \; dt ∧ dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Distribute the Hodge star by linearity

   .. math::

      ⋆ d⋆R^{♭♭} = \left[ \begin{alignedat}{5}
        (&         & + ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z &\:) \; ⋆ dx ∧ dy ∧ dz \\
        (& + ∂_t Q^x &         & - ∂_y R^z & + ∂_z R^y &\:) \; ⋆ dt ∧ dy ∧ dz \\
        (& + ∂_t Q^y & + ∂_x R^z &         & - ∂_z R^x &\:) \; ⋆ dt ∧ dz ∧ dx \\
        (& + ∂_t Q^z & - ∂_x R^y & + ∂_y R^x &         &\:) \; ⋆ dt ∧ dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Apply the Hodge star to the basis 3-forms

   Using the :ref:`tables for the Hodge dual <Hodge dual tables>`:

   .. math::

      ⋆ d⋆R^{♭♭} = \left[ \begin{alignedat}{5}
        (&         & + ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z &\:) \; dt \\
        (& + ∂_t Q^x &         & - ∂_y R^z & + ∂_z R^y &\:) \; dx \\
        (& + ∂_t Q^y & + ∂_x R^z &         & - ∂_z R^x &\:) \; dy \\
        (& + ∂_t Q^z & - ∂_x R^y & + ∂_y R^x &         &\:) \; dz \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`d⋆d R^{♭♭}`
------------------

.. {{{

Applying the exterior derivative to :math:`⋆d R^{♭♭}`, we obtain:

.. math::

   d⋆d R^{♭♭}
   &= \left[ \begin{alignedat}{4}
       & ( - ∂_t^2 R^x & + ∂_x^2 R^x &             &             & ) \; dt ∧ dx \\
       & ( - ∂_t^2 R^y &             & + ∂_y^2 R^y &             & ) \; dt ∧ dy \\
       & ( - ∂_t^2 R^z &             &             & + ∂_z^2 R^z & ) \; dt ∧ dz \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (            & + ∂_y^2 Q^x & + ∂_z^2 Q^x & ) \; dy ∧ dz \\
       & (+ ∂_x^2 Q^y &             & + ∂_z^2 Q^y & ) \; dz ∧ dx \\
       & (+ ∂_x^2 Q^z & + ∂_y^2 Q^z &             & ) \; dx ∧ dy \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_t ∂_y Q^z & + ∂_t ∂_z Q^y & ) \; dt ∧ dx \\
       & ( + ∂_t ∂_x Q^z &               & - ∂_t ∂_z Q^x & ) \; dt ∧ dy \\
       & ( - ∂_t ∂_x Q^y & + ∂_t ∂_y Q^x &               & ) \; dt ∧ dz \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_z ∂_x Q^y & - ∂_x ∂_y Q^y & ) \; dy ∧ dz \\
       & ( - ∂_y ∂_z Q^z &               & - ∂_x ∂_y Q^x & ) \; dz ∧ dx \\
       & ( - ∂_y ∂_z Q^y & - ∂_z ∂_x Q^x &               & ) \; dx ∧ dy \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & + ∂_x ∂_y R^y & + ∂_x ∂_z R^z & ) \; dt ∧ dx \\
       & ( + ∂_y ∂_x R^x &               & + ∂_y ∂_z R^z & ) \; dt ∧ dy \\
       & ( + ∂_z ∂_x R^x & + ∂_z ∂_y R^y &               & ) \; dt ∧ dz \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) \; dy ∧ dz \\
       & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) \; dz ∧ dx \\
       & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) \; dx ∧ dy \\
   \end{alignedat} \right] \\[2mm]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the exterior derivative

   .. math::

      d⋆dR^{♭♭} = d \left[ \begin{alignedat}{5}
          (&           & - ∂_x R^x & - ∂_y R^y & - ∂_z R^z &\:) \; dt \\
          (& - ∂_t R^x &           & - ∂_y Q^z & + ∂_z Q^y &\:) \; dx \\
          (& - ∂_t R^y & + ∂_x Q^z &           & - ∂_z Q^x &\:) \; dy \\
          (& - ∂_t R^z & - ∂_x Q^y & + ∂_y Q^x &           &\:) \; dz \\
      \end{alignedat} \right]

   .. rubric:: Apply the exterior derivative

   .. math::

      d⋆dR^{♭♭} = d \left[ \begin{alignedat}{5}
          &( & - & ∂_x ∂_x R^x & - & ∂_x ∂_y R^y & - & ∂_x ∂_z R^z & ) & \; dx ∧ dt \\
          &( & - & ∂_y ∂_x R^x & - & ∂_y ∂_y R^y & - & ∂_y ∂_z R^z & ) & \; dy ∧ dt \\
          &( & - & ∂_z ∂_x R^x & - & ∂_z ∂_y R^y & - & ∂_z ∂_z R^z & ) & \; dz ∧ dt \\[2mm]
          &( & - & ∂_t ∂_t R^x & - & ∂_t ∂_y Q^z & + & ∂_t ∂_z Q^y & ) & \; dt ∧ dx \\
          &( & - & ∂_y ∂_t R^x & - & ∂_y ∂_y Q^z & + & ∂_y ∂_z Q^y & ) & \; dy ∧ dx \\
          &( & - & ∂_z ∂_t R^x & - & ∂_z ∂_y Q^z & + & ∂_z ∂_z Q^y & ) & \; dz ∧ dx \\[2mm]
          &( & - & ∂_t ∂_t R^y & + & ∂_t ∂_x Q^z & - & ∂_t ∂_z Q^x & ) & \; dt ∧ dy \\
          &( & - & ∂_x ∂_t R^y & + & ∂_x ∂_x Q^z & - & ∂_x ∂_z Q^x & ) & \; dx ∧ dy \\
          &( & - & ∂_z ∂_t R^y & + & ∂_z ∂_x Q^z & - & ∂_z ∂_z Q^x & ) & \; dz ∧ dy \\[2mm]
          &( & - & ∂_t ∂_t R^z & - & ∂_t ∂_x Q^y & + & ∂_t ∂_y Q^x & ) & \; dt ∧ dz \\
          &( & - & ∂_x ∂_t R^z & - & ∂_x ∂_x Q^y & + & ∂_x ∂_y Q^x & ) & \; dx ∧ dz \\
          &( & - & ∂_y ∂_t R^z & - & ∂_y ∂_x Q^y & + & ∂_y ∂_y Q^x & ) & \; dy ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      d⋆dR^{♭♭} = d \left[ \begin{alignedat}{5}
          &( & - & ∂_x ∂_x R^x & - & ∂_x ∂_y R^y & - & ∂_x ∂_z R^z & ) & \; dx ∧ dt \\
          &( & - & ∂_y ∂_x R^x & - & ∂_y ∂_y R^y & - & ∂_y ∂_z R^z & ) & \; dy ∧ dt \\
          &( & - & ∂_z ∂_x R^x & - & ∂_z ∂_y R^y & - & ∂_z ∂_z R^z & ) & \; dz ∧ dt \\[2mm]
          &( & - & ∂_t ∂_t R^x & - & ∂_t ∂_y Q^z & + & ∂_t ∂_z Q^y & ) & \; dt ∧ dx \\
          &( & - & ∂_t ∂_t R^y & + & ∂_t ∂_x Q^z & - & ∂_t ∂_z Q^x & ) & \; dt ∧ dy \\
          &( & - & ∂_t ∂_t R^z & - & ∂_t ∂_x Q^y & + & ∂_t ∂_y Q^x & ) & \; dt ∧ dz \\[2mm]
          &( & - & ∂_z ∂_t R^y & + & ∂_z ∂_x Q^z & - & ∂_z ∂_z Q^x & ) & \; dz ∧ dy \\
          &( & - & ∂_y ∂_t R^z & - & ∂_y ∂_x Q^y & + & ∂_y ∂_y Q^x & ) & \; dy ∧ dz \\[2mm]
          &( & - & ∂_z ∂_t R^x & - & ∂_z ∂_y Q^z & + & ∂_z ∂_z Q^y & ) & \; dz ∧ dx \\
          &( & - & ∂_x ∂_t R^z & - & ∂_x ∂_x Q^y & + & ∂_x ∂_y Q^x & ) & \; dx ∧ dz \\[2mm]
          &( & - & ∂_y ∂_t R^x & - & ∂_y ∂_y Q^z & + & ∂_y ∂_z Q^y & ) & \; dy ∧ dx \\
          &( & - & ∂_x ∂_t R^y & + & ∂_x ∂_x Q^z & - & ∂_x ∂_z Q^x & ) & \; dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Reorder the exterior products

   .. math::

      d⋆dR^{♭♭} = d \left[ \begin{alignedat}{5}
          &( & + & ∂_x ∂_x R^x & + & ∂_x ∂_y R^y & + & ∂_x ∂_z R^z & ) & \; dt ∧ dx \\
          &( & + & ∂_y ∂_x R^x & + & ∂_y ∂_y R^y & + & ∂_y ∂_z R^z & ) & \; dt ∧ dy \\
          &( & + & ∂_z ∂_x R^x & + & ∂_z ∂_y R^y & + & ∂_z ∂_z R^z & ) & \; dt ∧ dz \\[2mm]
          &( & - & ∂_t ∂_t R^x & - & ∂_t ∂_y Q^z & + & ∂_t ∂_z Q^y & ) & \; dt ∧ dx \\
          &( & - & ∂_t ∂_t R^y & + & ∂_t ∂_x Q^z & - & ∂_t ∂_z Q^x & ) & \; dt ∧ dy \\
          &( & - & ∂_t ∂_t R^z & - & ∂_t ∂_x Q^y & + & ∂_t ∂_y Q^x & ) & \; dt ∧ dz \\[2mm]
          &( & + & ∂_z ∂_t R^y & - & ∂_z ∂_x Q^z & + & ∂_z ∂_z Q^x & ) & \; dy ∧ dz \\
          &( & - & ∂_y ∂_t R^z & - & ∂_y ∂_x Q^y & + & ∂_y ∂_y Q^x & ) & \; dy ∧ dz \\[2mm]
          &( & - & ∂_z ∂_t R^x & - & ∂_z ∂_y Q^z & + & ∂_z ∂_z Q^y & ) & \; dz ∧ dx \\
          &( & + & ∂_x ∂_t R^z & + & ∂_x ∂_x Q^y & - & ∂_x ∂_y Q^x & ) & \; dz ∧ dx \\[2mm]
          &( & + & ∂_y ∂_t R^x & + & ∂_y ∂_y Q^z & - & ∂_y ∂_z Q^y & ) & \; dx ∧ dy \\
          &( & - & ∂_x ∂_t R^y & + & ∂_x ∂_x Q^z & - & ∂_x ∂_z Q^x & ) & \; dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   Here we ar looking for terms that belong together.

   .. math::

      d⋆dR^{♭♭} = d \left[ \begin{alignedat}{5}
          &( & + & ∂_x ∂_x R^x & + & ∂_x ∂_y R^y & + & ∂_x ∂_z R^z & ) & \; dt ∧ dx \\
          &( & + & ∂_y ∂_x R^x & + & ∂_y ∂_y R^y & + & ∂_y ∂_z R^z & ) & \; dt ∧ dy \\
          &( & + & ∂_z ∂_x R^x & + & ∂_z ∂_y R^y & + & ∂_z ∂_z R^z & ) & \; dt ∧ dz \\[2mm]
          &( & - & ∂_t ∂_t R^x &   &             &   &             & ) & \; dt ∧ dx \\
          &( & - & ∂_t ∂_t R^y &   &             &   &             & ) & \; dt ∧ dy \\
          &( & - & ∂_t ∂_t R^z &   &             &   &             & ) & \; dt ∧ dz \\[2mm]
          &( &   &             & - & ∂_t ∂_y Q^z & + & ∂_t ∂_z Q^y & ) & \; dt ∧ dx \\
          &( &   &             & + & ∂_t ∂_x Q^z & - & ∂_t ∂_z Q^x & ) & \; dt ∧ dy \\
          &( &   &             & - & ∂_t ∂_x Q^y & + & ∂_t ∂_y Q^x & ) & \; dt ∧ dz \\[2mm]
          &( & + & ∂_z ∂_t R^y &   &             &   &             & ) & \; dy ∧ dz \\
          &( & - & ∂_y ∂_t R^z &   &             &   &             & ) & \; dy ∧ dz \\
          &( & - & ∂_z ∂_t R^x &   &             &   &             & ) & \; dz ∧ dx \\
          &( & + & ∂_x ∂_t R^z &   &             &   &             & ) & \; dz ∧ dx \\
          &( & + & ∂_y ∂_t R^x &   &             &   &             & ) & \; dx ∧ dy \\
          &( & - & ∂_x ∂_t R^y &   &             &   &             & ) & \; dx ∧ dy \\[2mm]
          &( &   &             &   &             & + & ∂_z ∂_z Q^x & ) & \; dy ∧ dz \\
          &( &   &             &   &             & + & ∂_y ∂_y Q^x & ) & \; dy ∧ dz \\
          &( &   &             &   &             & + & ∂_z ∂_z Q^y & ) & \; dz ∧ dx \\
          &( &   &             & + & ∂_x ∂_x Q^y &   &             & ) & \; dz ∧ dx \\
          &( &   &             & + & ∂_y ∂_y Q^z &   &             & ) & \; dx ∧ dy \\
          &( &   &             & + & ∂_x ∂_x Q^z &   &             & ) & \; dx ∧ dy \\[2mm]
          &( &   &             & - & ∂_z ∂_x Q^z &   &             & ) & \; dy ∧ dz \\
          &( &   &             & - & ∂_y ∂_x Q^y &   &             & ) & \; dy ∧ dz \\
          &( &   &             & - & ∂_z ∂_y Q^z &   &             & ) & \; dz ∧ dx \\
          &( &   &             &   &             & - & ∂_x ∂_y Q^x & ) & \; dz ∧ dx \\
          &( &   &             &   &             & - & ∂_y ∂_z Q^y & ) & \; dx ∧ dy \\
          &( &   &             &   &             & - & ∂_x ∂_z Q^x & ) & \; dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Reorder

   .. math::

      d⋆dR^{♭♭} &= \left[ \begin{alignedat}{4}
          ( & ∂_x ∂_x & \; R^x & \, + \, & ∂_x ∂_y & \; R^y & \, + \, & ∂_x ∂_z & \; R^z & \; ) & \; dt ∧ dx \\
          ( & ∂_x ∂_y & \; R^x & \, + \, & ∂_y ∂_y & \; R^y & \, + \, & ∂_y ∂_z & \; R^z & \; ) & \; dt ∧ dy \\
          ( & ∂_x ∂_z & \; R^x & \, + \, & ∂_y ∂_z & \; R^y & \, + \, & ∂_z ∂_z & \; R^z & \; ) & \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & - ∂_t^2 R^x & \; dt ∧ dx \\
          & - ∂_t^2 R^y & \; dt ∧ dy \\
          & - ∂_t^2 R^z & \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y Q^z & + ∂_t ∂_z Q^y & ) & \; dt ∧ dx \\
          & ( + ∂_t ∂_x Q^z &               & - ∂_t ∂_z Q^x & ) & \; dt ∧ dy \\
          & ( - ∂_t ∂_x Q^y & + ∂_t ∂_y Q^x &               & ) & \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) & \; dy ∧ dz \\
          & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) & \; dz ∧ dx \\
          & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) & \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (            & + ∂_y^2 Q^x & + ∂_z^2 Q^x & ) & \; dy ∧ dz \\
          & (+ ∂_x^2 Q^y &             & + ∂_z^2 Q^y & ) & \; dz ∧ dx \\
          & (+ ∂_x^2 Q^z & + ∂_y^2 Q^z &             & ) & \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_z ∂_x Q^z & - ∂_x ∂_y Q^y & ) & \; dy ∧ dz \\
          & ( - ∂_y ∂_z Q^z &               & - ∂_x ∂_y Q^x & ) & \; dz ∧ dx \\
          & ( - ∂_y ∂_z Q^y & - ∂_z ∂_x Q^x &               & ) & \; dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      d⋆d R^{♭♭}
      &= \left[ \begin{alignedat}{4}
          & ( - ∂_t^2 R^x & + ∂_x^2 R^x &             &             & ) \; dt ∧ dx \\
          & ( - ∂_t^2 R^y &             & + ∂_y^2 R^y &             & ) \; dt ∧ dy \\
          & ( - ∂_t^2 R^z &             &             & + ∂_z^2 R^z & ) \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (            & + ∂_y^2 Q^x & + ∂_z^2 Q^x & ) \; dy ∧ dz \\
          & (+ ∂_x^2 Q^y &             & + ∂_z^2 Q^y & ) \; dz ∧ dx \\
          & (+ ∂_x^2 Q^z & + ∂_y^2 Q^z &             & ) \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y Q^z & + ∂_t ∂_z Q^y & ) \; dt ∧ dx \\
          & ( + ∂_t ∂_x Q^z &               & - ∂_t ∂_z Q^x & ) \; dt ∧ dy \\
          & ( - ∂_t ∂_x Q^y & + ∂_t ∂_y Q^x &               & ) \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_z ∂_x Q^y & - ∂_x ∂_y Q^y & ) \; dy ∧ dz \\
          & ( - ∂_y ∂_z Q^z &               & - ∂_x ∂_y Q^x & ) \; dz ∧ dx \\
          & ( - ∂_y ∂_z Q^y & - ∂_z ∂_x Q^x &               & ) \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & + ∂_x ∂_y R^y & + ∂_x ∂_z R^z & ) \; dt ∧ dx \\
          & ( + ∂_y ∂_x R^x &               & + ∂_y ∂_z R^z & ) \; dt ∧ dy \\
          & ( + ∂_z ∂_x R^x & + ∂_z ∂_y R^y &               & ) \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) \; dy ∧ dz \\
          & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) \; dz ∧ dx \\
          & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]

   .. }}}

.. }}}

:math:`d⋆d⋆R^{♭♭}`
------------------

.. {{{

Applying the exterior derivative to :math:`⋆d⋆R^{♭♭}`, we obtain:

.. math::

   d⋆d⋆ R^{♭♭}
   &= \left[ \begin{alignedat}{4}
       & ( + ∂_t^2 Q^x & - ∂_x^2 Q^x &             &             & ) \; dt ∧ dx \\
       & ( + ∂_t^2 Q^y &             & - ∂_y^2 Q^y &             & ) \; dt ∧ dy \\
       & ( + ∂_t^2 Q^z &             &             & - ∂_z^2 Q^z & ) \; dt ∧ dx \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & + ∂_y^2 R^x   & + ∂_z^2 R^x   & ) \; dy ∧ dz \\
       & ( + ∂_x^2 R^y   &               & + ∂_z^2 R^y   & ) \; dz ∧ dx \\
       & ( + ∂_x^2 R^z   & + ∂_y^2 R^z   &               & ) \; dx ∧ dy \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_x ∂_y Q^y & - ∂_z ∂_x Q^z & ) \; dt ∧ dx \\
       & ( - ∂_x ∂_y Q^x &               & - ∂_y ∂_z Q^z & ) \; dt ∧ dy \\
       & ( - ∂_z ∂_x Q^x & - ∂_z ∂_y Q^y & -             & ) \; dt ∧ dx \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & + ∂_t ∂_y Q^z & - ∂_t ∂_z Q^y & ) \; dy ∧ dz \\
       & ( - ∂_t ∂_x Q^z &               & + ∂_t ∂_z Q^x & ) \; dz ∧ dx \\
       & ( + ∂_t ∂_x Q^y & - ∂_t ∂_y Q^x &               & ) \; dx ∧ dy \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) \; dt ∧ dx \\
       & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) \; dt ∧ dy \\
       & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) \; dt ∧ dz \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_x ∂_y R^y & - ∂_x ∂_z R^z & ) \; dy ∧ dz \\
       & ( - ∂_y ∂_x R^x &               & - ∂_y ∂_z R^z & ) \; dz ∧ dx \\
       & ( - ∂_z ∂_x R^x & - ∂_z ∂_y R^y &               & ) \; dx ∧ dy \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Take the exterior derivative

   .. math::

      d⋆d⋆ R^{♭♭} = d \left[ \begin{alignedat}{5}
          (&         & + ∂_x Q^x & + ∂_y Q^y & + ∂_z Q^z &) & \; & dt \\
          (& + ∂_t Q^x &         & - ∂_y R^z & + ∂_z R^y &) & \; & dx \\
          (& + ∂_t Q^y & + ∂_x R^z &         & - ∂_z R^x &) & \; & dy \\
          (& + ∂_t Q^z & - ∂_x R^y & + ∂_y R^x &         &) & \; & dz \\
      \end{alignedat} \right]

   .. rubric:: Apply the exterior derivative

   .. math::

      d⋆d⋆ R^{♭♭} = d \left[ \begin{alignedat}{5}
          ( & + & ∂_x ∂_x Q^x & + & ∂_x ∂_y Q^y & + & ∂_x ∂_z Q^z & ) & \; & dx ∧ dt \\
          ( & + & ∂_y ∂_x Q^x & + & ∂_y ∂_y Q^y & + & ∂_y ∂_z Q^z & ) & \; & dy ∧ dt \\
          ( & + & ∂_z ∂_x Q^x & + & ∂_z ∂_y Q^y & + & ∂_z ∂_z Q^z & ) & \; & dx ∧ dt \\[2mm]
          ( & + & ∂_t ∂_t Q^x & - & ∂_t ∂_y R^z & + & ∂_t ∂_z R^y & ) & \; & dt ∧ dx \\
          ( & + & ∂_y ∂_t Q^x & - & ∂_y ∂_y R^z & + & ∂_y ∂_z R^y & ) & \; & dy ∧ dx \\
          ( & + & ∂_z ∂_t Q^x & - & ∂_z ∂_y R^z & + & ∂_z ∂_z R^y & ) & \; & dz ∧ dx \\[2mm]
          ( & + & ∂_t ∂_t Q^y & + & ∂_t ∂_x R^z & - & ∂_t ∂_z R^x & ) & \; & dt ∧ dy \\
          ( & + & ∂_x ∂_t Q^y & + & ∂_x ∂_x R^z & - & ∂_x ∂_z R^x & ) & \; & dx ∧ dy \\
          ( & + & ∂_z ∂_t Q^y & + & ∂_z ∂_x R^z & - & ∂_z ∂_z R^x & ) & \; & dz ∧ dy \\[2mm]
          ( & + & ∂_t ∂_t Q^z & - & ∂_t ∂_x R^y & + & ∂_t ∂_y R^x & ) & \; & dt ∧ dz \\
          ( & + & ∂_x ∂_t Q^z & - & ∂_x ∂_x R^y & + & ∂_x ∂_y R^x & ) & \; & dx ∧ dz \\
          ( & + & ∂_y ∂_t Q^z & - & ∂_y ∂_x R^y & + & ∂_y ∂_y R^x & ) & \; & dy ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      d⋆d⋆ R^{♭♭} = d \left[ \begin{alignedat}{5}
          ( & + & ∂_x ∂_x Q^x & + & ∂_x ∂_y Q^y & + & ∂_x ∂_z Q^z & ) & \; & dx ∧ dt \\
          ( & + & ∂_y ∂_x Q^x & + & ∂_y ∂_y Q^y & + & ∂_y ∂_z Q^z & ) & \; & dy ∧ dt \\
          ( & + & ∂_z ∂_x Q^x & + & ∂_z ∂_y Q^y & + & ∂_z ∂_z Q^z & ) & \; & dx ∧ dt \\[2mm]
          ( & + & ∂_t ∂_t Q^x & - & ∂_t ∂_y R^z & + & ∂_t ∂_z R^y & ) & \; & dt ∧ dx \\
          ( & + & ∂_t ∂_t Q^y & + & ∂_t ∂_x R^z & - & ∂_t ∂_z R^x & ) & \; & dt ∧ dy \\
          ( & + & ∂_t ∂_t Q^z & - & ∂_t ∂_x R^y & + & ∂_t ∂_y R^x & ) & \; & dt ∧ dz \\[2mm]
          ( & + & ∂_z ∂_t Q^y & + & ∂_z ∂_x R^z & - & ∂_z ∂_z R^x & ) & \; & dz ∧ dy \\
          ( & + & ∂_y ∂_t Q^z & - & ∂_y ∂_x R^y & + & ∂_y ∂_y R^x & ) & \; & dy ∧ dz \\[2mm]
          ( & + & ∂_z ∂_t Q^x & - & ∂_z ∂_y R^z & + & ∂_z ∂_z R^y & ) & \; & dz ∧ dx \\
          ( & + & ∂_x ∂_t Q^z & - & ∂_x ∂_x R^y & + & ∂_x ∂_y R^x & ) & \; & dx ∧ dz \\[2mm]
          ( & + & ∂_y ∂_t Q^x & - & ∂_y ∂_y R^z & + & ∂_y ∂_z R^y & ) & \; & dy ∧ dx \\
          ( & + & ∂_x ∂_t Q^y & + & ∂_x ∂_x R^z & - & ∂_x ∂_z R^x & ) & \; & dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Reorder the exterior products

   .. math::

      d⋆d⋆ R^{♭♭} = d \left[ \begin{alignedat}{5}
          ( & - & ∂_x ∂_x Q^x & - & ∂_x ∂_y Q^y & - & ∂_x ∂_z Q^z & ) & \; & dt ∧ dx \\
          ( & - & ∂_y ∂_x Q^x & - & ∂_y ∂_y Q^y & - & ∂_y ∂_z Q^z & ) & \; & dt ∧ dy \\
          ( & - & ∂_z ∂_x Q^x & - & ∂_z ∂_y Q^y & - & ∂_z ∂_z Q^z & ) & \; & dt ∧ dx \\[2mm]
          ( & + & ∂_t ∂_t Q^x & - & ∂_t ∂_y R^z & + & ∂_t ∂_z R^y & ) & \; & dt ∧ dx \\
          ( & + & ∂_t ∂_t Q^y & + & ∂_t ∂_x R^z & - & ∂_t ∂_z R^x & ) & \; & dt ∧ dy \\
          ( & + & ∂_t ∂_t Q^z & - & ∂_t ∂_x R^y & + & ∂_t ∂_y R^x & ) & \; & dt ∧ dz \\[2mm]
          ( & - & ∂_z ∂_t Q^y & - & ∂_z ∂_x R^z & + & ∂_z ∂_z R^x & ) & \; & dy ∧ dz \\
          ( & + & ∂_y ∂_t Q^z & - & ∂_y ∂_x R^y & + & ∂_y ∂_y R^x & ) & \; & dy ∧ dz \\[2mm]
          ( & + & ∂_z ∂_t Q^x & - & ∂_z ∂_y R^z & + & ∂_z ∂_z R^y & ) & \; & dz ∧ dx \\
          ( & - & ∂_x ∂_t Q^z & + & ∂_x ∂_x R^y & - & ∂_x ∂_y R^x & ) & \; & dz ∧ dx \\[2mm]
          ( & - & ∂_y ∂_t Q^x & + & ∂_y ∂_y R^z & - & ∂_y ∂_z R^y & ) & \; & dx ∧ dy \\
          ( & + & ∂_x ∂_t Q^y & + & ∂_x ∂_x R^z & - & ∂_x ∂_z R^x & ) & \; & dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      d⋆d⋆ R^{♭♭} = d \left[ \begin{alignedat}{5}
          ( & - & ∂_x ∂_x Q^x & - & ∂_x ∂_y Q^y & - & ∂_x ∂_z Q^z & ) & \; & dt ∧ dx \\
          ( & - & ∂_y ∂_x Q^x & - & ∂_y ∂_y Q^y & - & ∂_y ∂_z Q^z & ) & \; & dt ∧ dy \\
          ( & - & ∂_z ∂_x Q^x & - & ∂_z ∂_y Q^y & - & ∂_z ∂_z Q^z & ) & \; & dt ∧ dx \\[2mm]
          ( & + & ∂_t ∂_t Q^x &   &             &   &             & ) & \; & dt ∧ dx \\
          ( & + & ∂_t ∂_t Q^y &   &             &   &             & ) & \; & dt ∧ dy \\
          ( & + & ∂_t ∂_t Q^z &   &             &   &             & ) & \; & dt ∧ dz \\[2mm]
          ( &   &             & - & ∂_t ∂_y R^z & + & ∂_t ∂_z R^y & ) & \; & dt ∧ dx \\
          ( &   &             & + & ∂_t ∂_x R^z & - & ∂_t ∂_z R^x & ) & \; & dt ∧ dy \\
          ( &   &             & - & ∂_t ∂_x R^y & + & ∂_t ∂_y R^x & ) & \; & dt ∧ dz \\[2mm]
          ( & - & ∂_z ∂_t Q^y &   &             &   &             & ) & \; & dy ∧ dz \\
          ( & + & ∂_y ∂_t Q^z &   &             &   &             & ) & \; & dy ∧ dz \\
          ( & + & ∂_z ∂_t Q^x &   &             &   &             & ) & \; & dz ∧ dx \\
          ( & - & ∂_x ∂_t Q^z &   &             &   &             & ) & \; & dz ∧ dx \\
          ( & - & ∂_y ∂_t Q^x &   &             &   &             & ) & \; & dx ∧ dy \\
          ( & + & ∂_x ∂_t Q^y &   &             &   &             & ) & \; & dx ∧ dy \\[2mm]
          ( &   &             &   &             & + & ∂_z ∂_z R^x & ) & \; & dy ∧ dz \\
          ( &   &             &   &             & + & ∂_y ∂_y R^x & ) & \; & dy ∧ dz \\
          ( &   &             &   &             & + & ∂_z ∂_z R^y & ) & \; & dz ∧ dx \\
          ( &   &             & + & ∂_x ∂_x R^y &   &             & ) & \; & dz ∧ dx \\
          ( &   &             & + & ∂_y ∂_y R^z &   &             & ) & \; & dx ∧ dy \\
          ( &   &             & + & ∂_x ∂_x R^z &   &             & ) & \; & dx ∧ dy \\[2mm]
          ( &   &             & - & ∂_z ∂_x R^z &   &             & ) & \; & dy ∧ dz \\
          ( &   &             & - & ∂_y ∂_x R^y &   &             & ) & \; & dy ∧ dz \\
          ( &   &             & - & ∂_z ∂_y R^z &   &             & ) & \; & dz ∧ dx \\
          ( &   &             &   &             & - & ∂_x ∂_y R^x & ) & \; & dz ∧ dx \\
          ( &   &             &   &             & - & ∂_y ∂_z R^y & ) & \; & dx ∧ dy \\
          ( &   &             &   &             & - & ∂_x ∂_z R^x & ) & \; & dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      d⋆d⋆ R^{♭♭} &= \left[ \begin{alignedat}{4}
          ( & + & ∂_t^2 Q^x & - & ∂_x ∂_x Q^x & - & ∂_x ∂_y Q^y & - & ∂_x ∂_z Q^z & ) & \; & dt ∧ dx \\
          ( & + & ∂_t^2 Q^y & - & ∂_x ∂_y Q^x & - & ∂_y ∂_y Q^y & - & ∂_y ∂_z Q^z & ) & \; & dt ∧ dy \\
          ( & + & ∂_t^2 Q^z & - & ∂_x ∂_z Q^x & - & ∂_z ∂_y Q^y & - & ∂_z ∂_z Q^z & ) & \; & dt ∧ dx \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          ( &   \; &             & \; -  \; & ∂_t ∂_y R^z & \; + \; & ∂_t ∂_z R^y & ) & \; & dt ∧ dx \\
          ( & + \; & ∂_t ∂_x R^z & \;    \; &             & \; - \; & ∂_t ∂_z R^x & ) & \; & dt ∧ dy \\
          ( & - \; & ∂_t ∂_x R^y & \; +  \; & ∂_t ∂_y R^x & \;   \; &             & ) & \; & dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          ( &   \; &             & \; + \; & ∂_y ∂_t Q^z & \; - \; & ∂_z ∂_t Q^y & ) & \; & dy ∧ dz \\
          ( & - \; & ∂_x ∂_t Q^z & \;   \; &             & \; + \; & ∂_z ∂_t Q^x & ) & \; & dz ∧ dx \\
          ( & + \; & ∂_x ∂_t Q^y & \; - \; & ∂_y ∂_t Q^x & \;   \; &             & ) & \; & dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          ( &   \; &           & \; + \; & ∂_y^2 R^x & \; + \; & ∂_z^2 R^x & ) & \; & dy ∧ dz \\
          ( & + \; & ∂_x^2 R^y & \;   \; &           & \; + \; & ∂_z^2 R^y & ) & \; & dz ∧ dx \\
          ( & + \; & ∂_x^2 R^z & \; + \; & ∂_y^2 R^z & \;   \; &           & ) & \; & dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          ( &   \; &             & \; - \; & ∂_y ∂_x R^y & \; - \; & ∂_z ∂_x R^z & ) & \; & dy ∧ dz \\
          ( & - \; & ∂_x ∂_y R^x & \;   \; &             & \; - \; & ∂_z ∂_y R^z & ) & \; & dz ∧ dx \\
          ( & - \; & ∂_x ∂_z R^x & \; - \; & ∂_y ∂_z R^y & \;   \; &             & ) & \; & dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      d⋆d⋆ R^{♭♭}
      &= \left[ \begin{alignedat}{4}
          & ( + ∂_t^2 Q^x & - ∂_x^2 Q^x &             &             & ) \; dt ∧ dx \\
          & ( + ∂_t^2 Q^y &             & - ∂_y^2 Q^y &             & ) \; dt ∧ dy \\
          & ( + ∂_t^2 Q^z &             &             & - ∂_z^2 Q^z & ) \; dt ∧ dx \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & + ∂_y^2 R^x   & + ∂_z^2 R^x   & ) \; dy ∧ dz \\
          & ( + ∂_x^2 R^y   &               & + ∂_z^2 R^y   & ) \; dz ∧ dx \\
          & ( + ∂_x^2 R^z   & + ∂_y^2 R^z   &               & ) \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_x ∂_y Q^y & - ∂_z ∂_x Q^z & ) \; dt ∧ dx \\
          & ( - ∂_x ∂_y Q^x &               & - ∂_y ∂_z Q^z & ) \; dt ∧ dy \\
          & ( - ∂_z ∂_x Q^x & - ∂_z ∂_y Q^y & -             & ) \; dt ∧ dx \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & + ∂_t ∂_y Q^z & - ∂_t ∂_z Q^y & ) \; dy ∧ dz \\
          & ( - ∂_t ∂_x Q^z &               & + ∂_t ∂_z Q^x & ) \; dz ∧ dx \\
          & ( + ∂_t ∂_x Q^y & - ∂_t ∂_y Q^x &               & ) \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) \; dt ∧ dx \\
          & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) \; dt ∧ dy \\
          & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_x ∂_y R^y & - ∂_x ∂_z R^z & ) \; dy ∧ dz \\
          & ( - ∂_y ∂_x R^x &               & - ∂_y ∂_z R^z & ) \; dz ∧ dx \\
          & ( - ∂_z ∂_x R^x & - ∂_z ∂_y R^y &               & ) \; dx ∧ dy \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`⋆d⋆d R^{♭♭}`
-------------------

.. {{{

.. math::

   ⋆d⋆d R^{♭♭}
   &= \left[ \begin{alignedat}{4}
       & ( + ∂_t^2 R^x & - ∂_x^2 R^x &             &             & ) \; dy ∧ dz \\
       & ( + ∂_t^2 R^y &             & - ∂_y^2 R^y &             & ) \; dy ∧ dx \\
       & ( + ∂_t^2 R^z &             &             & - ∂_z^2 R^z & ) \; dy ∧ dy \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & + ∂_y^2 Q^x & + ∂_z^2 Q^x & ) \; dt ∧ dx \\
       & ( + ∂_x^2 Q^y   &             & + ∂_z^2 Q^y & ) \; dt ∧ dy \\
       & ( + ∂_x^2 Q^z   & + ∂_y^2 Q^z &             & ) \; dt ∧ dz \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_x ∂_y Q^y & - ∂_z ∂_x Q^z & ) \; dt ∧ dx \\
       & ( - ∂_x ∂_y Q^x &               & - ∂_y ∂_z Q^z & ) \; dt ∧ dy \\
       & ( - ∂_z ∂_x Q^x & - ∂_y ∂_z Q^y &               & ) \; dt ∧ dz \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & + ∂_t ∂_y Q^z & - ∂_t ∂_z Q^y & ) \; dy ∧ dz \\
       & ( - ∂_t ∂_x Q^z &               & + ∂_t ∂_z Q^x & ) \; dy ∧ dx \\
       & ( + ∂_t ∂_x Q^y & - ∂_t ∂_y Q^x &               & ) \; dy ∧ dy \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) \; dt ∧ dx \\
       & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) \; dt ∧ dy \\
       & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) \; dt ∧ dz \\
   \end{alignedat} \right] \\[2mm]
   &+ \left[ \begin{alignedat}{4}
       & (               & - ∂_x ∂_y R^y & - ∂_x ∂_z R^z & ) \; dy ∧ dz \\
       & ( - ∂_y ∂_x R^x &               & - ∂_y ∂_z R^z & ) \; dz ∧ dx \\
       & ( - ∂_z ∂_x R^x & - ∂_z ∂_y R^y &               & ) \; dx ∧ dy \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: References

   * :ref:`Hodge dual tables`

   .. rubric:: Take the Hodge star

   .. math::

      ⋆d⋆d R^{♭♭} &= ⋆ \left[ \begin{alignedat}{4}
          ( & - ∂_t^2 R^x & ∂_x ∂_x & \; R^x & \, + \, & ∂_y ∂_x & \; R^y & \, + \, & ∂_x ∂_z & \; R^z & \; ) & \; dt ∧ dx \\
          ( & - ∂_t^2 R^y & ∂_x ∂_y & \; R^x & \, + \, & ∂_y ∂_y & \; R^y & \, + \, & ∂_y ∂_z & \; R^z & \; ) & \; dt ∧ dy \\
          ( & - ∂_t^2 R^z & ∂_x ∂_z & \; R^x & \, + \, & ∂_y ∂_z & \; R^y & \, + \, & ∂_z ∂_z & \; R^z & \; ) & \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ ⋆ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y Q^z & + ∂_t ∂_z Q^y & ) & \; dt ∧ dx \\
          & ( + ∂_t ∂_x Q^z &               & - ∂_t ∂_z Q^x & ) & \; dt ∧ dy \\
          & ( - ∂_t ∂_x Q^y & + ∂_t ∂_y Q^x &               & ) & \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ ⋆ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) & \; dy ∧ dz \\
          & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) & \; dz ∧ dx \\
          & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) & \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ ⋆ \left[ \begin{alignedat}{4}
          & (            & + ∂_y^2 Q^x & + ∂_z^2 Q^x & ) & \; dy ∧ dz \\
          & (+ ∂_x^2 Q^y &             & + ∂_z^2 Q^y & ) & \; dz ∧ dx \\
          & (+ ∂_x^2 Q^z & + ∂_y^2 Q^z &             & ) & \; dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ ⋆ \left[ \begin{alignedat}{4}
          & (               & - ∂_z ∂_x Q^z & - ∂_x ∂_y Q^y & ) & \; dy ∧ dz \\
          & ( - ∂_y ∂_z Q^z &               & - ∂_x ∂_y Q^x & ) & \; dz ∧ dx \\
          & ( - ∂_y ∂_z Q^y & - ∂_z ∂_x Q^x &               & ) & \; dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Distribute the Hodge star

   .. math::

      ⋆d⋆d R^{♭♭} &= \left[ \begin{alignedat}{4}
          ( & - ∂_t^2 R^x & ∂_x ∂_x & \; R^x & \, + \, & ∂_y ∂_x & \; R^y & \, + \, & ∂_x ∂_z & \; R^z & \; ) & \; ⋆ dt ∧ dx \\
          ( & - ∂_t^2 R^y & ∂_x ∂_y & \; R^x & \, + \, & ∂_y ∂_y & \; R^y & \, + \, & ∂_y ∂_z & \; R^z & \; ) & \; ⋆ dt ∧ dy \\
          ( & - ∂_t^2 R^z & ∂_x ∂_z & \; R^x & \, + \, & ∂_y ∂_z & \; R^y & \, + \, & ∂_z ∂_z & \; R^z & \; ) & \; ⋆ dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y Q^z & + ∂_t ∂_z Q^y & ) & \; ⋆ dt ∧ dx \\
          & ( + ∂_t ∂_x Q^z &               & - ∂_t ∂_z Q^x & ) & \; ⋆ dt ∧ dy \\
          & ( - ∂_t ∂_x Q^y & + ∂_t ∂_y Q^x &               & ) & \; ⋆ dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) & \; ⋆ dy ∧ dz \\
          & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) & \; ⋆ dz ∧ dx \\
          & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) & \; ⋆ dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (            & + ∂_y^2 Q^x & + ∂_z^2 Q^x & ) & \; ⋆ dy ∧ dz \\
          & (+ ∂_x^2 Q^y &             & + ∂_z^2 Q^y & ) & \; ⋆ dz ∧ dx \\
          & (+ ∂_x^2 Q^z & + ∂_y^2 Q^z &             & ) & \; ⋆ dx ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_z ∂_x Q^z & - ∂_x ∂_y Q^y & ) & \; ⋆ dy ∧ dz \\
          & ( - ∂_y ∂_z Q^z &               & - ∂_x ∂_y Q^x & ) & \; ⋆ dz ∧ dx \\
          & ( - ∂_y ∂_z Q^y & - ∂_z ∂_x Q^x &               & ) & \; ⋆ dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Apply the Hodge star

   .. math::

      ⋆d⋆d R^{♭♭} &= \left[ \begin{alignedat}{4}
          ( & + ∂_t^2 R^x & - \, & ∂_x ∂_x & \; R^x & \, - \, & ∂_y ∂_x & \; R^y & \, - \, & ∂_x ∂_z & \; R^z & \; ) & \; dy ∧ dz \\
          ( & + ∂_t^2 R^y & - \, & ∂_x ∂_y & \; R^x & \, - \, & ∂_y ∂_y & \; R^y & \, - \, & ∂_y ∂_z & \; R^z & \; ) & \; dy ∧ dx \\
          ( & + ∂_t^2 R^z & - \, & ∂_x ∂_z & \; R^x & \, - \, & ∂_y ∂_z & \; R^y & \, - \, & ∂_z ∂_z & \; R^z & \; ) & \; dy ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & + ∂_t ∂_y Q^z & - ∂_t ∂_z Q^y & ) & \; dy ∧ dz \\
          & ( - ∂_t ∂_x Q^z &               & + ∂_t ∂_z Q^x & ) & \; dy ∧ dx \\
          & ( + ∂_t ∂_x Q^y & - ∂_t ∂_y Q^x &               & ) & \; dy ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) & \; dt ∧ dx \\
          & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) & \; dt ∧ dy \\
          & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) & \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (            & + ∂_y^2 Q^x & + ∂_z^2 Q^x & ) & \; dt ∧ dx \\
          & (+ ∂_x^2 Q^y &             & + ∂_z^2 Q^y & ) & \; dt ∧ dy \\
          & (+ ∂_x^2 Q^z & + ∂_y^2 Q^z &             & ) & \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_z ∂_x Q^z & - ∂_x ∂_y Q^y & ) & \; dt ∧ dx \\
          & ( - ∂_y ∂_z Q^z &               & - ∂_x ∂_y Q^x & ) & \; dt ∧ dy \\
          & ( - ∂_y ∂_z Q^y & - ∂_z ∂_x Q^x &               & ) & \; dt ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

      ⋆d⋆d R^{♭♭}
      &= \left[ \begin{alignedat}{4}
          & ( + ∂_t^2 R^x & - ∂_x^2 R^x &             &             & ) \; dy ∧ dz \\
          & ( + ∂_t^2 R^y &             & - ∂_y^2 R^y &             & ) \; dy ∧ dx \\
          & ( + ∂_t^2 R^z &             &             & - ∂_z^2 R^z & ) \; dy ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & + ∂_y^2 Q^x & + ∂_z^2 Q^x & ) \; dt ∧ dx \\
          & ( + ∂_x^2 Q^y   &             & + ∂_z^2 Q^y & ) \; dt ∧ dy \\
          & ( + ∂_x^2 Q^z   & + ∂_y^2 Q^z &             & ) \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_x ∂_y Q^y & - ∂_z ∂_x Q^z & ) \; dt ∧ dx \\
          & ( - ∂_x ∂_y Q^x &               & - ∂_y ∂_z Q^z & ) \; dt ∧ dy \\
          & ( - ∂_z ∂_x Q^x & - ∂_y ∂_z Q^y &               & ) \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & + ∂_t ∂_y Q^z & - ∂_t ∂_z Q^y & ) \; dy ∧ dz \\
          & ( - ∂_t ∂_x Q^z &               & + ∂_t ∂_z Q^x & ) \; dy ∧ dx \\
          & ( + ∂_t ∂_x Q^y & - ∂_t ∂_y Q^x &               & ) \; dy ∧ dy \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_t ∂_y R^z & + ∂_t ∂_z R^y & ) \; dt ∧ dx \\
          & ( + ∂_t ∂_x R^z &               & - ∂_t ∂_z R^x & ) \; dt ∧ dy \\
          & ( - ∂_t ∂_x R^y & + ∂_t ∂_y R^x &               & ) \; dt ∧ dz \\
      \end{alignedat} \right] \\[2mm]
      &+ \left[ \begin{alignedat}{4}
          & (               & - ∂_x ∂_y R^y & - ∂_x ∂_z R^z & ) \; dy ∧ dz \\
          & ( - ∂_y ∂_x R^x &               & - ∂_y ∂_z R^z & ) \; dz ∧ dx \\
          & ( - ∂_z ∂_x R^x & - ∂_z ∂_y R^y &               & ) \; dx ∧ dy \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`d⋆d⋆ - ⋆d⋆d`
-------------------

.. {{{

.. math::

   (d⋆d⋆ - ⋆d⋆d) \left[ \begin{aligned}
       - & Q^x \; dt ∧ dx \\
       - & Q^y \; dt ∧ dy \\
       - & Q^z \; dt ∧ dz \\
         & R^x \; dy ∧ dz \\
         & R^y \; dz ∧ dx \\
         & R^z \; dx ∧ dy \\
   \end{aligned} \right]
   &= \left[ \begin{alignedat}{5}
       & ( + ∂_t^2 Q^x & - ∂_x^2 Q^x & - ∂_y^2 Q^x & - ∂_z^2 Q^x & \: ) \; dt∧dx \\
       & ( + ∂_t^2 Q^y & - ∂_x^2 Q^y & - ∂_y^2 Q^y & - ∂_z^2 Q^y & \: ) \; dt∧dy \\
       & ( + ∂_t^2 Q^z & - ∂_x^2 Q^z & - ∂_y^2 Q^z & - ∂_z^2 Q^z & \: ) \; dt∧dz \\
       & ( - ∂_t^2 R^x & + ∂_x^2 R^x & + ∂_y^2 R^x & + ∂_z^2 R^x & \: ) \; dy∧dz \\
       & ( - ∂_t^2 R^y & + ∂_x^2 R^y & + ∂_y^2 R^y & + ∂_z^2 R^y & \: ) \; dz∧dx \\
       & ( - ∂_t^2 R^z & + ∂_x^2 R^z & + ∂_y^2 R^z & + ∂_z^2 R^z & \: ) \; dx∧dy \\
   \end{alignedat} \right]

.. }}}
