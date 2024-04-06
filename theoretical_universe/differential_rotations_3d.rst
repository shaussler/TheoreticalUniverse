Rotations in 3 Dimensions
=========================

.. rst-class:: custom-author

   by Stéphane Haussler

Using the *free matrix representation* is powerfull when using a bivector
basis, since the elements of the matrix can be re-ordered at will. In three
dimensions, rotations are possible on the three planes. A general rotation is
a linear combination of the three associated basis bivectors:

.. math::

   \begin{equation}
   \renewcommand{\∧}{\wedge}
   R = R^x \ey \∧ \ez + R^y \ez \∧ \ex + R^z \ex \∧ \ey
   \end{equation}

With free matrix representation, the bivector can be written as a single
column:

.. math::

   \begin{equation}
   \renewcommand{\{}{\begin{bmatrix}} \renewcommand{\}}{\end{bmatrix}}
   \renewcommand{\∧}{\wedge}
   R =
   \{
     + R^x \ey \∧ \ez \\
     + R^y \ez \∧ \ex \\
     + R^z \ex \∧ \ey \\
   \}
   \end{equation}
   
Or with a row/column matrix notation:

.. math::

   \begin{equation}
   \renewcommand{\{}{\begin{bmatrix}} \renewcommand{\}}{\end{bmatrix}}
   \renewcommand{\∧}{\wedge}
   R =
   \{
                      & + R^z \ex \∧ \ey &                  \\
                      &                  & + R^x \ey \∧ \ez \\
     + R^y \ez \∧ \ex &                  &                  \\
   \} 
   \end{equation}

The anti-symmetric property of the wedge product :math:`\mathbf{e}_i \wedge \mathbf{e}_j = - \mathbf{e}_j \wedge
\mathbf{e}_i` permit to split the terms:

.. math::

   \begin{equation}
   \newcommand{\e}{\mathbf{e}}
   A \e_i \wedge \e_j = \frac{1}{2} (A\e_i \wedge \e_j - A\e_j \wedge e_i)
   \end{equation}

We obtain:

.. math::

   R
   = \frac{1}{2}
   \{                     & +R^z \ex \wedge \ey & -R^y \ex \wedge \ez \\
      -R^z \ey \wedge \ex &                     & +R^x \ey \wedge \ez \\
      +R^y \ez \wedge \ex & -R^x \ez \wedge \ey &                     \\
   \}

Or we can take the transpose:

.. math::

   R = \frac{1}{2}
   \{                       & -R^{z} \ey \wedge \ex & +R^{y} \ez \wedge \ex \\
      +R^{z} \ex \wedge \ey &                       & -R^{x} \ez \wedge \ey \\
      -R^{y} \ex \wedge \ez & +R^{x} \ey \wedge \ez &                       \\
   \}

Flattening of the first kind
----------------------------

.. {{{

The rotation :math:`R` is doubly contravariant. The object at hand can only act
on covectors. In this section, we transform the :math:`R` to the mixed tensor. 

.. math::

   \begin{equation}
   \newcommand{\∧}{\wedge} %u2227
   \newcommand{\♭}{\flat} %u266D
   \newcommand{\♯}{\sharp} %u266F
   R^{\flat\sharp} =
   \{
                      & - R^z \eY \∧ \ex & + R^y \eZ \∧ \ex \\
     + R^z \eX \∧ \ey &                  & - R^x \eZ \∧ \ey \\
     - R^y \eX \∧ \ez & + R^x \eY \∧ \ez &                  \\
   \}
   \end{equation}


.. admonition:: Full calculation
   :class: dropdown

   .. math::
   
      \begin{alignat*}{1}
      \newcommand{\∧}{\wedge} %u2227
      \newcommand{\♭}{\flat} %u266D
      \newcommand{\♯}{\sharp} %u266F
      R^{\flat\sharp}
      &= (R^{\sharp\sharp})^{\flat\sharp}
      \\ &=
      \{
                             & - R^z \ey \wedge \ex & + R^y \ez \wedge \ex \\
        + R^z \ex \wedge \ey &                      & - R^x \ez \wedge \ey \\
        - R^y \ex \wedge \ez & + R^x \ey \wedge \ez &                      \\
      \}^{\flat\sharp}
      \\ &=
      \{
                             & - R^z \ey \wedge \ex & + R^y \ez \wedge \ex \\
        + R^z \ex \wedge \ey &                      & - R^x \ez \wedge \ey \\
        - R^y \ex \wedge \ez & + R^x \ey \wedge \ez &                      \\
      \}^{\flat\sharp}
      \\ &=
      \{
                                  & - R^z (\ey \∧ \ex)^{\♭\♯} & + R^y (\ez \∧ \ex)^{\♭\♯} \\
        + R^z (\ex \∧ \ey)^{\♭\♯} &                           & - R^x (\ez \∧ \ey)^{\♭\♯} \\
        - R^y (\ex \∧ \ez)^{\♭\♯} & + R^x (\ey \∧ \ez)^{\♭\♯} &                           \\
      \}
      \\ &=
      \{
                         & - R^z \eY \∧ \ex & + R^y \eZ \∧ \ex \\
        + R^z \eX \∧ \ey &                  & - R^x \eZ \∧ \ey \\
        - R^y \eX \∧ \ez & + R^x \eY \∧ \ez &                  \\
      \}
      \end{alignat*}

.. }}}

Flatterning of the second kind
------------------------------

.. {{{

For all basis bivectors:

.. math::

   \begin{alignat*}{1}
   \newcommand{\eI}{\mathbf{e}^i}
   \newcommand{\x}{\otimes}
   \newcommand{\w}{\wedge}
   \newcommand{\fl}{\flat}
   \newcommand{\sh}{\sharp}
   (\ex \w \ey)^{\sh\fl} &= \eta_{y i} \ex \w \eI &= \eta_{y y} \ex \w \eY &= \ex \w \eY \\
   (\ey \w \ez)^{\sh\fl} &= \eta_{z i} \ey \w \eI &= \eta_{z z} \ey \w \eZ &= \ey \w \eZ \\
   (\ez \w \ex)^{\sh\fl} &= \eta_{x i} \ez \w \eI &= \eta_{x x} \ez \w \eX &= \ez \w \eX \\
   \end{alignat*}

Expanding the wedge product to its tensor form and simplifying, we find the
following explicit expression of the mixed wedge products in tensor form:

.. math::

   \begin{alignat*}{1}
   \newcommand{\eI}{\mathbf{e}^i}
   \newcommand{\x}{\otimes}
   \newcommand{\w}{\wedge}
   \newcommand{\η}{\flat} %u03b7
   \newcommand{\♭}{\flat} %u266D
   \newcommand{\♯}{\sharp} %u266F
   (\ex \w \ey)^{\♯\♭} &= (\ex \x \ey - \ey \x \ex)^{\♯\♭} &= \η_{yi} \ex \x \eI - \η_{xi} \ey \x \eI \\
   (\ey \w \ez)^{\♯\♭} &= (\ey \x \ez - \ez \x \ey)^{\♯\♭} &= \η_{zi} \ey \x \eI - \η_{yi} \ez \x \eI \\
   (\ez \w \ex)^{\♯\♭} &= (\ez \x \ex - \ex \x \ez)^{\♯\♭} &= \η_{xi} \ez \x \eI - \η_{zi} \ex \x \eI \\
   \end{alignat*}

.. math::

   \begin{alignat*}{1}
   \newcommand{\x}{\otimes}
   \newcommand{\w}{\wedge}
   \newcommand{\♭}{\flat} %u266D
   \newcommand{\♯}{\sharp} %u266F
   (\ex \w \ey)^{\♯\♭} &= \eta_{yy} \ex \x \ey - \eta_{xx} \ey \x \ex &= \ex \x \ey - \ey \x \ex \\
   (\ey \w \ez)^{\♯\♭} &= \eta_{zz} \ey \x \ez - \eta_{yy} \ez \x \ey &= \ey \x \ez - \ez \x \ey \\
   (\ez \w \ex)^{\♯\♭} &= \eta_{xx} \ez \x \ex - \eta_{zz} \ex \x \ez &= \ez \x \ex - \ex \x \ez \\
   \end{alignat*}

From the explicit calculation of the basis elements, we observe the following
properties:

====================== ============ =============================================================
Basis element          Symmetry     Expression
====================== ============ =============================================================
:math:`\ex \wedge \eY` Antisymetric :math:`\mathbf{e}^x \otimes \ey - \mathbf{e}^y \otimes \ex`
:math:`\ey \wedge \eZ` Antisymetric :math:`\mathbf{e}^y \otimes \ez - \mathbf{e}^z \otimes \ey`
:math:`\ez \wedge \eX` Antisymetric :math:`\mathbf{e}^z \otimes \ex - \mathbf{e}^x \otimes \ez`
====================== ============ =============================================================

.. math::

   \begin{equation}
   \newcommand{\∧}{\wedge} %u2227
   \newcommand{\♭}{\flat} %u266D
   \newcommand{\♯}{\sharp} %u266F
   R^{\flat\sharp} =
   \{
                      & - R^z \eY \∧ \ex & + R^y \eZ \∧ \ex \\
     + R^z \eX \∧ \ey &                  & - R^x \eZ \∧ \ey \\
     - R^y \eX \∧ \ez & + R^x \eY \∧ \ez &                  \\
   \}
   \end{equation}

.. admonition:: Step by step calculation
   :class: dropdown

   .. math::
   
      \begin{alignat*}{1}
      \newcommand{\∧}{\wedge} %u2227
      \newcommand{\♭}{\flat} %u266D
      \newcommand{\♯}{\sharp} %u266F
      R^{\flat\sharp}
      &= (R^{\sharp\sharp})^{\flat\sharp}
      \\ &=
      \{
                             & - R^z \ey \wedge \ex & + R^y \ez \wedge \ex \\
        + R^z \ex \wedge \ey &                      & - R^x \ez \wedge \ey \\
        - R^y \ex \wedge \ez & + R^x \ey \wedge \ez &                      \\
      \}^{\flat\sharp}
      \\ &=
      \{
                             & - R^z \ey \wedge \ex & + R^y \ez \wedge \ex \\
        + R^z \ex \wedge \ey &                      & - R^x \ez \wedge \ey \\
        - R^y \ex \wedge \ez & + R^x \ey \wedge \ez &                      \\
      \}^{\flat\sharp}
      \\ &=
      \{
                                  & - R^z (\ey \∧ \ex)^{\♭\♯} & + R^y (\ez \∧ \ex)^{\♭\♯} \\
        + R^z (\ex \∧ \ey)^{\♭\♯} &                           & - R^x (\ez \∧ \ey)^{\♭\♯} \\
        - R^y (\ex \∧ \ez)^{\♭\♯} & + R^x (\ey \∧ \ez)^{\♭\♯} &                           \\
      \}
      \\ &=
      \{
                         & - R^z \eY \∧ \ex & + R^y \eZ \∧ \ex \\
        + R^z \eX \∧ \ey &                  & - R^x \eZ \∧ \ey \\
        - R^y \eX \∧ \ez & + R^x \eY \∧ \ez &                  \\
      \}
      \end{alignat*}

.. }}}

Equivalence to the 3D rotation group :math:`\mathfrak{so}(3)`
-------------------------------------------------------------

.. {{{

Whether as a transpose or not, we identify the :math:`\mathfrak{so}(3)`
matrices as well as get a first hint that we are about to identify the
electromagnetic tensor. Choosing the implicit basis :math:`\mathbf{e}_i \wedge
\mathbf{e}_j` in a row major representation, we obtain:

.. math::

   \begin{align}
   R
   &= \frac{1}{2}
   \{
           & -R^z & +R^y \\
      +R^z &      & -R^x \\
      -R^y & +R^x &      \\
   \} \\
   &=
   R^x
   \{
       0 &  0 &  0 \\
       0 &  0 & -1 \\
       0 & +1 &  0 \\
   \}
   + R^y
   \{
       0 &  0 & +1 \\
       0 &  0 &  0 \\
      -1 &  0 &  0 \\
   \}
   + R^z
   \{
       0 & -1 &  0 \\
      +1 &  0 &  0 \\
       0 &  0 &  0 \\
   \}
   \end{align}

.. }}}

Equivalence to the cross product :math:`\times`
-----------------------------------------------

.. {{{

Rotations in three dimensions have a dual. We can either express a rotation
along the three planes, or we can express a rotation along the three directions
of space. Indeed, through the use of the Hodge star :math:`\star`, we fall back
to the description of rotations expressed as a cross product :math:`\times`:

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

