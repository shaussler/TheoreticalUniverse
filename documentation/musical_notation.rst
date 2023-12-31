The Musical Tensor Notation
===========================

.. rst-class:: custom-author

   by Stéphane Haussler

While exploring the idea of the musical notation for tensors, I found that Mr.
Hongbing Zhang has developed very similar ideas in his paper
`Matrix-Representations of Tensors <https://vixra.org/abs/1710.0196>`_.
Although I suspect the idea is not novel, I have not found other sources. I
have no access to resources behind paywalls.

Representation of Multilinear Forms
-----------------------------------

.. include:: ./musical_notation_multilinear_forms.rst

Matrix Multiplication
---------------------

Applying matrix :math:`A` to matrix :math:`B`:

.. math::

   \{ A^{\sharp\flat} B^{\sharp\flat} \}^\mu{}_\nu = A^\mu{}_\gamma B^\gamma{}_\nu

Applying matrix :math:`A` to vector :math:`\bv{v}`

.. math::

   \{ A^{\sharp\flat} v^{\sharp} \}^\mu = A^\mu{}_\gamma v^\gamma

.. math::

   \{ A^{\flat\flat} v^{\sharp} \}^\mu = A_\mu{}_\gamma v^\gamma

The new situation is to apply a vector :math:`v^\sharp` to a matrix :math:`A`.
This results in taking the transpose and then *follow matrix multiplication
rules fro mthe left*.

.. math::

   \{ v^\sharp A^{\flat\sharp} \}^\mu = v^\gamma A_\gamma{}^\mu = v^\gamma A^T_\mu{}^\gamma

.. math::

   \{ v^\sharp A^{\flat\flat} \}_\mu = v^\gamma A_\gamma{}_\mu = v^\gamma A^T_\mu{}_\gamma

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

Lowering the index of a contravariant/contravariant tensor is expressed with
:math:`A^{\eta\nu} \; \eta_{\eta\nu} = A_{\mu}{}^{\nu}` in tensor notation.
Following vanilla matrix multiplication rules for :math:`\alpha = \{ +1 & 0
\}^\sharp` and :math:`\beta=\{ 0 & -1 \}^\sharp`, we obtain:

.. math::

   \{ \alpha \\ \beta \}^\flat
   \{
      a & c \\
      b & d
   \}^{\sharp\sharp}
   =
   \{ \alpha & \beta \} \{ \{ a \\ b \} \\ \{ c \\ d\}\}
   =\alpha \; \{ a \\b \} + & \beta \; \{ c \\ d\}
   =\{
       \alpha a + \beta c \\
       \alpha b + \beta d
    \}

.. math::

   \{
       +1 &  0 \\
        0 & -1 \\
   \}^{\flat\flat}
   \{
      a & c \\
      b & d
   \}^{\sharp\sharp}
   =
   \{
       \{ +1 & 0 \} \; a + \{ 0 & -1 \} \; c \\
       \{ +1 & 0 \} \; b + \{ 0 & -1 \} \; d
   \}
   =
   \{
       \{ +a & -c \} \\
       \{ +b & -d \}
   \}
   =
   \{
       +a & +b \\
       -c & -d
   \}^{\flat\sharp}


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
   \{
       a \{ +1 \\  0 \} + c \{  0 \\ -1 \} \\
       b \{ +1 \\  0 \} + d \{  0 \\ -1 \} \\
   \}
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
   \}^{\flat\flat}
   \{ a & c \\
      b & d \\
   \}^{\sharp\flat} 
   &= \{
           \{ +1 \\ 0 \}^\flat \; a + \{ 0 \\ -1 \}^{\flat} \; b,&
           \{ +1 \\ 0 \}^\flat \; c + \{ 0 \\ -1 \}^{\flat} \; d
      \}\\
   &= \{ \{ +a \\ -b \}^{\flat} &
         \{ +c \\ -d \}^{\flat} \}
   = \{ +a & +c \\ -b & -d \}^{\flat\flat}
  \end{align}


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

Notable Difference
------------------

.. include:: ./musical_notation_notable_difference.rst
