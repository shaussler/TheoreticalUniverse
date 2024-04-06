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
   % ∂ u2202
   % ∧ u2227
   R = R^x ∂_y ∧ ∂_z + R^y ∂_z ∧ ∂_x + R^z ∂_x ∧ ∂_y
   \end{equation}

With free matrix representation, the bivector can be written as a single
column:

.. math::

   \begin{equation}
   % ∂ u2202
   % ∧ u2227
   R =
   \{
     + R^x ∂_y ∧ ∂_z \\
     + R^y ∂_z ∧ ∂_x \\
     + R^z ∂_x ∧ ∂_y \\
   \}
   \end{equation}
   
Or with a row/column matrix notation:

.. math::

   \begin{equation}
   % ∂ u2202
   % ∧ u2227
   R =
   \{
                     & + R^z ∂_x ∧ ∂_y &                 \\
                     &                 & + R^x ∂_y ∧ ∂_z \\
     + R^y ∂_z ∧ ∂_x &                 &                 \\
   \} 
   \end{equation}

The anti-symmetric property of the wedge product :math:`\partial_i \wedge
\partial_j = - \partial_j \wedge \partial_i` permit to split the terms:

.. math::

   \begin{equation}
   % ∂ u2202
   % ∧ u2227
   A ∂_i ∧ ∂_j = \frac{1}{2} (A ∂_i ∧ ∂_j - A ∂_j ∧ ∂_i)
   \end{equation}

We obtain:

.. math::

   \begin{equation}
   % ∂ u2202
   % ∧ u2227
   R
   = \frac{1}{2}
   \{
                      & + R^z ∂_x ∧ ∂_y & - R^y ∂_x ∧ ∂_z \\
      - R^z ∂_y ∧ ∂_x &                 & + R^x ∂_y ∧ ∂_z \\
      + R^y ∂_z ∧ ∂_x & - R^x ∂_z ∧ ∂_y &                 \\
   \}
   \end{equation}

Or we can take the transpose:

.. math::

   \begin{equation}
   % ∂ u2202
   % ∧ u2227
   R = \frac{1}{2}
   \{
                     & -R^z ∂_y ∧ ∂_x & +R^y ∂_z ∧ ∂_x \\
      +R^z ∂_x ∧ ∂_y &                & -R^x ∂_z ∧ ∂_y \\
      -R^y ∂_x ∧ ∂_z & +R^x ∂_y ∧ ∂_z &                \\
   \}
   \end{equation}

Flattening of the first kind
----------------------------

.. {{{

The rotation :math:`R` is doubly contravariant. The object at hand can only act
on covectors. In this section, we transform the :math:`R` to the mixed tensor. 

.. math::

   \begin{equation}
   % ∧ u2227
   % ♭ u266D
   % ♯ u266F
   R^{\flat\sharp} =
   \{
                      & - R^z dx^y ∧ ∂_x & + R^y dx^z ∧ ∂_x \\
     + R^z dx^x ∧ ∂_y &                  & - R^x dx^z ∧ ∂_y \\
     - R^y dx^x ∧ ∂_z & + R^x dx^y ∧ ∂_z &                  \\
   \}
   \end{equation}


.. admonition:: Full calculation
   :class: dropdown

   .. math::
   
      \begin{alignat*}{1}
      % ∧ u2227
      % ♭ u266D
      % ♯ u266F
      R^{♭♯}
      &= (R^{♯♯})^{♭♯}
      \\ &=
      \{
                        & - R^z ∂_y ∧ ∂_x & + R^y ∂_z ∧ ∂_x \\
        + R^z ∂_x ∧ ∂_y &                 & - R^x ∂_z ∧ ∂_y \\
        - R^y ∂_x ∧ ∂_z & + R^x ∂_y ∧ ∂_z &                 \\
      \}^{\flat\sharp}
      \\ &=
      \{
                        & - R^z ∂_y ∧ ∂_x & + R^y ∂_z ∧ ∂_x \\
        + R^z ∂_x ∧ ∂_y &                 & - R^x ∂_z ∧ ∂_y \\
        - R^y ∂_x ∧ ∂_z & + R^x ∂_y ∧ ∂_z &                 \\
      \}^{\flat\sharp}
      \\ &=
      \{
                               & - R^z (∂_y ∧ ∂_x)^{♭♯} & + R^y (∂_z ∧ ∂_x)^{♭♯} \\
        + R^z (∂_x ∧ ∂_y)^{♭♯} &                        & - R^x (∂_z ∧ ∂_y)^{♭♯} \\
        - R^y (∂_x ∧ ∂_z)^{♭♯} & + R^x (∂_y ∧ ∂_z)^{♭♯} &                        \\
      \}
      \\ &=
      \{
                         & - R^z dx^y ∧ ∂_x & + R^y dx^z ∧ ∂_x \\
        + R^z dx^x ∧ ∂_y &                  & - R^x dx^z ∧ ∂_y \\
        - R^y dx^x ∧ ∂_z & + R^x dx^y ∧ ∂_z &                  \\
      \}
      \end{alignat*}

.. }}}

Flatterning of the second kind
------------------------------

.. {{{

For all basis bivectors:

.. math::

   \begin{alignat*}{1}
   (∂_x ∧ ∂_y)^{♯♭} &= η_{yi} ∂_x ∧ dx^i &= η_{yy} ∂_x ∧ dx^y &= ∂_x ∧ dx^y \\
   (∂_y ∧ ∂_z)^{♯♭} &= η_{zi} ∂_y ∧ dx^i &= η_{zz} ∂_y ∧ dx^z &= ∂_y ∧ dx^z \\
   (∂_z ∧ ∂_x)^{♯♭} &= η_{xi} ∂_z ∧ dx^i &= η_{xx} ∂_z ∧ dx^x &= ∂_z ∧ dx^x \\
   \end{alignat*}

Expanding the wedge product to its tensor form and simplifying, we find the
following explicit expression of the mixed wedge products in tensor form:

.. math::

   \begin{alignat*}{1}
   (∂_x ∧ ∂_y)^{♯♭} &= (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♯♭} &= η_{yi} ∂_x ⊗ dx^i - η_{xi} ∂_y ⊗ dx^i \\
   (∂_y ∧ ∂_z)^{♯♭} &= (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♯♭} &= η_{zi} ∂_y ⊗ dx^i - η_{yi} ∂_z ⊗ dx^i \\
   (∂_z ∧ ∂_x)^{♯♭} &= (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♯♭} &= η_{xi} ∂_z ⊗ dx^i - η_{zi} ∂_x ⊗ dx^i \\
   \end{alignat*}

.. math::

   \begin{alignat*}{1}
   (∂_x ∧ ∂_y)^{♯♭} &= η_{yy} ∂_x ⊗ ∂_y - η_{xx} ∂_y ⊗ ∂_x &= ∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x \\
   (∂_y ∧ ∂_z)^{♯♭} &= η_{zz} ∂_y ⊗ ∂_z - η_{yy} ∂_z ⊗ ∂_y &= ∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♯♭} &= η_{xx} ∂_z ⊗ ∂_x - η_{zz} ∂_x ⊗ ∂_z &= ∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z \\
   \end{alignat*}

From the ∂_xplicit calculation of the basis elements, we observe the following
properties:

================== ============ ===============================
Basis element      Symmetry     Expression
================== ============ ===============================
:math:`∂_x ∧ dx^y` Antisymetric :math:`dx^x ⊗ ∂_y - dx^y ⊗ ∂_x`
:math:`∂_y ∧ dx^z` Antisymetric :math:`dx^y ⊗ ∂_z - dx^z ⊗ ∂_y`
:math:`∂_z ∧ dx^x` Antisymetric :math:`dx^z ⊗ ∂_x - dx^x ⊗ ∂_z`
================== ============ ===============================

.. math::

   \begin{equation}
   \newcommand{\∧}{\wedge} %u2227
   \newcommand{\♭}{\flat} %u266D
   \newcommand{\♯}{\sharp} %u266F
   R^{\flat\sharp} =
   \{
                      & - R^z dx^y ∧ ∂_x & + R^y dx^z ∧ ∂_x \\
     + R^z dx^x ∧ ∂_y &                  & - R^x dx^z ∧ ∂_y \\
     - R^y dx^x ∧ ∂_z & + R^x dx^y ∧ ∂_z &                  \\
   \}
   \end{equation}

.. admonition:: Step by step calculation
   :class: dropdown

   .. math::
   
      \begin{alignat*}{1}
      R^{♭♯}
      &= (R^{♯♯})^{♭♯} \\
      &= \{
                           & - R^z ∂_y ∧ ∂_x & + R^y ∂_z ∧ ∂_x \\
           + R^z ∂_x ∧ ∂_y &                 & - R^x ∂_z ∧ ∂_y \\
           - R^y ∂_x ∧ ∂_z & + R^x ∂_y ∧ ∂_z &                 \\
         \}^{♭♯} \\
      &= \{
                           & - R^z ∂_y ∧ ∂_x & + R^y ∂_z ∧ ∂_x \\
           + R^z ∂_x ∧ ∂_y &                & - R^x ∂_z ∧ ∂_y \\
           - R^y ∂_x ∧ ∂_z & + R^x ∂_y ∧ ∂_z &                \\
         \}^{\flat\sharp} \\
      &= \{
                                  & - R^z (∂_y ∧ ∂_x)^{♭♯} & + R^y (∂_z ∧ ∂_x)^{♭♯} \\
           + R^z (∂_x ∧ ∂_y)^{♭♯} &                        & - R^x (∂_z ∧ ∂_y)^{♭♯} \\
           - R^y (∂_x ∧ ∂_z)^{♭♯} & + R^x (∂_y ∧ ∂_z)^{♭♯} &                        \\
         \} \\
      &= \{
                            & - R^z dx^y ∧ ∂_x & + R^y dx^z ∧ ∂_x \\
           + R^z dx^x ∧ ∂_y &                  & - R^x dx^z ∧ ∂_y \\
           - R^y dx^x ∧ ∂_z & + R^x dx^y ∧ ∂_z &                  \\
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
   ⋆R &= ⋆(R^x   ∂_y ∧ ∂_z  + R^y   ∂_z ∧ ∂_x  + R^z   ∂_x ∧ ∂_y) \\
      &=   R^x ⋆(∂_y ∧ ∂_z) + R^y ⋆(∂_z ∧ ∂_x) + R^z ⋆(∂_x ∧ ∂_y) \\
      &=   R^x ∂_x + R^y ∂_y + R^z ∂_z
   \end{align*}

That is, the Hodge star of the rotation ∂_xpressed as a linear comibination of
bivectors is exactly a rotation in terms of cross products in the Hodge dual
space:

.. math::

   \begin{equation}
   ⋆R = R^x ∂_y ⨯ ∂_z + R^y ∂_z ⨯ ∂_x + R^z ∂_x ⨯ ∂_y
   \end{equation}

We could have written a covector in the same explicit manner. This notation is
very conveniant when performing calculations in Cartan's framework as it
permits to identify and organize terms for practical calculations by falling
back to regular matrix multiplication.

.. }}}
