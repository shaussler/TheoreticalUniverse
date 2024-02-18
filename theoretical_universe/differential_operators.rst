Differential operators in differential forms
============================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

In this article, I use the language of differential forms to express the
derivative, the gradient, the divergence, the curl and the laplacian in the
language of differential forms in three dimensions.

I assume the reader possesses a strong grasp of vector calculus and a
functional understanding of differential forms. To learn about differential
forms, I recommend `yet another great video serie by Michael Penn
<https://youtube.com/playlist?list=PL22w63XsKjqzQZtDZO_9s2HEMRJnaOTX7&si=4dDrAZ-oKa1rI7B8>`_.
I will try simplify the concept of the Hodge dual, often presented in a
needlessly complex manner, making it more accessible. A basic comprehension of
vectors, covectors, and tensor calculus will enhance the discussion.
Familiarity with the concepts of Grassman Algebra, Clifford Algebra (AKA
Geometric Algebra), Lie Groups and Algebra will certainly be a sign that the
reader understand the antisymmetry underlying differential forms.

The Hodge dual
--------------

.. {{{

.. }}}

Improving the notation of Cartan's formalism
--------------------------------------------

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

.. math::

   F^\sharp = F^i \partial_i

The basis covectors are the differentials:

.. math::

   \mathbf{e}^i = dx^i

Indeed get:

.. math::

   \mathbf{e}^i \cdot \mathbf{e}_j = dx^i \partial_j = \delta^i_j

Where :math:`g` is the metric tensor, and thus:

.. math::

   \begin{align}
   g_{ij} &= \partial_i \cdot \partial_j \\
   g^{ij} &= dx^i \cdot dx^j
   \end{align}

.. }}}

Derivative
----------

.. {{{

The partial derivatives are our basic vector:

.. math::

   \mathbf{e}_i = \partial_i

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

Laplace-de Rham operator
------------------------

Can be taken on functions and vectors.

.. admonition:: Proposition

   .. math::

      \Delta f = \delta d f

.. }}}
