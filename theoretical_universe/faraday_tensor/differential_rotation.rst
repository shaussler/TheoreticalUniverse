Maxwell Equations Are Rotations
===============================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

In this article, I derive the Maxwell equations in the frame of Cartan's
formalism and demonstrate that they represent the differential of a rotation in
Minkowski space.


Rotation in Space
-----------------

Take a rotation:

.. topic:: Rotation in Space

   .. math::
   
      \begin{equation}
      B^{♯♯}
      = \begin{bmatrix}
        a \; ∂_t ∧ ∂_x \\
        b \; ∂_t ∧ ∂_y \\
        c \; ∂_t ∧ ∂_z \\
        d \; ∂_y ∧ ∂_z \\
        e \; ∂_z ∧ ∂_x \\
        f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}
      \end{equation}

Rotation in Differential Form
-----------------------------

Determine the associated differential form. In other words, we fully flatten:

.. math::

   \begin{equation}
   B^{♭♭} = (B^{♯♯})^{♭♭}
   \end{equation}

Expand the full expression and distribute the flat operators :math:`♭`:

.. math::

   \begin{equation}
   B^{♭♭} =
   \begin{bmatrix}
     a \; ∂_t^♭ ∧ ∂_x^♭ \\
     b \; ∂_t^♭ ∧ ∂_y^♭ \\
     c \; ∂_t^♭ ∧ ∂_z^♭ \\
     d \; ∂_y^♭ ∧ ∂_z^♭ \\
     e \; ∂_z^♭ ∧ ∂_x^♭ \\
     f \; ∂_x^♭ ∧ ∂_y^♭ \\
   \end{bmatrix}
   \end{equation}

Expand and take out the Minkowski metric as the wedge product :math:`∧` is
bilinear:

.. math::

   \begin{equation}
   B^{♭♭}
   =
   \begin{bmatrix}
     a η_{αt} \; dx^α ∧ η_{βx} \; dx^β \\
     b η_{αt} \; dx^α ∧ η_{βy} \; dx^β \\
     c η_{αt} \; dx^α ∧ η_{βz} \; dx^β \\
     d η_{αy} \; dx^α ∧ η_{βz} \; dx^β \\
     e η_{αz} \; dx^α ∧ η_{βx} \; dx^β \\
     f η_{αx} \; dx^α ∧ η_{βy} \; dx^β \\
   \end{bmatrix}
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

Identify the non-zero components and apply numerical values

.. math::

   \begin{equation}
   B^{♭♭}
   =
   \begin{bmatrix}
     a \; η_{tt} η_{xx} \; dx^t ∧ dx^x \\
     b \; η_{tt} η_{yy} \; dx^t ∧ dx^y \\
     c \; η_{tt} η_{zz} \; dx^t ∧ dx^z \\
     d \; η_{yy} η_{zz} \; dx^y ∧ dx^z \\
     e \; η_{zz} η_{xx} \; dx^z ∧ dx^x \\
     f \; η_{xx} η_{yy} \; dx^x ∧ dx^y \\
   \end{bmatrix}
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

We get:

.. topic:: Rotation in Differential Form

   .. math::
   
      \begin{equation}
      B^{♭♭}
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

Differential Rotation
---------------------

Apply the differential operator :math:`d`:

.. math::

   \begin{equation}
   dR =
   d
   \begin{bmatrix}
     -a \; dx^t ∧ dx^x \\
     -b \; dx^t ∧ dx^y \\
     -c \; dx^t ∧ dx^z \\
     +d \; dx^y ∧ dx^z \\
     +e \; dx^z ∧ dx^x \\
     +f \; dx^x ∧ dx^y \\
   \end{bmatrix}
   =
   \begin{bmatrix}
     d(-a \; dx^t ∧ dx^x) \\
     d(-b \; dx^t ∧ dx^y) \\
     d(-c \; dx^t ∧ dx^z) \\
     d(+d \; dx^y ∧ dx^z) \\
     d(+e \; dx^z ∧ dx^x) \\
     d(+f \; dx^x ∧ dx^y) \\
   \end{bmatrix}
   \end{equation}

Expand:

.. math::

   \begin{equation}
   dR =
   \begin{bmatrix}
     ∂_y (-a) \; dx^y ∧ dx^t ∧ dx^x & ∂_z (-a) \; dx^z ∧ dx^t ∧ dx^x\\
     ∂_x (-b) \; dx^x ∧ dx^t ∧ dx^y & ∂_z (-b) \; dx^z ∧ dx^t ∧ dx^y\\
     ∂_x (-c) \; dx^x ∧ dx^t ∧ dx^z & ∂_y (-c) \; dx^y ∧ dx^t ∧ dx^z\\
     ∂_t (+d) \; dx^t ∧ dx^y ∧ dx^z & ∂_x (+d) \; dx^x ∧ dx^y ∧ dx^z\\
     ∂_t (+e) \; dx^t ∧ dx^z ∧ dx^x & ∂_y (+e) \; dx^y ∧ dx^z ∧ dx^x\\
     ∂_t (+f) \; dx^t ∧ dx^x ∧ dx^y & ∂_z (+f) \; dx^z ∧ dx^x ∧ dx^y\\
   \end{bmatrix}
   \end{equation}

Reorder:

.. math::

   \begin{equation}
   dR =
   \begin{bmatrix}
     ∂_y (-a) \; (+1) \; dx^t ∧ dx^x ∧ dx^y & ∂_z (-a) \; (-1) \; dx^t ∧ dx^z ∧ dx^x \\
     ∂_x (-b) \; (-1) \; dx^t ∧ dx^x ∧ dx^y & ∂_z (-b) \; (+1) \; dx^t ∧ dx^y ∧ dx^z \\
     ∂_x (-c) \; (+1) \; dx^t ∧ dx^z ∧ dx^x & ∂_y (-c) \; (-1) \; dx^t ∧ dx^y ∧ dx^z \\
     ∂_t (+d) \; (+1) \; dx^t ∧ dx^y ∧ dx^z & ∂_x (+d) \; (+1) \; dx^x ∧ dx^y ∧ dx^z \\
     ∂_t (-e) \; (-1) \; dx^t ∧ dx^z ∧ dx^x & ∂_y (+e) \; (+1) \; dx^x ∧ dx^y ∧ dx^z \\
     ∂_t (+f) \; (+1) \; dx^t ∧ dx^x ∧ dx^y & ∂_z (+f) \; (+1) \; dx^x ∧ dx^y ∧ dx^z \\
   \end{bmatrix}
   \end{equation}

Simplify

.. math::

   \begin{equation}
   dR =
   \begin{bmatrix}
     ∂_y (-a) \; dx^t ∧ dx^x ∧ dx^y & ∂_z (+a) \; dx^t ∧ dx^z ∧ dx^x \\
     ∂_x (+b) \; dx^t ∧ dx^x ∧ dx^y & ∂_z (-b) \; dx^t ∧ dx^y ∧ dx^z \\
     ∂_x (+c) \; dx^t ∧ dx^x ∧ dx^z & ∂_y (+c) \; dx^t ∧ dx^y ∧ dx^z \\
     ∂_t (+d) \; dx^t ∧ dx^y ∧ dx^z & ∂_x (+d) \; dx^x ∧ dx^y ∧ dx^z \\
     ∂_t (+e) \; dx^t ∧ dx^z ∧ dx^x & ∂_y (+e) \; dx^x ∧ dx^y ∧ dx^z \\
     ∂_t (+f) \; dx^t ∧ dx^x ∧ dx^y & ∂_z (+f) \; dx^x ∧ dx^y ∧ dx^z \\
   \end{bmatrix}
   \end{equation}

Reorder:

.. math::

   \begin{equation}
   dR =
   \begin{bmatrix}
     ∂_x (+d) \; dx^x ∧ dx^y ∧ dx^z & ∂_y (+e) \; dx^x ∧ dx^y ∧ dx^z & ∂_z (+f) \; dx^x ∧ dx^y ∧ dx^z \\
     ∂_t (+d) \; dx^t ∧ dx^y ∧ dx^z & ∂_y (+c) \; dx^t ∧ dx^y ∧ dx^z & ∂_z (-b) \; dx^t ∧ dx^y ∧ dx^z \\
     ∂_t (+e) \; dx^t ∧ dx^z ∧ dx^x & ∂_x (-c) \; dx^t ∧ dx^z ∧ dx^x & ∂_z (+a) \; dx^t ∧ dx^z ∧ dx^x \\
     ∂_t (+f) \; dx^t ∧ dx^x ∧ dx^y & ∂_x (+b) \; dx^t ∧ dx^x ∧ dx^y & ∂_y (-a) \; dx^t ∧ dx^x ∧ dx^y \\
   \end{bmatrix}
   \end{equation}

Gather:

.. math::

   \begin{equation}
   dR =
   \begin{bmatrix}
     (+ ∂_x d + ∂_y e +∂_z f) \; dx^x ∧ dx^y ∧ dx^z \\
     (+ ∂_t d + ∂_y c -∂_z b) \; dx^t ∧ dx^y ∧ dx^z \\
     (+ ∂_t e + ∂_x c +∂_z a) \; dx^t ∧ dx^z ∧ dx^x \\
     (+ ∂_t f + ∂_x b -∂_y a) \; dx^t ∧ dx^x ∧ dx^y \\
   \end{bmatrix}
   \end{equation}

See what is about to happen

.. math::

   \begin{equation}
   dR =
   \begin{bmatrix}
     ( &   &       & + & ∂_x d & + & ∂_y e & + & ∂_z f & ) & dx^x ∧ dx^y ∧ dx^z \\
     ( & + & ∂_t d & + &       & + & ∂_y c & - & ∂_z b & ) & dx^t ∧ dx^y ∧ dx^z \\
     ( & + & ∂_t e & - & ∂_x c &   &       & + & ∂_z a & ) & dx^t ∧ dx^z ∧ dx^x \\
     ( & + & ∂_t f & + & ∂_x b & - & ∂_y a &   &       & ) & dx^t ∧ dx^x ∧ dx^y \\
   \end{bmatrix}
   \end{equation}

Take the Hodge dual:

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

Conclude:

.. topic:: Hodge Dual of the Differential of Rotations in Differential Form

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

The inhomogenous equations
--------------------------

FirstHer we concentrate on the inhomogenous equations. In a previous article, we
have derived from the 1865 Maxell equations the following relations. 

.. math::

   \begin{matrix}
               & +∂_x \Ex & + ∂_y \Ey & + ∂_z \Ez & = & + μ_0 c ρ \\
     + ∂_t \Ex &          & - ∂_y \Bz & + ∂_z \By & = & - μ_0 J^x \\
     + ∂_t \Ey & +∂_x \Bz &           & - ∂_z \Bx & = & - μ_0 J^y \\
     + ∂_t \Ez & -∂_x \By & + ∂_y \Bx &           & = & - μ_0 J^z \\
   \end{matrix}

Wich were then written in the following matrix form.

.. math::

   \begin{bmatrix}
       ∂_t & ∂_x & ∂_y & ∂_z \\
   \end{bmatrix}
   \begin{bmatrix}
            & +\Ex & +\Ey & +\Ez \\
       +\Ex &      & +\Bz & -\By \\
       +\Ey & -\Bz &      & +\Bx \\
       +\Ez & +\By & -\Bx &      \\
   \end{bmatrix}
   =
   \begin{bmatrix}
       + μ_0 c ρ & - μ_0 J^x  & - μ_0 J^y  & - μ_0 J^z \\
   \end{bmatrix}

From there, we had deduced the tensor formulation in Abstract Index Notation.

