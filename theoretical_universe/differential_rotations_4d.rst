Rotations in Minkowski Space
============================

.. rst-class:: custom-author

   by Stéphane Haussler

Turning now to a bivectors in Minkowski space, any rotation can be written as
a linear combination of 6 parameters:

.. math::

   B^{\sharp\sharp}
   = \{
       F^{tx} \; \et \wedge \ex \\
       F^{ty} \; \et \wedge \ey \\
       F^{tz} \; \et \wedge \ez \\
       F^{xy} \; \ex \wedge \ey \\
       F^{yz} \; \ey \wedge \ez \\
       F^{zx} \; \ez \wedge \ex \\
   \}

The sharp symbol :math:`\sharp` indicates that the components are doubly
contravariant tensor components. Reordering to a row/column matrix
representation and using the antisimmetric property of the wedge product, we
obtain:

.. math::

   \begin{align}
   %
   \newcommand{\w}{\wedge}
   \newcommand{\et}{\; \mathbf{e}_t}
   \newcommand{\ex}{\; \mathbf{e}_x}
   \newcommand{\ey}{\; \mathbf{e}_y}
   \newcommand{\ez}{\; \mathbf{e}_z}
   %
   B^{\sharp\sharp}
   &= \frac{1}{2}
   \{
                           & + F^{tx} \et \w \ex & + F^{ty} \et \w \ey & + F^{tz} \et \w \ez \\
       - F^{tx} \ex \w \et &                     & + F^{xy} \ex \w \ey & - F^{zx} \ex \w \ez \\
       - F^{ty} \ey \w \et & - F^{xy} \ey \w \ex &                     & + F^{yz} \ey \w \ez \\
       - F^{tz} \ez \w \et & + F^{zx} \ez \w \ex & - F^{yz} \ez \w \ey &                     \\
   \}
   \end{align}

Metric
------

.. {{{

We choose the metric signature :math:`(+, -, -, -)`. The only non-zero components
are the diagonal components. The double contravariant minkowski metric tensor is usually represented in matrix notation
with:

.. math::

   \eta =
   \{
     + 1 &  0 &  0 &  0 \\
       0 & -1 &  0 &  0 \\
       0 &  0 & -1 &  0 \\
       0 &  0 &  0 & -1 \\
   \}

With *musical notation* and *free matrix representation*, we can write
explicitely the the coveriance/contravariance of the tensor as well as the
tensor basis:

.. math::

   \begin{equation}
   \newcommand{\x}{\otimes}
   \eta^{\sharp\sharp} =
   \{
     \begin{array}{rrrr}
     + 1 \et \x \et &  0 \ex \x \et &  0 \ey \x \et &  0 \ey \x \et \\
       0 \et \x \ex & -1 \ex \x \ex &  0 \ey \x \ex &  0 \ey \x \ex \\
       0 \et \x \ey &  0 \ex \x \ey & -1 \ey \x \ey &  0 \ey \x \ey \\
       0 \et \x \ez &  0 \ex \x \ez &  0 \ey \x \ez & -1 \ey \x \ez \\
     \end{array}
   \}
   \end{equation}

Which permits to rewrite the metrix tensor in a compact and convenient manner:

.. math::

   \eta^{\sharp\sharp} = 
   \{
       +1 \et \otimes \et \\
       -1 \ex \otimes \ex \\
       -1 \ey \otimes \ey \\
       -1 \ez \otimes \ez \\
   \}

Equivalently and with the same procedure and arguments, we express the doubly
covariant metric tensor with:

.. math::

   \eta^{\flat\flat} = 
   \{
       +1 \eT \otimes \eT \\
       -1 \eX \otimes \eX \\
       -1 \eY \otimes \eY \\
       -1 \eZ \otimes \eZ \\
   \}

For the basis vectors, this means:
    
.. math::

   \mathbf{e}_\mu \wedge \mathbf{e}_\nu
   = \frac{1}{2}
   (\mathbf{e}_\mu \otimes \mathbf{e}_\nu - \mathbf{e}_\nu \otimes \mathbf{e}_\mu)

We can flatten a basis vector with the flat operator :math:`\flat`

.. math::

   (\mathbf{e}_\mu)^\flat = \eta_{\mu\nu} \mathbf{e}^\nu

And flatten the wedge product like so

.. math::

   (\mathbf{e}_\mu \wedge \mathbf{e}_\nu)^{\flat\sharp}
   = \eta_{\gamma\mu} \mathbf{e}^\gamma \wedge \mathbf{e}_\nu

.. math::

   (\mathbf{e}_\mu \wedge \mathbf{e}_\nu)^{\sharp\flat}
   = \eta_{\gamma\nu} \mathbf{e}_\mu \wedge \mathbf{e}^\gamma

.. math::

   (\mathbf{e}_\mu \wedge \mathbf{e}_\nu)^{\flat\flat}
   = \eta_{\delta\mu} \eta_{\gamma\nu} \mathbf{e}^\delta \wedge \mathbf{e}^\gamma

.. }}}

Flattening of the first kind
----------------------------

.. {{{

For all basis bivectors:

.. math::

   \begin{alignat*}{1}
   \newcommand{\eG}{\mathbf{e}^\gamma}
   \newcommand{\g}{\gamma}
   \newcommand{\w}{\wedge}
   \newcommand{\fl}{\flat}
   \newcommand{\sh}{\sharp}
   (\et \w \ex)^{\fl\sh} &= \eta_{t \g} \eG \w \ex &= \eta_{t t} \et \w \ex &= + \et \w \ex \\
   (\et \w \ey)^{\fl\sh} &= \eta_{t \g} \eG \w \ey &= \eta_{t t} \et \w \ey &= + \et \w \ey \\
   (\et \w \ez)^{\fl\sh} &= \eta_{t \g} \eG \w \ez &= \eta_{t t} \et \w \ez &= + \et \w \ez \\
   (\ex \w \ey)^{\fl\sh} &= \eta_{x \g} \eG \w \ey &= \eta_{x x} \ex \w \ey &= - \ex \w \ey \\
   (\ey \w \ez)^{\fl\sh} &= \eta_{y \g} \eG \w \ez &= \eta_{y y} \ey \w \ez &= - \ey \w \ez \\
   (\ez \w \ex)^{\fl\sh} &= \eta_{z \g} \eG \w \ex &= \eta_{z z} \ez \w \ex &= - \ez \w \ex \\
   \end{alignat*}

Expanding and simplifying, this results in the following explicit expression of
the mixed wedge products:

.. math::

   \begin{alignat*}{1}
   \newcommand{\eG}{\mathbf{e}^\gamma}
   \newcommand{\g}{\gamma}
   \newcommand{\x}{\otimes}
   \newcommand{\w}{\wedge}
   \newcommand{\fl}{\flat}
   \newcommand{\sh}{\sharp}
   (\et \w \ex)^{\fl\sh} &= (\et \x \ex - \ex \x \et)^{\fl\sh} &=& \eta_{t \g} \eG \x \ex - \eta_{x \g} \eG \x \et \\
   (\et \w \ey)^{\fl\sh} &= (\et \x \ey - \ey \x \et)^{\fl\sh} &=& \eta_{t \g} \eG \x \ey - \eta_{y \g} \eG \x \et \\
   (\et \w \ez)^{\fl\sh} &= (\et \x \ez - \ez \x \et)^{\fl\sh} &=& \eta_{t \g} \eG \x \ez - \eta_{z \g} \eG \x \et \\
   (\ex \w \ey)^{\fl\sh} &= (\ex \x \ey - \ey \x \ex)^{\fl\sh} &=& \eta_{x \g} \eG \x \ey - \eta_{y \g} \eG \x \ex \\
   (\ey \w \ez)^{\fl\sh} &= (\ey \x \ez - \ez \x \ey)^{\fl\sh} &=& \eta_{y \g} \eG \x \ez - \eta_{z \g} \eG \x \ey \\
   (\ez \w \ex)^{\fl\sh} &= (\ez \x \ex - \ex \x \ez)^{\fl\sh} &=& \eta_{z \g} \eG \x \ex - \eta_{x \g} \eG \x \ez \\
   \end{alignat*}

.. math::

   \begin{alignat*}{1}
   \newcommand{\x}{\otimes}
   \newcommand{\w}{\wedge}
   \newcommand{\fl}{\flat}
   \newcommand{\sh}{\sharp}
   (\et \w \ex)^{\fl\sh} &= \eta_{t t} \eT \x \ex - \eta_{x x} \eX \x \et &= + \eT \x \ex + \eX \x \et \\
   (\et \w \ey)^{\fl\sh} &= \eta_{t t} \eT \x \ey - \eta_{y y} \eY \x \et &= + \eT \x \ey + \eY \x \et \\
   (\et \w \ez)^{\fl\sh} &= \eta_{t t} \eT \x \ez - \eta_{z z} \eZ \x \et &= + \eT \x \ez + \eZ \x \et \\
   (\ex \w \ey)^{\fl\sh} &= \eta_{x x} \eX \x \ey - \eta_{y y} \eY \x \ex &= - \eX \x \ey + \eY \x \ex \\
   (\ey \w \ez)^{\fl\sh} &= \eta_{y y} \eY \x \ez - \eta_{z z} \eZ \x \ey &= - \eY \x \ez + \eZ \x \ey \\
   (\ez \w \ex)^{\fl\sh} &= \eta_{z z} \eZ \x \ex - \eta_{x x} \eX \x \ez &= - \eZ \x \ex + \eX \x \ez \\
   \end{alignat*}

.. math::

   \begin{alignat*}{}
   \eT \wedge \ex &= + \mathbf{e}^t \otimes \ex + \mathbf{e}^x \otimes \et \\
   \eT \wedge \ey &= + \mathbf{e}^t \otimes \ey + \mathbf{e}^y \otimes \et \\
   \eT \wedge \ez &= + \mathbf{e}^t \otimes \ez + \mathbf{e}^z \otimes \et \\
   \eX \wedge \ey &= + \mathbf{e}^x \otimes \ey - \mathbf{e}^y \otimes \ex \\
   \eY \wedge \ez &= + \mathbf{e}^y \otimes \ez - \mathbf{e}^z \otimes \ey \\
   \eZ \wedge \ex &= + \mathbf{e}^z \otimes \ex - \mathbf{e}^x \otimes \ez \\
   \end{alignat*}

From the explicit calculation of the basis elements, we observe the following
properties:

====================== ============
Basis element          Symmetry
====================== ============
:math:`\eT \wedge \ex` Symetric
:math:`\eT \wedge \ey` Symetric
:math:`\eT \wedge \ez` Symetric
:math:`\eX \wedge \ey` Antisymetric
:math:`\eY \wedge \ez` Antisymetric
:math:`\eZ \wedge \ex` Antisymetric
====================== ============

.. }}}

Flatterning of the second kind
------------------------------

.. {{{

For all basis bivectors:

.. math::

   \begin{alignat*}{1}
   \newcommand{\eG}{\mathbf{e}^\gamma}
   \newcommand{\g}{\gamma}
   \newcommand{\x}{\otimes}
   \newcommand{\w}{\wedge}
   \newcommand{\fl}{\flat}
   \newcommand{\sh}{\sharp}
   (\et \w \ex)^{\sh\fl} &= \eta_{x \g} \et \w \eG &= \eta_{x x} \et \w \eX &= - \et \w \eX \\
   (\et \w \ey)^{\sh\fl} &= \eta_{y \g} \et \w \eG &= \eta_{y y} \et \w \eY &= - \et \w \eY \\
   (\et \w \ez)^{\sh\fl} &= \eta_{z \g} \et \w \eG &= \eta_{z z} \et \w \eZ &= - \et \w \eZ \\
   (\ex \w \ey)^{\sh\fl} &= \eta_{y \g} \ex \w \eG &= \eta_{y y} \ex \w \eY &= - \ex \w \eY \\
   (\ey \w \ez)^{\sh\fl} &= \eta_{z \g} \ey \w \eG &= \eta_{z z} \ey \w \eZ &= - \ey \w \eZ \\
   (\ez \w \ex)^{\sh\fl} &= \eta_{x \g} \ez \w \eG &= \eta_{x x} \ez \w \eX &= - \ez \w \eX \\
   \end{alignat*}

Expanding and simplifying, this results in the following explicit expression of
the mixed wedge products:

.. math::

   \begin{alignat*}{1}
   \newcommand{\eG}{\mathbf{e}^\gamma}
   \newcommand{\g}{\gamma}
   \newcommand{\x}{\otimes}
   \newcommand{\w}{\wedge}
   \newcommand{\fl}{\flat}
   \newcommand{\sh}{\sharp}
   (\et \w \ex)^{\sh\fl} &= (\et \x \ex - \ex \x \et)^{\sh\sh} &= \eta_{x \g} \et \x \eG - \eta_{t \g} \ex \x \eG \\
   (\et \w \ey)^{\sh\fl} &= (\et \x \ey - \ey \x \et)^{\sh\sh} &= \eta_{y \g} \et \x \eG - \eta_{t \g} \ey \x \eG \\
   (\et \w \ez)^{\sh\fl} &= (\et \x \ez - \ez \x \et)^{\sh\sh} &= \eta_{z \g} \et \x \eG - \eta_{t \g} \ez \x \eG \\
   (\ex \w \ey)^{\sh\fl} &= (\ex \x \ey - \ey \x \ex)^{\sh\sh} &= \eta_{y \g} \ex \x \eG - \eta_{x \g} \ey \x \eG \\
   (\ey \w \ez)^{\sh\fl} &= (\ey \x \ez - \ez \x \ey)^{\sh\sh} &= \eta_{z \g} \ey \x \eG - \eta_{y \g} \ez \x \eG \\
   (\ez \w \ex)^{\sh\fl} &= (\ez \x \ex - \ex \x \ez)^{\sh\sh} &= \eta_{x \g} \ez \x \eG - \eta_{z \g} \ex \x \eG \\
   \end{alignat*}

.. math::

   \begin{alignat*}{1}
   \newcommand{\x}{\otimes}
   \newcommand{\w}{\wedge}
   \newcommand{\fl}{\flat}
   \newcommand{\sh}{\sharp}
   (\et \w \ex)^{\fl\sh} &= \eta_{x x} \et \x \ex - \eta_{t t} \ex \x \et &= - \et \x \ex - \ex \x \et \\
   (\et \w \ey)^{\fl\sh} &= \eta_{y y} \et \x \ey - \eta_{t t} \ey \x \et &= - \et \x \ey - \ey \x \et \\
   (\et \w \ez)^{\fl\sh} &= \eta_{z z} \et \x \ez - \eta_{t t} \ez \x \et &= - \et \x \ez - \ez \x \et \\
   (\ex \w \ey)^{\fl\sh} &= \eta_{y y} \ex \x \ey - \eta_{x x} \ey \x \ex &= - \ex \x \ey + \ey \x \ex \\
   (\ey \w \ez)^{\fl\sh} &= \eta_{z z} \ey \x \ez - \eta_{y y} \ez \x \ey &= - \ey \x \ez + \ez \x \ey \\
   (\ez \w \ex)^{\fl\sh} &= \eta_{x x} \ez \x \ex - \eta_{z z} \ex \x \ez &= - \ez \x \ex + \ex \x \ez \\
   \end{alignat*}

From the explicit calculation of the basis elements, we observe the following
properties:

====================== ============ =============================================================
Basis element          Symmetry     Expression
====================== ============ =============================================================
:math:`\et \wedge \eX` Symetric     :math:`+ \mathbf{e}^t \otimes \ex + \mathbf{e}^x \otimes \et`
:math:`\et \wedge \eY` Symetric     :math:`+ \mathbf{e}^t \otimes \ey + \mathbf{e}^y \otimes \et`
:math:`\et \wedge \eZ` Symetric     :math:`+ \mathbf{e}^t \otimes \ez + \mathbf{e}^z \otimes \et`
:math:`\ex \wedge \eY` Antisymetric :math:`+ \mathbf{e}^x \otimes \ey - \mathbf{e}^y \otimes \ex`
:math:`\ey \wedge \eZ` Antisymetric :math:`+ \mathbf{e}^y \otimes \ez - \mathbf{e}^z \otimes \ey`
:math:`\ez \wedge \eX` Antisymetric :math:`+ \mathbf{e}^z \otimes \ex - \mathbf{e}^x \otimes \ez`
====================== ============ =============================================================

.. }}}

Raising the indices Version 1
-----------------------------

.. {{{

In this section, I raise the indice using the free matrix notaion. The mixed
tensor is obtained by applying the flatternig operator :math:`\flat`:

.. math::

   \begin{equation}
   B^{\sharp\flat}
   =
   \{
     F^{tx} \; \et \wedge \ex \\
     F^{ty} \; \et \wedge \ey \\
     F^{tz} \; \et \wedge \ez \\
     F^{xy} \; \ex \wedge \ey \\
     F^{yz} \; \ey \wedge \ez \\
     F^{zx} \; \ez \wedge \ex \\
   \}^{\sharp\flat}
   =
   \{
     - F^{tx} \; \et \wedge \eX \\
     - F^{ty} \; \et \wedge \eY \\
     - F^{tz} \; \et \wedge \eZ \\
     - F^{xy} \; \ex \wedge \eY \\
     - F^{yz} \; \ey \wedge \eZ \\
     - F^{zx} \; \ez \wedge \eX \\
   \}
   \end{equation}

.. admonition:: Every calculation step
   :class: dropdown

   .. math::
   
      \begin{align*}
      B^{\sharp\flat}
      &=
      \{
        F^{tx} \; \et \wedge \ex \\
        F^{ty} \; \et \wedge \ey \\
        F^{tz} \; \et \wedge \ez \\
        F^{xy} \; \ex \wedge \ey \\
        F^{yz} \; \ey \wedge \ez \\
        F^{zx} \; \ez \wedge \ex \\
      \}^{\sharp\flat}
      =
      \{
        F^{tx} \; (\et \wedge \ex)^{\sharp\flat} \\
        F^{ty} \; (\et \wedge \ey)^{\sharp\flat} \\
        F^{tz} \; (\et \wedge \ez)^{\sharp\flat} \\
        F^{xy} \; (\ex \wedge \ey)^{\sharp\flat} \\
        F^{yz} \; (\ey \wedge \ez)^{\sharp\flat} \\
        F^{zx} \; (\ez \wedge \ex)^{\sharp\flat} \\
      \}
      =
      \{
        F^{tx} \; \et \wedge \eta_{x \gamma}\mathbf{e}^\gamma \\
        F^{ty} \; \et \wedge \eta_{y \gamma}\mathbf{e}^\gamma \\
        F^{tz} \; \et \wedge \eta_{z \gamma}\mathbf{e}^\gamma \\
        F^{xy} \; \ex \wedge \eta_{y \gamma}\mathbf{e}^\gamma \\
        F^{yz} \; \ey \wedge \eta_{z \gamma}\mathbf{e}^\gamma \\
        F^{zx} \; \ez \wedge \eta_{x \gamma}\mathbf{e}^\gamma \\
      \} \\
      &=
      \{
        F^{tx} \; \eta_{x \gamma} \et \wedge \mathbf{e}^\gamma \\
        F^{ty} \; \eta_{y \gamma} \et \wedge \mathbf{e}^\gamma \\
        F^{tz} \; \eta_{z \gamma} \et \wedge \mathbf{e}^\gamma \\
        F^{xy} \; \eta_{y \gamma} \ex \wedge \mathbf{e}^\gamma \\
        F^{yz} \; \eta_{z \gamma} \ey \wedge \mathbf{e}^\gamma \\
        F^{zx} \; \eta_{x \gamma} \ez \wedge \mathbf{e}^\gamma \\
      \}
      =
      \{
        F^{tx} \; \eta_{x x} \et \wedge \eX \\
        F^{ty} \; \eta_{y y} \et \wedge \eY \\
        F^{tz} \; \eta_{z z} \et \wedge \eZ \\
        F^{xy} \; \eta_{y y} \ex \wedge \eY \\
        F^{yz} \; \eta_{z z} \ey \wedge \eZ \\
        F^{zx} \; \eta_{x x} \ez \wedge \eX \\
      \}
      =
      \{
        - F^{tx} \; \et \wedge \eX \\
        - F^{ty} \; \et \wedge \eY \\
        - F^{tz} \; \et \wedge \eZ \\
        - F^{xy} \; \ex \wedge \eY \\
        - F^{yz} \; \ey \wedge \eZ \\
        - F^{zx} \; \ez \wedge \eX \\
      \}
      \end{align*}

Taking into account the symetric property of :math:`\et \wedge \eX`, :math:`\et
\wedge \eY`, and :math:`\et \wedge \eZ`, as well the antisymetric property of
:math:`\ex \wedge \eY`, :math:`\ey \wedge \eZ`, and :math:`\ez \wedge \eX`
demonstrated above, this results in:

.. math::

   \begin{align}
   \newcommand{\w}{\wedge}
   B^{\sharp\flat}
   &= \frac{1}{2}
   \{
                         & - F^{tx} \et \w \eX & - F^{ty} \et \w \eY & - F^{tz} \et \w \eZ \\
     - F^{tx} \ex \w \eT &                     & - F^{xy} \ex \w \eY & + F^{zx} \ex \w \eZ \\
     - F^{ty} \ey \w \eT & + F^{xy} \ey \w \eX &                     & - F^{yz} \ey \w \eZ \\
     - F^{tz} \ez \w \eT & - F^{zx} \ez \w \eX & + F^{yz} \ez \w \eY &                     \\
   \}
   \end{align}

.. }}}

Raising the indices Version 2
-----------------------------

.. {{{

We can and raise the indices by applying the Minkowski metric to each
components. This calculation can be performed in abstract index notation using
Einstein's summation convention. The following symmetries greatly simplify the
calculations:

* All off-diagonal terms of the minkowski metric are zero
* All diagonal terms of the rotation tensor are zero
* The doubly contravariant rotation tensor is antisymmetric: :math:`F^{\mu\nu}
  = -F^{\nu\mu}`

With :math:`F^{tt}=0`, as well as :math:`\eta^{tx}=0`,
:math:`\eta^{ty}=0`:math:`\eta^{tz}=0`, we expand and obtain:

.. math::

   \begin{alignat*}{3}
   \renewcommand{\γ}{\gamma}
   \renewcommand{\η}{\eta}
   F^t{}_x &= F^{t\γ} \η_{\γ x} &= F^{tx} \η_{xx} &= -F^{tx} \\
   F^t{}_y &= F^{t\γ} \η_{\γ y} &= F^{ty} \η_{yy} &= -F^{ty} \\
   F^t{}_z &= F^{t\γ} \η_{\γ z} &= F^{tz} \η_{zz} &= -F^{tz} \\
   \end{alignat*}

With :math:`F^{xx}=F^{yy}=F^{zz}=0`, :math:`F^{\mu\nu}=-F^{\nu\mu}`, as well as
:math:`\eta^{tx}=0`, :math:`\eta^{ty}=0`:math:`\eta^{tz}=0`, we expand and
obtain:

.. math::

   \begin{alignat*}{3}
   F^x{}_t &= F^{x\gamma} \eta_{\gamma t} &= F^{xt} \eta_{tt} &= -F^{tx} \\
   F^y{}_t &= F^{y\gamma} \eta_{\gamma t} &= F^{yt} \eta_{tt} &= -F^{ty} \\
   F^z{}_t &= F^{z\gamma} \eta_{\gamma t} &= F^{zt} \eta_{tt} &= -F^{tz} \\
   \end{alignat*}

In the same manner, we get:

.. math::

   \begin{alignat}{2}
   F^x{}_y &= F^{x\gamma} \eta_{\gamma y} &= F^{xy} \eta_{yy} &= -F^{xy} \\
   F^y{}_z &= F^{y\gamma} \eta_{\gamma z} &= F^{yz} \eta_{zz} &= -F^{yz} \\
   F^z{}_x &= F^{z\gamma} \eta_{\gamma x} &= F^{zx} \eta_{xx} &= -F^{zx} \\
   \end{alignat}

We have a mixed tensor of Rank two with the form:

.. math::

   \begin{align}
   \newcommand{\w}{\wedge}
   B^{\sharp\flat}
   &= \frac{1}{2} \{
     F^t{}_t \et \w \eT & F^t{}_x \et \w \eX & F^t{}_y \et \w \eY & F^t{}_z \et \w \eZ \\
     F^x{}_t \ex \w \eT & F^x{}_x \ex \w \eX & F^x{}_y \ex \w \eY & F^x{}_z \ex \w \eZ \\
     F^y{}_t \ey \w \eT & F^y{}_x \ey \w \eX & F^y{}_y \ey \w \eY & F^y{}_z \ey \w \eZ \\
     F^z{}_t \ez \w \eT & F^z{}_x \ez \w \eX & F^z{}_y \ez \w \eY & F^z{}_z \ez \w \eZ \\
   \}
   \end{align}

All diagonal components are zero since:

.. math::

   \mathbf{e}_\mu \wedge \mathbf{e}^\mu
   = \frac{1}{2}
   (\mathbf{e}_\mu \otimes \mathbf{e}^\mu - \mathbf{e}_\mu \otimes \mathbf{e}^\mu)
   =0

This result in:

.. math::

   \begin{align}
   \newcommand{\w}{\wedge}
   B^{\sharp\flat}
   &= \frac{1}{2}
   \{
                          & F^t{}_x \et \w \eX & F^t{}_y \et \w \eY & F^t{}_z \et \w \eZ \\
       F^x{}_t \ex \w \eT &                    & F^x{}_y \ex \w \eY & F^x{}_z \ex \w \eZ \\
       F^y{}_t \ey \w \eT & F^y{}_x \ey \w \eX &                    & F^y{}_z \ey \w \eZ \\
       F^z{}_t \ez \w \eT & F^z{}_x \ez \w \eX & F^z{}_y \ez \w \eY &                    \\
   \}
   \end{align}

Further expanding all coefficients, we obtain:

.. math::

   \begin{align}
   \newcommand{\{}{\begin{bmatrix}} \newcommand{\}}{\end{bmatrix}}
   \newcommand{\γ}{\gamma} %u03b3
   \newcommand{\∧}{\wedge} %u2227
   \newcommand{\η}{\eta} %u03b
   B^{\sharp\flat}
   &= \frac{1}{2}
   \{
                                  & F^{t\γ} \η_{\γ x} \et \∧ \eX & F^{t \γ} \η_{\γ y} \et \∧ \eY & F^{t \γ} \η_{\γ z} \et \∧ \eZ \\
     F^{x\g} \η_{\γ t} \ex \∧ \eT &                              & F^{x \γ} \η_{\γ y} \ex \∧ \eY & F^{x \γ} \η_{\γ z} \ex \∧ \eZ \\
     F^{y\g} \η_{\γ t} \ey \∧ \eT & F^{y\γ} \η_{\γ x} \ey \∧ \eX &                               & F^{y \γ} \η_{\γ z} \ey \∧ \eZ \\
     F^{z\g} \η_{\γ t} \ez \∧ \eT & F^{z\γ} \η_{\γ x} \ez \∧ \eX & F^{z \γ} \η_{\γ y} \ez \∧ \eY &                               \\
   \}
   \end{align}

Since only the diagonal elements of the metric tensor are non-zero:

.. math::

   \begin{align}
   \newcommand{\{}{\begin{bmatrix}} \newcommand{\}}{\end{bmatrix}}
   \newcommand{\∧}{\wedge} %u2227
   \newcommand{\η}{\eta} %u03b7
   B^{\sharp\flat}
   &= \frac{1}{2}
   \{
                               & F^{tx} \η_{xx} \et \∧ \eX & F^{ty} \η_{yy} \et \∧ \eY & F^{tz} \η_{zz} \et \∧ \eZ \\
     F^{xt} \η_{tt} \ex \∧ \eT &                           & F^{xy} \η_{yy} \ex \∧ \eY & F^{xz} \η_{zz} \ex \∧ \eZ \\
     F^{yt} \η_{tt} \ey \∧ \eT & F^{yx} \η_{xx} \ey \∧ \eX &                           & F^{yz} \η_{zz} \ey \∧ \eZ \\
     F^{zt} \η_{tt} \ez \∧ \eT & F^{zx} \η_{xx} \ez \∧ \eX & F^{zy} \η_{yy} \ez \∧ \eY &                           \\
   \}
   \end{align}

This elements of the Minkowski metric are replaced by their numerical values:

.. math::

   \begin{align}
   \newcommand{\{}{\begin{bmatrix}} \newcommand{\}}{\end{bmatrix}}
   \newcommand{\et}{\mathbf{e_t}} \newcommand{\ex}{\mathbf{e_x}}
   \newcommand{\ey}{\mathbf{e_y}} \newcommand{\ez}{\mathbf{e_z}}
   \newcommand{\∧}{\wedge} %u2227
   B^{\sharp\flat}
   &= \frac{1}{2} \{
                         & - F^{tx} \et \∧ \eX & - F^{ty} \et \∧ \eY & - F^{tz} \et \∧ \eZ \\
     + F^{xt} \ex \∧ \eT &                     & - F^{xy} \ex \∧ \eY & - F^{xz} \ex \∧ \eZ \\
     + F^{yt} \ey \∧ \eT & - F^{yx} \ey \∧ \eX &                     & - F^{yz} \ey \∧ \eZ \\
     + F^{zt} \ez \∧ \eT & - F^{zx} \ez \∧ \eX & - F^{zy} \ez \∧ \eY &                     \\
   \}
   \end{align}

The antisymetric properties of the components of the double contravariant
rotation tensors permit to simplify and conclude:

.. math::

   \begin{align}
   \newcommand{\{}{\begin{bmatrix}} \newcommand{\}}{\end{bmatrix}}
   \newcommand{\et}{\mathbf{e_t}} \newcommand{\ex}{\mathbf{e_x}}
   \newcommand{\ey}{\mathbf{e_y}} \newcommand{\ez}{\mathbf{e_z}}
   \newcommand{\eT}{\mathbf{e^t}} \newcommand{\eX}{\mathbf{e^x}}
   \newcommand{\eY}{\mathbf{e^y}} \newcommand{\eZ}{\mathbf{e^z}}
   \newcommand{\∧}{\wedge} %u2227
   B^{\sharp\flat}
   &= \frac{1}{2} \{
                          & - F^{tx} \; \et \∧ \eX & - F^{ty} \et \∧ \eY & - F^{tz} \et \∧w \eZ \\
      - F^{tx} \ex \∧ \eT &                        & - F^{xy} \ex \∧ \eY & + F^{zx} \ex \∧w \eZ \\
      - F^{ty} \ey \∧ \eT & + F^{xy} \; \ey \∧ \eX &                     & - F^{yz} \ey \∧w \eZ \\
      - F^{tz} \ez \∧ \eT & - F^{zx} \; \ez \∧ \eX & + F^{yz} \ez \∧ \eY &                      \\
   \}
   \end{align}

.. }}}

:math:`\mathfrak{so}(1,3)` Lie Algegra of the Lorentz group
-----------------------------------------------------------

.. {{{

.. }}}

