The Minkowski Metric
====================

.. warning:

   Under construction

Flat metric tensor:

.. math::

   \eta_{\mu\nu} = e_\mu \cdot e_\nu 

.. math::

   \eta^{\mu\nu} = e^\mu \cdot e^\nu 

By definition:

.. math::

   e_\mu \cdot e^\nu = \delta_\mu^\nu

.. math::

   e^\mu \cdot e_\nu = \delta^\mu_\nu


The rules of matrix multiplication and the metric tensor:

.. math::

   \eta^{\sharp\sharp}
   =
   \begin{bmatrix}
   \begin{bmatrix}
   1  \\
   0  \\
   0  \\
   0  \\
   \end{bmatrix}^{\sharp} \\
   \begin{bmatrix}
   0  \\
   -1 \\
   0  \\
   0  \\
   \end{bmatrix}^{\sharp}  \\
   \begin{bmatrix}
   0  \\
   0  \\
   -1 \\
   0  \\
   \end{bmatrix}^{\sharp}  \\
   \begin{bmatrix}
   0  \\
   0  \\
   -1 \\
   0  \\
   \end{bmatrix}^{\sharp} 
   \end{bmatrix}^{\sharp}
   =
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1 \\
   \end{bmatrix}^{\sharp\sharp}


https://vixra.org/abs/1710.0196

.. I love the paper. I was/am reviewing electromagnetism, the Faraday tensor and
.. the Tensor formulation of EM. This is a little of a pet project where I take
.. the time to look at all details and existing formulations of Maxwell equations.
.. I am in particular looking at explicit and computable form of the equations. I
.. mean by that a tensor form and differential forms approach  that can be
.. manipulated and explicitely permit computation like lowering indices or change
.. basis. And by that I mean Matrix form. To my surprise it turns out that all
.. textbooks are a little weak and inconsistent regarding the matrix
.. representation of the minkowski metric as well as the Faraday tensor. I came to
.. the same conclusion as Mr. Hongbing Zhang and that is how I found the paper
.. while looking into it.
