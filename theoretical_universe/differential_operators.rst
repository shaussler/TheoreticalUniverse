Differential Operators
======================

.. rst-class:: custom-author

   by Stéphane Haussler

In this article, I use the language of differential forms to systematically
express the derivative, the differential, the gradient, the divergence, the
curl and the laplacian in three dimensions.

I assume the reader possesses a strong grasp of vector calculus, a working
understanding of differential forms and the wedge product, as well as of
:ref:`the Hoddge dual <hodge_duality>`. To learn about differential forms, `see
yet another great video serie by Michael Penn
<https://youtube.com/playlist?list=PL22w63XsKjqzQZtDZO_9s2HEMRJnaOTX7&si=4dDrAZ-oKa1rI7B8>`_.
Implicitely assumed with the above requisites is a basic understanding of
tensor calculus, and in particular the concept of vector and covector. Some
familiarity with the concepts of of either Grassman Algebra, Clifford Algebra
(AKA Geometric Algebra), or Lie Algebra is not necessary but certainly welcome
for a deeper understanding of the antisymmetries at hand.

Derivative
----------

.. {{{

The partial derivatives are the basis vectors. I am personally still wrapping
my head around it and refer for details to `Tangent Space Basis
<https://www.youtube.com/watch?v=rWSoPR8j6Gg>`_ and `Constructing Tangent
Vectors <https://www.youtube.com/watch?v=rWSoPR8j6Gg&t>`_ by `qncubed3
<https://www.youtube.com/@qncubed3>`_, or `Coordinate Basis
<https://www.youtube.com/watch?v=BjU8-n4ixqo&list=PLBh2i93oe2qvRGAtgkTszX7szZDVd6jh1&index=22>`_
by `brightsideofmaths <https://www.youtube.com/@brightsideofmaths>`_.

.. topic:: Proposition

   .. math::
   
      \mathbf{e}_i = \partial_i

.. }}}

Differential
------------

.. {{{

The differential applied to the partial derivative results in:

.. math::

   dx^i ∂_j = δ^i_j

This is the definition for a covector, and we conclude that the differential
operator is a covector.

.. topic:: Proposition

   .. math::
   
      \mathbf{e}^i = dx^i

.. }}}

Gradient
--------

.. {{{

.. topic:: Proposition

   .. math::

      (df)^{\sharp} = \mathbf{\nabla} f

Expand :math:`df`:

.. math::

   \begin{equation}
   (df)^♯ = ( dx ∂_x f + dy ∂_y f + dz ∂_z f)^♯
   \end{equation}

Distribute the sharp operator :math:`♯`:

.. math::

   \begin{equation}
   (df)^♯ = (dx)^♯ ∂_x f + (dy)^♯ ∂_y f + (dz)^♯ ∂_z f
   \end{equation}

Which permits to conclude:

.. math::

   \begin{equation}
   (df)^♯ = ∂_x f ∂_x + ∂_y f ∂_y + ∂_z f ∂_z
   \end{equation}

In other words and for clarity:

.. math::

   \begin{equation}
   \newcommand{\e}{\mathbf{e}}
   (df)^♯ = ∂_x f \e_x + ∂_y f \e_y + ∂_z f \e_z
   \end{equation}

.. }}}

Divergence
----------

.. {{{

.. topic:: Proposition

   .. math::

      \star d \star F^\flat = \mathbf{\nabla} \cdot \mathbf{F}

We begin with :math:`F` as a vector :math:`\mathbf{F} = F^\sharp = F^i
\partial_i` and flatten:

.. math::

   F^♭ = \begin{bmatrix}
           F^x ∂_x \\
           F^y ∂_y \\
           F^z ∂_z \\
         \end{bmatrix}^♭
       = \begin{bmatrix}
           F^x (∂_x)^♭ \\
           F^y (∂_y)^♭ \\
           F^z (∂_z)^♭ \\
         \end{bmatrix}
       = \begin{bmatrix}
           F^x dx \\
           F^y dy \\
           F^z dz \\
         \end{bmatrix}

Apply the :math:`\star` operator:

.. math::

   \star F^\flat
   = ⋆
   \begin{bmatrix}
     F^x dx \\
     F^y dy \\
     F^z dz \\
   \end{bmatrix}
   =
   \begin{bmatrix}
     F^x ⋆ dx \\
     F^y ⋆ dy \\
     F^z ⋆ dz \\
   \end{bmatrix}
   =
   \begin{bmatrix}
     F^x dy ∧ dz \\
     F^y dz ∧ dx \\
     F^z dx ∧ dy \\
   \end{bmatrix}

Apply the :math:`d` operator:

.. math::

   d ⋆ F^♭ = d
   \begin{bmatrix}
     F^x dy \wedge dz \\
     F^y dz \wedge dx \\
     F^z dx \wedge dy \\
   \end{bmatrix}
   =
   \begin{bmatrix}
     ∂_x F^x dx ∧ dy ∧ dz \\
     ∂_y F^y dy ∧ dz ∧ dx \\
     ∂_z F^z dz ∧ dx ∧ dy \\
   \end{bmatrix}
   =
   \begin{bmatrix}
   ∂_x F^x dx ∧ dy ∧ dz \\
   ∂_y F^y dx ∧ dy ∧ dz \\
   ∂_z F^z dx ∧ dy ∧ dz \\
   \end{bmatrix}

Which can be brought back to a zero form by applying yet again the Hodge star
:math:`⋆`:

.. math::

   ⋆ d ⋆ F^♭
   =
   \begin{bmatrix}
     ∂_x F^x ⋆ dx ∧ dy ∧ dz \\
     ∂_y F^y ⋆ dx ∧ dy ∧ dz \\
     ∂_z F^z ⋆ dx ∧ dy ∧ dz \\
   \end{bmatrix}
   =
   \begin{bmatrix}
     ∂_x F^x \mathbf{1} \\
     ∂_y F^y \mathbf{1} \\
     ∂_z F^z \mathbf{1} \\
   \end{bmatrix}
   = ∂_x F^x + ∂_y F^y + ∂_z F^z

.. }}}

Curl
----

.. {{{

.. topic:: Proposition

   .. math::

      (⋆(dF^♭))^♯ = ∇^♯ ⨯ F^♯

The full expression of the curl of a vector field is

.. math::

   ∇^♯ ⨯ F^♯ =
   \begin{bmatrix}
     (∂_y F^z - ∂ F^y) \; ∂_x \\
     (∂_z F^x - ∂ F^z) \; ∂_y \\
     (∂_x F^y - ∂ F^x) \; ∂_z \}
   \end{bmatrix}

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

.. topic:: Proposition

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

.. note::

   The Laplacian is only valid for functions (a 1-form). The Laplacian can be
   generalized to n-forms with the Laplace-de Rham operator.

.. }}}

