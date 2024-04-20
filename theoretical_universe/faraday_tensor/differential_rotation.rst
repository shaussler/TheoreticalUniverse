Of Maxwell Equations and Rotations
==================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

This article investigates the connection between :ref:`rotations
<rotation_in_the_cartan_hodge_formalism>`, the exterior derivative, and the
equations of Mr. Maxwell. I utilize :ref:`the Cartan-Hodge's formalism
<the_cartan_hodge_formalism>` together with Minkowski space-time. I demonstrate
that applying the exterior derivative to rotations yields the equations
governing electromagnetism. These experssions reveal Maxwell equations are a
twist in the fabric of spacetime.

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

Rotation as Differential Forms
------------------------------

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

   Apply the numerical values of the :math:`η` components:

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        a \; (+1) (-1) \; dx^t ∧ dx^x \\
        b \; (+1) (-1) \; dx^t ∧ dx^y \\
        c \; (+1) (-1) \; dx^t ∧ dx^z \\
        d \; (-1) (-1) \; dx^y ∧ dx^z \\
        e \; (-1) (-1) \; dx^z ∧ dx^x \\
        f \; (-1) (-1) \; dx^x ∧ dx^y \\
      \end{bmatrix}
      \end{equation}

   Conclude:

   .. math::

      \begin{equation}
      R^{♭♭}
      =
      \begin{bmatrix}
        -a \; dx^t ∧ dx^x \\
        -b \; dx^t ∧ dx^y \\
        -c \; dx^t ∧ dx^z \\
        +d \; dx^y ∧ dx^z \\
        +e \; dx^z ∧ dx^x \\
        +f \; dx^x ∧ dx^y \\
      \end{bmatrix}
      \end{equation}

   .. }}}

.. }}}

The exterior Derivative of a Rotation
-------------------------------------

Apply the exterior derivative operator :math:`d`:

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

   Notice the terms are ordered along the diagonals, which makes it easy to
   pick up, gather and re-order. When ordering into a column we choose:

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

   Optionally, we can take the :ref:`Hodge dual <duality_in_minkowski_space>`
   to transform 3-forms elements to 1-forms:

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

The inhomogenous equations
--------------------------

FirstHer we concentrate on the inhomogenous equations. In a previous article, we
have derived from the 1865 Maxell equations the following relations. 

.. math::

   \begin{equation}
   \newcommand{\Ex}{\tilde{E}^x}
   \newcommand{\Ey}{\tilde{E}^y}
   \newcommand{\Ez}{\tilde{E}^z}
   \newcommand{\Bx}{B^x}
   \newcommand{\By}{B^y}
   \newcommand{\Bz}{B^z}
   \begin{matrix}
               & +∂_x \Ex & + ∂_y \Ey & + ∂_z \Ez & = & + μ_0 c ρ \\
     + ∂_t \Ex &          & - ∂_y \Bz & + ∂_z \By & = & - μ_0 J^x \\
     + ∂_t \Ey & +∂_x \Bz &           & - ∂_z \Bx & = & - μ_0 J^y \\
     + ∂_t \Ez & -∂_x \By & + ∂_y \Bx &           & = & - μ_0 J^z \\
   \end{matrix}
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

From there, we had deduced the tensor formulation in Abstract Index Notation.

