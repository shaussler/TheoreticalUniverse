The Musical Tensor Notation
===========================

.. rst-class:: custom-author

   by Stéphane Haussler

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

   \{ a \\ b \}^{\flat} \{ +1 & 0 \\ 0 & -1 \\ \}^{\sharp\sharp}
   = \{ a & b \} \{ \{ +1 \\ 0 \} \\ \{ 0 \\ -1 \} \}
   = a \, \{ +1 \\ 0 \} + b \, \{ 0 \\ -1 \}
   = \{ +a \\ -b \}

.. rubric:: Rank (1,0) to (0,1)

Flattening a vector to a covector is expressed with :math:`\eta_{\mu\nu} A^\mu
= A_\nu` in tensor notation. Following vanilla matrix multiplication rules for
:math:`\alpha = \{ +1 & 0 \}^\flat` and :math:`\beta=\{ 0 & -1 \}^\flat`, we
obtain:

.. math::

   \{ \alpha \\ \beta \}^\flat \{ a \\ b \}^\sharp
   = \{ \alpha & \beta \} \{ a \\ b \}
   = \alpha a + \beta b

.. math::

   \{ +1 & 0 \\ 0 & -1 \}^{\flat\flat} \{ a \\ b \}^\sharp
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

   \{ a & c \\ b & d \}^{\flat\flat} \{ \alpha \\ \beta \}^\sharp
   = \{ \{ a & b \} & \{ c & d \} \} \{ \alpha \\ \beta \}
   = \{ a & b \} \; \alpha + \{ c & d \} \; \beta
   = \{ a \alpha + c \beta \; , & b \alpha + d \beta \}

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
       a \{ +1 \\ 0 \} + c \{  0 \\ -1 \} \; , &
       b \{ +1 \\ 0 \} + d \{  0 \\ -1 \}
   \}
   =
   \{
       +a & +b \\
       -c & -d
   \}^{\sharp\flat}

.. rubric:: Rank (2,0) to (1,1)

.. rubric:: Rank (1,1) to (2,0)

Raising the index of a contravariant/covariant tensor is expressed with
:math:`A^{\mu}{}_{\eta} \; \eta^{\eta\nu} = A^{\mu\nu}` in tensor notation.
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

Lowering the index of a contravariant/covariant tensor is expressed with
:math:`\eta_{\mu\nu} A^{\mu}{}_{\eta} = A_{\mu\nu}` in tensor notation.
Following vanilla matrix multiplication rules for :math:`\alpha = \{ +1 & 0
\}^\flat` and :math:`\beta=\{ 0 & -1 \}^\flat`, we obtain:

.. math::

   \{ \alpha \\ \beta \}^\flat
   \{
       a & c \\
       b & d \\
   \}^{\sharp\flat}
   = \{ \alpha & \beta \}
     \{
         a & c \\
         b & d \\
     \}
   = \{ \alpha a + \beta b, \; \alpha c + \beta d \}

.. math::

   \begin{align}
   \{
       +1 &  0 \\
        0 & -1 \\
   \}^{\sharp\sharp}
   \{
       a & c \\
       b & d \\
   \}^{\sharp\flat} 
   &= \{
           \{ +1 \\ 0 \}^\flat \; a + \{ 0 \\ -1 \}^{\flat} \; b,&
           \{ +1 \\ 0 \}^\flat \; c + \{ 0 \\ -1 \}^{\flat} \; d
      \}\\
   &= \{ \{ +a \\ -b \}^{\flat}, &
         \{ +c \\ -d \}^{\flat}
      \}
   = \{ +a & +c \\ -b & -d \}^{\flat\flat}
  \end{align}

Notable Difference
------------------

The doubly contravariant electromagnetic tensor is generally written as a
row/column matrix.  The relation between row/column and row/row representations
is a transpose. Taking the doubly contravariant electromagnetic tensor as an
example:

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
   \end{bmatrix}^{\sharp\sharp}

