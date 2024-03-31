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

The content of this article might not be wildely known as I have not found the
observations detailed here mentioned anywhere. If I am mistaken and you are
aware of freely available resources, open an issue and I will include a
reference. If you find mistakes, don't hesitate to open an issue or directly
provide corrections by sending a merge request to my `Github repository
<https://github.com/shaussler/TheoreticalUniverse/>`_.

I assume the reader posses a strong grasp of vector calculus as well as working
understanding of differential forms, the wedge product, and :ref:`the concept
of the Hodge dual <differential_operators:The Hodge Dual>`. With respect to
wording, note that I interchangeably use the words *oriented surface*,
*bivector* and *pseudo-vectors* as they are :ref:`the same objects
<differential_operators:The Hodge Dual>`, albeit named in different contexts.

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

In turn through the use of the Hodge star :math:`\star`, we fall back to the
description of rotations as describe with the cross product :math:`\times`:

.. math::

   \begin{align*}
   & \star (
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
   R^{z} \ez \\
   &=
   R^{x} \ey \times \ez +
   R^{y} \ez \times \ex +
   R^{z} \ex \times \ey \\
   \end{align*}

We could have written a covector in the same explicit manner. This notation is
very conveniant when performing calculations in Cartan's framework as it
permits to identify and organize terms for practical calculations by falling
back to regular matrix multiplication.

.. }}}

Rotations in Minkowski space
----------------------------

.. {{{

Hence a general bivector in Minkowski space can be written as:

.. math::

   \begin{align}
   B
   &= \{
       F^{tx} \; \et \wedge \ex \\
       F^{ty} \; \et \wedge \ey \\
       F^{tz} \; \et \wedge \ez \\
       F^{xy} \; \ex \wedge \ey \\
       F^{yz} \; \ey \wedge \ez \\
       F^{zx} \; \ez \wedge \ex \\
   \}
   \end{align}


.. math::

   \begin{align}
   B
   &= \frac{1}{2} \{
                                  & + F^{tx} \; \et \wedge \ex & + F^{ty} \; \et \wedge \ey & + F^{tz} \; \et \wedge \ez \\ 
       - F^{tx} \; \ex \wedge \et &                            & + F^{xy} \; \ex \wedge \ey & - F^{zx} \; \ex \wedge \ez \\
       - F^{ty} \; \ey \wedge \et & - F^{xy} \; \ey \wedge \ex &                            & + F^{yz} \; \ey \wedge \ez \\
       - F^{tz} \; \ez \wedge \et & + F^{zx} \; \ez \wedge \ex & - F^{yz} \; \ez \wedge \ey &                            \\
   \}
   \end{align}

Rotation Hodge Dual
-------------------

.. math::

   \begin{alignat*}{2}
   \star (\mathbf{e}_t \wedge \mathbf{e}_x) &= - &\mathbf{e}_y \wedge \mathbf{e}_z \\
   \star (\mathbf{e}_t \wedge \mathbf{e}_y) &= - &\mathbf{e}_z \wedge \mathbf{e}_x \\
   \star (\mathbf{e}_t \wedge \mathbf{e}_z) &= - &\mathbf{e}_x \wedge \mathbf{e}_y \\
   \star (\mathbf{e}_x \wedge \mathbf{e}_y) &=   &\mathbf{e}_t \wedge \mathbf{e}_z \\
   \star (\mathbf{e}_y \wedge \mathbf{e}_z) &=   &\mathbf{e}_t \wedge \mathbf{e}_x \\
   \star (\mathbf{e}_z \wedge \mathbf{e}_x) &=   &\mathbf{e}_t \wedge \mathbf{e}_y \\
   \end{alignat*}

.. }}}
