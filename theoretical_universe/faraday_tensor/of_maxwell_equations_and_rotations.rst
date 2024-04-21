.. Theoretical Universe (c) by Stéphane Haussler
.. 
.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Of Maxwell Equations and Rotations
==================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

This article investigates the connection between :ref:`rotations
<rotations_in_differential_form>`, the exterior derivative, and the equations
of Mr. Maxwell. I utilize :ref:`the Cartan-Hodge's formalism
<the_cartan_hodge_formalism>` in Minkowski space-time. I demonstrate that
applying the exterior derivative to rotations yields the equations governing
electromagnetism. These experssions reveal Maxwell equations are a twist in the
fabric of spacetime.

The content in this articles might not be wildely known as I have not found my
observations mentioned anywhere. Feel free to open an issue and I will include
a reference if you are aware of one. If you find mistakes, don't hesitate to
open an issue or directly provide corrections by sending a merge request to my
`Github repository <https://github.com/shaussler/TheoreticalUniverse/>`_.

Rotations in Space-Time
-----------------------

.. {{{

A rotation in space-time is a linear combination of the 6 independent basis
planes. More details can be found in my articly on :ref:`rotations in Minkowski
Space <rotations_in_minkowski_space>`.

.. topic:: Rotation in Minkowski Space

   .. math::

      \begin{equation}
      R^{♯♯}
      = \begin{bmatrix}
        a \; ∂_t ∧ ∂_x \\
        b \; ∂_t ∧ ∂_y \\
        c \; ∂_t ∧ ∂_z \\
        d \; ∂_y ∧ ∂_z \\
        e \; ∂_z ∧ ∂_x \\
        f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}
      \end{equation}

.. }}}

Rotations in Differential Forms
-------------------------------

.. {{{

For the rotations in terms of basis bivectors, we determine the associated
differential form. In other words, we fully flatten the rotation:

.. math::

   \begin{equation}
   R^{♭♭} = (R^{♯♯})^{♭♭}
   \end{equation}

and obtain:

.. topic:: Rotation in Differential Form

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        -a \; dt ∧ dx \\
        -b \; dt ∧ dy \\
        -c \; dt ∧ dz \\
        +d \; dy ∧ dz \\
        +e \; dz ∧ dx \\
        +f \; dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Expand the full expression and distribute the flat operators :math:`♭`:

   .. math::

      \begin{equation}
      R^{♭♭} =
      \begin{bmatrix}
        a \; ∂_t^♭ ∧ ∂_x^♭ \\
        b \; ∂_t^♭ ∧ ∂_y^♭ \\
        c \; ∂_t^♭ ∧ ∂_z^♭ \\
        d \; ∂_y^♭ ∧ ∂_z^♭ \\
        e \; ∂_z^♭ ∧ ∂_x^♭ \\
        f \; ∂_x^♭ ∧ ∂_y^♭ \\
      \end{bmatrix}
      \end{equation}

   Expand with the Minkowski metric:

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        a \; η_{αt} \; dx^α ∧ η_{βx} \; dx^β \\
        b \; η_{αt} \; dx^α ∧ η_{βy} \; dx^β \\
        c \; η_{αt} \; dx^α ∧ η_{βz} \; dx^β \\
        d \; η_{αy} \; dx^α ∧ η_{βz} \; dx^β \\
        e \; η_{αz} \; dx^α ∧ η_{βx} \; dx^β \\
        f \; η_{αx} \; dx^α ∧ η_{βy} \; dx^β \\
      \end{bmatrix}
      \end{equation}

   The wedge product :math:`∧` is bilinear and the Minkowski metric components
   :math:`η`'s can be taken in front:

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        a \; η_{αt} η_{βx} \; dx^α ∧ dx^β \\
        b \; η_{αt} η_{βy} \; dx^α ∧ dx^β \\
        c \; η_{αt} η_{βz} \; dx^α ∧ dx^β \\
        d \; η_{αy} η_{βz} \; dx^α ∧ dx^β \\
        e \; η_{αz} η_{βx} \; dx^α ∧ dx^β \\
        f \; η_{αx} η_{βy} \; dx^α ∧ dx^β \\
      \end{bmatrix}
      \end{equation}

   Identify the non-zero components of the Minkowski metric :math:`η`:

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        a \; η_{tt} η_{xx} \; dx^t ∧ dx^x \\
        b \; η_{tt} η_{yy} \; dx^t ∧ dx^y \\
        c \; η_{tt} η_{zz} \; dx^t ∧ dx^z \\
        d \; η_{yy} η_{zz} \; dx^y ∧ dx^z \\
        e \; η_{zz} η_{xx} \; dx^z ∧ dx^x \\
        f \; η_{xx} η_{yy} \; dx^x ∧ dx^y \\
      \end{bmatrix}
      \end{equation}

   We use the definition of the :math:`dx^μ` symbols:

   .. math::

      \begin{equation}
      \begin{matrix}
        dx^t = dt \\
        dx^x = dx \\
        dx^y = dy \\
        dx^z = dz \\
      \end{matrix}
      \end{equation}

   We obtain:

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        a \; η_{tt} η_{xx} \; dt ∧ dx \\
        b \; η_{tt} η_{yy} \; dt ∧ dy \\
        c \; η_{tt} η_{zz} \; dt ∧ dz \\
        d \; η_{yy} η_{zz} \; dy ∧ dz \\
        e \; η_{zz} η_{xx} \; dz ∧ dx \\
        f \; η_{xx} η_{yy} \; dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

   Apply the numerical values of the :math:`η` components:

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        a \; (+1) (-1) \; dt ∧ dx \\
        b \; (+1) (-1) \; dt ∧ dy \\
        c \; (+1) (-1) \; dt ∧ dz \\
        d \; (-1) (-1) \; dy ∧ dz \\
        e \; (-1) (-1) \; dz ∧ dx \\
        f \; (-1) (-1) \; dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

   Conclude:

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        -a \; dt ∧ dx \\
        -b \; dt ∧ dy \\
        -c \; dt ∧ dz \\
        +d \; dy ∧ dz \\
        +e \; dz ∧ dx \\
        +f \; dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

   .. }}}

.. }}}

The Exterior Derivative of a Rotation
-------------------------------------

.. {{{

I now apply the exterior derivative operator :math:`d` to the rotation in
differential form:

.. math::

   \begin{equation}
   dR^{♭♭} =
   d
   \begin{bmatrix}
     -a \; dt ∧ dx \\
     -b \; dt ∧ dy \\
     -c \; dt ∧ dz \\
     +d \; dy ∧ dz \\
     +e \; dz ∧ dx \\
     +f \; dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

After a straightforward calculations, we obtain:

.. topic:: Hodge Dual of the exterior derivative of Rotations in Differential
   Form

   .. math::

      \begin{equation}\
      \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
      ⋆(dR^{♭♭}) =
      \begin{bmatrix}
        ( \; \phan   & - ∂_x d & - ∂_y e & - ∂_z f \; ) \; dt \\
        ( \; - ∂_t d & \phan   & - ∂_y c & + ∂_z b \; ) \; dx \\
        ( \; - ∂_t e & + ∂_x c & \phan   & - ∂_z a \; ) \; dy \\
        ( \; - ∂_t f & - ∂_x b & + ∂_y a & \phan   \; ) \; dz \\
      \end{bmatrix}
      \end{equation}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Distribute the exterior derivative:

   .. math::

      \begin{equation}
      dR^{♭♭} =
      \begin{bmatrix}
        d(-a \; dt ∧ dx) \\
        d(-b \; dt ∧ dy) \\
        d(-c \; dt ∧ dz) \\
        d(+d \; dy ∧ dz) \\
        d(+e \; dz ∧ dx) \\
        d(+f \; dx ∧ dy) \\
      \end{bmatrix}
      \end{equation}

   Apply the exterior derivative:

   .. math::

      {\scriptsize
      \begin{equation}
      dR^{♭♭} =
      \begin{bmatrix}
                               &                          &  ∂_y (-a) \; dy ∧ dt ∧ dx & ∂_z (-a) \; dz ∧ dt ∧ dx \\
                               & ∂_x (-b) \; dx ∧ dt ∧ dy &                           & ∂_z (-b) \; dz ∧ dt ∧ dy \\
                               & ∂_x (-c) \; dx ∧ dt ∧ dz &  ∂_y (-c) \; dy ∧ dt ∧ dz &                          \\
      ∂_t (+d) \; dt ∧ dy ∧ dz & ∂_x (+d) \; dx ∧ dy ∧ dz &                           &                          \\
      ∂_t (+e) \; dt ∧ dz ∧ dx &                          &  ∂_y (+e) \; dy ∧ dz ∧ dx &                          \\
      ∂_t (+f) \; dt ∧ dx ∧ dy &                          &                           & ∂_z (+f) \; dz ∧ dx ∧ dy \\
      \end{bmatrix}
      \end{equation}
      }

   Reorder the wedge products:

   .. math::

      {\scriptsize
      \begin{equation}
      dR^{♭♭} =
      \begin{bmatrix}
                                 &                             & ∂_y (-a)(+1)\; dt ∧ dx ∧ dy & ∂_z (-a)(-1)\; dt ∧ dz ∧ dx \\
                                 & ∂_x (-b)(-1)\; dt ∧ dx ∧ dy &                             & ∂_z (-b)(+1)\; dt ∧ dy ∧ dz \\
                                 & ∂_x (-c)(+1)\; dt ∧ dz ∧ dx & ∂_y (-c)(-1)\; dt ∧ dy ∧ dz &                             \\
      ∂_t (+d)(+1)\; dt ∧ dy∧ dz & ∂_x (+d)(+1)\; dx ∧ dy ∧ dz &                             &                             \\
      ∂_t (+e)(+1)\; dt ∧ dz∧ dx &                             & ∂_y (+e)(+1)\; dx ∧ dy ∧ dz &                             \\
      ∂_t (+f)(+1)\; dt ∧ dx∧ dy &                             &                             & ∂_z (+f)(+1)\; dx ∧ dy ∧ dz \\
      \end{bmatrix}
      \end{equation}
      }

   Simplify:

   .. math::

      {\scriptsize
      \begin{equation}
      dR^{♭♭} =
      \begin{bmatrix}
                             &                         & ∂_y (-a)\; dt ∧ dx ∧ dy & ∂_z (+a)\; dt ∧ dz ∧ dx \\
                             & ∂_x (+b)\; dt ∧ dx ∧ dy &                         & ∂_z (-b)\; dt ∧ dy ∧ dz \\
                             & ∂_x (-c)\; dt ∧ dz ∧ dx & ∂_y (+c)\; dt ∧ dy ∧ dz &                         \\
      ∂_t (+d)\; dt ∧ dy∧ dz & ∂_x (+d)\; dx ∧ dy ∧ dz &                         &                         \\
      ∂_t (+e)\; dt ∧ dz∧ dx &                         & ∂_y (+e)\; dx ∧ dy ∧ dz &                         \\
      ∂_t (+f)\; dt ∧ dx∧ dy &                         &                         & ∂_z (+f)\; dx ∧ dy ∧ dz \\
      \end{bmatrix}
      \end{equation}
      }

   We gather the terms and reorder into columns choosing:

   * The first row with wedge products that do not contain :math:`dt`
   * The second row with wedge products that do not contain :math:`dx`
   * The third row with wedge products that do not contain :math:`dy`
   * The fourth row with wedge products that do not contain :math:`dz`

   The ordering is not strictly necessary, but merely :ref:`the free matrix
   representation <the_free_matrix_representation>` permits to gather the term
   in a manner that makes sense:

   .. math::

      \begin{equation}
      \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
      dR =
      \begin{bmatrix}
        ( \; \phan   & + ∂_x d & + ∂_y e & + ∂_z f \; ) \; dx^x ∧ dx^y ∧ dx^z \\
        ( \; + ∂_t d & \phan   & + ∂_y c & - ∂_z b \; ) \; dx^t ∧ dx^y ∧ dx^z \\
        ( \; + ∂_t e & - ∂_x c &   \phan & + ∂_z a \; ) \; dx^t ∧ dx^z ∧ dx^x \\
        ( \; + ∂_t f & + ∂_x b & - ∂_y a & \phan   \; ) \; dx^t ∧ dx^x ∧ dx^y \\
      \end{bmatrix}
      \end{equation}

   We can take the :ref:`Hodge dual <duality_in_minkowski_space>` to transform
   3-forms to 1-forms:

   .. math::

      \begin{equation}
      \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
      ⋆(dR) =
      \begin{bmatrix}
        ( \; \phan   & + ∂_x d & + ∂_y e & + ∂_z f \; ) \; (-dt) \\
        ( \; + ∂_t d & \phan   & + ∂_y c & - ∂_z b \; ) \; (-dx) \\
        ( \; + ∂_t e & - ∂_x c & \phan   & + ∂_z a \; ) \; (-dy) \\
        ( \; + ∂_t f & + ∂_x b & - ∂_y a & \phan   \; ) \; (-dz) \\
      \end{bmatrix}
      \end{equation}

   We finally obtain our final expression:

   .. math::

      \begin{equation}\
      \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
      ⋆(dR) =
      \begin{bmatrix}
        ( \; \phan   & - ∂_x d & - ∂_y e & - ∂_z f \; ) \; dt \\
        ( \; - ∂_t d & \phan   & - ∂_y c & + ∂_z b \; ) \; dx \\
        ( \; - ∂_t e & + ∂_x c & \phan   & - ∂_z a \; ) \; dy \\
        ( \; - ∂_t f & - ∂_x b & + ∂_y a & \phan   \; ) \; dz \\
      \end{bmatrix}
      \end{equation}

   .. }}}

.. }}}

The Exterior Derivative of the Hodge Dual of a Rotation
-------------------------------------------------------

.. {{{

I have shown above that a rotation in differential form is
expressed as:

.. math::

   \begin{equation}
   \newcommand{\+}{\phantom+}
   R^{♭♭}
   =
   \begin{bmatrix}
     -a \; dt ∧ dx \\
     -b \; dt ∧ dy \\
     -c \; dt ∧ dz \\
    \+d \; dy ∧ dz \\
    \+e \; dz ∧ dx \\
    \+f \; dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

The hodge dual is:

.. topic:: Hodge Dual of a Rotation in Differential Form:

   .. math::

      \begin{equation}
      ⋆R^{♭♭}
      =
      \begin{bmatrix}
        a \; dy ∧ dz \\
        b \; dz ∧ dx \\
        c \; dx ∧ dy \\
        d \; dt ∧ dx \\
        e \; dt ∧ dy \\
        f \; dt ∧ dz \\
      \end{bmatrix}
      \end{equation}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Take the hodge dual

   .. math::

      \begin{equation}
      \newcommand{\+}{\phantom+}
      ⋆R^{♭♭}
      = ⋆
      \begin{bmatrix}
        - a \; dt ∧ dx \\
        - b \; dt ∧ dy \\
        - c \; dt ∧ dz \\
       \+ d \; dy ∧ dz \\
       \+ e \; dz ∧ dx \\
       \+ f \; dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

   Distribute the Hodge operator :math:`⋆`

   .. math::

      \begin{equation}
      \newcommand{\+}{\phantom+}
      ⋆R^{♭♭}
      =
      \begin{bmatrix}
        - a \; ⋆ (dt ∧ dx) \\
        - b \; ⋆ (dt ∧ dy) \\
        - c \; ⋆ (dt ∧ dz) \\
       \+ d \; ⋆ (dy ∧ dz) \\
       \+ e \; ⋆ (dz ∧ dx) \\
       \+ f \; ⋆ (dx ∧ dy) \\
      \end{bmatrix}
      \end{equation}

   Apply :ref:`the Hodge dual to the basis elements
   <duality_in_minkowski_space>`:

   .. math::

      \begin{equation}
      \newcommand{\+}{\phantom+}
      ⋆R^{♭♭}
      =
      \begin{bmatrix}
         - a \; (-1) \; dy ∧ dz \\
         - b \; (-1) \; dz ∧ dx \\
         - c \; (-1) \; dx ∧ dy \\
        \+ d \; (+1) \; dt ∧ dx \\
        \+ e \; (+1) \; dt ∧ dy \\
        \+ f \; (+1) \; dt ∧ dz \\
      \end{bmatrix}
      \end{equation}

   Conclude:

   .. math::

      \begin{equation}
      ⋆R^{♭♭}
      =
      \begin{bmatrix}
        a \; dy ∧ dz \\
        b \; dz ∧ dx \\
        c \; dx ∧ dy \\
        d \; dt ∧ dx \\
        e \; dt ∧ dy \\
        f \; dt ∧ dz \\
      \end{bmatrix}
      \end{equation}

   .. }}}

I now calculate the exterior derivative of the Hodge dual of a rotation in
differential form and we get:

.. topic:: Hodge Dual of the Exterior Derivative of the Hodge Dual of a
   Rotation

   .. math::

      \begin{equation}
      \newcommand{\_}{\phantom{∂_m m}} % Phantom for alignment
      ⋆d(⋆R^{♭♭})
      =
      \begin{bmatrix}
      (   \_    & - ∂_x a & - ∂_y b & - ∂_z c ) ⋆ dt \\
      ( - ∂_t a &   \_    & + ∂_y f & - ∂_z e ) ⋆ dx \\
      ( - ∂_t b & - ∂_x f &   \_    & + ∂_z d ) ⋆ dy \\
      ( - ∂_t c & + ∂_x e & - ∂_y d &   \_    ) ⋆ dz \\
      \end{bmatrix}
      \end{equation}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Take the exterior derivative:

   .. math::

      \begin{equation}
      d(⋆R^{♭♭})
      =d
      \begin{bmatrix}
        a \; dy ∧ dz \\
        b \; dz ∧ dx \\
        c \; dx ∧ dy \\
        d \; dt ∧ dx \\
        e \; dt ∧ dy \\
        f \; dt ∧ dz \\
      \end{bmatrix}
      \end{equation}

   Distribute the exterior derivative:

   .. math::

      \begin{equation}
      d(⋆R^{♭♭})
      =
      \begin{bmatrix}
        d(a \; dy ∧ dz) \\
        d(b \; dz ∧ dx) \\
        d(c \; dx ∧ dy) \\
        d(d \; dt ∧ dx) \\
        d(e \; dt ∧ dy) \\
        d(f \; dt ∧ dz) \\
      \end{bmatrix}
      \end{equation}

   Apply:

   .. math::

      {\scriptsize
      \begin{equation}
      d(⋆R^{♭♭})
      =
      \begin{bmatrix}
       ∂_t (+a)\; dt ∧ dy ∧ dz) & ∂_x (+a)\; dx ∧ dy ∧ dz &                         &                         \\
       ∂_t (+b)\; dt ∧ dz ∧ dx) &                         & ∂_y (+b)\; dy ∧ dz ∧ dx &                         \\
       ∂_t (+c)\; dt ∧ dx ∧ dy) &                         &                         & ∂_z (+c)\; dz ∧ dx ∧ dy \\
                                &                         & ∂_y (+d)\; dy ∧ dt ∧ dx & ∂_z (+d)\; dz ∧ dt ∧ dx \\
                                & ∂_x (+e)\; dx ∧ dt ∧ dy &                         & ∂_z (+e)\; dz ∧ dt ∧ dy \\
                                & ∂_x (+f)\; dx ∧ dt ∧ dz & ∂_y (+f)\; dy ∧ dt ∧ dz &                         \\
      \end{bmatrix}
      \end{equation}
      }

   Reorder the 3-forms:

   .. math::

      {\scriptsize
      \begin{equation}
      d(⋆R^{♭♭})
      =
      \begin{bmatrix}
       ∂_t (+a)(+1)\; dt ∧ dy ∧ dz & ∂_x (+a)(+1)\; dx ∧ dy ∧ dz &                             &                             \\
       ∂_t (+b)(+1)\; dt ∧ dz ∧ dx &                             & ∂_y (+b)(+1)\; dx ∧ dy ∧ dz &                             \\
       ∂_t (+c)(+1)\; dt ∧ dx ∧ dy &                             &                             & ∂_z (+c)(+1)\; dx ∧ dy ∧ dz \\
                                   &                             & ∂_y (+d)(+1)\; dt ∧ dx ∧ dy & ∂_z (+d)(-1)\; dt ∧ dz ∧ dx \\
                                   & ∂_x (+e)(-1)\; dt ∧ dx ∧ dy &                             & ∂_z (+e)(+1)\; dt ∧ dy ∧ dz \\
                                   & ∂_x (+f)(+1)\; dt ∧ dz ∧ dx & ∂_y (+f)(-1)\; dt ∧ dy ∧ dz &                             \\
      \end{bmatrix}
      \end{equation}
      }

   Apply values:

   .. math::

      {\scriptsize
      \begin{equation}
      d(⋆R^{♭♭})
      =
      \begin{bmatrix}
       ∂_t (+a)\; dt ∧ dy ∧ dz & ∂_x (+a)\; dx ∧ dy ∧ dz &                         &                         \\
       ∂_t (+b)\; dt ∧ dz ∧ dx &                         & ∂_y (+b)\; dx ∧ dy ∧ dz &                         \\
       ∂_t (+c)\; dt ∧ dx ∧ dy &                         &                         & ∂_z (+c)\; dx ∧ dy ∧ dz \\
                               &                         & ∂_y (+d)\; dt ∧ dx ∧ dy & ∂_z (-d)\; dt ∧ dz ∧ dx \\
                               & ∂_x (-e)\; dt ∧ dx ∧ dy &                         & ∂_z (+e)\; dt ∧ dy ∧ dz \\
                               & ∂_x (+f)\; dt ∧ dz ∧ dx & ∂_y (-f)\; dt ∧ dy ∧ dz &                         \\
      \end{bmatrix}
      \end{equation}
      }

   We gather the terms and reorder into columns choosing:

   * The first row with wedge products that do not contain :math:`dt`
   * The second row with wedge products that do not contain :math:`dx`
   * The third row with wedge products that do not contain :math:`dy`
   * The fourth row with wedge products that do not contain :math:`dz`

   The ordering is not strictly necessary, but merely :ref:`the free matrix
   representation <the_free_matrix_representation>` permits to gather the term
   in a manner that makes sense:

   .. math::

      \begin{equation}
      \newcommand{\_}{\phantom{∂_m m}} % Phantom for alignment
      d(⋆R^{♭♭})
      =
      \begin{bmatrix}
      (   \_    + ∂_x a + ∂_y b + ∂_z c ) dx ∧ dy ∧ dz \\
      ( + ∂_t a   \_    - ∂_y f + ∂_z e ) dt ∧ dy ∧ dz \\
      ( + ∂_t b + ∂_x f   \_    - ∂_z d ) dt ∧ dz ∧ dx \\
      ( + ∂_t c - ∂_x e + ∂_y d   \_    ) dt ∧ dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

   We can take the :ref:`Hodge dual <duality_in_minkowski_space>` to transform
   the 3-forms to 1-forms:

   .. math::

      \begin{equation}
      \newcommand{\_}{\phantom{∂_m m}} % Phantom for alignment
      ⋆d(⋆R^{♭♭})
      =
      \begin{bmatrix}
      (   \_    & + ∂_x a & + ∂_y b & + ∂_z c ) ⋆ dx ∧ dy ∧ dz \\
      ( + ∂_t a &   \_    & - ∂_y f & + ∂_z e ) ⋆ dt ∧ dy ∧ dz \\
      ( + ∂_t b & + ∂_x f &   \_    & - ∂_z d ) ⋆ dt ∧ dz ∧ dx \\
      ( + ∂_t c & - ∂_x e & + ∂_y d &   \_    ) ⋆ dt ∧ dx ∧ dy \\
      \end{bmatrix}
      \end{equation}

   Apply:

   .. math::

      \begin{equation}
      \newcommand{\_}{\phantom{∂_m m}} % Phantom for alignment
      ⋆d(⋆R^{♭♭})
      =
      \begin{bmatrix}
      (   \_    & + ∂_x a & + ∂_y b & + ∂_z c ) ⋆ - dt \\
      ( + ∂_t a &   \_    & - ∂_y f & + ∂_z e ) ⋆ - dx \\
      ( + ∂_t b & + ∂_x f &   \_    & - ∂_z d ) ⋆ - dy \\
      ( + ∂_t c & - ∂_x e & + ∂_y d &   \_    ) ⋆ - dz \\
      \end{bmatrix}
      \end{equation}

   Conclude:

   .. math::

      \begin{equation}
      \newcommand{\_}{\phantom{∂_m m}} % Phantom for alignment
      ⋆d(⋆R^{♭♭})
      =
      \begin{bmatrix}
      (   \_    & - ∂_x a & - ∂_y b & - ∂_z c ) ⋆ dt \\
      ( - ∂_t a &   \_    & + ∂_y f & - ∂_z e ) ⋆ dx \\
      ( - ∂_t b & - ∂_x f &   \_    & + ∂_z d ) ⋆ dy \\
      ( - ∂_t c & + ∂_x e & - ∂_y d &   \_    ) ⋆ dz \\
      \end{bmatrix}
      \end{equation}

   .. }}}

.. }}}

Identifying the Equations of Mr. Maxwell
----------------------------------------

.. {{{

In a :ref:`previous article
<deriving_the_faraday_tensor_from_the_1865_maxwell_equations>`, I :ref:`derived
from the 1865 Maxell equations the following form <the_ordered_equations>`:

.. math::

   \begin{equation}
   dR^{♭♭} =
   d
   \begin{bmatrix}
     -a \; dt ∧ dx \\
     -b \; dt ∧ dy \\
     -c \; dt ∧ dz \\
     +d \; dy ∧ dz \\
     +e \; dz ∧ dx \\
     +f \; dx ∧ dy \\
   \end{bmatrix}
   =
   d
   \begin{bmatrix}
     a \; dx ∧ dt \\
     b \; dy ∧ dt \\
     c \; dz ∧ dt \\
     d \; dy ∧ dz \\
     e \; dz ∧ dx \\
     f \; dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

.. rubric:: Inhomogenous Maxwell equations

.. math::

   \begin{equation}
   \newcommand{\E}{\tilde{E}}
   \begin{matrix}
                & + ∂_x \E^x & + ∂_y \E^y & + ∂_z \E^z & = & + μ_0 c ρ \\
     + ∂_t \E^x &            & - ∂_y  B^z & + ∂_z  B^y & = & - μ_0 J^x \\
     + ∂_t \E^y & + ∂_x  B^z &            & - ∂_z  B^x & = & - μ_0 J^y \\
     + ∂_t \E^z & - ∂_x  B^y & + ∂_y  B^x &            & = & - μ_0 J^z \\
   \end{matrix}
   \end{equation}

.. math::

   \begin{equation}
   \newcommand{\_}{\phantom{∂_m m}} % Phantom for alignment
   ⋆d(⋆R^{♭♭})
   =
   \begin{bmatrix}
   (   \_    & - ∂_x a & - ∂_y b & - ∂_z c ) ⋆ dt \\
   ( - ∂_t a &   \_    & + ∂_y f & - ∂_z e ) ⋆ dx \\
   ( - ∂_t b & - ∂_x f &   \_    & + ∂_z d ) ⋆ dy \\
   ( - ∂_t c & + ∂_x e & - ∂_y d &   \_    ) ⋆ dz \\
   \end{bmatrix}
   \end{equation}

And we identify:

.. math::

   \begin{equation}
   \newcommand{\E}{\tilde{E}}
   \begin{matrix}
   \E^x = -a \\
   \E^y = -b \\
   \E^z = -c \\
    B^x = -d \\
    B^y = -e \\
    B^z = -f \\
   \end{matrix}
   \end{equation}

The Maxwell's equations are:

.. math::

   \begin{equation}
   \newcommand{\_}{\phantom{∂_m X^m}}
   \newcommand{\E}{\tilde{E}}
   \begin{bmatrix}
   (  \_       & + ∂_x \E^x & + ∂_y \E^y & + ∂_z \E^z) dt \\
   (+ ∂_t \E^x &   \_       & - ∂_y  B^z & + ∂_z  B^y) dx \\
   (+ ∂_t \E^y & + ∂_x  B^z &   \_       & - ∂_z  B^x) dy \\
   (+ ∂_t \E^z & - ∂_x  B^y & + ∂_y  B^x &   \_      ) dz \\
   \end{bmatrix}
   =
   \begin{bmatrix}
   + μ_0 c ρ \; dt \\
   - μ_0 J^x \; dx \\
   - μ_0 J^y \; dy \\
   - μ_0 J^z \; dz \\
   \end{bmatrix}
   \end{equation}

.. topic:: Electromagnetism is a Clockwise Twist in the Fabric of Spacetime

   .. math::

      \begin{equation}
      \newcommand{\E}{\tilde{E}}
      ⋆ d ⋆
      \begin{bmatrix}
        -\E^x \; dx ∧ dt \\
        -\E^y \; dy ∧ dt \\
        -\E^z \; dz ∧ dt \\
        - B^x \; dy ∧ dz \\
        - B^y \; dz ∧ dx \\
        - B^z \; dx ∧ dy \\
      \end{bmatrix}
      =
      \begin{bmatrix}
      + μ_0 c ρ \; dt \\
      - μ_0 J^x \; dx \\
      - μ_0 J^y \; dy \\
      - μ_0 J^z \; dz \\
      \end{bmatrix}
      \end{equation}

.. rubric:: Homogenous Maxwell equations

.. math::

   \begin{equation}
   \begin{matrix} \newcommand{\E}{\tilde{E}}
                & + ∂_x  B^x & + ∂_y  B^y & + ∂_z  B^z & = & 0 \\
     + ∂_t  B^x &            & + ∂_y \E^z & - ∂_z \E^y & = & 0 \\
     + ∂_t  B^y & - ∂_x \E^z &            & + ∂_z \E^x & = & 0 \\
     + ∂_t  B^z & + ∂_x \E^y & - ∂_y \E^x &            & = & 0 \\
   \end{matrix}
   \end{equation}

.. math::

   \begin{equation}\
   \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
   ⋆(dR^{♭♭}) =
   \begin{bmatrix}
     ( \; \phan   & - ∂_x d & - ∂_y e & - ∂_z f \; ) \; dt \\
     ( \; - ∂_t d & \phan   & - ∂_y c & + ∂_z b \; ) \; dx \\
     ( \; - ∂_t e & + ∂_x c & \phan   & - ∂_z a \; ) \; dy \\
     ( \; - ∂_t f & - ∂_x b & + ∂_y a & \phan   \; ) \; dz \\
   \end{bmatrix}
   \end{equation}

Wich were then written in the following matrix form.

.. math::

   \begin{equation}
   \newcommand{\Ex}{\tilde{E}^x}
   \newcommand{\Ey}{\tilde{E}^y}
   \newcommand{\Ez}{\tilde{E}^z}
   \newcommand{\Bx}{B^x}
   \newcommand{\By}{B^y}
   \newcommand{\Bz}{B^z}
   \begin{bmatrix}
           & + \Ex & + \Ey & + \Ez \\
     + \Ex &       & + \Bz & - \By \\
     + \Ey & - \Bz &       & + \Bx \\
     + \Ez & + \By & - \Bx &       \\
   \end{bmatrix}
   \end{equation}

.. math::

   \begin{equation}
   dR^{♭♭} =
   d
   \begin{bmatrix}
     -a \; dt ∧ dx \\
     -b \; dt ∧ dy \\
     -c \; dt ∧ dz \\
     +d \; dy ∧ dz \\
     +e \; dz ∧ dx \\
     +f \; dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

.. }}}
