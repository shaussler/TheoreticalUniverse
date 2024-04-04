Rotations in Cartan's Formalism
===============================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

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
*pseudo-vectors* as they are :ref:`the same objects <hodge_dual:The Hodge
Dual>`, albeit named in different contexts.

Formalism
---------

.. {{{

I use matrix notation in a manner which is not fully conventional, but that I
hope highlights symmetries and that the reader will find obvious. Everything in
a matrix is expressed with its basis vectors and can be reordered at will. For
example, a vector is often expressed with an implicit basis as:

.. math::

   v = \{ x \\ y \\ z\}

I merely propose to write the basis explicitely in the matrix:

.. math::

   v = \{ x \mathbf{e}_x \\ y \mathbf{e}_y \\ z \mathbf{e}_x \}

Which means that a :math:`+` sign can be added anywhere and the expression
written in the standard form:

.. math::

   v = x \mathbf{e}_x + y \mathbf{e}_y + z \mathbf{e}_x

.. }}}

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
   \{ + R^{x} \mathbf{e}_y \wedge \mathbf{e}_z \\
      + R^{y} \mathbf{e}_z \wedge \mathbf{e}_x \\
      + R^{z} \mathbf{e}_x \wedge \mathbf{e}_y \\
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
   R^{x} \star \ey \wedge \ez +
   R^{y} \star \ez \wedge \ex +
   R^{z} \star \ex \wedge \ey \\
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
   B^{\sharp\sharp}
   &= \frac{1}{2} \{
                                  & + F^{tx} \; \et \wedge \ex & + F^{ty} \; \et \wedge \ey & + F^{tz} \; \et \wedge \ez \\ 
       - F^{tx} \; \ex \wedge \et &                            & + F^{xy} \; \ex \wedge \ey & - F^{zx} \; \ex \wedge \ez \\
       - F^{ty} \; \ey \wedge \et & - F^{xy} \; \ey \wedge \ex &                            & + F^{yz} \; \ey \wedge \ez \\
       - F^{tz} \; \ez \wedge \et & + F^{zx} \; \ez \wedge \ex & - F^{yz} \; \ez \wedge \ey &                            \\
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
   (\et \wedge \ex)^{\flat\sharp} &=&& \eta_{t \gamma} \mathbf{e}^\gamma \wedge \ex &=&& \eta_{t t} \et \wedge \ex &=&& + \et \wedge \ex \\
   (\et \wedge \ey)^{\flat\sharp} &=&& \eta_{t \gamma} \mathbf{e}^\gamma \wedge \ey &=&& \eta_{t t} \et \wedge \ey &=&& + \et \wedge \ey \\
   (\et \wedge \ez)^{\flat\sharp} &=&& \eta_{t \gamma} \mathbf{e}^\gamma \wedge \ez &=&& \eta_{t t} \et \wedge \ez &=&& + \et \wedge \ez \\
   (\ex \wedge \ey)^{\flat\sharp} &=&& \eta_{x \gamma} \mathbf{e}^\gamma \wedge \ey &=&& \eta_{x x} \ex \wedge \ey &=&& - \ex \wedge \ey \\
   (\ey \wedge \ez)^{\flat\sharp} &=&& \eta_{y \gamma} \mathbf{e}^\gamma \wedge \ez &=&& \eta_{y y} \ey \wedge \ez &=&& - \ey \wedge \ez \\
   (\ez \wedge \ex)^{\flat\sharp} &=&& \eta_{z \gamma} \mathbf{e}^\gamma \wedge \ex &=&& \eta_{z z} \ez \wedge \ex &=&& - \ez \wedge \ex \\
   \end{alignat*}

Expanding and simplifying, this results in the following explicit expression of
the mixed wedge products:

.. math::

   \begin{alignat*}{1}
   (\et \wedge \ex)^{\flat\sharp} &= (\et \otimes \ex - \ex \otimes \et)^{\flat\sharp} &=& \eta_{t \gamma} \mathbf{e}^\gamma \otimes \ex - \eta_{x \gamma} \mathbf{e}^\gamma \otimes \et \\
   (\et \wedge \ey)^{\flat\sharp} &= (\et \otimes \ey - \ey \otimes \et)^{\flat\sharp} &=& \eta_{t \gamma} \mathbf{e}^\gamma \otimes \ey - \eta_{y \gamma} \mathbf{e}^\gamma \otimes \et \\
   (\et \wedge \ez)^{\flat\sharp} &= (\et \otimes \ez - \ez \otimes \et)^{\flat\sharp} &=& \eta_{t \gamma} \mathbf{e}^\gamma \otimes \ez - \eta_{z \gamma} \mathbf{e}^\gamma \otimes \et \\
   (\ex \wedge \ey)^{\flat\sharp} &= (\ex \otimes \ey - \ey \otimes \ex)^{\flat\sharp} &=& \eta_{x \gamma} \mathbf{e}^\gamma \otimes \ey - \eta_{y \gamma} \mathbf{e}^\gamma \otimes \ex \\
   (\ey \wedge \ez)^{\flat\sharp} &= (\ey \otimes \ez - \ez \otimes \ey)^{\flat\sharp} &=& \eta_{y \gamma} \mathbf{e}^\gamma \otimes \ez - \eta_{z \gamma} \mathbf{e}^\gamma \otimes \ey \\
   (\ez \wedge \ex)^{\flat\sharp} &= (\ez \otimes \ex - \ex \otimes \ez)^{\flat\sharp} &=& \eta_{z \gamma} \mathbf{e}^\gamma \otimes \ex - \eta_{x \gamma} \mathbf{e}^\gamma \otimes \ez \\
   \end{alignat*}

.. math::

   \begin{alignat*}{1}
   (\et \wedge \ex)^{\flat\sharp} &= \eta_{t t} \mathbf{e}^t \otimes \ex - \eta_{x x} \mathbf{e}^x \otimes \et &= + \mathbf{e}^t \otimes \ex + \mathbf{e}^x \otimes \et \\
   (\et \wedge \ey)^{\flat\sharp} &= \eta_{t t} \mathbf{e}^t \otimes \ey - \eta_{y y} \mathbf{e}^y \otimes \et &= + \mathbf{e}^t \otimes \ey + \mathbf{e}^y \otimes \et \\
   (\et \wedge \ez)^{\flat\sharp} &= \eta_{t t} \mathbf{e}^t \otimes \ez - \eta_{z z} \mathbf{e}^z \otimes \et &= + \mathbf{e}^t \otimes \ez + \mathbf{e}^z \otimes \et \\
   (\ex \wedge \ey)^{\flat\sharp} &= \eta_{x x} \mathbf{e}^x \otimes \ey - \eta_{y y} \mathbf{e}^y \otimes \ex &= - \mathbf{e}^x \otimes \ey + \mathbf{e}^y \otimes \ex \\
   (\ey \wedge \ez)^{\flat\sharp} &= \eta_{y y} \mathbf{e}^y \otimes \ez - \eta_{z z} \mathbf{e}^z \otimes \ey &= - \mathbf{e}^y \otimes \ez + \mathbf{e}^z \otimes \ey \\
   (\ez \wedge \ex)^{\flat\sharp} &= \eta_{z z} \mathbf{e}^z \otimes \ex - \eta_{x x} \mathbf{e}^x \otimes \ez &= - \mathbf{e}^z \otimes \ex + \mathbf{e}^x \otimes \ez \\
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
   (\et \wedge \ex)^{\sharp\flat} &=&& \eta_{x \gamma} \et \wedge \mathbf{e}^\gamma &=&& \eta_{x x} \et \wedge \eX &=&& - \et \wedge \eX \\
   (\et \wedge \ey)^{\sharp\flat} &=&& \eta_{y \gamma} \et \wedge \mathbf{e}^\gamma &=&& \eta_{y y} \et \wedge \eY &=&& - \et \wedge \eY \\
   (\et \wedge \ez)^{\sharp\flat} &=&& \eta_{z \gamma} \et \wedge \mathbf{e}^\gamma &=&& \eta_{z z} \et \wedge \eZ &=&& - \et \wedge \eZ \\
   (\ex \wedge \ey)^{\sharp\flat} &=&& \eta_{y \gamma} \ex \wedge \mathbf{e}^\gamma &=&& \eta_{y y} \ex \wedge \eY &=&& - \ex \wedge \eY \\
   (\ey \wedge \ez)^{\sharp\flat} &=&& \eta_{z \gamma} \ey \wedge \mathbf{e}^\gamma &=&& \eta_{z z} \ey \wedge \eZ &=&& - \ey \wedge \eZ \\
   (\ez \wedge \ex)^{\sharp\flat} &=&& \eta_{x \gamma} \ez \wedge \mathbf{e}^\gamma &=&& \eta_{x x} \ez \wedge \eX &=&& - \ez \wedge \eX \\
   \end{alignat*}

Expanding and simplifying, this results in the following explicit expression of
the mixed wedge products:

.. math::

   \begin{alignat*}{1}
   (\et \wedge \ex)^{\sharp\flat} &= (\et \otimes \ex - \ex \otimes \et)^{\sharp\sharp} &=& \eta_{x \gamma} \et \otimes \mathbf{e}^\gamma - \eta_{t \gamma} \ex \otimes \mathbf{e}^\gamma \\
   (\et \wedge \ey)^{\sharp\flat} &= (\et \otimes \ey - \ey \otimes \et)^{\sharp\sharp} &=& \eta_{y \gamma} \et \otimes \mathbf{e}^\gamma - \eta_{t \gamma} \ey \otimes \mathbf{e}^\gamma \\
   (\et \wedge \ez)^{\sharp\flat} &= (\et \otimes \ez - \ez \otimes \et)^{\sharp\sharp} &=& \eta_{z \gamma} \et \otimes \mathbf{e}^\gamma - \eta_{t \gamma} \ez \otimes \mathbf{e}^\gamma \\
   (\ex \wedge \ey)^{\sharp\flat} &= (\ex \otimes \ey - \ey \otimes \ex)^{\sharp\sharp} &=& \eta_{y \gamma} \ex \otimes \mathbf{e}^\gamma - \eta_{x \gamma} \ey \otimes \mathbf{e}^\gamma \\
   (\ey \wedge \ez)^{\sharp\flat} &= (\ey \otimes \ez - \ez \otimes \ey)^{\sharp\sharp} &=& \eta_{z \gamma} \ey \otimes \mathbf{e}^\gamma - \eta_{y \gamma} \ez \otimes \mathbf{e}^\gamma \\
   (\ez \wedge \ex)^{\sharp\flat} &= (\ez \otimes \ex - \ex \otimes \ez)^{\sharp\sharp} &=& \eta_{x \gamma} \ez \otimes \mathbf{e}^\gamma - \eta_{z \gamma} \ex \otimes \mathbf{e}^\gamma \\
   \end{alignat*}

.. math::

   \begin{alignat*}{1}
   (\et \wedge \ex)^{\flat\sharp} &= \eta_{x x} \mathbf{e}^t \otimes \ex - \eta_{t t} \mathbf{e}^x \otimes \et &= - \mathbf{e}^t \otimes \ex - \mathbf{e}^x \otimes \et \\
   (\et \wedge \ey)^{\flat\sharp} &= \eta_{y y} \mathbf{e}^t \otimes \ey - \eta_{t t} \mathbf{e}^y \otimes \et &= - \mathbf{e}^t \otimes \ey - \mathbf{e}^y \otimes \et \\
   (\et \wedge \ez)^{\flat\sharp} &= \eta_{z z} \mathbf{e}^t \otimes \ez - \eta_{t t} \mathbf{e}^z \otimes \et &= - \mathbf{e}^t \otimes \ez - \mathbf{e}^z \otimes \et \\
   (\ex \wedge \ey)^{\flat\sharp} &= \eta_{y y} \mathbf{e}^x \otimes \ey - \eta_{x x} \mathbf{e}^y \otimes \ex &= - \mathbf{e}^x \otimes \ey + \mathbf{e}^y \otimes \ex \\
   (\ey \wedge \ez)^{\flat\sharp} &= \eta_{z z} \mathbf{e}^y \otimes \ez - \eta_{y y} \mathbf{e}^z \otimes \ey &= - \mathbf{e}^y \otimes \ez + \mathbf{e}^z \otimes \ey \\
   (\ez \wedge \ex)^{\flat\sharp} &= \eta_{x x} \mathbf{e}^z \otimes \ex - \eta_{z z} \mathbf{e}^x \otimes \ez &= - \mathbf{e}^z \otimes \ex + \mathbf{e}^x \otimes \ez \\
   \end{alignat*}

.. math::

   \begin{alignat*}{1}
   \et \wedge \eX &= + \mathbf{e}^t \otimes \ex + \mathbf{e}^x \otimes \et \\
   \et \wedge \eY &= + \mathbf{e}^t \otimes \ey + \mathbf{e}^y \otimes \et \\
   \et \wedge \eZ &= + \mathbf{e}^t \otimes \ez + \mathbf{e}^z \otimes \et \\
   \ex \wedge \eY &= + \mathbf{e}^x \otimes \ey - \mathbf{e}^y \otimes \ex \\
   \ey \wedge \eZ &= + \mathbf{e}^y \otimes \ez - \mathbf{e}^z \otimes \ey \\
   \ez \wedge \eX &= + \mathbf{e}^z \otimes \ex - \mathbf{e}^x \otimes \ez \\
   \end{alignat*}

From the explicit calculation of the basis elements, we observe the following
properties:

====================== ============
Basis element          Symmetry
====================== ============
:math:`\et \wedge \eX` Symetric
:math:`\et \wedge \eY` Symetric
:math:`\et \wedge \eZ` Symetric
:math:`\ex \wedge \eY` Antisymetric
:math:`\ey \wedge \eZ` Antisymetric
:math:`\ez \wedge \eX` Antisymetric
====================== ============

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
   B^{\sharp\flat}
   &= \frac{1}{2} \{
                                 & - F^t{}^x \; \et \wedge \eX & - F^t{}^y \; \et \wedge \eY & - F^t{}^z \; \et \wedge \eZ \\ 
     - F^t{}^x \; \ex \wedge \eT &                             & - F^x{}^y \; \ex \wedge \eY & + F^z{}^x \; \ex \wedge \eZ \\
     - F^t{}^y \; \ey \wedge \eT & + F^x{}^y \; \ey \wedge \eX &                             & - F^y{}^z \; \ey \wedge \eZ \\
     - F^t{}^z \; \ez \wedge \eT & - F^z{}^x \; \ez \wedge \eX & + F^y{}^z \; \ez \wedge \eY &                             \\
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
   B^{\sharp\flat}
   &= \frac{1}{2} \{
       F^t{}_t \; \et \wedge \eT & F^t{}_x \; \et \wedge \eX & F^t{}_y \; \et \wedge \eY & F^t{}_z \; \et \wedge \eZ \\ 
       F^x{}_t \; \ex \wedge \eT & F^x{}_x \; \ex \wedge \eX & F^x{}_y \; \ex \wedge \eY & F^x{}_z \; \ex \wedge \eZ \\
       F^y{}_t \; \ey \wedge \eT & F^y{}_x \; \ey \wedge \eX & F^y{}_y \; \ey \wedge \eY & F^y{}_z \; \ey \wedge \eZ \\
       F^z{}_t \; \ez \wedge \eT & F^z{}_x \; \ez \wedge \eX & F^z{}_y \; \ez \wedge \eY & F^z{}_z \; \ez \wedge \eZ \\
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
   B^{\sharp\flat}
   &= \frac{1}{2} \{
                                 & F^t{}_x \; \et \wedge \eX & F^t{}_y \; \et \wedge \eY & F^t{}_z \; \et \wedge \eZ \\ 
       F^x{}_t \; \ex \wedge \eT &                           & F^x{}_y \; \ex \wedge \eY & F^x{}_z \; \ex \wedge \eZ \\
       F^y{}_t \; \ey \wedge \eT & F^y{}_x \; \ey \wedge \eX &                           & F^y{}_z \; \ey \wedge \eZ \\
       F^z{}_t \; \ez \wedge \eT & F^z{}_x \; \ez \wedge \eX & F^z{}_y \; \ez \wedge \eY &                           \\
   \}
   \end{align}

Further expanding all coefficients, we obtain:

.. math::

   \begin{align}
   B^{\sharp\flat}
   &= \frac{1}{2} \{
                                                    & F^{t\gamma}\eta_{\gamma x} \; \et \wedge \eX & F^{t\gamma}\eta_{\gamma y} \; \et \wedge \eY & F^{t\gamma}\eta_{\gamma z} \; \et \wedge \eZ \\ 
      F^{x\gamma} \eta_{\gamma t} \; \ex \wedge \eT &                                              & F^{x\gamma}\eta_{\gamma y} \; \ex \wedge \eY & F^{x\gamma}\eta_{\gamma z} \; \ex \wedge \eZ \\
      F^{y\gamma} \eta_{\gamma t} \; \ey \wedge \eT & F^{y\gamma}\eta_{\gamma x} \; \ey \wedge \eX &                                              & F^{y\gamma}\eta_{\gamma z} \; \ey \wedge \eZ \\
      F^{z\gamma} \eta_{\gamma t} \; \ez \wedge \eT & F^{z\gamma}\eta_{\gamma_x} \; \ez \wedge \eX & F^{z\gamma}\eta_{\gamma y} \; \ez \wedge \eY &                                              \\
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
      + F^{zt} \; \ez \wedge \eT & - F^{zx} \; \ez \wedge \eX & - F^{zy} \; \ez \wedge \eY &                          \\
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
      - F^{tz} \; \ez \wedge \eT & - F^{zx} \; \ez \wedge \eX & + F^{yz} \; \ez \wedge \eY &                          \\
   \}
   \end{align}


.. }}}

