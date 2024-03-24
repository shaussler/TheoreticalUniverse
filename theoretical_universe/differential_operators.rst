Differential operators in differential forms
============================================

.. rst-class:: custom-author

   by Stéphane Haussler

In this article, I use the language of differential forms to systematically
express the derivative, the gradient, the divergence, the curl and the
laplacian in three dimensions. I will simplify the concept of the Hodge dual in
three dimensions, making it more accessible.

I assume the reader possesses a strong grasp of vector calculus and a
functional understanding of differential forms. To learn about differential
forms, I can only recommend `yet another great video serie by Michael Penn
<https://youtube.com/playlist?list=PL22w63XsKjqzQZtDZO_9s2HEMRJnaOTX7&si=4dDrAZ-oKa1rI7B8>`_.
Implicitely assumed with the above requirements is the understanding of tensor
calculus, and in particular the concept of vectors and covectors. Some basic
familiarity with the concepts of Grassman Algebra, Clifford Algebra (AKA
Geometric Algebra), Lie Groups and Algebra is not necessary but welcome for the
understanding of the antisymmetries at hand.

The Hodge dual
--------------

.. {{{

The concept of the Hodge dual is often presented in a needlessly complex
manner, taking into account from the get go a number of dimensions above three,
and any metric signatures. When the actually quite natural and simple concept
of the Hodge dual is undersood with the three dimensions we are accustomed to
live in, extending to the 4-dimensional Minkowski space may feel quite natural.

First consider a coordinate basis in 3 dimensions that corresponds to our
intuitive understanding of dimensions :math:`\mathbf{e}_x`,
:math:`\mathbf{e}_y` and :math:`\mathbf{e}_z`. Now observe that we did not
merely define three unit vectors, but also three *unit surfaces* that we name
using the wedge :math:`\wedge` symbol :math:`\mathbf{e}_x \wedge \mathbf{e}_y`,
:math:`\mathbf{e}_y \wedge \mathbf{e}_z`, and :math:`\mathbf{e}_z \wedge
\mathbf{e}_x`:

.. image:: _static/hodge_dual_coordinates.png
   :align: center
   :width: 60%

The naming of the surfaces is carefully chosen counterclock wise. The reason is
that given a vector together with a number for the surface, we can uniquely
determine the second vector needed to obtain that surface. The surface need be
oriented and a sign convention chosen (Here counterclockwise is positive). For
example, :math:`\mathbf{e}_z \wedge \mathbf{e}_x = - \mathbf{e}_x \wedge
\mathbf{e}_z`. Each basis surface can be associated with a unique basis vector:

.. math::

   \mathbf{e}_x \wedge \mathbf{e}_y \rightarrow \mathbf{e}_z \\
   \mathbf{e}_y \wedge \mathbf{e}_z \rightarrow \mathbf{e}_x \\
   \mathbf{e}_z \wedge \mathbf{e}_x \rightarrow \mathbf{e}_y

Using the :math:`\star` Hodge dual operator to describe that relation, we have:

.. math::

   \star \mathbf{e}_x \wedge \mathbf{e}_y = \mathbf{e}_z \\
   \star \mathbf{e}_y \wedge \mathbf{e}_z = \mathbf{e}_x \\
   \star \mathbf{e}_z \wedge \mathbf{e}_x = \mathbf{e}_y

This association defines a dual vector to every oriented surfaces and is called
the Hodge dual, noted with the star :math:`\star` operator. The relation holds
in both direction:

.. math::

   \star \mathbf{e}_z = \mathbf{e}_x \wedge \mathbf{e}_y \\
   \star \mathbf{e}_x = \mathbf{e}_y \wedge \mathbf{e}_z \\
   \star \mathbf{e}_y = \mathbf{e}_z \wedge \mathbf{e}_x

The Hodge dual in three dimensions is the cross product. The cross product
defines a vector perpendicular to the surface whose length is proportional to
the amount of rotation:

.. math::

   \mathbf{e}_x \times \mathbf{e}_y = \star \mathbf{e}_x \wedge \mathbf{e}_y = \mathbf{e}_z \\
   \mathbf{e}_y \times \mathbf{e}_z = \star \mathbf{e}_y \wedge \mathbf{e}_z = \mathbf{e}_x \\
   \mathbf{e}_z \times \mathbf{e}_x = \star \mathbf{e}_z \wedge \mathbf{e}_x = \mathbf{e}_y

This establishes the deep connection between the Hodge dual, rotations,
surfaces, and the cross product.

Going one step futher, we observe that we did not merely define unit surfaces,
but also unit volumes that we note :math:`\mathbf{e}_x \wedge \mathbf{e}_y
\wedge \mathbf{e}_z`. We can associate the unit volume with numbers:

.. math::

   \star \mathbf{1} = \mathbf{e}_x \wedge \mathbf{e}_y \wedge \mathbf{e}_z

As well as:

.. math::

   \star \mathbf{e}_x \wedge \mathbf{e}_y \wedge \mathbf{e}_z = \mathbf{1}

Where :math:`\mathbf{1}` is the unit number. In other words any number can be
expressed as a linear combination of :math:`1`.

For the vector basis the following objects are defined:

* Real numbers.
* Vectors.
* Bivectors correspoding to surfaces and often called pseudo-vectors.
* Trivectors corresponding to volumes and often called pseudo-scalars.

Placing a mirror in front of this object:

* Scalars (Real numbers) are not changed.
* Vector are not changed.
* Surfaces are flipped and the sign changes.
* Volumes are flipped and the sign changes.

This is the reason behind the naming *pseudo-vector*. When placed in front of a
mirror, the sign of a positive oriented surface goes to negative. The
corresponding Hodge dual to the surface is a vector, and the Hodge dual of the
positive surface is a vector which is flipped. These objects are associated to
vectors that do not behave like a vector in front of a mirror.

This is also the reason behind the name *pseudo-scalar*. When placed in front
of a mirror, the sign of a positive oriented volume goes to negative. The Hodge
dual of the positive the volume is positive scalar. The sign of the Hodge dual
of the image is a negative scalar. These objects are associated to scalars that
do not behave like scalars in front of a mirror.

.. }}}

Improving on the notation of Cartan's formalism
-----------------------------------------------

.. {{{

I will be using matrix notation in a manner which is not fully conventional,
but that I hope highlight symmetries and the reader will find obvious.
Everything in a matrix is expressed with its basis vectors and can be reordered
at will. For example, a vector is often expressed as:

.. math::

   v = \{ x \\ y \\ z\}

I merely propse to explicitely write the basis explicitely:

.. math::

   v = \{ x \mathbf{e}_x \\ y \mathbf{e}_y \\ z \mathbf{e}_x \}

Which really means that a :math:`+` sign can be added anywhere and the
expression written in the standard form:

.. math::

   v = x \mathbf{e}_x + y \mathbf{e}_y + z \mathbf{e}_x 

This is quite powerfull when using a pseudo-vector or pseudo-scalar basis:

.. math::

   \{                                          & +a^{xy} \mathbf{e}_x \wedge \mathbf{e}_y & -a^{zx} \mathbf{e}_x \wedge \mathbf{e}_z \\
      -a^{xy} \mathbf{e}_y \wedge \mathbf{e}_x &                                          & +a^{yz} \mathbf{e}_y \wedge \mathbf{e}_z \\
      +a^{zx} \mathbf{e}_z \wedge \mathbf{e}_x & -a^{yz} \mathbf{e}_y \wedge \mathbf{e}_y &                                          \}

That we can for example reorder if we want to:

.. math::

   \{ + 2 a^{yz} \mathbf{e}_y \wedge \mathbf{e}_z \\
      + 2 a^{zx} \mathbf{e}_z \wedge \mathbf{e}_x \\
      + 2 a^{xy} \mathbf{e}_x \wedge \mathbf{e}_y \}

Or write as a sum:

.. math::

   2 a^{yz} \mathbf{e}_y \wedge \mathbf{e}_z +
   2 a^{zx} \mathbf{e}_z \wedge \mathbf{e}_x +
   2 a^{xy} \mathbf{e}_x \wedge \mathbf{e}_y

And we can write a covector in the same explicit manner. This notation is
extremely conveniant when performing calculations in Cartan's framework and
permits also to fall back on regular matrix multiplication or express tensors
in the same convenient manner.

.. }}}

Notation
--------

.. {{{

The vector field :math:`\mathbf{F}` is noted with the musical isomorphism
:math:`\sharp` as :math:`F^\sharp`, which either declare :math:`F` is a vector,
or transform a covector to a vector:

.. math::

   \mathbf{F}=F^\sharp=(F^\sharp)^\sharp=(F^\flat)^\sharp

The component of :math:`F^\sharp` are noted with upper indices consistently
with the rules of Ricci calculus and utilizing Einstein summation convention.

.. }}}

Derivative
----------

.. {{{

The partial derivatives are our basis vectors:

.. math::

   \mathbf{e}_i = \partial_i

.. }}}

Differential
------------

.. {{{

The differentials are our basis covectors:

.. math::

   \mathbf{e}^i = dx^i

.. }}}

Gradiant
--------

.. {{{

.. admonition:: Proposition

   .. math::

      (df)^{\sharp} = \mathbf{\nabla} f

.. math::

   \begin{align}
   df^{\sharp} & = ( \partial_x f dx + \partial_y f dy + \partial_z f dz )^{\sharp} \\
               & = \partial_x f (dx)^{\sharp} + \partial_y f (dy)^{\sharp} + \partial_z f (dz)^{\sharp} \\
               & = \partial_x f \partial_x + \partial_y f \partial_y + \partial_z f \partial_z \\
   \end{align}

.. }}}

Divergence
----------

.. {{{

.. admonition:: Proposition

   .. math::

      \star d \star F^\flat = \mathbf{\nabla} \cdot \mathbf{F}

.. admonition:: Proposition

   .. math::

      \nabla^\flat F^\sharp = \mathbf{\nabla} \cdot \mathbf{F}

We begin with :math:`F` as a vector :math:`\mathbf{F} = F^\sharp = F^i
\partial_i` and flatten:

.. math::

   F^\flat = \{ F^x \partial_x \\
                F^y \partial_y \\
                F^z \partial_z \}^\flat
           = \{ F^x dx \\
                F^y dy \\
                F^z dz \}

Apply the :math:`\star` operator:

.. math::

   \star F^\flat = \{ F^x \star dx     \\ F^y \star dy     \\ F^z \star dz     \}
                 = \{ F^x dy \wedge dz \\ F^y dz \wedge dx \\ F^z dx \wedge dy \}

Apply the :math:`d` operator:

.. math::

   d \star F^\flat = d \{ F^x dy \wedge dz \\
                          F^y dz \wedge dx \\
                          F^z dx \wedge dy \}
   = \{ \partial_x F^x dx \wedge dy \wedge dz \\
        \partial_y F^y dy \wedge dz \wedge dx \\
        \partial_z F^z dz \wedge dx \wedge dy \}
   = \{ \partial_x F^x dx \wedge dy \wedge dz \\
        \partial_y F^y dx \wedge dy \wedge dz \\
        \partial_z F^z dx \wedge dy \wedge dz \}

Which can be brought back to a zero form by applying yet again the Hodge star: 

.. math::

   \star d \star F^\flat
   = \{ \partial_x F^x \star dx \wedge dy \wedge dz \\
        \partial_y F^y \star dx \wedge dy \wedge dz \\
        \partial_z F^z \star dx \wedge dy \wedge dz \}
   = \{ \partial_x F^x \mathbf{1} \\
        \partial_y F^y \mathbf{1} \\
        \partial_z F^z \mathbf{1} \}
   = \partial_x F^x + \partial_y F^y + \partial_z F^z

.. }}}

Curl
----

.. {{{

.. admonition:: Proposition

   .. math::
   
      (\star(dF^\flat))^\sharp = \nabla^\sharp \times F^\sharp


The full expression of the curl of a vector field is

.. math::

   \nabla^\sharp \times F^\sharp =
   \{ (\partial_y F^z - \partial F^y) \; \partial_x \\
      (\partial_z F^x - \partial F^z) \; \partial_y \\
      (\partial_x F^y - \partial F^x) \; \partial_z \}

We demonstrate this is also equal to:

The vector field is:

.. math::

   F^\sharp = \{ F^x \px \\ F^y \py \\ F^z \pz \}
            = F^x \px + F^y \py + F^z \pz

Flattening the vector field result in:

.. math::

   F^\flat = \{ F^x dx \\ F^y dy \\ F^z dz \}
           = F^x dx + F^y dy + F^z dz

Taking the differential, we have: 

.. math::

   dF^\flat =
   \{ \partial_x F^x dx \wedge dx & \partial_y F^x dy \wedge dx & \partial_z F^x dz \wedge dx \\
      \partial_x F^y dx \wedge dy & \partial_y F^y dy \wedge dy & \partial_z F^y dz \wedge dy \\
      \partial_x F^z dx \wedge dz & \partial_y F^z dy \wedge dy & \partial_z F^z dz \wedge dz \}

Or with more natural row/column convention:

.. math::

   dF^\flat =
   \{ \partial_x F^x dx \wedge dx & \partial_x F^y dx \wedge dy & \partial_x F^z dx \wedge dz \\
      \partial_y F^x dy \wedge dx & \partial_y F^y dy \wedge dy & \partial_y F^z dy \wedge dy \\
      \partial_z F^x dz \wedge dx & \partial_z F^y dz \wedge dy & \partial_z F^z dz \wedge dz \}

Where :math:`dx^i \wedge dx^i = 0`:

.. math::

   dF^\flat =
   \{                             & \partial_x F^y dx \wedge dy & \partial_x F^z dx \wedge dz \\
      \partial_y F^x dy \wedge dx &                             & \partial_y F^z dy \wedge dy \\
      \partial_z F^x dz \wedge dx & \partial_z F^y dz \wedge dy &                             \}


And :math:`dx^i \wedge dx^j = -dx^j \wedge dx^i`:

.. math::

   dF^\flat =
   \{                              & +\partial_x F^y dx \wedge dy & -\partial_x F^z dz \wedge dx \\
      -\partial_y F^x dx \wedge dy &                              & +\partial_y F^z dy \wedge dy \\
      +\partial_z F^x dz \wedge dx & -\partial_z F^y dy \wedge dz &                              \}

That we reorder to:

.. math::

   dF^\flat =
   \{ +\partial_y F^z dy \wedge dy - \partial_z F^y dy \wedge dz \\
      +\partial_z F^x dz \wedge dx - \partial_x F^z dz \wedge dx \\
      +\partial_x F^y dx \wedge dy - \partial_y F^x dx \wedge dy \}

.. math::

   dF^\flat =
   \{ (\partial_y F^z - \partial_z F^y) dy \wedge dz \\
      (\partial_z F^x - \partial_x F^z) dz \wedge dx \\
      (\partial_x F^y - \partial_y F^x) dx \wedge dy \}

Where we can now take the star operator:

.. math::

   \star dF^\flat =
   \{ (\partial_y F^z - \partial_z F^y) \star dy \wedge dz \\
      (\partial_z F^x - \partial_x F^z) \star dz \wedge dx \\
      (\partial_x F^y - \partial_y F^x) \star dx \wedge dy \}

.. math::

   \star dF^\flat =
   \{ (\partial_y F^z - \partial_z F^y) dx \\
      (\partial_z F^x - \partial_x F^z) dy \\
      (\partial_x F^y - \partial_y F^x) dz \}

We can then sharpen the covector to its vector form:

.. math::

   (\star dF^\flat)^\sharp
   =
   \{ (\partial_y F^z - \partial_z F^y) dx^\sharp \\
      (\partial_z F^x - \partial_x F^z) dy^\sharp \\
      (\partial_x F^y - \partial_y F^x) dz^\sharp \}

.. math::

   (\star dF^\flat)^\sharp
   =
   \{ (\partial_y F^z - \partial_z F^y) \px \\
      (\partial_z F^x - \partial_x F^z) \py \\
      (\partial_x F^y - \partial_y F^x) \pt \}

.. }}}

Laplacian
---------

.. {{{

.. admonition:: Proposition

   .. math::

      \star d \star d f = \mathbf{\nabla}^2 f

The differential of a function (zero form) is:

.. math::

   df = \partial_x f dx + \partial_y f dy + \partial_z f dz

Taking the Hodge dual:

.. math::

   \star df = \partial_x f dy \wedge dz + \partial_y dz \wedge dx + \partial_z f dx \wedge dy

Taking the differential

.. math::

   \begin{align}
   d \star df &= \frac{\partial^2 f}{\partial x} dx \wedge dy \wedge dz +
                 \frac{\partial^2 f}{\partial y} dy \wedge dz \wedge dx +
                 \frac{\partial^2 f}{\partial z} dz \wedge dx \wedge dy \\
              &= \frac{\partial^2 f}{\partial x} dx \wedge dy \wedge dz +
                 \frac{\partial^2 f}{\partial y} dx \wedge dy \wedge dz +
                 \frac{\partial^2 f}{\partial z} dx \wedge dy \wedge dz \\
              &= (
                     \frac{\partial^2 f}{\partial x} +
                     \frac{\partial^2 f}{\partial y} +
                     \frac{\partial^2 f}{\partial z}
                 ) dx \wedge dy \wedge dz \\
   \end{align}

Taking the Hodge dual, we tranform volumes to functions and obtain the
expression for the laplacian:

.. math::

   \star d \star df = (
       \frac{\partial^2 f}{\partial x} +
       \frac{\partial^2 f}{\partial y} +
       \frac{\partial^2 f}{\partial z}
   )

.. }}}

Laplace operator
----------------

.. {{{

The Laplace operator is defined on functions:

.. admonition:: Proposition

   .. math::

      \Delta f = \star d \star d f

.. }}}

Laplace-de Rham operator
------------------------

.. {{{

.. warning::

   Under construction

The Laplace operator can be generalized to the Laplace-deRham operator
:math:`\Delta = d \delta + \delta d` where `\delta = (-1)^k \star d \star`.

.. }}}
