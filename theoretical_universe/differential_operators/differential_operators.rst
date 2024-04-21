.. Theoretical Universe (c) by Stéphane Haussler
.. 
.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

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
  
      \begin{equation}
      \mathbf{e}_i = \partial_i
      \end{equation}

.. }}}

Differential
------------

.. {{{

The differential applied to the partial derivative results in:

.. math::

   \begin{equation}
   dx^i ∂_j = δ^i_j
   \end{equation}

This is the definition for a covector, and we conclude that the differential
operator is a covector.

.. topic:: Proposition

   .. math::
   
      \begin{equation}
      \mathbf{e}^i = dx^i
      \end{equation}

.. }}}

Gradient
--------

.. {{{

.. topic:: Proposition

   .. math::

      \begin{equation}
      (df)^{♯} = \mathbf{∇} f
      \end{equation}

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

      \begin{equation}
      ⋆ d ⋆ F^♭t = \mathbf{∇} \cdot \mathbf{F}
      \end{equation}

We begin with :math:`F` as a vector :math:`\mathbf{F} = F^\sharp = F^i
\partial_i` and flatten:

.. math::

   \begin{equation}
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
   \end{equation}

Apply the :math:`\star` operator:

.. math::


   \begin{equation}
   ⋆ F^♭ = ⋆ \begin{bmatrix}
               F^x dx \\
               F^y dy \\
               F^z dz \\
             \end{bmatrix}
         = \begin{bmatrix}
             F^x ⋆ dx \\
             F^y ⋆ dy \\
             F^z ⋆ dz \\
           \end{bmatrix}
         = \begin{bmatrix}
             F^x dy ∧ dz \\
             F^y dz ∧ dx \\
             F^z dx ∧ dy \\
           \end{bmatrix}
   \end{equation}

Apply the :math:`d` operator:

.. math::

   \begin{equation}
   d ⋆ F^♭ = d
   \begin{bmatrix}
     F^x dy ∧ dz \\
     F^y dz ∧ dx \\
     F^z dx ∧ dy \\
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
   \end{equation}

Which can be brought back to a zero form by applying yet again the Hodge star
:math:`⋆`:

.. math::

   \begin{equation}
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
   \end{equation}

.. }}}

Curl
----

.. {{{

.. topic:: Proposition

   .. math::

      \begin{equation}
      (⋆(dF^♭))^♯ = ∇^♯ ⨯ F^♯
      \end{equation}

The vector field is:

.. math::

   \begin{equation}
   F^♯
   =
   \begin{bmatrix}
     F^x ∂_x \\
     F^y ∂_y \\
     F^z ∂_z \\
   \end{bmatrix}
   = F^x ∂_x + F^y ∂_y + F^z ∂_z
   \end{equation}

Flattening the vector field result in:

.. math::

   \begin{equation}
   F^\flat =
   \begin{bmatrix}
     F^x dx \\
     F^y dy \\
     F^z dz \\
   \end{bmatrix}
   = F^x dx + F^y dy + F^z dz
   \end{equation}

Taking the differential, we have:

.. math::

   \begin{equation}
   dF^♭ =
   \begin{bmatrix}
     ∂_x F^x dx ∧ dx & ∂_y F^x dy ∧ dx & ∂_z F^x dz ∧ dx \\
     ∂_x F^y dx ∧ dy & ∂_y F^y dy ∧ dy & ∂_z F^y dz ∧ dy \\
     ∂_x F^z dx ∧ dz & ∂_y F^z dy ∧ dy & ∂_z F^z dz ∧ dz \\
   \end{bmatrix}
   \end{equation}

Or with more natural row/column convention:

.. math::

   \begin{equation}
   dF^♭ =
   \begin{bmatrix}
     ∂_x F^x dx ∧ dx & ∂_x F^y dx ∧ dy & ∂_x F^z dx ∧ dz \\
     ∂_y F^x dy ∧ dx & ∂_y F^y dy ∧ dy & ∂_y F^z dy ∧ dy \\
     ∂_z F^x dz ∧ dx & ∂_z F^y dz ∧ dy & ∂_z F^z dz ∧ dz \\
   \end{bmatrix}
   \end{equation}

Where :math:`dx^i ∧ dx^i = 0`:

.. math::

   \begin{equation}
   dF^♭ =
   \begin{bmatrix}
                     & ∂_x F^y dx ∧ dy & ∂_x F^z dx ∧ dz \\
     ∂_y F^x dy ∧ dx &                 & ∂_y F^z dy ∧ dy \\
     ∂_z F^x dz ∧ dx & ∂_z F^y dz ∧ dy &                 \\
   \end{bmatrix}
   \end{equation}

And :math:`dx^i ∧ dx^j = -dx^j ∧ dx^i`:

.. math::

   \begin{equation}
   dF^♭ =
   \begin{bmatrix}
                       & + ∂_x F^y dx ∧ dy & - ∂_x F^z dz ∧ dx \\
     - ∂_y F^x dx ∧ dy &                   & + ∂_y F^z dy ∧ dy \\
     + ∂_z F^x dz ∧ dx & - ∂_z F^y dy ∧ dz &                   \\
   \end{bmatrix}
   \end{equation}

That we reorder to:

.. math::

   \begin{equation}
   dF^♭ =
   \begin{bmatrix}
     + ∂_y F^z dy ∧ dy - ∂_z F^y dy ∧ dz \\
     + ∂_z F^x dz ∧ dx - ∂_x F^z dz ∧ dx \\
     + ∂_x F^y dx ∧ dy - ∂_y F^x dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

.. math::

   \begin{equation}
   dF^♭ =
   \begin{bmatrix}
     (∂_y F^z - ∂_z F^y) dy ∧ dz \\
     (∂_z F^x - ∂_x F^z) dz ∧ dx \\
     (∂_x F^y - ∂_y F^x) dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

Where we can now take the star operator:

.. math::

   \begin{equation}
   ⋆ dF^♭ =
   \begin{bmatrix}
     (∂_y F^z - ∂_z F^y) ⋆ dy ∧ dz \\
     (∂_z F^x - ∂_x F^z) ⋆ dz ∧ dx \\
     (∂_x F^y - ∂_y F^x) ⋆ dx ∧ dy \\
   \end{bmatrix}
   \end{equation}

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

Where we have recovered the expression of the curl of a vector field:

.. math::

   \begin{equation}
   ∇^♯ ⨯ F^♯ =
   \begin{bmatrix}
     (∂_y F^z - ∂ F^y) \; ∂_x \\
     (∂_z F^x - ∂ F^z) \; ∂_y \\
     (∂_x F^y - ∂ F^x) \; ∂_z \\
   \end{bmatrix}
   \end{equation}


.. }}}

Laplacian
---------

.. {{{

.. topic:: Proposition

   .. math::

      \begin{equation}
      ⋆ d ⋆ d f = \mathbf{∇}^2 f
      \end{equation}

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

