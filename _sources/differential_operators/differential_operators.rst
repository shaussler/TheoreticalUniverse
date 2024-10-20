.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Differential Operators
======================

.. rst-class:: custom-author

   by Stéphane Haussler

In this article, I use the language of differential forms to systematically
express the derivative, the differential, the gradient, the divergence, the curl
and the laplacian in 3-dimensional Euclidean space.

I assume the reader possesses a strong grasp of vector calculus, a working
understanding of differential forms, the exterior product, musical operators, as
well as :ref:`the Hoddge dual <hodge_duality>`. To learn about differential
forms, `see yet another great video serie by Michael Penn
<https://youtube.com/playlist?list=PL22w63XsKjqzQZtDZO_9s2HEMRJnaOTX7&si=4dDrAZ-oKa1rI7B8>`_.
Implicitely assumed with the above requisites is a basic understanding of tensor
calculus, and in particular the concept of vector and covector. Some familiarity
with the concepts of of either Grassman Algebra, Clifford Algebra (AKA Geometric
Algebra), or Lie Algebra is not necessary but certainly welcome for a deeper
understanding of the antisymmetries at hand.

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

   .. math:: \mathbf{e}_i = \partial_i

.. }}}

Differential
------------

.. {{{

The differential applied to the partial derivative results in:

.. math:: dx^i ∂_j = δ^i_j

This is the definition for a covector, and we conclude that the differential
operator is a covector.

.. topic:: Proposition

   .. math:: \mathbf{e}^i = dx^i

.. }}}

Gradient
--------

.. {{{

.. topic:: Proposition

   .. math:: (df)^{♯} = \mathbf{∇} f

Expand :math:`df`:

.. math:: (df)^♯ = ( dx ∂_x f + dy ∂_y f + dz ∂_z f)^♯

Distribute the sharp operator :math:`♯`:

.. math:: (df)^♯ = (dx)^♯ ∂_x f + (dy)^♯ ∂_y f + (dz)^♯ ∂_z f

Which permits to conclude:

.. math:: (df)^♯ = ∂_x f ∂_x + ∂_y f ∂_y + ∂_z f ∂_z

In other words and for clarity:

.. math:: (df)^♯ = ∂_x f \mathbf{e}_x + ∂_y f \mathbf{e}_y + ∂_z f \mathbf{e}_z

.. }}}

Divergence
----------

.. {{{

.. topic:: Proposition

   .. math:: ⋆ d ⋆ F^♭ = \mathbf{∇} \cdot \mathbf{F}

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

   ⋆ F^♭ = ⋆ \begin{bmatrix}
       F^x   dx \\
       F^y   dy \\
       F^z   dz \\
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

Apply the :math:`d` operator:

.. math::

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

Which can be brought back to a zero form by applying yet again the Hodge star
:math:`⋆`:

.. math::

   ⋆ d ⋆ F^♭ = \begin{bmatrix}
     ∂_x F^x ⋆ dx ∧ dy ∧ dz \\
     ∂_y F^y ⋆ dx ∧ dy ∧ dz \\
     ∂_z F^z ⋆ dx ∧ dy ∧ dz \\
   \end{bmatrix}
   = \begin{bmatrix}
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

   .. math:: (⋆(dF^♭))^♯ = ∇^♯ ⨯ F^♯

The vector field is:

.. math::

   F^♯ = \begin{bmatrix}
       F^x ∂_x \\
       F^y ∂_y \\
       F^z ∂_z \\
   \end{bmatrix}
   = F^x ∂_x + F^y ∂_y + F^z ∂_z

Flattening the vector field result in:

.. math::

   F^\flat = \begin{bmatrix}
       F^x \; dx \\
       F^y \; dy \\
       F^z \; dz \\
   \end{bmatrix}
   = F^x dx + F^y dy + F^z dz

Taking the differential, we have:

.. math::

   dF^♭ = \begin{bmatrix}
       ∂_x F^x dx ∧ dx & ∂_y F^x dy ∧ dx & ∂_z F^x dz ∧ dx \\
       ∂_x F^y dx ∧ dy & ∂_y F^y dy ∧ dy & ∂_z F^y dz ∧ dy \\
       ∂_x F^z dx ∧ dz & ∂_y F^z dy ∧ dy & ∂_z F^z dz ∧ dz \\
   \end{bmatrix}

Or with more natural row/column convention:

.. math::

   dF^♭ = \begin{bmatrix}
       ∂_x F^x dx ∧ dx & ∂_x F^y dx ∧ dy & ∂_x F^z dx ∧ dz \\
       ∂_y F^x dy ∧ dx & ∂_y F^y dy ∧ dy & ∂_y F^z dy ∧ dy \\
       ∂_z F^x dz ∧ dx & ∂_z F^y dz ∧ dy & ∂_z F^z dz ∧ dz \\
   \end{bmatrix}

Where :math:`dx^i ∧ dx^i = 0`:

.. math::

   dF^♭ = \begin{bmatrix}
                       & ∂_x F^y dx ∧ dy & ∂_x F^z dx ∧ dz \\
       ∂_y F^x dy ∧ dx &                 & ∂_y F^z dy ∧ dy \\
       ∂_z F^x dz ∧ dx & ∂_z F^y dz ∧ dy &                 \\
   \end{bmatrix}

And :math:`dx^i ∧ dx^j = -dx^j ∧ dx^i`:

.. math::

   dF^♭ = \begin{bmatrix}
                         & + ∂_x F^y dx ∧ dy & - ∂_x F^z dz ∧ dx \\
       - ∂_y F^x dx ∧ dy &                   & + ∂_y F^z dy ∧ dy \\
       + ∂_z F^x dz ∧ dx & - ∂_z F^y dy ∧ dz &                   \\
   \end{bmatrix}

That we reorder to:

.. math::

   dF^♭ = \begin{bmatrix}
       + ∂_y F^z dy ∧ dy - ∂_z F^y \; dy ∧ dz \\
       + ∂_z F^x dz ∧ dx - ∂_x F^z \; dz ∧ dx \\
       + ∂_x F^y dx ∧ dy - ∂_y F^x \; dx ∧ dy \\
   \end{bmatrix}

.. math::

   dF^♭ = \begin{bmatrix}
       (∂_y F^z - ∂_z F^y) \; dy ∧ dz \\
       (∂_z F^x - ∂_x F^z) \; dz ∧ dx \\
       (∂_x F^y - ∂_y F^x) \; dx ∧ dy \\
   \end{bmatrix}

Where we can now take the star operator:

.. math::

   ⋆ dF^♭ = \begin{bmatrix}
       (∂_y F^z - ∂_z F^y) ⋆ dy ∧ dz \\
       (∂_z F^x - ∂_x F^z) ⋆ dz ∧ dx \\
       (∂_x F^y - ∂_y F^x) ⋆ dx ∧ dy \\
   \end{bmatrix}

.. math::

   ⋆ dF^♭ = \begin{bmatrix}
       (∂_y F^z - ∂_z F^y) \; dx \\
       (∂_z F^x - ∂_x F^z) \; dy \\
       (∂_x F^y - ∂_y F^x) \; dz \\
   \end{bmatrix}

We can then sharpen the covector to its vector form:

.. math::

   (⋆ dF^♭)^♯ = \begin{bmatrix}
       (∂_y F^z - ∂_z F^y) \; dx^♯ \\
       (∂_z F^x - ∂_x F^z) \; dy^♯ \\
       (∂_x F^y - ∂_y F^x) \; dz^♯ \\
   \end{bmatrix}

.. math::

   (⋆ dF^♭)^♯ = \begin{bmatrix}
       (∂_y F^z - ∂_z F^y) \; ∂_x \\
       (∂_z F^x - ∂_x F^z) \; ∂_y \\
       (∂_x F^y - ∂_y F^x) \; ∂_t \\
   \end{bmatrix}

Where we have recovered the expression of the curl of a vector field:

.. math::

   ∇^♯ ⨯ F^♯ = \begin{bmatrix}
       (∂_y F^z - ∂ F^y) \; ∂_x \\
       (∂_z F^x - ∂ F^z) \; ∂_y \\
       (∂_x F^y - ∂ F^x) \; ∂_z \\
   \end{bmatrix}


.. }}}

Laplacian
---------

.. {{{

.. topic:: Proposition

   .. math:: ⋆ d ⋆ d f = \mathbf{∇}^2 f

The differential of a function (zero form) is:

.. math:: df = ∂_x f dx + ∂_y f dy + ∂_z f dz

Taking the Hodge dual:

.. math:: ⋆ df = ∂_x f dy ∧ dz + ∂_y dz ∧ dx + ∂_z f dx ∧ dy

Taking the differential

.. math::

   d ⋆ df &= \frac{∂^2 f}{∂ x^2} dx ∧ dy ∧ dz + \frac{∂^2 f}{∂ y^2} dy ∧ dz ∧ dx + \frac{∂^2 f}{∂ z^2} dz ∧ dx ∧ dy \\
          &= \frac{∂^2 f}{∂ x^2} dx ∧ dy ∧ dz + \frac{∂^2 f}{∂ y^2} dx ∧ dy ∧ dz + \frac{∂^2 f}{∂ z^2} dx ∧ dy ∧ dz \\
          &= \left( \frac{∂^2 f}{∂ x^2} + \frac{∂^2 f}{∂ y^2} + \frac{∂^2 f}{∂ z^2} \right) \; dx ∧ dy ∧ dz         \\

Taking the Hodge dual, we tranform volumes to functions and obtain the
expression for the laplacian:

.. math::

   ⋆ d ⋆ df = \left( \frac{∂^2 f}{∂ x^2} + \frac{∂^2 f}{∂ y^2} + \frac{∂^2 f}{∂ z^2} \right)

The Laplacian in vector calculus is the divergence :math:`\mathbf{∇} \cdot`
applied to the gradiant of a function :math:`\mathbf{∇} f`:

.. math:: \mathbf{∇} \cdot \mathbf{∇} f

Where the divergence is :math:`⋆ d ⋆` and the gradient of a function is
:math:`df` brings the zero-form to a zero form.

.. }}}


d'Alembertian
-------------

.. {{{

.. warning:: Under construction

.. }}}

.. _the_laplace_de_rham_operator:

The Laplace-De Rham Operator
----------------------------

.. {{{

.. warning:: Under construction

The Laplacian is only valid for functions (zero-forms). The Laplacian can be
generalized to n-forms with the Laplace-de Rham operator.

.. math:: ∆ = dδ + δd = (d + δ)^2

Considering a k-form in a space with dimension :math:`n` and parity `s`, the
`general expression for codifferential
<https://en.m.wikipedia.org/wiki/Hodge_star_operator#Codifferential>`_ is:

.. math:: δ = (-1)^{n(k+1)+1} s  ⋆ d ⋆

In Euclidean space with :math:`n=3`, the metric signature is :math:`(+,+,+)` and
the parity therefore :math:`(1)⨯(1)⨯(1)=1`. The codifferential is then:

.. math:: \delta = (-1)^k ⋆ d ⋆

.. topic:: Laplace-De Rham Operator in Euclidean Space

   .. math:: dδ + δd = d ⋆ d ⋆ + (-1)^k ⋆ d ⋆ d

In Minkowski space with :math:`n=4`, the metric signature is :math:`(+,-,-,-)`
and the parity therefore :math:`(+1)⨯(-1)⨯(-1)⨯(-1)=-1`. The codifferential is
then:

.. math::

   δ & = (-1)^{n(k+1)+1}   s  ⋆ d ⋆ \\
     & = (-1)^{4(k+1)+1} (-1) ⋆ d ⋆ \\
     & = (-1)^{4(k+1)+2}      ⋆ d ⋆ \\
     & =                      ⋆ d ⋆ \\

.. topic:: Laplace-De Rham Operator in Minkowski Space

   .. math:: dδ + δd = d ⋆ d ⋆ + ⋆ d ⋆ d

.. }}}

.. 3-Forms
.. -------
.. 
.. .. warning:: Under Construction
.. 
.. .. math::
.. 
..    d ⋆ d ⋆ + ⋆ d ⋆ d F3
..    &= d ⋆ d ⋆ + ⋆ d ⋆ d \begin{bmatrix}
..    -a \; dx ∧ dy ∧ dz \\
..    +b \; dt ∧ dy ∧ dz \\
..    +c \; dt ∧ dz ∧ dx \\
..    +d \; dt ∧ dx ∧ dy \\
..    \end{bmatrix} \\
.. 
.. .. math::
.. 
..    \begin{bmatrix}
..              & + ∂_x^2 a & + ∂_y^2 a & + ∂_z^2 a & + ∂_x ∂_t b & + ∂_y ∂_t c & + ∂_z ∂_t d & dx∧dy∧dz \\
..    + ∂_t^2 b &           & - ∂_y^2 b & - ∂_z^2 b & + ∂_x ∂_t a & + ∂_y ∂_x c & + ∂_z ∂_x d & dt∧dy∧dz \\
..    + ∂_t^2 c & - ∂_x^2 c &           & - ∂_z^2 c & + ∂_y ∂_t a & + ∂_y ∂_x b & + ∂_z ∂_y d & dt∧dz∧dx \\
..    + ∂_t^2 d & - ∂_x^2 d & - ∂_y^2 d &           & + ∂_z ∂_t a & + ∂_z ∂_x b & + ∂_z ∂_y c & dt∧dx∧dy \\
..    \end{bmatrix}
.. 
.. .. math::
.. 
..    \begin{bmatrix}
..              & + ∂_x^2 a & + ∂_y^2 a & + ∂_z^2 a & + ∂_t ∂_x b & + ∂_t ∂_y c & + ∂_t ∂_z d & dx∧dy∧dz \\
..    + ∂_t^2 b &           & - ∂_y^2 b & - ∂_z^2 b & + ∂_t ∂_x a & + ∂_x ∂_y c & + ∂_x ∂_z d & dt∧dy∧dz \\
..    + ∂_t^2 c & - ∂_x^2 c &           & - ∂_z^2 c & + ∂_t ∂_y a & + ∂_x ∂_y b & + ∂_y ∂_z d & dt∧dz∧dx \\
..    + ∂_t^2 d & - ∂_x^2 d & - ∂_y^2 d &           & + ∂_t ∂_z a & + ∂_x ∂_z b & + ∂_y ∂_z c & dt∧dx∧dy \\
..    \end{bmatrix}


