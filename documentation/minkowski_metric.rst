The Minkowski Metric
====================

.. rst-class:: custom-author

   by Stéphane Haussler

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


The rules of matrix multiplication and the metric tensor.

The metric tensor
-----------------

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

.. math::

   \begin{align}
   \eta^{\flat\flat}
   &=
       \begin{bmatrix}
       \begin{bmatrix}
        1  &
        0  &
        0  &
        0
       \end{bmatrix} &
       \begin{bmatrix}
        0 &
       -1 &
        0 &
        0 
       \end{bmatrix} &
       \begin{bmatrix}
        0 &
        0 &
       -1 &
        0
       \end{bmatrix} &
       \begin{bmatrix}
        0 &
        0 &
       -1 &
        0
       \end{bmatrix}
       \end{bmatrix} \\
   &=
       \begin{bmatrix}
        1 &  0 &  0 &  0 \\
        0 & -1 &  0 &  0 \\
        0 &  0 & -1 &  0 \\
        0 &  0 &  0 & -1 \\
       \end{bmatrix}^{\sharp\sharp}
   \end{align}

Applying metric tensor to ifself
--------------------------------

.. warning::

   .. rubric:: Applying the metric tensor

   .. math::

      \eta_{\mu\delta} \; \eta^{\delta\nu} = \delta_\mu{}^\nu

   .. math::
   
      {\scriptsize 
      \begin{align}
      \eta^{\flat\flat} \eta^{\sharp\sharp}
      = & \EtaFlatFlat \EtaSharpSharp \\
      \eta^{\flat\flat} \eta^{\sharp\sharp}
      = & \EtaRowRow \EtaColCol \\
      = & \{ 1 \EtatCol &  0 \EtaxCol &  0 \EtayCol &  0 \EtazCol \} + \\
        & \{ 0 \EtatCol & -1 \EtaxCol &  0 \EtayCol &  0 \EtazCol \} + \\
        & \{ 0 \EtatCol &  0 \EtaxCol & -1 \EtayCol &  0 \EtazCol \} + \\
        & \{ 0 \EtatCol &  0 \EtaxCol &  0 \EtayCol & -1 \EtazCol \}   \\ 
      \eta^{\flat\flat} \eta^{\sharp\sharp}
      = & \{ 1 & 0 & 0 & 0 \\
             0 & 0 & 0 & 0 \\
             0 & 0 & 0 & 0 \\
             0 & 0 & 0 & 0 \} +
          \{ 0 & 0 & 0 & 0 \\
             0 & 1 & 0 & 0 \\
             0 & 0 & 0 & 0 \\
             0 & 0 & 0 & 0 \} + 
          \{ 0 & 0 & 0 & 0 \\
             0 & 0 & 0 & 0 \\
             0 & 0 & 1 & 0 \\
             0 & 0 & 0 & 0 \} + 
          \{ 0 & 0 & 0 & 0 \\
             0 & 0 & 0 & 0 \\
             0 & 0 & 0 & 0 \\
             0 & 0 & 0 & 1 \} \\ 
      \eta^{\flat\flat} \eta^{\sharp\sharp}
      = & \{ 1 & 0 & 0 & 0 \\
             0 & 1 & 0 & 0 \\
             0 & 0 & 1 & 0 \\
             0 & 0 & 0 & 1 \}
      \end{align}
      }

Applying the metric tensor
--------------------------

.. math::

   a_i A^i{}_j = b_j \\
   a^i A_i{}_j = b_j \\
   a^k g_{ik} g^{im} A_m{}_j = b_j

So my thing would then be:

.. math::

   \partial_\mu F^\mu{}_\nu = J_\nu \\
   \partial^\delta \eta_{\mu\delta} \eta^{\mu\gamma} F_\gamma{}_\nu = J_\nu \\
   \eta_{\mu\delta} \partial^\delta \eta^{\mu\gamma} F_\gamma{}_\nu = J_\nu \\
   \eta_{\mu\delta} \partial^\delta F_\gamma{}_\nu \eta^{\mu\gamma} = J_\nu \\
   \eta_{\mu\delta} \partial^\delta F_\gamma{}_\nu \eta^{\gamma\mu} = J_\nu \\
   \partial^\mu F_\mu{}_\nu = J_\nu \\

So that:

.. math::

   {\scriptsize
   \begin{align}
   J_\nu &= \partial_\mu F^\mu{}_\nu\\
   J_\nu &= \partial^\delta \eta_{\mu\delta} \eta^{\mu\gamma} F_\gamma{}_\nu \\
         &= \{ +\partial_t \\ -\partial_x \\ -\partial_y \\ -\partial_z \} \EtaRowRow \EtaColCol F^{\flat\flat} \\
   J_\nu &= \eta_{\mu\delta} \partial^\delta \eta^{\mu\gamma} F_\gamma{}_\nu \\
   J_\nu &= \eta_{\mu\delta} \partial^\delta F_\gamma{}_\nu \eta^{\mu\gamma} \\
   J_\nu &= \eta_{\mu\delta} \partial^\delta F_\gamma{}_\nu \eta^{\gamma\mu} \\
   J_\nu &= \eta_{\mu\delta} \partial^\delta F_\nu{}_\gamma \eta^{\gamma\mu} \\
         &= \EtaRowRow \{ +\partial_t \\ -\partial_x \\ -\partial_y \\ -\partial_z \} F^{\flat\flat T} \EtaColCol
         \\
   J_\nu &= \partial^\mu F_\mu{}_\nu \\
   \end{align}
   }


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
