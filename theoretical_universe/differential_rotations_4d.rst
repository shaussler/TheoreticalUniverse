Rotations in Minkowski Space
============================

.. rst-class:: custom-author

   by Stéphane Haussler

Turning now to a bivectors in Minkowski space, **any rotation can be written as
a linear combination of 6 parameters**:

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
obtain the **contravariant matrix representation of a rotation**:

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

Recall that using :ref:`the Minkowski metric <minkowski_metric:The Minkowski
Metric>`, we can flatten a basis vector with the flat operator :math:`♭`:

.. math::

   \begin{equation}
   (∂_μ)^♭ = η_{μν} dx^ν
   \end{equation}

And likewise flatten any index of the doubly contravariant wedge product:

.. math::

   \begin{matrix}
   (∂_μ ∧ ∂_ν)^{♭♯} &= η_{γμ} dx^γ ∧ ∂_ν         \\
   (∂_μ ∧ ∂_ν)^{♯♭} &= η_{γν} ∂_μ ∧ dx^γ         \\
   (∂_μ ∧ ∂_ν)^{♭♭} &= η_{δμ} η_{γν} dx^δ ∧ dx^γ \\
   \end{matrix}

Flattening of the first index
-----------------------------

.. {{{

We apply the :math:`♭♯` operators to flatten the first index of each basis
bivectors:

.. math::

   \begin{array}{r}
   (∂_t ∧ ∂_x)^{♭♯} &=& + dx^t ∧ ∂_x \\
   (∂_t ∧ ∂_y)^{♭♯} &=& + dx^t ∧ ∂_y \\
   (∂_t ∧ ∂_z)^{♭♯} &=& + dx^t ∧ ∂_z \\
   (∂_x ∧ ∂_y)^{♭♯} &=& - dx^x ∧ ∂_y \\
   (∂_y ∧ ∂_z)^{♭♯} &=& - dx^y ∧ ∂_z \\
   (∂_z ∧ ∂_x)^{♭♯} &=& - dx^z ∧ ∂_x \\
   \end{array}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Distribute the musical operators to their respective indices:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& (∂_t^♭ ∧ ∂_x^♯) \\
      (∂_t ∧ ∂_y)^{♭♯} &=& (∂_t^♭ ∧ ∂_y^♯) \\
      (∂_t ∧ ∂_z)^{♭♯} &=& (∂_t^♭ ∧ ∂_z^♯) \\
      (∂_x ∧ ∂_y)^{♭♯} &=& (∂_x^♭ ∧ ∂_y^♯) \\
      (∂_y ∧ ∂_z)^{♭♯} &=& (∂_y^♭ ∧ ∂_z^♯) \\
      (∂_z ∧ ∂_x)^{♭♯} &=& (∂_z^♭ ∧ ∂_x^♯) \\
      \end{array}

   Apply the musical operators:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& η_{tγ} dx^γ ∧ ∂_x \\
      (∂_t ∧ ∂_y)^{♭♯} &=& η_{tγ} dx^γ ∧ ∂_y \\
      (∂_t ∧ ∂_z)^{♭♯} &=& η_{tγ} dx^γ ∧ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &=& η_{xγ} dx^γ ∧ ∂_y \\
      (∂_y ∧ ∂_z)^{♭♯} &=& η_{yγ} dx^γ ∧ ∂_z \\
      (∂_z ∧ ∂_x)^{♭♯} &=& η_{zγ} dx^γ ∧ ∂_x \\
      \end{array}

   Identify the non-zero terms of the metric:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& η_{tt} dx^t ∧ ∂_x \\
      (∂_t ∧ ∂_y)^{♭♯} &=& η_{tt} dx^t ∧ ∂_y \\
      (∂_t ∧ ∂_z)^{♭♯} &=& η_{tt} dx^t ∧ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &=& η_{xx} dx^x ∧ ∂_y \\
      (∂_y ∧ ∂_z)^{♭♯} &=& η_{yy} dx^y ∧ ∂_z \\
      (∂_z ∧ ∂_x)^{♭♯} &=& η_{zz} dx^z ∧ ∂_x \\
      \end{array}

   Apply the numerical values:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& + dx^t ∧ ∂_x \\
      (∂_t ∧ ∂_y)^{♭♯} &=& + dx^t ∧ ∂_y \\
      (∂_t ∧ ∂_z)^{♭♯} &=& + dx^t ∧ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &=& - dx^x ∧ ∂_y \\
      (∂_y ∧ ∂_z)^{♭♯} &=& - dx^y ∧ ∂_z \\
      (∂_z ∧ ∂_x)^{♭♯} &=& - dx^z ∧ ∂_x \\
      \end{array}

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{array}{r}
   (∂_t ∧ ∂_x)^{♭♯} &=& + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
   (∂_t ∧ ∂_y)^{♭♯} &=& + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
   (∂_t ∧ ∂_z)^{♭♯} &=& + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
   (∂_x ∧ ∂_y)^{♭♯} &=& - dx^x ⊗ ∂_y + dx^y ⊗ ∂_x \\
   (∂_y ∧ ∂_z)^{♭♯} &=& - dx^y ⊗ ∂_z + dx^z ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♭♯} &=& - dx^z ⊗ ∂_x + dx^x ⊗ ∂_z \\
   \end{array}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Expand wedge products to their tensor expressions:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& (∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t)^{♭♯} \\
      (∂_t ∧ ∂_y)^{♭♯} &=& (∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t)^{♭♯} \\
      (∂_t ∧ ∂_z)^{♭♯} &=& (∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t)^{♭♯} \\
      (∂_x ∧ ∂_y)^{♭♯} &=& (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♭♯} \\
      (∂_y ∧ ∂_z)^{♭♯} &=& (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♭♯} \\
      (∂_z ∧ ∂_x)^{♭♯} &=& (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♭♯} \\
      \end{array}

   Distribute the musical operators:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& (∂_t^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_t^♯) \\
      (∂_t ∧ ∂_y)^{♭♯} &=& (∂_t^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_t^♯) \\
      (∂_t ∧ ∂_z)^{♭♯} &=& (∂_t^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_t^♯) \\
      (∂_x ∧ ∂_y)^{♭♯} &=& (∂_x^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_x^♯) \\
      (∂_y ∧ ∂_z)^{♭♯} &=& (∂_y^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_y^♯) \\
      (∂_z ∧ ∂_x)^{♭♯} &=& (∂_z^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_z^♯) \\
      \end{array}

   Apply the musical operators:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_t \\
      (∂_x ∧ ∂_y)^{♭♯} &=& η_{xγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &=& η_{yγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &=& η_{zγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_z \\
      \end{array}

   Select non-zero metric elements:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_t \\
      (∂_x ∧ ∂_y)^{♭♯} &=& η_{xx} dx^x ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &=& η_{yy} dx^y ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &=& η_{zz} dx^z ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_z \\
      \end{array}

   Apply numerical values:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &=& + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &=& + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
      (∂_x ∧ ∂_y)^{♭♯} &=& - dx^x ⊗ ∂_y + dx^y ⊗ ∂_x \\
      (∂_y ∧ ∂_z)^{♭♯} &=& - dx^y ⊗ ∂_z + dx^z ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &=& - dx^z ⊗ ∂_x + dx^x ⊗ ∂_z \\
      \end{array}

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{array}{r}
   dx^t ∧ ∂_x &=& + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
   dx^t ∧ ∂_y &=& + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
   dx^t ∧ ∂_z &=& + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
   dx^x ∧ ∂_y &=& + dx^x ⊗ ∂_y - dx^y ⊗ ∂_x \\
   dx^y ∧ ∂_z &=& + dx^y ⊗ ∂_z - dx^z ⊗ ∂_y \\
   dx^z ∧ ∂_x &=& + dx^z ⊗ ∂_x - dx^x ⊗ ∂_z \\
   \end{array}

.. }}}

Flattening of the second index
------------------------------

.. {{{

We apply the :math:`♯♭` operators to flatten the second index of each basis
bivectors and obtain:

.. math::

   \begin{array}{}
   (∂_t ∧ ∂_x)^{♯♭} &=& - ∂_t ∧ dx^x \\
   (∂_t ∧ ∂_y)^{♯♭} &=& - ∂_t ∧ dx^y \\
   (∂_t ∧ ∂_z)^{♯♭} &=& - ∂_t ∧ dx^z \\
   (∂_x ∧ ∂_y)^{♯♭} &=& - ∂_x ∧ dx^y \\
   (∂_y ∧ ∂_z)^{♯♭} &=& - ∂_y ∧ dx^z \\
   (∂_z ∧ ∂_x)^{♯♭} &=& - ∂_z ∧ dx^x \\
   \end{array}

.. admonition:: All calculation steps
   :class: dropdown

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& ∂_t ∧ η_{xγ} dx^γ &=& η_{xγ} ∂_t ∧ dx^γ&=& η_{xx} ∂_t ∧ dx^x &=& - ∂_t ∧ dx^x \\
      (∂_t ∧ ∂_y)^{♯♭} &=& ∂_t ∧ η_{yγ} dx^γ &=& η_{yγ} ∂_t ∧ dx^γ&=& η_{yy} ∂_t ∧ dx^y &=& - ∂_t ∧ dx^y \\
      (∂_t ∧ ∂_z)^{♯♭} &=& ∂_t ∧ η_{zγ} dx^γ &=& η_{zγ} ∂_t ∧ dx^γ&=& η_{zz} ∂_t ∧ dx^z &=& - ∂_t ∧ dx^z \\
      (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x ∧ η_{yγ} dx^γ &=& η_{yγ} ∂_x ∧ dx^γ&=& η_{yy} ∂_x ∧ dx^y &=& - ∂_x ∧ dx^y \\
      (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y ∧ η_{zγ} dx^γ &=& η_{zγ} ∂_y ∧ dx^γ&=& η_{zz} ∂_y ∧ dx^z &=& - ∂_y ∧ dx^z \\
      (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z ∧ η_{xγ} dx^γ &=& η_{xγ} ∂_z ∧ dx^γ&=& η_{xx} ∂_z ∧ dx^x &=& - ∂_z ∧ dx^x \\
      \end{array}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{array}{}
   (∂_t ∧ ∂_x)^{♯♭} &=& - ∂_t ⊗ dx^x - ∂_x ⊗ dx^t \\
   (∂_t ∧ ∂_y)^{♯♭} &=& - ∂_t ⊗ dx^y - ∂_y ⊗ dx^t \\
   (∂_t ∧ ∂_z)^{♯♭} &=& - ∂_t ⊗ dx^z - ∂_z ⊗ dx^t \\
   (∂_x ∧ ∂_y)^{♯♭} &=& - ∂_x ⊗ dx^y + ∂_y ⊗ dx^x \\
   (∂_y ∧ ∂_z)^{♯♭} &=& - ∂_y ⊗ dx^z + ∂_z ⊗ dx^y \\
   (∂_z ∧ ∂_x)^{♯♭} &=& - ∂_z ⊗ dx^x + ∂_x ⊗ dx^z \\
   \end{array}

.. admonition:: All calculation steps
   :class: dropdown

   Expand in terms of tensor product:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& (∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t)^{♯♭} \\
      (∂_t ∧ ∂_y)^{♯♭} &=& (∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t)^{♯♭} \\
      (∂_t ∧ ∂_z)^{♯♭} &=& (∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t)^{♯♭} \\
      (∂_x ∧ ∂_y)^{♯♭} &=& (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♯♭} \\
      (∂_y ∧ ∂_z)^{♯♭} &=& (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♯♭} \\
      (∂_z ∧ ∂_x)^{♯♭} &=& (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♯♭} \\
      \end{array}

   Apply the flattening operator :math:`♭` to the second tensor component:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& (∂_t^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_t^♭) \\
      (∂_t ∧ ∂_y)^{♯♭} &=& (∂_t^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_t^♭) \\
      (∂_t ∧ ∂_z)^{♯♭} &=& (∂_t^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_t^♭) \\
      (∂_x ∧ ∂_y)^{♯♭} &=& (∂_x^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_x^♭) \\
      (∂_y ∧ ∂_z)^{♯♭} &=& (∂_y^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_y^♭) \\
      (∂_z ∧ ∂_x)^{♯♭} &=& (∂_z^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_z^♭) \\
      \end{array}

   Expand:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& ∂_t ⊗ η_{xγ} dx^γ - η_{tγ} ∂_x ⊗ dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &=& ∂_t ⊗ η_{yγ} dx^γ - η_{tγ} ∂_y ⊗ dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &=& ∂_t ⊗ η_{zγ} dx^γ - η_{tγ} ∂_z ⊗ dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x ⊗ η_{yγ} dx^γ - η_{xγ} ∂_y ⊗ dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y ⊗ η_{zγ} dx^γ - η_{yγ} ∂_z ⊗ dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z ⊗ η_{xγ} dx^γ - η_{zγ} ∂_x ⊗ dx^γ \\
      \end{array}

   Due to the linearity of the tensor product, the Minkowski metric components
   can be taken out in front of the expression:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& η_{xγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_x ⊗ dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &=& η_{yγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_y ⊗ dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &=& η_{zγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_z ⊗ dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &=& η_{yγ} ∂_x ⊗ dx^γ - η_{xγ} ∂_y ⊗ dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &=& η_{zγ} ∂_y ⊗ dx^γ - η_{yγ} ∂_z ⊗ dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &=& η_{xγ} ∂_z ⊗ dx^γ - η_{zγ} ∂_x ⊗ dx^γ \\
      \end{array}

   Indentify the non-zero component of the Minkowski metric and replace with
   numerical values:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& η_{xx} ∂_t ⊗ dx^x - η_{tt} ∂_ex ⊗ dx^t &=& - ∂_t ⊗ dx^x - ∂_x ⊗ dx^t \\
      (∂_t ∧ ∂_y)^{♯♭} &=& η_{yy} ∂_t ⊗ dx^y - η_{tt} ∂_ey ⊗ dx^t &=& - ∂_t ⊗ dx^y - ∂_y ⊗ dx^t \\
      (∂_t ∧ ∂_z)^{♯♭} &=& η_{zz} ∂_t ⊗ dx^z - η_{tt} ∂_ez ⊗ dx^t &=& - ∂_t ⊗ dx^z - ∂_z ⊗ dx^t \\
      (∂_x ∧ ∂_y)^{♯♭} &=& η_{yy} ∂_x ⊗ dx^y - η_{xx} ∂_ey ⊗ dx^x &=& - ∂_x ⊗ dx^y + ∂_y ⊗ dx^x \\
      (∂_y ∧ ∂_z)^{♯♭} &=& η_{zz} ∂_y ⊗ dx^z - η_{yy} ∂_ez ⊗ dx^y &=& - ∂_y ⊗ dx^z + ∂_z ⊗ dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &=& η_{xx} ∂_z ⊗ dx^x - η_{zz} ∂_ex ⊗ dx^z &=& - ∂_z ⊗ dx^x + ∂_x ⊗ dx^z \\
      \end{array}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{array}{r}
   ∂_t ∧ dx^x &=& + ∂_t ⊗ dx^x + ∂_x ⊗ dx^t \\
   ∂_t ∧ dx^y &=& + ∂_t ⊗ dx^y + ∂_y ⊗ dx^t \\
   ∂_t ∧ dx^z &=& + ∂_t ⊗ dx^z + ∂_z ⊗ dx^t \\
   ∂_x ∧ dx^y &=& + ∂_x ⊗ dx^y - ∂_y ⊗ dx^x \\
   ∂_y ∧ dx^z &=& + ∂_y ⊗ dx^z - ∂_z ⊗ dx^y \\
   ∂_z ∧ dx^x &=& + ∂_z ⊗ dx^x - ∂_x ⊗ dx^z \\
   \end{array}

.. }}}

Symmetries of the mixed wedge product
-------------------------------------

.. {{{

From the flattening of the first and second indices, we identified the
expression of the mixed wedge product in terms of tensor products. We conclude
that not all elements of the mixed wedge product in Minkowski space are
antisymmetric. **The elements depending on time are symmetric**.

.. rubric:: Covariant-contravariant basis elements

================== ============ =================================
Basis element      Symmetry     Expression
================== ============ =================================
:math:`dx^t ∧ ∂_x` Symetric     :math:`+ dx^t ⊗ ∂_x + dx^x ⊗ ∂_t`
:math:`dx^t ∧ ∂_y` Symetric     :math:`+ dx^t ⊗ ∂_y + dx^y ⊗ ∂_t`
:math:`dx^t ∧ ∂_z` Symetric     :math:`+ dx^t ⊗ ∂_z + dx^z ⊗ ∂_t`
:math:`dx^x ∧ ∂_y` Antisymetric :math:`+ dx^x ⊗ ∂_y - dx^y ⊗ ∂_x`
:math:`dx^y ∧ ∂_z` Antisymetric :math:`+ dx^y ⊗ ∂_z - dx^z ⊗ ∂_y`
:math:`dx^z ∧ ∂_x` Antisymetric :math:`+ dx^z ⊗ ∂_x - dx^x ⊗ ∂_z`
================== ============ =================================

.. rubric:: Contravariant-covariant basis elements

================== ============ =================================
Basis element      Symmetry     Expression
================== ============ =================================
:math:`∂_t ∧ dx^x` Symetric     :math:`+ ∂_t ⊗ dx^x + ∂_x ⊗ dx^t`
:math:`∂_t ∧ dx^y` Symetric     :math:`+ ∂_t ⊗ dx^y + ∂_y ⊗ dx^t`
:math:`∂_t ∧ dx^z` Symetric     :math:`+ ∂_t ⊗ dx^z + ∂_z ⊗ dx^t`
:math:`∂_x ∧ dx^y` Antisymetric :math:`+ ∂_x ⊗ dx^y - ∂_y ⊗ dx^x`
:math:`∂_y ∧ dx^z` Antisymetric :math:`+ ∂_y ⊗ dx^z - ∂_z ⊗ dx^y`
:math:`∂_z ∧ dx^x` Antisymetric :math:`+ ∂_z ⊗ dx^x - ∂_x ⊗ dx^z`
================== ============ =================================

.. }}}

The Mixed Rotation Tensor
-------------------------

.. {{{

In this section, I raise the indice using the free matrix notaion. The mixed
tensor is obtained by applying the flatternig operator :math:`\flat`:

.. math::

   \begin{equation}
   B^{♯♭}
   =
   \begin{bmatrix}
     F^{tx} \; ∂_t ∧ ∂_x \\
     F^{ty} \; ∂_t ∧ ∂_y \\
     F^{tz} \; ∂_t ∧ ∂_z \\
     F^{xy} \; ∂_x ∧ ∂_y \\
     F^{yz} \; ∂_y ∧ ∂_z \\
     F^{zx} \; ∂_z ∧ ∂_x \\
   \end{bmatrix}^{♯♭}
   =
   \begin{bmatrix}
     - F^{tx} \; ∂_t ∧ dx^x \\
     - F^{ty} \; ∂_t ∧ dx^y \\
     - F^{tz} \; ∂_t ∧ dx^z \\
     - F^{xy} \; ∂_x ∧ dx^y \\
     - F^{yz} \; ∂_y ∧ dx^z \\
     - F^{zx} \; ∂_z ∧ dx^x \\
   \end{bmatrix}
   \end{equation}

.. admonition:: Every calculation step
   :class: dropdown

   .. math::
   
      \begin{align*}
      B^{♯♭}
      &=
      \begin{bmatrix}
        F^{tx} \; ∂_t ∧ ∂_x \\
        F^{ty} \; ∂_t ∧ ∂_y \\
        F^{tz} \; ∂_t ∧ ∂_z \\
        F^{xy} \; ∂_x ∧ ∂_y \\
        F^{yz} \; ∂_y ∧ ∂_z \\
        F^{zx} \; ∂_z ∧ ∂_x \\
      \end{bmatrix}^{♯♭}
      =
      \begin{bmatrix}
        F^{tx} \; (∂_t ∧ ∂_x)^{♯♭} \\
        F^{ty} \; (∂_t ∧ ∂_y)^{♯♭} \\
        F^{tz} \; (∂_t ∧ ∂_z)^{♯♭} \\
        F^{xy} \; (∂_x ∧ ∂_y)^{♯♭} \\
        F^{yz} \; (∂_y ∧ ∂_z)^{♯♭} \\
        F^{zx} \; (∂_z ∧ ∂_x)^{♯♭} \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        F^{tx} \; ∂_t ∧ η_{xγ} dx^γ \\
        F^{ty} \; ∂_t ∧ η_{yγ} dx^γ \\
        F^{tz} \; ∂_t ∧ η_{zγ} dx^γ \\
        F^{xy} \; ∂_x ∧ η_{yγ} dx^γ \\
        F^{yz} \; ∂_y ∧ η_{zγ} dx^γ \\
        F^{zx} \; ∂_z ∧ η_{xγ} dx^γ \\
      \end{bmatrix} \\
      &=
      \begin{bmatrix}
        F^{tx} \; η_{xγ} ∂_t ∧ dx^γ \\
        F^{ty} \; η_{yγ} ∂_t ∧ dx^γ \\
        F^{tz} \; η_{zγ} ∂_t ∧ dx^γ \\
        F^{xy} \; η_{yγ} ∂_x ∧ dx^γ \\
        F^{yz} \; η_{zγ} ∂_y ∧ dx^γ \\
        F^{zx} \; η_{xγ} ∂_z ∧ dx^γ \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        F^{tx} \; η_{xx} ∂_t ∧ dx^x \\
        F^{ty} \; η_{yy} ∂_t ∧ dx^y \\
        F^{tz} \; η_{zz} ∂_t ∧ dx^z \\
        F^{xy} \; η_{yy} ∂_x ∧ dx^y \\
        F^{yz} \; η_{zz} ∂_y ∧ dx^z \\
        F^{zx} \; η_{xx} ∂_z ∧ dx^x \\
      \end{bmatrix}
      =
      \begin{bmatrix}
        - F^{tx} \; ∂_t ∧ dx^x \\
        - F^{ty} \; ∂_t ∧ dx^y \\
        - F^{tz} \; ∂_t ∧ dx^z \\
        - F^{xy} \; ∂_x ∧ dx^y \\
        - F^{yz} \; ∂_y ∧ dx^z \\
        - F^{zx} \; ∂_z ∧ dx^x \\
      \end{bmatrix}
      \end{align*}

Taking into account the symetric property of :math:`∂_t ∧ dx^x`, :math:`∂_t
∧ dx^y`, and :math:`∂_t ∧ dx^z`, as well the antisymetric property of
:math:`∂_x ∧ dx^y`, :math:`∂_ey ∧ dx^z`, and :math:`∂_z ∧ dx^x`
demonstrated above, this results in:

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \begin{bmatrix}
                         & - F^{tx} ∂_t ∧ dx^x & - F^{ty} ∂_t ∧ d^y & - F^{tz} ∂_t ∧ dx^z \\
     - F^{tx} ∂_x ∧ dx^t &                     & - F^{xy} ∂_x ∧ d^y & + F^{zx} ∂_x ∧ dx^z \\
     - F^{ty} ∂_y ∧ dx^t & + F^{xy} ∂_y ∧ dx^x &                    & - F^{yz} ∂_y ∧ dx^z \\
     - F^{tz} ∂_z ∧ dx^t & - F^{zx} ∂_z ∧ dx^x & + F^{yz} ∂_z ∧ d^y &                     \\
   \end{bmatrix}
   \end{align}

.. }}}

Calculating the mixed rotation tensor again, but without the Cartan-Hodge formalism
-----------------------------------------------------------------------------------

.. warning::

   While interesting to compare the advantages of the formalism, this will be
   taken out

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
   F^t{}_x &= F^{tγ} η_{γx} &= F^{tx} η_{xx} &= -F^{tx} \\
   F^t{}_y &= F^{tγ} η_{γy} &= F^{ty} η_{yy} &= -F^{ty} \\
   F^t{}_z &= F^{tγ} η_{γz} &= F^{tz} η_{zz} &= -F^{tz} \\
   \end{alignat*}

With :math:`F^{xx}=F^{yy}=F^{zz}=0`, :math:`F^{\mu\nu}=-F^{\nu\mu}`, as well as
:math:`\eta^{tx}=0`, :math:`\eta^{ty}=0`:math:`\eta^{tz}=0`, we expand and
obtain:

.. math::

   \begin{alignat*}{3}
   F^x{}_t &= F^{xγ} η_{γt} &= F^{xt} η_{tt} &= -F^{tx} \\
   F^y{}_t &= F^{yγ} η_{γt} &= F^{yt} η_{tt} &= -F^{ty} \\
   F^z{}_t &= F^{zγ} η_{γt} &= F^{zt} η_{tt} &= -F^{tz} \\
   \end{alignat*}

In the same manner, we get:

.. math::

   \begin{alignat}{2}
   F^x{}_y &= F^{xγ} η_{γy} &= F^{xy} η_{yy} &= -F^{xy} \\
   F^y{}_z &= F^{yγ} η_{γz} &= F^{yz} η_{zz} &= -F^{yz} \\
   F^z{}_x &= F^{zγ} η_{γx} &= F^{zx} η_{xx} &= -F^{zx} \\
   \end{alignat}

We have a mixed tensor of Rank two with the form:

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \begin{bmatrix}
     F^t{}_t ∂_t ∧ dx^t & F^t{}_x ∂_t ∧ dx^x & F^t{}_y ∂_t ∧ dx^y & F^t{}_z ∂_t ∧ dx^z \\
     F^x{}_t ∂_x ∧ dx^t & F^x{}_x ∂_x ∧ dx^x & F^x{}_y ∂_x ∧ dx^y & F^x{}_z ∂_x ∧ dx^z \\
     F^y{}_t ∂_y ∧ dx^t & F^y{}_x ∂_y ∧ dx^x & F^y{}_y ∂_y ∧ dx^y & F^y{}_z ∂_y ∧ dx^z \\
     F^z{}_t ∂_z ∧ dx^t & F^z{}_x ∂_z ∧ dx^x & F^z{}_y ∂_z ∧ dx^y & F^z{}_z ∂_z ∧ dx^z \\
   \end{bmatrix}
   \end{align}

All diagonal components are zero since:

.. math::

   \begin{equation}
   ∂_μ ∧ dx^μ = \frac{1}{2}(∂_μ ⊗ dx^μ - ∂_μ ⊗ dx^μ = 0
   \end{equation}

This result in:

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \begin{bmatrix}
                        & F^t{}_x ∂_t ∧ dx^x & F^t{}_y ∂_t ∧ dx^y & F^t{}_z ∂_t ∧ dx^z \\
     F^x{}_t ∂_x ∧ dx^t &                    & F^x{}_y ∂_x ∧ dx^y & F^x{}_z ∂_x ∧ dx^z \\
     F^y{}_t ∂_y ∧ dx^t & F^y{}_x ∂_y ∧ dx^x &                    & F^y{}_z ∂_y ∧ dx^z \\
     F^z{}_t ∂_z ∧ dx^t & F^z{}_x ∂_z ∧ dx^x & F^z{}_y ∂_z ∧ dx^y &                    \\
   \end{bmatrix}
   \end{align}

Further expanding all coefficients, we obtain:

.. math::

   \begin{align}
   B^{\sharp\flat}
   &= \frac{1}{2}
   \begin{bmatrix}
                              & F^{tγ} η_{γx} ∂_t ∧ dx^x & F^{tγ} η_{γy} ∂_t ∧ dx^y & F^{tγ} η_{γz} ∂_t ∧ dx^z \\
     F^{xγ} η_{γt} ∂_x ∧ dx^t &                          & F^{xγ} η_{γy} ∂_x ∧ dx^y & F^{xγ} η_{γz} ∂_x ∧ dx^z \\
     F^{yγ} η_{γt} ∂_y ∧ dx^t & F^{yγ} η_{γx} ∂_y ∧ dx^x &                          & F^{yγ} η_{γz} ∂_y ∧ dx^z \\
     F^{zγ} η_{γt} ∂_z ∧ dx^t & F^{zγ} η_{γx} ∂_z ∧ dx^x & F^{zγ} η_{γy} ∂_z ∧ dx^y &                          \\
   \end{bmatrix}
   \end{align}

Since only the diagonal elements of the metric tensor are non-zero:

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \begin{bmatrix}
                              & F^{tx} η_{xx} ∂_t ∧ dx^x & F^{ty} η_{yy} ∂_t ∧ dx^y & F^{tz} η_{zz} ∂_t ∧ dx^z \\
     F^{xt} η_{tt} ∂_x ∧ dx^t &                          & F^{xy} η_{yy} ∂_x ∧ dx^y & F^{xz} η_{zz} ∂_x ∧ dx^z \\
     F^{yt} η_{tt} ∂_y ∧ dx^t & F^{yx} η_{xx} ∂_y ∧ dx^x &                          & F^{yz} η_{zz} ∂_y ∧ dx^z \\
     F^{zt} η_{tt} ∂_z ∧ dx^t & F^{zx} η_{xx} ∂_z ∧ dx^x & F^{zy} η_{yy} ∂_z ∧ dx^y &                          \\
   \end{bmatrix}
   \end{align}

This elements of the Minkowski metric are replaced by their numerical values:

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \begin{bmatrix}
                         & - F^{tx} ∂_t ∧ dx^x & - F^{ty} ∂_t ∧ dx^y & - F^{tz} ∂_t ∧ dx^z \\
     + F^{xt} ∂_x ∧ dx^t &                     & - F^{xy} ∂_x ∧ dx^y & - F^{xz} ∂_x ∧ dx^z \\
     + F^{yt} ∂_y ∧ dx^t & - F^{yx} ∂_y ∧ dx^x &                     & - F^{yz} ∂_y ∧ dx^z \\
     + F^{zt} ∂_z ∧ dx^t & - F^{zx} ∂_z ∧ dx^x & - F^{zy} ∂_z ∧ dx^y &                     \\
   \end{bmatrix}
   \end{align}

The antisymetric properties of the components of the double contravariant
rotation tensors permit to simplify and conclude:

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \begin{bmatrix}
                         & - F^{tx} \; ∂_t ∧ dx^x & - F^{ty} ∂_t ∧ dx^y & - F^{tz} ∂_t ∧ dx^z \\
     - F^{tx} ∂_x ∧ dx^t &                        & - F^{xy} ∂_x ∧ dx^y & + F^{zx} ∂_x ∧ dx^z \\
     - F^{ty} ∂_y ∧ dx^t & + F^{xy} \; ∂_y ∧ dx^x &                     & - F^{yz} ∂_y ∧ dx^z \\
     - F^{tz} ∂_z ∧ dx^t & - F^{zx} \; ∂_z ∧ dx^x & + F^{yz} ∂_z ∧ dx^y &                     \\
   \end{bmatrix}
   \end{align}

.. }}}

The :math:`\mathfrak{so}(1,3)` Lie Algegra of the Lorentz group
---------------------------------------------------------------

.. {{{

.. }}}

