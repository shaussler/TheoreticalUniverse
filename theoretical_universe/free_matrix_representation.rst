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

This is powerfull when using a pseudo-vector or pseudo-scalar basis, since the
elements of the matrix can be re-ordered at will.

.. math::

   \{
                          & +a^{xy} \ex \wedge \ey & -a^{zx} \ex \wedge \ez \\
   -a^{xy} \ey \wedge \ex &                        & +a^{yz} \ey \wedge \ez \\
   +a^{zx} \ez \wedge \ex & -a^{yz} \ez \wedge \ey &                        \\
   \}
   =
   \{
   + 2 a^{yz} \ey \wedge \ez \\
   + 2 a^{zx} \ez \wedge \ex \\
   + 2 a^{xy} \ex \wedge \ey \\
   \}

The transpose can be taken if it permits to use the usual rules of matrix
multiplication:

.. math::

   \{
                          & -a^{xy} \ey \wedge \ex & +a^{zx} \ez \wedge \ex \\
   +a^{xy} \ex \wedge \ey &                        & -a^{yz} \ez \wedge \ey \\
   -a^{zx} \ex \wedge \ez & +a^{yz} \ey \wedge \ez &                        \\
   \}

All above matrix representations can writen as a sum:

.. math::

   2 a^{yz} \ey \wedge \ez +
   2 a^{zx} \ez \wedge \ex +
   2 a^{xy} \ex \wedge \ey

We could have written a covector in the same explicit manner. This notation is
very conveniant when performing calculations in Cartan's framework as it
permits to identify and organize terms for practical calculations by falling
back to regular matrix multiplication.
