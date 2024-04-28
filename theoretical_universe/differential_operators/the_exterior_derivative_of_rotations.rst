.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _the_exterior_derivative_of_rotations_in_spacetime:

The Exterior Derivative of Rotations in Spacetime
=================================================

.. rst-class:: custom-author

   by Stéphane Haussler

This article investigates the exterior derivative of :ref:`rotations expressed
in differential form <rotations_in_minkowski_space>`. We employ :ref:`the
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

Spacetime Rotations
-------------------

.. {{{

Rotations in spacetime can occur in six independent planes. Any rotation can be
decomposed into a linear combination of basis rotations within each plane:

.. topic:: Rotation in Minkowski Space

   .. math::

      R^{♯♯} = \begin{bmatrix}
          a \; ∂_t ∧ ∂_x \\ b \; ∂_t ∧ ∂_y \\ c \; ∂_t ∧ ∂_z \\
          d \; ∂_y ∧ ∂_z \\ e \; ∂_z ∧ ∂_x \\ f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}

.. }}}

Spacetime Rotations in Differential Forms
-----------------------------------------

.. {{{

The generic rotation above is doubly contravariant, given in terms of the wedge
product :math:`∧` of vectors corresponding to our physical understanding of
space (and time). By fully flattening, we obtain the associated doubly covariant
differential 2-form representative of the rotation:

.. topic:: Rotation in Differential Form

   .. math::

      \newcommand{\+}{\phantom{+}}
      R^{♭♭} = \begin{bmatrix}
           - a \; dt ∧ dx \\  - b \; dt ∧ dy \\  - c \; dt ∧ dz \\
          \+ d \; dy ∧ dz \\ \+ e \; dz ∧ dx \\ \+ f \; dx ∧ dy \\
      \end{bmatrix}

.. admonition:: All Calculation Steps
   :class: dropdown

   .. {{{

   Apply the flat operator :math:`flat` to each components of the doubly
   contravariant rotation tensor :math:`R^{♯♯}`:

   .. math:: R^{♭♭} = (R^{♯♯})^{♭♭}

   Expand the full expression and distribute the flat operators :math:`♭`:

   .. math::

      R^{♭♭} = \begin{bmatrix}
          a \; ∂_t^♭ ∧ ∂_x^♭ \\ b \; ∂_t^♭ ∧ ∂_y^♭ \\ c \; ∂_t^♭ ∧ ∂_z^♭ \\
          d \; ∂_y^♭ ∧ ∂_z^♭ \\ e \; ∂_z^♭ ∧ ∂_x^♭ \\ f \; ∂_x^♭ ∧ ∂_y^♭ \\
      \end{bmatrix}

   Expand with the Minkowski metric:

   .. math::

      \begin{equation}
          R^{♭♭} = \begin{bmatrix}
              a \; η_{αt} \; dx^α ∧ η_{βx} \; dx^β \\
              b \; η_{αt} \; dx^α ∧ η_{βy} \; dx^β \\
              c \; η_{αt} \; dx^α ∧ η_{βz} \; dx^β \\
              d \; η_{αy} \; dx^α ∧ η_{βz} \; dx^β \\
              e \; η_{αz} \; dx^α ∧ η_{βx} \; dx^β \\
              f \; η_{αx} \; dx^α ∧ η_{βy} \; dx^β \\
          \end{bmatrix}
      \end{equation}

   The wedge product :math:`∧` is bilinear and the Minkowski metric components
   :math:`η`'s can be taken in front of the expression:

   .. math::

      \begin{equation}
          R^{♭♭} = \begin{bmatrix}
              a \; η_{αt} η_{βx} \; dx^α ∧ dx^β \\
              b \; η_{αt} η_{βy} \; dx^α ∧ dx^β \\
              c \; η_{αt} η_{βz} \; dx^α ∧ dx^β \\
              d \; η_{αy} η_{βz} \; dx^α ∧ dx^β \\
              e \; η_{αz} η_{βx} \; dx^α ∧ dx^β \\
              f \; η_{αx} η_{βy} \; dx^α ∧ dx^β \\
          \end{bmatrix}
      \end{equation}

   Identify the non-zero components of the Minkowski metric :math:`η_{μν}`:

   .. math::

      \begin{equation}
          R^{♭♭} = \begin{bmatrix}
              a \; η_{tt} η_{xx} \; dx^t ∧ dx^x \\
              b \; η_{tt} η_{yy} \; dx^t ∧ dx^y \\
              c \; η_{tt} η_{zz} \; dx^t ∧ dx^z \\
              d \; η_{yy} η_{zz} \; dx^y ∧ dx^z \\
              e \; η_{zz} η_{xx} \; dx^z ∧ dx^x \\
              f \; η_{xx} η_{yy} \; dx^x ∧ dx^y \\
          \end{bmatrix}
      \end{equation}

   For readability, replace the :math:`dx^μ` symbols by their explicit
   expressions:

   .. math:: dx^t &= dt \\ dx^x &= dx \\ dx^y &= dy \\ dx^z &= dz

   We obtain:

   .. math::

      R^{♭♭} = \begin{bmatrix}
          a \; η_{tt} η_{xx} \; dt ∧ dx \\
          b \; η_{tt} η_{yy} \; dt ∧ dy \\
          c \; η_{tt} η_{zz} \; dt ∧ dz \\
          d \; η_{yy} η_{zz} \; dy ∧ dz \\
          e \; η_{zz} η_{xx} \; dz ∧ dx \\
          f \; η_{xx} η_{yy} \; dx ∧ dy \\
      \end{bmatrix}

   Apply the numerical values of the Minkowski metric components :math:`η_{μν}`:

   .. math::

      R^{♭♭} = \begin{bmatrix}
          a \; (+1) (-1) \; dt ∧ dx \\
          b \; (+1) (-1) \; dt ∧ dy \\
          c \; (+1) (-1) \; dt ∧ dz \\
          d \; (-1) (-1) \; dy ∧ dz \\
          e \; (-1) (-1) \; dz ∧ dx \\
          f \; (-1) (-1) \; dx ∧ dy \\
      \end{bmatrix}

   Conclude:

   .. math::

      \newcommand{\+}{\phantom{+}}
      R^{♭♭} = \begin{bmatrix}
             - a \; dt ∧ dx \\  - b \; dt ∧ dy \\  - c \; dt ∧ dz \\
            \+ d \; dy ∧ dz \\ \+ e \; dz ∧ dx \\ \+ f \; dx ∧ dy \\
      \end{bmatrix}

   .. }}}

The hodge dual is:

.. topic:: Hodge Dual of a Rotation in Differential Form

   .. math::

      ⋆ R^{♭♭} = \begin{bmatrix}
          a \; dy ∧ dz \\ b \; dz ∧ dx \\ c \; dx ∧ dy \\
          d \; dt ∧ dx \\ e \; dt ∧ dy \\ f \; dt ∧ dz \\
      \end{bmatrix}

.. admonition:: All Calculation Steps
   :class: dropdown

   .. {{{

   Take the hodge dual:

   .. math::

      \newcommand{\+}{\phantom+}
      ⋆ R^{♭♭} = ⋆ \begin{bmatrix}
           - a \; dt ∧ dx \\  - b \; dt ∧ dy \\  - c \; dt ∧ dz \\
          \+ d \; dy ∧ dz \\ \+ e \; dz ∧ dx \\ \+ f \; dx ∧ dy \\
      \end{bmatrix}

   Distribute the Hodge operator :math:`⋆`:

   .. math::

      \newcommand{\+}{\phantom+}
      ⋆ R^{♭♭} = \begin{bmatrix}
           - a \; ⋆ (dt ∧ dx) \\  - b \; ⋆ (dt ∧ dy) \\  - c \; ⋆ (dt ∧ dz) \\
          \+ d \; ⋆ (dy ∧ dz) \\ \+ e \; ⋆ (dz ∧ dx) \\ \+ f \; ⋆ (dx ∧ dy) \\
      \end{bmatrix}

   Apply :ref:`their Hodge dual to each basis element
   <duality_in_minkowski_space>`:

   .. math::

      \newcommand{\+}{\phantom+}
      ⋆ R^{♭♭} = \begin{bmatrix}
           - a \; (-1) \; dy ∧ dz \\
           - b \; (-1) \; dz ∧ dx \\
           - c \; (-1) \; dx ∧ dy \\
          \+ d \; (+1) \; dt ∧ dx \\
          \+ e \; (+1) \; dt ∧ dy \\
          \+ f \; (+1) \; dt ∧ dz \\
      \end{bmatrix}

   Conclude:

   .. math::

      ⋆ R^{♭♭} = \begin{bmatrix}
          a \; dy ∧ dz \\ b \; dz ∧ dx \\ c \; dx ∧ dy \\
          d \; dt ∧ dx \\ e \; dt ∧ dy \\ f \; dt ∧ dz \\
      \end{bmatrix}

   .. }}}

.. }}}

Exterior Derivative of a Rotation
---------------------------------

.. {{{

Applying in sequence the exterior derivative operator :math:`d` and the Hodge
dual operator :math:`⋆` to the doubly covariant rotation :math:`⋆ d R^{♭♭}`, we
obtain:

.. topic:: Hodge Dual of the Exterior Derivative of Rotations in Differential
   Form

   .. math::

      \newcommand{\_}{\phantom{∂_m m}}
      ⋆ (dR^{♭♭}) = \begin{bmatrix}
          ( \_      & - ∂_x d & - ∂_y e & - ∂_z f \, ) \; dt \\
          ( - ∂_t d & \_      & - ∂_y c & + ∂_z b \, ) \; dx \\
          ( - ∂_t e & + ∂_x c & \_      & - ∂_z a \, ) \; dy \\
          ( - ∂_t f & - ∂_x b & + ∂_y a & \_      \, ) \; dz \\
      \end{bmatrix}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Distribute the exterior derivative:

   .. math::

      dR^{♭♭} = \begin{bmatrix}
          d( - a \; dt ∧ dx ) \\ d( - b \; dt ∧ dy ) \\ d( - c \; dt ∧ dz ) \\
          d( + d \; dy ∧ dz ) \\ d( + e \; dz ∧ dx ) \\ d( + f \; dx ∧ dy ) \\
      \end{bmatrix}

   Apply the exterior derivative:

   .. math::

      {\scriptsize dR^{♭♭} = \begin{bmatrix}
                                  &                         & ∂_y (-a)\; dy ∧ dt ∧ dx & ∂_z (-a)\; dz ∧ dt ∧ dx \\
                                  & ∂_x (-b)\; dx ∧ dt ∧ dy &                         & ∂_z (-b)\; dz ∧ dt ∧ dy \\
                                  & ∂_x (-c)\; dx ∧ dt ∧ dz & ∂_y (-c)\; dy ∧ dt ∧ dz &                         \\
          ∂_t (+d)\; dt ∧ dy ∧ dz & ∂_x (+d)\; dx ∧ dy ∧ dz &                         &                         \\
          ∂_t (+e)\; dt ∧ dz ∧ dx &                         & ∂_y (+e)\; dy ∧ dz ∧ dx &                         \\
          ∂_t (+f)\; dt ∧ dx ∧ dy &                         &                         & ∂_z (+f)\; dz ∧ dx ∧ dy \\
      \end{bmatrix}}

   Reorder the wedge products :math:`dx^μ \wedge dx^{ν} ∧ dx^{ξ}`. The sign is flipped for every odd permutations:

   .. math::

      {\scriptsize dR^{♭♭} = \begin{bmatrix}
                                   &                         & ∂_y (-a)(+1)\; dt∧dx∧dy & ∂_z (-a)(-1)\; dt∧dz∧dx \\
                                   & ∂_x (-b)(-1)\; dt∧dx∧dy &                         & ∂_z (-b)(+1)\; dt∧dy∧dz \\
                                   & ∂_x (-c)(+1)\; dt∧dz∧dx & ∂_y (-c)(-1)\; dt∧dy∧dz &                         \\
          ∂_t (+d)(+1)\; dt∧dy∧ dz & ∂_x (+d)(+1)\; dx∧dy∧dz &                         &                         \\
          ∂_t (+e)(+1)\; dt∧dz∧ dx &                         & ∂_y (+e)(+1)\; dx∧dy∧dz &                         \\
          ∂_t (+f)(+1)\; dt∧dx∧ dy &                         &                         & ∂_z (+f)(+1)\; dx∧dy∧dz \\
      \end{bmatrix}}

   Simplify:

   .. math::

      {\scriptsize dR^{♭♭} = \begin{bmatrix}
                                 &                         & ∂_y (-a)\; dt ∧ dx ∧ dy & ∂_z (+a)\; dt ∧ dz ∧ dx \\
                                 & ∂_x (+b)\; dt ∧ dx ∧ dy &                         & ∂_z (-b)\; dt ∧ dy ∧ dz \\
                                 & ∂_x (-c)\; dt ∧ dz ∧ dx & ∂_y (+c)\; dt ∧ dy ∧ dz &                         \\
          ∂_t (+d)\; dt ∧ dy∧ dz & ∂_x (+d)\; dx ∧ dy ∧ dz &                         &                         \\
          ∂_t (+e)\; dt ∧ dz∧ dx &                         & ∂_y (+e)\; dx ∧ dy ∧ dz &                         \\
          ∂_t (+f)\; dt ∧ dx∧ dy &                         &                         & ∂_z (+f)\; dx ∧ dy ∧ dz \\
      \end{bmatrix}}

   Organize the terms into a single column, although the specific ordering is
   not mandatory. However, for clarity, the free matrix representation allows us
   to arrange the terms in a logical manner. Note that:

   * The first row excludes the terms with :math:`dt`
   * The second row excludes the terms with :math:`dx`
   * The third row excludes the terms with :math:`dy`
   * The fourth row excludes the terms with :math:`dz`

   .. math::

      \newcommand{\_}{\phantom{∂_m m}}
      dR = \begin{bmatrix}
          ( \; \_      & + ∂_x d & + ∂_y e & + ∂_z f \; ) \; dx^x ∧ dx^y ∧ dx^z \\
          ( \; + ∂_t d & \_      & + ∂_y c & - ∂_z b \; ) \; dx^t ∧ dx^y ∧ dx^z \\
          ( \; + ∂_t e & - ∂_x c & \_      & + ∂_z a \; ) \; dx^t ∧ dx^z ∧ dx^x \\
          ( \; + ∂_t f & + ∂_x b & - ∂_y a & \_      \; ) \; dx^t ∧ dx^x ∧ dx^y \\
      \end{bmatrix}

   Apply the Hodge dual operation :math:`⋆` to convert 3-forms to 1-forms:

   .. math::

      \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
      ⋆(dR) = \begin{bmatrix}
        ( \; \phan   & + ∂_x d & + ∂_y e & + ∂_z f \; ) \; (-dt) \\
        ( \; + ∂_t d & \phan   & + ∂_y c & - ∂_z b \; ) \; (-dx) \\
        ( \; + ∂_t e & - ∂_x c & \phan   & + ∂_z a \; ) \; (-dy) \\
        ( \; + ∂_t f & + ∂_x b & - ∂_y a & \phan   \; ) \; (-dz) \\
      \end{bmatrix}

   Conclude:

   .. math::

      \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
      ⋆ (dR) = \begin{bmatrix}
          ( \; \phan   & - ∂_x d & - ∂_y e & - ∂_z f \; ) \; dt \\
          ( \; - ∂_t d & \phan   & - ∂_y c & + ∂_z b \; ) \; dx \\
          ( \; - ∂_t e & + ∂_x c & \phan   & - ∂_z a \; ) \; dy \\
          ( \; - ∂_t f & - ∂_x b & + ∂_y a & \phan   \; ) \; dz \\
      \end{bmatrix}

   .. }}}

.. }}}

Exterior Derivative of the Hodge Dual of a Rotation
---------------------------------------------------

.. {{{

Applying in sequence the Hodge dual operator :math:`⋆` and the exterior
derivative operator :math:`d` to the doubly covariant rotation :math:`d ⋆
R^{♭♭}`, we obtain:

.. topic:: Exterior Derivative of the Hodge Dual of Rotations in Differential
   Form

   .. math::

      \newcommand{\_}{\phantom{∂_m m}}
      d( ⋆ R^{♭♭} ) = \begin{bmatrix}
          ( \_      &+ ∂_x a & + ∂_y b & + ∂_z c \, ) \; dx ∧ dy ∧ dz \\
          ( + ∂_t a &\_      & - ∂_y f & + ∂_z e \, ) \; dt ∧ dy ∧ dz \\
          ( + ∂_t b &+ ∂_x f & \_      & - ∂_z d \, ) \; dt ∧ dz ∧ dx \\
          ( + ∂_t c &- ∂_x e & + ∂_y d & \_      \, ) \; dt ∧ dx ∧ dy \\
      \end{bmatrix}

.. admonition:: All Calculation Steps
   :class: dropdown

   .. {{{

   Take the exterior derivative:

   .. math::

      d(⋆R^{♭♭}) = d \begin{bmatrix}
        a \; dy ∧ dz \\ b \; dz ∧ dx \\ c \; dx ∧ dy \\
        d \; dt ∧ dx \\ e \; dt ∧ dy \\ f \; dt ∧ dz \\
      \end{bmatrix}

   Distribute the exterior derivative:

   .. math::

      d(⋆R^{♭♭}) = \begin{bmatrix}
        d(a \; dy ∧ dz) \\ d(b \; dz ∧ dx) \\ d(c \; dx ∧ dy) \\
        d(d \; dt ∧ dx) \\ d(e \; dt ∧ dy) \\ d(f \; dt ∧ dz) \\
      \end{bmatrix}

   Apply:

   .. math::

      {\scriptsize d(⋆R^{♭♭}) = \begin{bmatrix}
       ∂_t (+a)\; dt ∧ dy ∧ dz) & ∂_x (+a)\; dx ∧ dy ∧ dz &                         &                         \\
       ∂_t (+b)\; dt ∧ dz ∧ dx) &                         & ∂_y (+b)\; dy ∧ dz ∧ dx &                         \\
       ∂_t (+c)\; dt ∧ dx ∧ dy) &                         &                         & ∂_z (+c)\; dz ∧ dx ∧ dy \\
                                &                         & ∂_y (+d)\; dy ∧ dt ∧ dx & ∂_z (+d)\; dz ∧ dt ∧ dx \\
                                & ∂_x (+e)\; dx ∧ dt ∧ dy &                         & ∂_z (+e)\; dz ∧ dt ∧ dy \\
                                & ∂_x (+f)\; dx ∧ dt ∧ dz & ∂_y (+f)\; dy ∧ dt ∧ dz &                         \\
      \end{bmatrix}}

   Reorder the 3-forms:

   .. math::

      {\scriptsize d(⋆R^{♭♭}) = \begin{bmatrix}
       ∂_t (+a)(+1)\; dt ∧ dy ∧ dz & ∂_x (+a)(+1)\; dx ∧ dy ∧ dz &                             &                             \\
       ∂_t (+b)(+1)\; dt ∧ dz ∧ dx &                             & ∂_y (+b)(+1)\; dx ∧ dy ∧ dz &                             \\
       ∂_t (+c)(+1)\; dt ∧ dx ∧ dy &                             &                             & ∂_z (+c)(+1)\; dx ∧ dy ∧ dz \\
                                   &                             & ∂_y (+d)(+1)\; dt ∧ dx ∧ dy & ∂_z (+d)(-1)\; dt ∧ dz ∧ dx \\
                                   & ∂_x (+e)(-1)\; dt ∧ dx ∧ dy &                             & ∂_z (+e)(+1)\; dt ∧ dy ∧ dz \\
                                   & ∂_x (+f)(+1)\; dt ∧ dz ∧ dx & ∂_y (+f)(-1)\; dt ∧ dy ∧ dz &                             \\
      \end{bmatrix}}

   Apply values:

   .. math::

      {\scriptsize d(⋆R^{♭♭}) = \begin{bmatrix}
       ∂_t (+a)\; dt ∧ dy ∧ dz & ∂_x (+a)\; dx ∧ dy ∧ dz &                         &                         \\
       ∂_t (+b)\; dt ∧ dz ∧ dx &                         & ∂_y (+b)\; dx ∧ dy ∧ dz &                         \\
       ∂_t (+c)\; dt ∧ dx ∧ dy &                         &                         & ∂_z (+c)\; dx ∧ dy ∧ dz \\
                               &                         & ∂_y (+d)\; dt ∧ dx ∧ dy & ∂_z (-d)\; dt ∧ dz ∧ dx \\
                               & ∂_x (-e)\; dt ∧ dx ∧ dy &                         & ∂_z (+e)\; dt ∧ dy ∧ dz \\
                               & ∂_x (+f)\; dt ∧ dz ∧ dx & ∂_y (-f)\; dt ∧ dy ∧ dz &                         \\
      \end{bmatrix}}

   Organize the terms into a single column, although the specific ordering is
   not mandatory. However, for clarity, the free matrix representation allows us
   to arrange the terms in a logical manner. Note that:

   * The first row excludes the terms with :math:`dt`
   * The second row excludes the terms with :math:`dx`
   * The third row excludes the terms with :math:`dy`
   * The fourth row excludes the terms with :math:`dz`

   .. math::

      \newcommand{\_}{\phantom{∂_m m}}
      d( ⋆ R^{♭♭} ) = \begin{bmatrix}
          ( \_      &+ ∂_x a & + ∂_y b & + ∂_z c \, ) \; dx ∧ dy ∧ dz \\
          ( + ∂_t a &\_      & - ∂_y f & + ∂_z e \, ) \; dt ∧ dy ∧ dz \\
          ( + ∂_t b &+ ∂_x f & \_      & - ∂_z d \, ) \; dt ∧ dz ∧ dx \\
          ( + ∂_t c &- ∂_x e & + ∂_y d & \_      \, ) \; dt ∧ dx ∧ dy \\
      \end{bmatrix}

   .. }}}

.. }}}

Applying the Laplace-De Rham Operator
-------------------------------------

.. {{{

From

.. math:: dδ + δd = d ⋆ d ⋆ + ⋆ d ⋆ d

.. }}}
