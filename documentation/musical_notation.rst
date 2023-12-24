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

Representation of the Metric Tensor
-----------------------------------

For the purpose of of this article, I will be using a metric tensor akin to the
flat Minkowski metric, with one time dimension but only one spatial dimension
for simplicity.

.. math::

   \eta^{\sharp\sharp}
   = \{ +1 &  0 \\ 0 & -1 \}^{\sharp\sharp}
   = \{ \{ +1 \\ 0 \} \\ \{ 0 \\ -1 \} \}

.. math::

   \eta^{\flat\flat}
   = \{ +1 & 0 \\ 0 & -1 \}^{\flat\flat}
   = \{ \{ +1 &  0 \} & \{ 0 & -1 \} \}

Raising and Lowering Indices
----------------------------

.. rubric:: Rank (0,1) to (1,0)

Sharpening a covector to a vector is expressed with :math:`A_\mu \eta^{\mu\nu}
= A^\nu` in tensor notation. Following vanilla matrix multiplication rules for
:math:`\alpha = \{ +1 & 0 \}^\sharp` and :math:`\beta=\{ 0 & -1 \}^\sharp`, we
obtain:

.. math::

   \{ a \\ b\}^\flat \{ \alpha \\ \beta \}^\sharp
   = \{ a & b \} \{ \alpha \\ \beta \}
   = a \alpha + b \beta


.. math::

   \{ a \\ b \}^{\flat}
   \{ +1 & 0 \\ 0 & -1 \\ \}^{\sharp\sharp}
   = \{ a & b \} \{ \{ +1 \\ 0 \} \\ \{ 0 \\ -1 \} \}
   = a \, \{ +1 \\ 0 \} + b \, \{ 0 \\ -1 \}
   = \{ +a \\ -b \}

.. rubric:: Rank (1,0) to (0,1)

Flattening a vector to a covector is expressed with :math:`A^\mu \eta_{\mu\nu}
= A_\nu` in tensor notation. Following vanilla matrix multiplication rules for
:math:`\alpha = \{ +1 & 0 \}^\flat` and :math:`\beta=\{ 0 & -1 \}^\flat`, we
obtain:

.. math::

   \{ \alpha \\ \beta \}^\flat \{ a \\ b \}^\sharp
   = \{ \alpha & \beta \} \{ a \\ b \}
   = \alpha a + \beta b

.. math::

   \{ +1 & 0 \\ 0 & -1 \}^{\flat\flat}
   \{ a \\ b \}^\sharp
   = \{ \{ +1 &  0 \}, & \{ 0 & -1 \} \} \{ a \\ b \}
   = \{ +1,  0 \} \; a + \{ 0, -1 \} \; b
   = \{ +a, -b \}
   = \{ +a \\ -b \}^\flat

.. rubric:: Rank (0,2) to (1,1)

Raising the index of a covariant/covariant tensor is expressed with
:math:`A_{\eta\nu} \; \eta^{\eta\nu} = A^{\mu}{}_{\nu}` in tensor notation.
Following vanilla matrix multiplication rules for :math:`\alpha = \{ +1 & 0
\}^\sharp` and :math:`\beta=\{ 0 & -1 \}^\sharp`, we obtain:

.. math::

   \{
       a & c \\
       b & d \\
   \}^{\flat\flat}
   \{
       +1 &  0 \\
        0 & -1 \\
   \}^{\sharp\sharp}
   = 
   \{
       \{ a & c \} & \{ b & d \}
   \}
   \{ \alpha \\ \beta \}
   = \{ a & c \} \; \alpha + \{ b & d \} \; \beta
   = \{ a \alpha + b \beta \; , & c \alpha + d \beta \}

.. math::

   \{
       a & c \\
       b & d \\
   \}^{\flat\flat}
   \{
       +1 &  0 \\
        0 & -1 \\
   \}^{\sharp\sharp}
   = 
   \{
       a \{ +1 \\ 0 \} + b \{  0 \\ -1 \} \; , &
       c \{ +1 \\ 0 \} + d \{  0 \\ -1 \}
   \}
   =
   \{
       +a & +c \\
       -b & -d
   \}^{\sharp\flat}

.. rubric:: Rank (2,0) to (1,1)

.. rubric:: Rank (1,1) to (2,0)

Raising the index of a contravariant/covariant tensor in tensor notation is
expressed with :math:`A^{\mu}{}_{\eta} \; \eta^{\eta\nu} = A^{\mu\nu}`.
Following vanilla matrix multiplication rules for :math:`\alpha = \{ +1 & 0
\}^\sharp` and :math:`\beta=\{ 0 & -1 \}^\sharp`, we obtain:

.. math::

   \{
       a & c \\
       b & d \\
   \}^{\sharp\flat}
   \{ \alpha \\ \beta \}^\sharp
   =
   \{
       a & c \\
       b & d \\
   \}
   \{ \alpha \\ \beta \}
   =
   \{
       a \alpha + c \beta \\
       b \alpha + d \beta
   \}

.. math::

   \{
       a & c \\
       b & d \\
   \}^{\sharp\flat}
   \{
       +1 &  0 \\
        0 & -1 \\
   \}^{\sharp\sharp}
   =
   \begin{bmatrix}
       a \{ +1 \\  0 \} + c \{  0 \\ -1 \} \\
       b \{ +1 \\  0 \} + d \{  0 \\ -1 \} \\
   \end{bmatrix}
   =
   \{
       \{ +a \\ -c \\ \} \\
       \{  b \\ -d \\ \} \\
   \}
   =
   \{
       +a & +b \\
       -c & -d \\
   \}^{\sharp\sharp}

.. rubric:: Rank (1,1) to (0,2)

Lowering the Indice of a Rank 2 Contravariant/Covariant Tensor

The goal here is to lower a contravariant/covariant tensor
:math:`[T^\mu{}_\nu]`, or in musical notation :math:`T^{\sharp\sharp}`

Following matrix multiplication rules, we get:

.. math::

   \begin{bmatrix} \alpha & \beta \end{bmatrix}
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}
   =
   \begin{bmatrix}
       \begin{bmatrix} \alpha &  \beta \end{bmatrix}
       \begin{bmatrix}  a     \\  b    \end{bmatrix}, \;
       \begin{bmatrix} \alpha &  \beta \end{bmatrix}
       \begin{bmatrix}  c     \\  d \\ \end{bmatrix}
   \end{bmatrix}
   =
   \begin{bmatrix} \alpha a + \beta b, \; \alpha c + \beta d \end{bmatrix}

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
          \begin{bmatrix}+a, 0\end{bmatrix} + \begin{bmatrix}0, -b\end{bmatrix}, &
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
       \end{bmatrix}^{\flat} \\
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

