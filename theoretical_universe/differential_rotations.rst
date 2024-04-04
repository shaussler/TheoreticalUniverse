Rotations in Cartan's Formalism
===============================

.. rst-class:: custom-author

   by Stéphane Haussler

In this article, I explicitely express rotations in Cartan's formalism and
improve on the notation link with the practicality of calculations in Cartan's
formalism to matrix multiplication. You will see (anti-)symmetries pop out of
the Hodge star operator when ordering the differential forms into matrices.

The matrix representation of differential forms described in this article might
not be wildely known as I have not found the observations detailed here
mentioned anywhere. If I am mistaken and you are aware of freely available
resources, open an issue and I will include a reference. If you find mistakes,
don't hesitate to open an issue or directly provide corrections by sending a
merge request to my `Github repository
<https://github.com/shaussler/TheoreticalUniverse/>`_.

I assume the reader posses a strong grasp of vector calculus as well as working
understanding of differential forms, the wedge product, and :ref:`the concept
of the Hodge dual <hodge_dual:The Hodge Dual>`. With respect to wording, note
that I interchangeably use the words *oriented surface*, *bivector* and
*pseudo-vectors* as they are :ref:`the same objects <hodge_dual:Pseudo vectors
and pseudo scalars>`, albeit named in different contexts.

.. admonition:: Notation
   :class: dropdown

   .. include:: differential_matrices.rst

Rotations in three dimensions
-----------------------------

.. {{{

The notation is powerfull when using a pseudo-vector basis, since the elements
of the matrix can be re-ordered at will. Concretely, a rotation :math:`R` in 3
dimensions is a linear combination of the three associated basis bivectors:

.. math::

   R = 
   R^{x} \ey \wedge \ez +
   R^{y} \ez \wedge \ex +
   R^{z} \ex \wedge \ey

Equivalently, we can write the bivectors in a single column:

.. math::

   R =
   \{ + R^{x} \ey \wedge \ez \\
      + R^{y} \ez \wedge \ex \\
      + R^{z} \ex \wedge \ey \\
   \}
   
Or use a row/column matrix notation:

.. math::

   R =
   \{                       & +R^{z} \ex \wedge \ey &                       \\
                            &                       & +R^{x} \ey \wedge \ez \\
      +R^{y} \ez \wedge \ex &                       &                       \\
   \} \\

We are free to split the terms by using the antisymmetric properties of the
wedge product to obtain:

.. math::

   R
   = \frac{1}{2}
   \{                       & +R^{z} \ex \wedge \ey & -R^{y} \ex \wedge \ez \\
      -R^{z} \ey \wedge \ex &                       & +R^{x} \ey \wedge \ez \\
      +R^{y} \ez \wedge \ex & -R^{x} \ez \wedge \ey &                       \\
   \}

Or even free to invert rows and columns, thus taking the transpose, all while
keeping an equal sign:

.. math::

   R =
   \{                       & -R^{z} \ey \wedge \ex & +R^{y} \ez \wedge \ex \\
      +R^{z} \ex \wedge \ey &                       & -R^{x} \ez \wedge \ey \\
      -R^{y} \ex \wedge \ez & +R^{x} \ey \wedge \ez &                       \\
   \}

Through the use of the Hodge star :math:`\star`, we fall back to the
description of rotations as describe with the cross product :math:`\times`:

.. math::

   \begin{align*}
   \star R &= \star (
       R^{x} \ey \wedge \ez +
       R^{y} \ez \wedge \ex +
       R^{z} \ex \wedge \ey 
   )\\
   &=
   R^{x} \star (\ey \wedge \ez) +
   R^{y} \star (\ez \wedge \ex) +
   R^{z} \star (\ex \wedge \ey) \\
   &=
   R^{x} \ex +
   R^{y} \ey +
   R^{z} \ez
   \end{align*}

That is, the Hodge star of the rotation expressed as a linear comibination of
bivectors is exactly a rotation in terms of cross products in the Hodge dual
space:

.. math::

   \star R &=
   R^{x} \ey \times \ez +
   R^{y} \ez \times \ex +
   R^{z} \ex \times \ey \\

We could have written a covector in the same explicit manner. This notation is
very conveniant when performing calculations in Cartan's framework as it
permits to identify and organize terms for practical calculations by falling
back to regular matrix multiplication.

.. }}}

Rotations in Minkowski space
----------------------------

.. {{{

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

.. }}}

Metric signature
----------------

.. {{{

We choose the metric signature :math:`(+, -, -, -)`. The only non-zero components
are the diagonal components:

.. math::

   \begin{alignat*}{2}
   \eta_{tt} &= \eta^{tt} &= +1 \\
   \eta_{xx} &= \eta^{xx} &= -1 \\
   \eta_{yy} &= \eta^{yy} &= -1 \\
   \eta_{zz} &= \eta^{zz} &= -1 \\
   \end{alignat*}

.. math::

   \eta^{\sharp\sharp} = 
   \{
       +1 \et \otimes \et \\
       -1 \ex \otimes \ex \\
       -1 \ey \otimes \ey \\
       -1 \ez \otimes \ez \\
   \}

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

First flattening
----------------

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

Second flattening
-----------------

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

Raising the Indices Version 1
-----------------------------

.. {{{

In this section, I raise the indice using the free matrix notaion. The mixed
tensor is obtained by applying the flatternig operator :math:`\flat`:

.. math::

   \begin{align*}
   B^{\sharp\flat}
   &= \{
       F^{tx} \; \et \wedge \ex \\
       F^{ty} \; \et \wedge \ey \\
       F^{tz} \; \et \wedge \ez \\
       F^{xy} \; \ex \wedge \ey \\
       F^{yz} \; \ey \wedge \ez \\
       F^{zx} \; \ez \wedge \ex \\
   \}^{\sharp\flat}
   = \{
       F^{tx} \; (\et \wedge \eX)^{\sharp\flat} \\
       F^{ty} \; (\et \wedge \eY)^{\sharp\flat} \\
       F^{tz} \; (\et \wedge \eZ)^{\sharp\flat} \\
       F^{xy} \; (\ex \wedge \eY)^{\sharp\flat} \\
       F^{yz} \; (\ey \wedge \eZ)^{\sharp\flat} \\
       F^{zx} \; (\ez \wedge \eX)^{\sharp\flat} \\
   \}
   = \{
       F^{tx} \; \eta_{x \gamma} \et \wedge \mathbf{e}^\gamma \\
       F^{ty} \; \eta_{y \gamma} \et \wedge \mathbf{e}^\gamma \\
       F^{tz} \; \eta_{z \gamma} \et \wedge \mathbf{e}^\gamma \\
       F^{xy} \; \eta_{y \gamma} \ex \wedge \mathbf{e}^\gamma \\
       F^{yz} \; \eta_{z \gamma} \ey \wedge \mathbf{e}^\gamma \\
       F^{zx} \; \eta_{x \gamma} \ez \wedge \mathbf{e}^\gamma \\
   \} \\
   &= \{
       F^{tx} \; \eta_{x x} \et \wedge \eX \\
       F^{ty} \; \eta_{y y} \et \wedge \eY \\
       F^{tz} \; \eta_{z z} \et \wedge \eZ \\
       F^{xy} \; \eta_{y y} \ex \wedge \eY \\
       F^{yz} \; \eta_{z z} \ey \wedge \eZ \\
       F^{zx} \; \eta_{x x} \ez \wedge \eX \\
   \}
   = \{
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
   F^t{}_x &= F^{t\gamma} \eta_{\gamma x} &= F^{tx} \eta_{xx} &= -F^{tx} \\
   F^t{}_y &= F^{t\gamma} \eta_{\gamma y} &= F^{ty} \eta_{yy} &= -F^{ty} \\
   F^t{}_z &= F^{t\gamma} \eta_{\gamma z} &= F^{tz} \eta_{zz} &= -F^{tz} \\
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
                          & F^t{}_x \; \et \w \eX & F^t{}_y \et \w \eY & F^t{}_z \et \w \eZ \\
       F^x{}_t \ex \w \eT &                       & F^x{}_y \ex \w \eY & F^x{}_z \ex \w \eZ \\
       F^y{}_t \ey \w \eT & F^y{}_x \; \ey \w \eX &                    & F^y{}_z \ey \w \eZ \\
       F^z{}_t \ez \w \eT & F^z{}_x \; \ez \w \eX & F^z{}_y \ez \w \eY &                    \\
   \}
   \end{align}

Further expanding all coefficients, we obtain:

.. math::

   \begin{align}
   \newcommand{\g}{\gamma}
   \newcommand{\w}{\wedge}
   B^{\sharp\flat}
   &= \frac{1}{2}
   \{
                                      & F^{t\g}\eta_{\g x} \et \w \eX & F^{t \g} \eta_{\g y} \et \w \eY & F^{t \g}\eta_{\g z} \et \w \eZ \\
       F^{x\g} \eta_{\g t} \ex \w \eT &                               & F^{x \g} \eta_{\g y} \ex \w \eY & F^{x \g}\eta_{\g z} \ex \w \eZ \\
       F^{y\g} \eta_{\g t} \ey \w \eT & F^{y\g}\eta_{\g x} \ey \w \eX &                                 & F^{y \g}\eta_{\g z} \ey \w \eZ \\
       F^{z\g} \eta_{\g t} \ez \w \eT & F^{z\g}\eta_{\g x} \ez \w \eX & F^{z \g} \eta_{\g y} \ez \w \eY &                                \\
   \}
   \end{align}

Since only the diagonal elements of the metric tensor are non-zero:

.. math::

   \begin{align}
   B^{\sharp\flat}
   &= \frac{1}{2} \{
                                         & F^{tx}\eta_{xx} \; \et \wedge \eX & F^{ty}\eta_{yy} \; \et \wedge \eY & F^{tz}\eta_{zz} \; \et \wedge \eZ \\
      F^{xt} \eta_{tt} \; \ex \wedge \eT &                                   & F^{xy}\eta_{yy} \; \ex \wedge \eY & F^{xz}\eta_{zz} \; \ex \wedge \eZ \\
      F^{yt} \eta_{tt} \; \ey \wedge \eT & F^{yx}\eta_{xx} \; \ey \wedge \eX &                                   & F^{yz}\eta_{zz} \; \ey \wedge \eZ \\
      F^{zt} \eta_{tt} \; \ez \wedge \eT & F^{zx}\eta_{xx} \; \ez \wedge \eX & F^{zy}\eta_{yy} \; \ez \wedge \eY &                                   \\
   \}
   \end{align}

This elements of the Minkowski metric are replaced by their numerical values:

.. math::

   \begin{align}
   B^{\sharp\flat}
   &= \frac{1}{2} \{
                                 & - F^{tx} \; \et \wedge \eX & - F^{ty} \; \et \wedge \eY & - F^{tz} \; \et \wedge \eZ \\
      + F^{xt} \; \ex \wedge \eT &                            & - F^{xy} \; \ex \wedge \eY & - F^{xz} \; \ex \wedge \eZ \\
      + F^{yt} \; \ey \wedge \eT & - F^{yx} \; \ey \wedge \eX &                            & - F^{yz} \; \ey \wedge \eZ \\
      + F^{zt} \; \ez \wedge \eT & - F^{zx} \; \ez \wedge \eX & - F^{zy} \; \ez \wedge \eY &                            \\
   \}
   \end{align}

The antisymetric properties of the components of the double contravariant
rotation tensors permit to simplify and conclude:

.. math::

   \begin{align}
   B^{\sharp\flat}
   &= \frac{1}{2} \{
                                 & - F^{tx} \; \et \wedge \eX & - F^{ty} \; \et \wedge \eY & - F^{tz} \; \et \wedge \eZ \\
      - F^{tx} \; \ex \wedge \eT &                            & - F^{xy} \; \ex \wedge \eY & + F^{zx} \; \ex \wedge \eZ \\
      - F^{ty} \; \ey \wedge \eT & + F^{xy} \; \ey \wedge \eX &                            & - F^{yz} \; \ey \wedge \eZ \\
      - F^{tz} \; \ez \wedge \eT & - F^{zx} \; \ez \wedge \eX & + F^{yz} \; \ez \wedge \eY &                            \\
   \}
   \end{align}


.. }}}

