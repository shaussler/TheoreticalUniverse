Rotations in Minkowski Space
============================

.. rst-class:: custom-author

   by Stéphane Haussler

Turning now to a bivectors in Minkowski space, any rotation can be written as
a linear combination of 6 parameters:

.. math::

   \begin{equation}
   B^{♯♯}
   = \begin{bmatrix}
     F^{tx} ∂_t ∧ ∂_x \\
     F^{ty} ∂_t ∧ ∂_y \\
     F^{tz} ∂_t ∧ ∂_z \\
     F^{xy} ∂_x ∧ ∂_y \\
     F^{yz} ∂_y ∧ ∂_z \\
     F^{zx} ∂_z ∧ ∂_x \\
   \end{bmatrix}
   \end{equation}

The sharp symbol :math:`\sharp` indicates that the components are doubly
contravariant tensor components. Reordering to a row/column matrix
representation and using the antisimmetric property of the wedge product, we
obtain:

.. math::

   \begin{equation}
   B^{♯♯}
   = \frac{1}{2}
   \begin{bmatrix}
                          & + F^{tx} ∂_t ∧ ∂_x & + F^{ty} ∂_t ∧ ∂_y & + F^{tz} ∂_t ∧ ∂_z \\
       - F^{tx} ∂_x ∧ ∂_t &                    & + F^{xy} ∂_x ∧ ∂_y & - F^{zx} ∂_x ∧ ∂_z \\
       - F^{ty} ∂_y ∧ ∂_t & - F^{xy} ∂_y ∧ ∂_x &                    & + F^{yz} ∂_y ∧ ∂_z \\
       - F^{tz} ∂_z ∧ ∂_t & + F^{zx} ∂_z ∧ ∂_x & - F^{yz} ∂_z ∧ ∂_y &                    \\
   \end{bmatrix}
   \end{equation}

Metric
------

.. {{{

We choose the metric signature :math:`(+, -, -, -)`. The only non-zero components
are the diagonal components. The double contravariant minkowski metric tensor is usually represented in matrix notation
with:

.. math::

   η =
   \begin{bmatrix}
     + 1 &  0 &  0 &  0 \\
       0 & -1 &  0 &  0 \\
       0 &  0 & -1 &  0 \\
       0 &  0 &  0 & -1 \\
   \end{bmatrix}

With *musical notation* and *free matrix representation*, we can write
explicitely the the coveriance/contravariance of the tensor as well as the
tensor basis:

.. math::

   \begin{equation}
   \eta^{♯♯} =
   \begin{bmatrix}
     \begin{array}{rrrr}
     + 1 \; ∂_t ⊗ ∂_t &  0 \; ∂_x ⊗ ∂_t &  0 \; ∂_y ⊗ ∂_t &  0 \; ∂_y ⊗ ∂_t \\
       0 \; ∂_t ⊗ ∂_x & -1 \; ∂_x ⊗ ∂_x &  0 \; ∂_y ⊗ ∂_x &  0 \; ∂_y ⊗ ∂_x \\
       0 \; ∂_t ⊗ ∂_y &  0 \; ∂_x ⊗ ∂_y & -1 \; ∂_y ⊗ ∂_y &  0 \; ∂_y ⊗ ∂_y \\
       0 \; ∂_t ⊗ ∂_z &  0 \; ∂_x ⊗ ∂_z &  0 \; ∂_y ⊗ ∂_z & -1 \; ∂_y ⊗ ∂_z \\
     \end{array}
   \end{bmatrix}
   \end{equation}

Which permits to rewrite the metrix tensor in a compact and convenient manner:

.. math::

   \begin{equation}
   \eta^{♯♯} =
   \begin{bmatrix}
     +1 ∂_t ⊗ ∂_t \\
     -1 ∂_x ⊗ ∂_x \\
     -1 ∂_y ⊗ ∂_y \\
     -1 ∂_z ⊗ ∂_z \\
   \end{bmatrix}
   \end{equation}

Equivalently and with the same procedure and arguments, we express the doubly
covariant metric tensor with:

.. math::

   \begin{equation}
   \eta^{♭♭} =
   \begin{bmatrix}
     +1 dx^t ⊗ dx^t \\
     -1 dx^x ⊗ dx^x \\
     -1 dx^y ⊗ dx^y \\
     -1 dx^z ⊗ dx^z \\
   \end{bmatrix}
   \end{equation}

For the basis vectors, this means:

.. math::

   ∂_μ ∧ ∂_ν = \frac{1}{2} (∂_μ ⊗ ∂_ν - ∂_ν ⊗ ∂_μ)

We can flatten a basis vector with the flat operator :math:`♭`

.. math::

   (∂_μ)^♭ = η_{μν} dx^ν

And flatten the wedge product like so

.. math::

   (∂_μ ∧ ∂_ν)^{♭♯} = η_{γμ} dx^γ ∧ ∂_ν

.. math::

   (∂_μ ∧ ∂_ν)^{♯♭} = η_{γν} ∂_μ ∧ dx^γ

.. math::

   (∂_μ ∧ ∂_ν)^{♭♭} = η_{δμ} η_{γν} dx^δ ∧ dx^γ

.. }}}

Flattening of the first kind
----------------------------

.. {{{

For all basis bivectors:

.. math::

   \begin{array}{r}
   (∂_t ∧ ∂_x)^{♭♯} &=& η_{tγ} dx^γ ∧ ∂_x &=& η_{tt} ∂_t ∧ ∂_x &=& + ∂_t ∧ ∂_x \\
   (∂_t ∧ ∂_y)^{♭♯} &=& η_{tγ} dx^γ ∧ ∂_y &=& η_{tt} ∂_t ∧ ∂_y &=& + ∂_t ∧ ∂_y \\
   (∂_t ∧ ∂_z)^{♭♯} &=& η_{tγ} dx^γ ∧ ∂_z &=& η_{tt} ∂_t ∧ ∂_z &=& + ∂_t ∧ ∂_z \\
   (∂_x ∧ ∂_y)^{♭♯} &=& η_{xγ} dx^γ ∧ ∂_y &=& η_{xx} ∂_x ∧ ∂_y &=& - ∂_x ∧ ∂_y \\
   (∂_y ∧ ∂_z)^{♭♯} &=& η_{yγ} dx^γ ∧ ∂_z &=& η_{yy} ∂_y ∧ ∂_z &=& - ∂_y ∧ ∂_z \\
   (∂_z ∧ ∂_x)^{♭♯} &=& η_{zγ} dx^γ ∧ ∂_x &=& η_{zz} ∂_z ∧ ∂_x &=& - ∂_z ∧ ∂_x \\
   \end{array}

Expanding and simplifying, this results in the following explicit expression of
the mixed wedge products:

.. math::

   \begin{array}{r}
   (∂_t ∧ ∂_x)^{♭♯} &=& (∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_t \\
   (∂_t ∧ ∂_y)^{♭♯} &=& (∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_t \\
   (∂_t ∧ ∂_z)^{♭♯} &=& (∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_t \\
   (∂_x ∧ ∂_y)^{♭♯} &=& (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♭♯} &=& η_{xγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_x \\
   (∂_y ∧ ∂_z)^{♭♯} &=& (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♭♯} &=& η_{yγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♭♯} &=& (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♭♯} &=& η_{zγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_z \\
   \end{array}

.. math::

   \begin{array}{r}
   (∂_t ∧ ∂_x)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_t &=& + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
   (∂_t ∧ ∂_y)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_t &=& + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
   (∂_t ∧ ∂_z)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_t &=& + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
   (∂_x ∧ ∂_y)^{♭♯} &=& η_{xx} dx^x ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_x &=& - dx^x ⊗ ∂_y + dx^y ⊗ ∂_x \\
   (∂_y ∧ ∂_z)^{♭♯} &=& η_{yy} dx^y ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_y &=& - dx^y ⊗ ∂_z + dx^z ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♭♯} &=& η_{zz} dx^z ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_z &=& - dx^z ⊗ ∂_x + dx^x ⊗ ∂_z \\
   \end{array}

.. math::

   \begin{array}{r}
   dx^t ∧ ∂_x &=& + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
   dx^t ∧ ∂_y &=& + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
   dx^t ∧ ∂_z &=& + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
   dx^x ∧ ∂_y &=& + dx^x ⊗ ∂_y - dx^y ⊗ ∂_x \\
   dx^y ∧ ∂_z &=& + dx^y ⊗ ∂_z - dx^z ⊗ ∂_y \\
   dx^z ∧ ∂_x &=& + dx^z ⊗ ∂_x - dx^x ⊗ ∂_z \\
   \end{array}

From the explicit calculation of the basis elements, we observe the following
properties:

================== ============
Basis element      Symmetry
================== ============
:math:`dx^t ∧ ∂_x` Symetric
:math:`dx^t ∧ ∂_y` Symetric
:math:`dx^t ∧ ∂_z` Symetric
:math:`dx^x ∧ ∂_y` Antisymetric
:math:`dx^y ∧ ∂_z` Antisymetric
:math:`dx^z ∧ ∂_x` Antisymetric
================== ============

.. }}}

Flattening of the second kind
-----------------------------

.. {{{

For all basis bivectors:

.. math::

   \begin{array}{}
   (∂_t ∧ ∂_x)^{♯♭} &=& η_{xγ} ∂_t ∧ dx^γ &=& η_{xx} ∂_t ∧ dx^x &=& - ∂_t ∧ dx^x \\
   (∂_t ∧ ∂_y)^{♯♭} &=& η_{yγ} ∂_t ∧ dx^γ &=& η_{yy} ∂_t ∧ dx^y &=& - ∂_t ∧ dx^y \\
   (∂_t ∧ ∂_z)^{♯♭} &=& η_{zγ} ∂_t ∧ dx^γ &=& η_{zz} ∂_t ∧ dx^z &=& - ∂_t ∧ dx^z \\
   (∂_x ∧ ∂_y)^{♯♭} &=& η_{yγ} ∂_x ∧ dx^γ &=& η_{yy} ∂_x ∧ dx^y &=& - ∂_x ∧ dx^y \\
   (∂_y ∧ ∂_z)^{♯♭} &=& η_{zγ} ∂_y ∧ dx^γ &=& η_{zz} ∂_y ∧ dx^z &=& - ∂_y ∧ dx^z \\
   (∂_z ∧ ∂_x)^{♯♭} &=& η_{xγ} ∂_z ∧ dx^γ &=& η_{xx} ∂_z ∧ dx^x &=& - ∂_z ∧ dx^x \\
   \end{array}

Expanding and simplifying, this results in the following explicit expression of
the mixed wedge products:

.. math::

   \begin{array}{}
   (∂_t ∧ ∂_x)^{♯♭} &=& (∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t)^{♯♯} &=& η_{xγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_x ⊗ dx^γ \\
   (∂_t ∧ ∂_y)^{♯♭} &=& (∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t)^{♯♯} &=& η_{yγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_y ⊗ dx^γ \\
   (∂_t ∧ ∂_z)^{♯♭} &=& (∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t)^{♯♯} &=& η_{zγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_z ⊗ dx^γ \\
   (∂_x ∧ ∂_y)^{♯♭} &=& (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♯♯} &=& η_{yγ} ∂_x ⊗ dx^γ - η_{xγ} ∂_y ⊗ dx^γ \\
   (∂_y ∧ ∂_z)^{♯♭} &=& (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♯♯} &=& η_{zγ} ∂_y ⊗ dx^γ - η_{yγ} ∂_z ⊗ dx^γ \\
   (∂_z ∧ ∂_x)^{♯♭} &=& (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♯♯} &=& η_{xγ} ∂_z ⊗ dx^γ - η_{zγ} ∂_x ⊗ dx^γ \\
   \end{array}

.. math::

   \begin{array}{}
   (∂_t ∧ ∂_x)^{♭♯} &=& η_{xx} ∂_t ⊗ ∂_x - η_{tt} ∂_ex ⊗ ∂_t &=& - ∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t \\
   (∂_t ∧ ∂_y)^{♭♯} &=& η_{yy} ∂_t ⊗ ∂_y - η_{tt} ∂_ey ⊗ ∂_t &=& - ∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t \\
   (∂_t ∧ ∂_z)^{♭♯} &=& η_{zz} ∂_t ⊗ ∂_z - η_{tt} ∂_ez ⊗ ∂_t &=& - ∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t \\
   (∂_x ∧ ∂_y)^{♭♯} &=& η_{yy} ∂_x ⊗ ∂_y - η_{xx} ∂_ey ⊗ ∂_x &=& - ∂_x ⊗ ∂_y + ∂_y ⊗ ∂_x \\
   (∂_y ∧ ∂_z)^{♭♯} &=& η_{zz} ∂_y ⊗ ∂_z - η_{yy} ∂_ez ⊗ ∂_y &=& - ∂_y ⊗ ∂_z + ∂_z ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♭♯} &=& η_{xx} ∂_z ⊗ ∂_x - η_{zz} ∂_ex ⊗ ∂_z &=& - ∂_z ⊗ ∂_x + ∂_x ⊗ ∂_z \\
   \end{array}

From the explicit calculation of the basis elements, we observe the following
properties:

================== ============ =====================================================
Basis element      Symmetry     Expression
================== ============ =====================================================
:math:`∂_t ∧ dx^x` Symetric     :math:`+ dx^t \otimes \ex + \mathbf{e}^x \otimes \et`
:math:`∂_t ∧ dx^y` Symetric     :math:`+ dx^t \otimes \ey + \mathbf{e}^y \otimes \et`
:math:`∂_t ∧ dx^z` Symetric     :math:`+ dx^t \otimes \ez + \mathbf{e}^z \otimes \et`
:math:`∂_x ∧ dx^y` Antisymetric :math:`+ dx^x \otimes \ey - \mathbf{e}^y \otimes \ex`
:math:`∂_y ∧ dx^z` Antisymetric :math:`+ dx^y \otimes \ez - \mathbf{e}^z \otimes \ey`
:math:`∂_z ∧ dx^x` Antisymetric :math:`+ dx^z \otimes \ex - \mathbf{e}^x \otimes \ez`
================== ============ =====================================================

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

