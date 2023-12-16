The Musical Tensor Notation
===========================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

.. note::

   During development of the musical notation, I found that Mr. Hongbing Zhang
   had already developed these ideas in his paper `Matrix-Representations of
   Tensors <https://vixra.org/abs/1710.0196>`_. I suspect the idea is not new
   but have not found other sources where the idea is clearly laid out. Of
   course, I will not even try access resources behind paywalls.

Representation of multilinear forms
-----------------------------------

.. include:: ./summary_musical_notation.rst

Metric Tensor
-------------

For the purpose of of this article, I will be using a metric tensor akin to the
flat Minkowski metric, with one time dimension but only one spatial dimension
for simplicity.

.. math::

   \begin{bmatrix}
       +1 &  0 \\
        0 & -1\\
   \end{bmatrix}^{\sharp\sharp}

Raising the indice
------------------

Consider the following vanilla matrix multiplication:

.. math::

   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}
   \begin{bmatrix}
       \alpha \\
       \beta
   \end{bmatrix}
   =
   \begin{bmatrix}
       a \alpha + c \beta \\
       b \alpha + d \beta
   \end{bmatrix}

We can use :math:`\alpha=\begin{bmatrix}+1 \\ 0\end{bmatrix}` and
:math:`\beta=\begin{bmatrix}0 \\ -1\end{bmatrix}` to match our metric tensor.
This leads to:

.. math::

   {\small
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}^{\sharp\flat}
   \begin{bmatrix}
       +1 &  0 \\
        0 & -1\\
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}
   \begin{bmatrix}
       \begin{bmatrix}
       +1 \\
        0 \\
       \end{bmatrix} \\
       \begin{bmatrix}
        0 \\
       -1 \\
       \end{bmatrix} \\
   \end{bmatrix}
   =
   \begin{bmatrix}
       a 
       \begin{bmatrix}
       +1 \\
        0 \\
       \end{bmatrix} +
       c
       \begin{bmatrix}
         0 \\
        -1
       \end{bmatrix} \\
       b
       \begin{bmatrix}
       +1 \\
        0 \\
       \end{bmatrix} +
       d
       \begin{bmatrix}
         0 \\
        -1
       \end{bmatrix} \\
   \end{bmatrix}
   =
   \begin{bmatrix}
       \begin{bmatrix}
       +a \\
       -c \\
       \end{bmatrix} \\
       \begin{bmatrix}
        b \\
       -d \\
       \end{bmatrix} \\
   \end{bmatrix}
   =
   \begin{bmatrix}
        a &  b \\
       -c & -d \\
   \end{bmatrix}^{\sharp\sharp}
   }

In tensor notation, this correspond to:

.. math::

   A^{\mu\nu}=A^{\mu}{}_{\nu} \; \eta^{\mu\nu}

The tensor formulation is certainly compact and elegant. However it does not
allow for explicit calculations and does not explicitely show underlying
symmetries.

Lowering the Indice
-------------------

.. rubric:: For a Vector

.. math::

   \begin{align}
   \begin{bmatrix}
       +1 &  0 \\
        0 & -1\\
   \end{bmatrix}^{\flat\flat}
   \begin{bmatrix}
       a \\
       b \\
   \end{bmatrix}^{\sharp}
   =
   \begin{bmatrix}
        a \\
       -b \\
   \end{bmatrix}^{\flat}
   \end{align}

.. admonition:: Every Step in Excrutiating Details
   :class: dropdown

   .. math::
   
      \begin{align}
      \begin{bmatrix}
          +1 &  0 \\
           0 & -1\\
      \end{bmatrix}^{\flat\flat}
      \begin{bmatrix}
          a \\
          b \\
      \end{bmatrix}^{\sharp}
      & =
      \begin{bmatrix}
          \begin{bmatrix} +1 &  0 \end{bmatrix}, &
          \begin{bmatrix}  0 & -1 \end{bmatrix}
      \end{bmatrix}
      \begin{bmatrix}
          a \\
          b \\
      \end{bmatrix} \\
      & =
      \begin{bmatrix} +1 &  0 \end{bmatrix} \; a +
      \begin{bmatrix}  0 & -1 \end{bmatrix} \; b \\
      & =
      \begin{bmatrix} +a &  0 \end{bmatrix} +
      \begin{bmatrix}  0 & -b \end{bmatrix} \\
      & =
      \begin{bmatrix}
          +a & -b \\
      \end{bmatrix} \\
      & =
      \begin{bmatrix}
           a \\
          -b \\
      \end{bmatrix}^{\flat}
      \end{align}

.. rubric:: For a Rank 2 Tensor

The goal here is to lower a contravariant/convariant tensor
:math:`[T^\mu{}_\nu]`, or in musical notation :math:`T^{\sharp\sharp}`

Following matrix multiplication rules, we get:

.. math::

   \begin{bmatrix}
       \alpha &
       \beta
   \end{bmatrix}
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}
   =
   \begin{bmatrix}
       \begin{bmatrix}
           \alpha &
           \beta
       \end{bmatrix}
       \begin{bmatrix}
           a \\
           b \\
       \end{bmatrix}, \;
       \begin{bmatrix}
           \alpha &
           \beta
       \end{bmatrix}
       \begin{bmatrix}
           c \\
           d \\
       \end{bmatrix}
   \end{bmatrix}
   =
   \begin{bmatrix}
       \alpha a + \beta b
       , \;
       \alpha c + \beta d
   \end{bmatrix}

Extending matrix multiplication rules with e.g.
:math:`\alpha=\begin{bmatrix}+1, 0\end{bmatrix}` and
:math:`\beta=\begin{bmatrix}0, -1\end{bmatrix}`,
we obtain:

.. math::

   \begin{align}
   \begin{bmatrix}
       \begin{bmatrix} +1 &  0 \end{bmatrix}, & \begin{bmatrix}  0 & -1 \end{bmatrix}
   \end{bmatrix}
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}
   &=
   \begin{bmatrix}
       \begin{bmatrix}+1, 0\end{bmatrix} \; a + \begin{bmatrix}0, -1\end{bmatrix} \; b,&
       \begin{bmatrix}+1, 0\end{bmatrix} \; c + \begin{bmatrix}0, -1\end{bmatrix} \; d 
   \end{bmatrix} \\
   &= 
   \begin{bmatrix}
       \begin{bmatrix}+a, 0\end{bmatrix} + \begin{bmatrix}0, -b\end{bmatrix},&
       \begin{bmatrix}+c, 0\end{bmatrix} + \begin{bmatrix}0, -d\end{bmatrix}
   \end{bmatrix} \\
   &= 
   \begin{bmatrix}
       \begin{bmatrix}+a, -b\end{bmatrix}, &
       \begin{bmatrix}+c, -d\end{bmatrix}
   \end{bmatrix} \\
   \end{align}

More generally, we can follow matrix multiplication rules to lower the indice.
Part of the operations can be done by head. With all possible steps, this is:

.. math::

   \begin{align}
   \begin{bmatrix}
       +1 &  0 \\
        0 & -1\\
   \end{bmatrix}^{\flat\flat}
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}^{\sharp\flat}
   & =
   \begin{bmatrix}
       \begin{bmatrix} +1 &  0 \end{bmatrix}, & \begin{bmatrix}  0 & -1 \end{bmatrix}
   \end{bmatrix}
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix} \\
   & =
   \begin{bmatrix}
       \begin{bmatrix}
           \begin{bmatrix} +1 &  0 \end{bmatrix}, & \begin{bmatrix}  0 & -1 \end{bmatrix}
       \end{bmatrix}
       \begin{bmatrix}
           a \\
           b \\
       \end{bmatrix}, &
       \begin{bmatrix}
           \begin{bmatrix} +1 &  0 \end{bmatrix}, & \begin{bmatrix}  0 & -1 \end{bmatrix}
       \end{bmatrix}
       \begin{bmatrix}
           c \\
           d \\
       \end{bmatrix}
   \end{bmatrix} \\
   & =
   \begin{bmatrix}
       \begin{bmatrix} +a & -b \end{bmatrix}, & \begin{bmatrix} c & -d \end{bmatrix} \\
   \end{bmatrix} \\
   & =
   \begin{bmatrix}
        a &  c \\
       -b & -d \\
   \end{bmatrix}^{\flat\flat}
   \end{align}

.. math::

   \begin{align}
   \begin{bmatrix}
       +1 &  0 \\
        0 & -1\\
   \end{bmatrix}^{\flat\flat}
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}^{\sharp\flat}
   & =
   \begin{bmatrix}
       \begin{bmatrix}
           +1 \\
            0
       \end{bmatrix}^{\flat} &
       \begin{bmatrix}
            0 \\
           -1
       \end{bmatrix}^{\flat}
   \end{bmatrix}
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}^{\sharp\flat} \\
   & =
   \begin{bmatrix}
       \begin{bmatrix}
           \begin{bmatrix}
               +1 \\
                0 
           \end{bmatrix}^{\flat} &
           \begin{bmatrix}
                0 \\
               -1
           \end{bmatrix}^{\flat}
       \end{bmatrix}
       \begin{bmatrix}
           a \\
           b \\
       \end{bmatrix}^{\sharp}, &
       \begin{bmatrix}
           \begin{bmatrix}
               +1 \\
                0
           \end{bmatrix}^{\sharp} &
           \begin{bmatrix}
                0 \\
               -1
           \end{bmatrix}^{\sharp}
       \end{bmatrix}
       \begin{bmatrix}
           c \\
           d 
       \end{bmatrix}^{\sharp}
   \end{bmatrix} \\
   & =
   \begin{bmatrix}
       \begin{bmatrix}
           +a \\
           -b
        \end{bmatrix}^{\flat} &
        \begin{bmatrix}
            c \\
           -d
        \end{bmatrix}^{\flat} \\
   \end{bmatrix} \\
   & =
   \begin{bmatrix}
        a &  c \\
       -b & -d \\
   \end{bmatrix}^{\flat\flat}
   \end{align}

