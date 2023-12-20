The Musical Tensor Notation
===========================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

.. note::

   While exploring the idea of musical notation, I found that Mr. Hongbing
   Zhang had already developed very similar ideas in his paper
   `Matrix-Representations of Tensors <https://vixra.org/abs/1710.0196>`_.
   Although I suspect the idea is not novel, I have not found other sources. I
   have no access to resources behind paywalls.

Representation of Multilinear Forms
-----------------------------------

.. include:: ./summary_musical_notation.rst

Raising and Lowering Indices
----------------------------

Exemplary and Simplified Flat Minkowski Metric
''''''''''''''''''''''''''''''''''''''''''''''

For the purpose of of this article, I will be using a metric tensor akin to the
flat Minkowski metric, with one time dimension but only one spatial dimension
for simplicity.

.. math::

   \eta^{\sharp\sharp}
   =
   \begin{bmatrix}
       +1 &  0 \\
        0 & -1
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
       \begin{bmatrix}
       +1 \\
        0 
       \end{bmatrix} \\
       \begin{bmatrix}
        0 \\
       -1
       \end{bmatrix}
   \end{bmatrix}

.. math::

   \eta^{\flat\flat}
   =
   \begin{bmatrix}
       +1 &  0 \\
        0 & -1
   \end{bmatrix}^{\flat\flat}
   =
   \begin{bmatrix}
       \begin{bmatrix}
       +1 &
        0 
       \end{bmatrix} &
       \begin{bmatrix}
        0 &
       -1
       \end{bmatrix}
   \end{bmatrix}


Sharpening a Covector to a Vector
'''''''''''''''''''''''''''''''''

Following matrix multiplication rules, we have:

.. math::

   \begin{bmatrix}
       a &
       b
   \end{bmatrix}
   \begin{bmatrix}
       \alpha \\
       \beta \\
   \end{bmatrix}
   =
   a \alpha + b \beta

Using :math:`\alpha=\begin{bmatrix}+1 \\ 0\end{bmatrix}` and
:math:`\beta=\begin{bmatrix}0 \\ -1\end{bmatrix}`, we obtain:

.. math::

   \begin{bmatrix}
       a &
       b
   \end{bmatrix}
   \begin{bmatrix}
       \begin{bmatrix} +1 \\  0 \end{bmatrix}, & \begin{bmatrix}  0 \\ -1 \end{bmatrix}
   \end{bmatrix}
   =
   a \, \begin{bmatrix}+1 \\ 0\end{bmatrix} + b \, \begin{bmatrix}0 \\ -1\end{bmatrix}
   =
   \begin{bmatrix}+a \\ -b\end{bmatrix}

With musical notation:

.. math::

   \begin{align}
   \begin{bmatrix}
       a \\
       b \\
   \end{bmatrix}^{\flat}
   \begin{bmatrix}
       +1 &  0 \\
        0 & -1\\
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
       a \\
       b \\
   \end{bmatrix}^{\flat}
   \begin{bmatrix}
       \begin{bmatrix}
           +1 \\
            0
       \end{bmatrix}^{\sharp}
       \begin{bmatrix}
            0 \\
           -1
       \end{bmatrix}^{\sharp}
   \end{bmatrix}^{\sharp}
   =
   \begin{bmatrix}
        a \\
       -b \\
   \end{bmatrix}^{\sharp}
   \end{align}

In tensor notation, this corresponds to:

.. math::

   A_\mu \eta^{\mu\nu} = A^\nu

Raising the Indice of a Rank 2 Tensor
'''''''''''''''''''''''''''''''''''''

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

Using :math:`\alpha=\begin{bmatrix}+1 \\ 0\end{bmatrix}` and
:math:`\beta=\begin{bmatrix}0 \\ -1\end{bmatrix}`, we obtain:

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

   A^{\mu}{}_{\nu} \; \eta^{\mu\nu} = A^{\mu\nu}

Flattening a Vector to a Covector
'''''''''''''''''''''''''''''''''

The goal here is to flatten a vector to a covector

Following matrix multiplication rules, we get:

.. math::

   \begin{bmatrix}
       \alpha &
       \beta
   \end{bmatrix}
   \begin{bmatrix}
       a \\
       b \\
   \end{bmatrix}
   =
   \alpha a + \beta b

Using :math:`\alpha=\begin{bmatrix}+1, 0\end{bmatrix}` and
:math:`\beta=\begin{bmatrix}0, -1\end{bmatrix}`, we obtain:

.. math::

   \begin{align}
       \begin{bmatrix}
           \begin{bmatrix} +1 &  0 \end{bmatrix}, & \begin{bmatrix}  0 & -1 \end{bmatrix}
       \end{bmatrix}
       \begin{bmatrix}
           a \\
           b \\
       \end{bmatrix}
   &=
       \begin{bmatrix}+1, 0\end{bmatrix} \; a + \begin{bmatrix}0, -1\end{bmatrix} \; b \\
   &=
       \begin{bmatrix}+a, -b\end{bmatrix}
   \end{align}

With musical notation:

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
       \begin{bmatrix}
           +1 \\
            0
       \end{bmatrix}^{\flat}
       \begin{bmatrix}
            0 \\
           -1
       \end{bmatrix}^{\flat}
   \end{bmatrix}^{\flat}
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

.. admonition:: Same calculation with too many details
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

Lowering the Indice of a Rank 2 Tensor
''''''''''''''''''''''''''''''''''''''

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

Using :math:`\alpha=\begin{bmatrix}+1, 0\end{bmatrix}` and
:math:`\beta=\begin{bmatrix}0, -1\end{bmatrix}`, we obtain:

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
           \begin{bmatrix}+a, -b\end{bmatrix}, &
           \begin{bmatrix}+c, -d\end{bmatrix}
       \end{bmatrix} \\
   \end{align}

.. admonition:: Same calculation with too many details
   :class: dropdown

   .. math::
   
      \begin{align}
          \begin{bmatrix}
              \begin{bmatrix} +1 &  0 \end{bmatrix}, & \begin{bmatrix}  0 & -1 \end{bmatrix}
          \end{bmatrix}
          \begin{bmatrix}
              a & c \\
              b & d \\
          \end{bmatrix}
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

The musical notation efficiently condenses larger matrices, simplifying their
representation. However, in this specific case, the notation doesn't offer
substantial benefits. Nevertheless, it stands as an exemplary illustration of
the method.

.. math::

   \begin{align}
       \begin{bmatrix}
           +1 &  0 \\
            0 & -1 
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
           \end{bmatrix}^{\flat}
           \begin{bmatrix}
                0 \\
               -1
           \end{bmatrix}^{\flat}
       \end{bmatrix}^{\flat}
       \begin{bmatrix}
           a & c \\
           b & d \\
       \end{bmatrix}^{\sharp\flat} \\
   & =
       \begin{bmatrix}
           \begin{bmatrix}
               +a \\
               -b
            \end{bmatrix}^{\flat}
            \begin{bmatrix}
               +c \\
               -d
            \end{bmatrix}^{\flat} \\
       \end{bmatrix} \\
   & =
       \begin{bmatrix}
           +a & +c \\
           -b & -d \\
       \end{bmatrix}^{\flat\flat}
   \end{align}

.. admonition:: Same calculation with too many details
   :class: dropdown

   .. math::
   
      \begin{align}
          \begin{bmatrix}
              +1 &  0 \\
               0 & -1 
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
              \end{bmatrix}^{\flat}
              \begin{bmatrix}
                   0 \\
                  -1
              \end{bmatrix}^{\flat}
          \end{bmatrix}^{\flat}
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
                  \end{bmatrix}^{\flat}
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
                  \end{bmatrix}^{\sharp}
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
                  \begin{bmatrix}
                      +a \\
                       0 
                  \end{bmatrix}^{\flat} +
                  \begin{bmatrix}
                       0 \\
                      -b
                  \end{bmatrix}^{\flat}
              \end{bmatrix}
              , &
              \begin{bmatrix}
                  \begin{bmatrix}
                      +c \\
                       0
                  \end{bmatrix}^{\sharp} +
                  \begin{bmatrix}
                       0 \\
                      -d
                  \end{bmatrix}^{\sharp}
              \end{bmatrix}
          \end{bmatrix} \\
      & =
          \begin{bmatrix}
              \begin{bmatrix}
                  +a \\
                  -b
               \end{bmatrix}^{\flat}
               \begin{bmatrix}
                  +c \\
                  -d
               \end{bmatrix}^{\flat} \\
          \end{bmatrix} \\
      & =
          \begin{bmatrix}
              +a & +c \\
              -b & -d \\
          \end{bmatrix}^{\flat\flat}
      \end{align}

Notable Differences
-------------------

In the litterature, the doubly contravariant electromagnetic tensor is mostly
written as a row/column matrix. This notation is very unfortunate and a row/row
matrix much more appropriate, as it permits to apply the rules of matrix
multiplication. The relation between row/column and row/row representations is
a transpose operation.

.. math::

   \begin{bmatrix}
                    & -\tilde{E^x} & -\tilde{E^y} & - \tilde{E^z} \\
       +\tilde{E^x} &              & -       B^z  & +        B^y  \\
       +\tilde{E^y} & +       B^z  &              & -        B^x  \\
       +\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}^{T}
   =
   \begin{bmatrix}
                    & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
       -\tilde{E^x} &              & +       B^z  & -        B^y  \\
       -\tilde{E^y} & -       B^z  &              & +        B^x  \\
       -\tilde{E^z} & +       B^y  & -       B^x  &               \\
   \end{bmatrix}

