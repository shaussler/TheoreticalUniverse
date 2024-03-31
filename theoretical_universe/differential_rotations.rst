Rotations in Cartan's Formalism
===============================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

In this article, I explicitely express rotations in Cartan's formalism and
improve on the notation to link the practical calculations with differential
forms to matrix multiplication. Note that I have not seen anybody mentioning it
or highlighting it, you can see the symmetry pop out of the Hodge star operator
when ordering differential forms into row and columns.

.. note::

   Bivector and pseudo-vectors are the same object and the wording used
   interchangeably. For details, see :ref:`my article at section *The Hodge
   Dual* <differential_operators:The Hodge Dual>`

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
of the matrix can be re-ordered at will.

.. math::

   \{ + R^{yz} \mathbf{e}_y \wedge \mathbf{e}_z \\
      + R^{zx} \mathbf{e}_z \wedge \mathbf{e}_x \\
      + R^{xy} \mathbf{e}_x \wedge \mathbf{e}_y \\
   \}
   = 
   \{                        & +R^{xy} \ex \wedge \ey &                        \\
                             &                        & +R^{yz} \ey \wedge \ez \\
      +R^{zx} \ez \wedge \ex &                        &                        \\
   \} \\

.. math::

   \{ + R^{yz} \mathbf{e}_y \wedge \mathbf{e}_z \\
      + R^{zx} \mathbf{e}_z \wedge \mathbf{e}_x \\
      + R^{xy} \mathbf{e}_x \wedge \mathbf{e}_y \\
   \}
   = \frac{1}{2}
   \{                        & +R^{xy} \ex \wedge \ey & -R^{zx} \ex \wedge \ez \\
      -R^{xy} \ey \wedge \ex &                        & +R^{yz} \ey \wedge \ez \\
      +R^{zx} \ez \wedge \ex & -R^{yz} \ez \wedge \ey &                        \\
   \}

The transpose can be taken if it permits to use the usual rules of matrix
multiplication:

.. math::

   \{                        & -R^{xy} \ey \wedge \ex & +a^{zx} \ez \wedge \ex \\
      +R^{xy} \ex \wedge \ey &                        & -a^{yz} \ez \wedge \ey \\
      -R^{zx} \ex \wedge \ez & +R^{yz} \ey \wedge \ez &                        \\
   \}

All above matrix representations can writen as a sum:

.. math::

   R^{yz} \ey \wedge \ez +
   R^{zx} \ez \wedge \ex +
   R^{xy} \ex \wedge \ey

In turn through the use of the Hodge star :math:`\star`, we fall back to the
description of rotations as describe with the cross product :math:`\times`:

.. math::

   \begin{align*}
   & \star (
       R^{yz} \ey \wedge \ez +
       R^{zx} \ez \wedge \ex +
       R^{xy} \ex \wedge \ey 
   )\\
   &=
   R^{yz} \star \ey \wedge \ez +
   R^{zx} \star \ez \wedge \ex +
   R^{xy} \star \ex \wedge \ey \\
   &=
   R^{yz} \ex +
   R^{zx} \ey +
   R^{xy} \ez \\
   &=
   R^{yz} \ey \times \ez +
   R^{zx} \ez \times \ex +
   R^{xy} \ex \times \ey \\
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
