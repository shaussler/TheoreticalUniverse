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
     a \; ∂_t ∧ ∂_x \\
     b \; ∂_t ∧ ∂_y \\
     c \; ∂_t ∧ ∂_z \\
     d \; ∂_y ∧ ∂_z \\
     e \; ∂_z ∧ ∂_x \\
     f \; ∂_x ∧ ∂_y \\
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
                        & + a \; ∂_t ∧ ∂_x & + b \; ∂_t ∧ ∂_y & + c \; ∂_t ∧ ∂_z \\
       - a \; ∂_x ∧ ∂_t &                  & + f \; ∂_x ∧ ∂_y & - e \; ∂_x ∧ ∂_z \\
       - b \; ∂_y ∧ ∂_t & - f \; ∂_y ∧ ∂_x &                  & + d \; ∂_y ∧ ∂_z \\
       - c \; ∂_z ∧ ∂_t & + e \; ∂_z ∧ ∂_x & - d \; ∂_z ∧ ∂_y &                  \\
   \end{bmatrix}
   \end{equation}

Recall that using :ref:`the Minkowski metric <formalism_minkowski_metric:The
Minkowski Metric>`, we can flatten a basis vector with the flat operator
:math:`♭`:

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

Flattening the First Index
--------------------------

.. {{{

We apply the :math:`♭♯` operators to flatten the first index of each basis
bivectors:

.. math::

   \begin{array}{r}
   (∂_t ∧ ∂_x)^{♭♯} &=& + dx^t ∧ ∂_x \\
   (∂_t ∧ ∂_y)^{♭♯} &=& + dx^t ∧ ∂_y \\
   (∂_t ∧ ∂_z)^{♭♯} &=& + dx^t ∧ ∂_z \\
   (∂_y ∧ ∂_z)^{♭♯} &=& - dx^y ∧ ∂_z \\
   (∂_z ∧ ∂_x)^{♭♯} &=& - dx^z ∧ ∂_x \\
   (∂_x ∧ ∂_y)^{♭♯} &=& - dx^x ∧ ∂_y \\
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

   Identify the non-zero metric elements:

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
   (∂_y ∧ ∂_z)^{♭♯} &=& - dx^y ⊗ ∂_z + dx^z ⊗ ∂_y \\
   (∂_z ∧ ∂_x)^{♭♯} &=& - dx^z ⊗ ∂_x + dx^x ⊗ ∂_z \\
   (∂_x ∧ ∂_y)^{♭♯} &=& - dx^x ⊗ ∂_y + dx^y ⊗ ∂_x \\
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
      (∂_y ∧ ∂_z)^{♭♯} &=& (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♭♯} \\
      (∂_z ∧ ∂_x)^{♭♯} &=& (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♭♯} \\
      (∂_x ∧ ∂_y)^{♭♯} &=& (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♭♯} \\
      \end{array}

   Distribute the musical operators:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& (∂_t^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_t^♯) \\
      (∂_t ∧ ∂_y)^{♭♯} &=& (∂_t^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_t^♯) \\
      (∂_t ∧ ∂_z)^{♭♯} &=& (∂_t^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_t^♯) \\
      (∂_y ∧ ∂_z)^{♭♯} &=& (∂_y^♭ ⊗ ∂_z^♯ - ∂_z^♭ ⊗ ∂_y^♯) \\
      (∂_z ∧ ∂_x)^{♭♯} &=& (∂_z^♭ ⊗ ∂_x^♯ - ∂_x^♭ ⊗ ∂_z^♯) \\
      (∂_x ∧ ∂_y)^{♭♯} &=& (∂_x^♭ ⊗ ∂_y^♯ - ∂_y^♭ ⊗ ∂_x^♯) \\
      \end{array}

   Apply the musical operators:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &=& η_{tγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_t \\
      (∂_y ∧ ∂_z)^{♭♯} &=& η_{yγ} dx^γ ⊗ ∂_z - η_{zγ} dx^γ ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &=& η_{zγ} dx^γ ⊗ ∂_x - η_{xγ} dx^γ ⊗ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &=& η_{xγ} dx^γ ⊗ ∂_y - η_{yγ} dx^γ ⊗ ∂_x \\
      \end{array}

   Select non-zero metric elements:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &=& η_{tt} dx^t ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_t \\
      (∂_y ∧ ∂_z)^{♭♯} &=& η_{yy} dx^y ⊗ ∂_z - η_{zz} dx^z ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &=& η_{zz} dx^z ⊗ ∂_x - η_{xx} dx^x ⊗ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &=& η_{xx} dx^x ⊗ ∂_y - η_{yy} dx^y ⊗ ∂_x \\
      \end{array}

   Apply numerical values:

   .. math::

      \begin{array}{r}
      (∂_t ∧ ∂_x)^{♭♯} &=& + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
      (∂_t ∧ ∂_y)^{♭♯} &=& + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
      (∂_t ∧ ∂_z)^{♭♯} &=& + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
      (∂_y ∧ ∂_z)^{♭♯} &=& - dx^y ⊗ ∂_z + dx^z ⊗ ∂_y \\
      (∂_z ∧ ∂_x)^{♭♯} &=& - dx^z ⊗ ∂_x + dx^x ⊗ ∂_z \\
      (∂_x ∧ ∂_y)^{♭♯} &=& - dx^x ⊗ ∂_y + dx^y ⊗ ∂_x \\
      \end{array}

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{array}{r}
   dx^t ∧ ∂_x &=& + dx^t ⊗ ∂_x + dx^x ⊗ ∂_t \\
   dx^t ∧ ∂_y &=& + dx^t ⊗ ∂_y + dx^y ⊗ ∂_t \\
   dx^t ∧ ∂_z &=& + dx^t ⊗ ∂_z + dx^z ⊗ ∂_t \\
   dx^y ∧ ∂_z &=& + dx^y ⊗ ∂_z - dx^z ⊗ ∂_y \\
   dx^z ∧ ∂_x &=& + dx^z ⊗ ∂_x - dx^x ⊗ ∂_z \\
   dx^x ∧ ∂_y &=& + dx^x ⊗ ∂_y - dx^y ⊗ ∂_x \\
   \end{array}

.. }}}

Flattening the Second Index
---------------------------

.. {{{

We apply the :math:`♯♭` operators to flatten the second index of each basis
bivectors and obtain:

.. math::

   \begin{array}{}
   (∂_t ∧ ∂_x)^{♯♭} &=& - ∂_t ∧ dx^x \\
   (∂_t ∧ ∂_y)^{♯♭} &=& - ∂_t ∧ dx^y \\
   (∂_t ∧ ∂_z)^{♯♭} &=& - ∂_t ∧ dx^z \\
   (∂_y ∧ ∂_z)^{♯♭} &=& - ∂_y ∧ dx^z \\
   (∂_z ∧ ∂_x)^{♯♭} &=& - ∂_z ∧ dx^x \\
   (∂_x ∧ ∂_y)^{♯♭} &=& - ∂_x ∧ dx^y \\
   \end{array}

.. admonition:: All calculation steps
   :class: dropdown

   Distribute the musical operators:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& ∂_t^♯ ∧ ∂_x^♭ \\
      (∂_t ∧ ∂_y)^{♯♭} &=& ∂_t^♯ ∧ ∂_y^♭ \\
      (∂_t ∧ ∂_z)^{♯♭} &=& ∂_t^♯ ∧ ∂_z^♭ \\
      (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y^♯ ∧ ∂_z^♭ \\
      (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z^♯ ∧ ∂_x^♭ \\
      (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x^♯ ∧ ∂_y^♭ \\
      \end{array}

   Apply the musical operators:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& ∂_t ∧ η_{xγ} dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &=& ∂_t ∧ η_{yγ} dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &=& ∂_t ∧ η_{zγ} dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y ∧ η_{zγ} dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z ∧ η_{xγ} dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x ∧ η_{yγ} dx^γ \\
      \end{array}

   Take out the metric components:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& η_{xγ} ∂_t ∧ dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &=& η_{yγ} ∂_t ∧ dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &=& η_{zγ} ∂_t ∧ dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &=& η_{zγ} ∂_y ∧ dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &=& η_{xγ} ∂_z ∧ dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &=& η_{yγ} ∂_x ∧ dx^γ \\
      \end{array}

   Identify the non-zero metric components:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& η_{xx} ∂_t ∧ dx^x \\
      (∂_t ∧ ∂_y)^{♯♭} &=& η_{yy} ∂_t ∧ dx^y \\
      (∂_t ∧ ∂_z)^{♯♭} &=& η_{zz} ∂_t ∧ dx^z \\
      (∂_y ∧ ∂_z)^{♯♭} &=& η_{zz} ∂_y ∧ dx^z \\
      (∂_z ∧ ∂_x)^{♯♭} &=& η_{xx} ∂_z ∧ dx^x \\
      (∂_x ∧ ∂_y)^{♯♭} &=& η_{yy} ∂_x ∧ dx^y \\
      \end{array}

   Apply numerical values:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& - ∂_t ∧ dx^x \\
      (∂_t ∧ ∂_y)^{♯♭} &=& - ∂_t ∧ dx^y \\
      (∂_t ∧ ∂_z)^{♯♭} &=& - ∂_t ∧ dx^z \\
      (∂_y ∧ ∂_z)^{♯♭} &=& - ∂_y ∧ dx^z \\
      (∂_z ∧ ∂_x)^{♯♭} &=& - ∂_z ∧ dx^x \\
      (∂_x ∧ ∂_y)^{♯♭} &=& - ∂_x ∧ dx^y \\
      \end{array}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{array}{}
   (∂_t ∧ ∂_x)^{♯♭} &=& - ∂_t ⊗ dx^x - ∂_x ⊗ dx^t \\
   (∂_t ∧ ∂_y)^{♯♭} &=& - ∂_t ⊗ dx^y - ∂_y ⊗ dx^t \\
   (∂_t ∧ ∂_z)^{♯♭} &=& - ∂_t ⊗ dx^z - ∂_z ⊗ dx^t \\
   (∂_y ∧ ∂_z)^{♯♭} &=& - ∂_y ⊗ dx^z + ∂_z ⊗ dx^y \\
   (∂_z ∧ ∂_x)^{♯♭} &=& - ∂_z ⊗ dx^x + ∂_x ⊗ dx^z \\
   (∂_x ∧ ∂_y)^{♯♭} &=& - ∂_x ⊗ dx^y + ∂_y ⊗ dx^x \\
   \end{array}

.. admonition:: All calculation steps
   :class: dropdown

   .. {{{

   Expand in terms of tensor product:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& (∂_t ⊗ ∂_x - ∂_x ⊗ ∂_t)^{♯♭} \\
      (∂_t ∧ ∂_y)^{♯♭} &=& (∂_t ⊗ ∂_y - ∂_y ⊗ ∂_t)^{♯♭} \\
      (∂_t ∧ ∂_z)^{♯♭} &=& (∂_t ⊗ ∂_z - ∂_z ⊗ ∂_t)^{♯♭} \\
      (∂_y ∧ ∂_z)^{♯♭} &=& (∂_y ⊗ ∂_z - ∂_z ⊗ ∂_y)^{♯♭} \\
      (∂_z ∧ ∂_x)^{♯♭} &=& (∂_z ⊗ ∂_x - ∂_x ⊗ ∂_z)^{♯♭} \\
      (∂_x ∧ ∂_y)^{♯♭} &=& (∂_x ⊗ ∂_y - ∂_y ⊗ ∂_x)^{♯♭} \\
      \end{array}

   Distribute the flattening operator :math:`♭` to the second tensor component:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& (∂_t^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_t^♭) \\
      (∂_t ∧ ∂_y)^{♯♭} &=& (∂_t^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_t^♭) \\
      (∂_t ∧ ∂_z)^{♯♭} &=& (∂_t^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_t^♭) \\
      (∂_y ∧ ∂_z)^{♯♭} &=& (∂_y^♯ ⊗ ∂_z^♭ - ∂_z^♯ ⊗ ∂_y^♭) \\
      (∂_z ∧ ∂_x)^{♯♭} &=& (∂_z^♯ ⊗ ∂_x^♭ - ∂_x^♯ ⊗ ∂_z^♭) \\
      (∂_x ∧ ∂_y)^{♯♭} &=& (∂_x^♯ ⊗ ∂_y^♭ - ∂_y^♯ ⊗ ∂_x^♭) \\
      \end{array}

   Apply and expand:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& ∂_t ⊗ η_{xγ} dx^γ - η_{tγ} ∂_x ⊗ dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &=& ∂_t ⊗ η_{yγ} dx^γ - η_{tγ} ∂_y ⊗ dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &=& ∂_t ⊗ η_{zγ} dx^γ - η_{tγ} ∂_z ⊗ dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &=& ∂_y ⊗ η_{zγ} dx^γ - η_{yγ} ∂_z ⊗ dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &=& ∂_z ⊗ η_{xγ} dx^γ - η_{zγ} ∂_x ⊗ dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &=& ∂_x ⊗ η_{yγ} dx^γ - η_{xγ} ∂_y ⊗ dx^γ \\
      \end{array}

   Due to the linearity of the tensor product, the Minkowski metric components
   can be taken out in front of the expression:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& η_{xγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_x ⊗ dx^γ \\
      (∂_t ∧ ∂_y)^{♯♭} &=& η_{yγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_y ⊗ dx^γ \\
      (∂_t ∧ ∂_z)^{♯♭} &=& η_{zγ} ∂_t ⊗ dx^γ - η_{tγ} ∂_z ⊗ dx^γ \\
      (∂_y ∧ ∂_z)^{♯♭} &=& η_{zγ} ∂_y ⊗ dx^γ - η_{yγ} ∂_z ⊗ dx^γ \\
      (∂_z ∧ ∂_x)^{♯♭} &=& η_{xγ} ∂_z ⊗ dx^γ - η_{zγ} ∂_x ⊗ dx^γ \\
      (∂_x ∧ ∂_y)^{♯♭} &=& η_{yγ} ∂_x ⊗ dx^γ - η_{xγ} ∂_y ⊗ dx^γ \\
      \end{array}

   Identify the non-zero metric components:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& η_{xx} ∂_t ⊗ dx^x - η_{tt} ∂_ex ⊗ dx^t \\
      (∂_t ∧ ∂_y)^{♯♭} &=& η_{yy} ∂_t ⊗ dx^y - η_{tt} ∂_ey ⊗ dx^t \\
      (∂_t ∧ ∂_z)^{♯♭} &=& η_{zz} ∂_t ⊗ dx^z - η_{tt} ∂_ez ⊗ dx^t \\
      (∂_y ∧ ∂_z)^{♯♭} &=& η_{zz} ∂_y ⊗ dx^z - η_{yy} ∂_ez ⊗ dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &=& η_{xx} ∂_z ⊗ dx^x - η_{zz} ∂_ex ⊗ dx^z \\
      (∂_x ∧ ∂_y)^{♯♭} &=& η_{yy} ∂_x ⊗ dx^y - η_{xx} ∂_ey ⊗ dx^x \\
      \end{array}

   Apply numerical values:

   .. math::

      \begin{array}{}
      (∂_t ∧ ∂_x)^{♯♭} &=& - ∂_t ⊗ dx^x - ∂_x ⊗ dx^t \\
      (∂_t ∧ ∂_y)^{♯♭} &=& - ∂_t ⊗ dx^y - ∂_y ⊗ dx^t \\
      (∂_t ∧ ∂_z)^{♯♭} &=& - ∂_t ⊗ dx^z - ∂_z ⊗ dx^t \\
      (∂_y ∧ ∂_z)^{♯♭} &=& - ∂_y ⊗ dx^z + ∂_z ⊗ dx^y \\
      (∂_z ∧ ∂_x)^{♯♭} &=& - ∂_z ⊗ dx^x + ∂_x ⊗ dx^z \\
      (∂_x ∧ ∂_y)^{♯♭} &=& - ∂_x ⊗ dx^y + ∂_y ⊗ dx^x \\
      \end{array}

   .. }}}

We can then identify the expressions for the mixed wedge product explicitely in
terms of tensor products:

.. math::

   \begin{array}{r}
   ∂_t ∧ dx^x &=& + ∂_t ⊗ dx^x + ∂_x ⊗ dx^t \\
   ∂_t ∧ dx^y &=& + ∂_t ⊗ dx^y + ∂_y ⊗ dx^t \\
   ∂_t ∧ dx^z &=& + ∂_t ⊗ dx^z + ∂_z ⊗ dx^t \\
   ∂_y ∧ dx^z &=& + ∂_y ⊗ dx^z - ∂_z ⊗ dx^y \\
   ∂_z ∧ dx^x &=& + ∂_z ⊗ dx^x - ∂_x ⊗ dx^z \\
   ∂_x ∧ dx^y &=& + ∂_x ⊗ dx^y - ∂_y ⊗ dx^x \\
   \end{array}

.. }}}

Symmetries of the Mixed Wedge Product
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
:math:`dx^y ∧ ∂_z` Antisymetric :math:`+ dx^y ⊗ ∂_z - dx^z ⊗ ∂_y`
:math:`dx^z ∧ ∂_x` Antisymetric :math:`+ dx^z ⊗ ∂_x - dx^x ⊗ ∂_z`
:math:`dx^x ∧ ∂_y` Antisymetric :math:`+ dx^x ⊗ ∂_y - dx^y ⊗ ∂_x`
================== ============ =================================

.. rubric:: Contravariant-covariant basis elements

================== ============ =================================
Basis element      Symmetry     Expression
================== ============ =================================
:math:`∂_t ∧ dx^x` Symetric     :math:`+ ∂_t ⊗ dx^x + ∂_x ⊗ dx^t`
:math:`∂_t ∧ dx^y` Symetric     :math:`+ ∂_t ⊗ dx^y + ∂_y ⊗ dx^t`
:math:`∂_t ∧ dx^z` Symetric     :math:`+ ∂_t ⊗ dx^z + ∂_z ⊗ dx^t`
:math:`∂_y ∧ dx^z` Antisymetric :math:`+ ∂_y ⊗ dx^z - ∂_z ⊗ dx^y`
:math:`∂_z ∧ dx^x` Antisymetric :math:`+ ∂_z ⊗ dx^x - ∂_x ⊗ dx^z`
:math:`∂_x ∧ dx^y` Antisymetric :math:`+ ∂_x ⊗ dx^y - ∂_y ⊗ dx^x`
================== ============ =================================

.. }}}

The :math:`♯♭` Rotation Tensor
------------------------------

.. {{{

In this section, I raise the indice using the free matrix notaion. The mixed
tensor is obtained by applying the flatternig operator :math:`\flat`:

.. math::

   \begin{equation}
   B^{♯♭}
   =
   \begin{bmatrix}
     a \; ∂_t ∧ ∂_x \\
     b \; ∂_t ∧ ∂_y \\
     c \; ∂_t ∧ ∂_z \\
     d \; ∂_y ∧ ∂_z \\
     e \; ∂_z ∧ ∂_x \\
     f \; ∂_x ∧ ∂_y \\
   \end{bmatrix}^{♯♭}
   =
   \begin{bmatrix}
     - a \; ∂_t ∧ dx^x \\
     - b \; ∂_t ∧ dx^y \\
     - c \; ∂_t ∧ dx^z \\
     - d \; ∂_y ∧ dx^z \\
     - e \; ∂_z ∧ dx^x \\
     - f \; ∂_x ∧ dx^y \\
   \end{bmatrix}
   \end{equation}

.. admonition:: Every calculation steps
   :class: dropdown

   .. {{{

   Apply the musical operator :math:`♯♭`

   .. math::

      \begin{equation}
      B^{♯♭} =
      \begin{bmatrix}
        a \; ∂_t ∧ ∂_x \\
        b \; ∂_t ∧ ∂_y \\
        c \; ∂_t ∧ ∂_z \\
        d \; ∂_y ∧ ∂_z \\
        e \; ∂_z ∧ ∂_x \\
        f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}^{♯♭}
      \end{equation}

   Distribute the musical operators to each matrix elements:

   .. math::

      \begin{equation}
      B^{♯♭} =
      \begin{bmatrix}
        a \; (∂_t ∧ ∂_x)^{♯♭} \\
        b \; (∂_t ∧ ∂_y)^{♯♭} \\
        c \; (∂_t ∧ ∂_z)^{♯♭} \\
        d \; (∂_y ∧ ∂_z)^{♯♭} \\
        e \; (∂_z ∧ ∂_x)^{♯♭} \\
        f \; (∂_x ∧ ∂_y)^{♯♭} \\
      \end{bmatrix}
      \end{equation}

   Distribute the musical operators:

   .. math::

      \begin{equation}
      B^{♯♭} =
      \begin{bmatrix}
        a \; (∂_t^♯ ∧ ∂_x^♭) \\
        b \; (∂_t^♯ ∧ ∂_y^♭) \\
        c \; (∂_t^♯ ∧ ∂_z^♭) \\
        d \; (∂_y^♯ ∧ ∂_z^♭) \\
        e \; (∂_z^♯ ∧ ∂_x^♭) \\
        f \; (∂_x^♯ ∧ ∂_y^♭) \\
      \end{bmatrix}
      \end{equation}

   Apply and expand:

   .. math::

      \begin{equation}
      B^{♯♭} =
      \begin{bmatrix}
        a \; ∂_t ∧ η_{xγ} dx^γ \\
        b \; ∂_t ∧ η_{yγ} dx^γ \\
        c \; ∂_t ∧ η_{zγ} dx^γ \\
        d \; ∂_y ∧ η_{zγ} dx^γ \\
        e \; ∂_z ∧ η_{xγ} dx^γ \\
        f \; ∂_x ∧ η_{yγ} dx^γ \\
      \end{bmatrix}
      \end{equation}

   The metric tensor can be taken out due to mulilinearity:

   .. math::

      \begin{equation}
      B^{♯♭} =
      \begin{bmatrix}
        a \; η_{xγ} ∂_t ∧ dx^γ \\
        b \; η_{yγ} ∂_t ∧ dx^γ \\
        c \; η_{zγ} ∂_t ∧ dx^γ \\
        d \; η_{zγ} ∂_y ∧ dx^γ \\
        e \; η_{xγ} ∂_z ∧ dx^γ \\
        f \; η_{yγ} ∂_x ∧ dx^γ \\
      \end{bmatrix}
      \end{equation}

   Most terms of the Minkowski metric are zero:

   .. math::

      \begin{equation}
      B^{♯♭} =
      \begin{bmatrix}
        a \; η_{xx} ∂_t ∧ dx^x \\
        b \; η_{yy} ∂_t ∧ dx^y \\
        c \; η_{zz} ∂_t ∧ dx^z \\
        d \; η_{zz} ∂_y ∧ dx^z \\
        e \; η_{xx} ∂_z ∧ dx^x \\
        f \; η_{yy} ∂_x ∧ dx^y \\
      \end{bmatrix}
      \end{equation}

   Use the numerical values of the Minkowski metric:

   .. math::

      \begin{equation}
      B^{♯♭} =
      \begin{bmatrix}
        - a \; ∂_t ∧ dx^x \\
        - b \; ∂_t ∧ dx^y \\
        - c \; ∂_t ∧ dx^z \\
        - d \; ∂_y ∧ dx^z \\
        - e \; ∂_z ∧ dx^x \\
        - f \; ∂_x ∧ dx^y \\
      \end{bmatrix}
      \end{equation}

   .. }}}

Taking into account the symetric property of :math:`∂_t ∧ dx^x`, :math:`∂_t
∧ dx^y`, and :math:`∂_t ∧ dx^z`, as well the antisymetric property of
:math:`∂_x ∧ dx^y`, :math:`∂_ey ∧ dx^z`, and :math:`∂_z ∧ dx^x`
demonstrated above, this results in:

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \begin{bmatrix}
                       & - a \; ∂_t ∧ dx^x & - b \; ∂_t ∧ d^y & - c \; ∂_t ∧ dx^z \\
     - a \; ∂_x ∧ dx^t &                   & - f \; ∂_x ∧ d^y & + e \; ∂_x ∧ dx^z \\
     - b \; ∂_y ∧ dx^t & + f \; ∂_y ∧ dx^x &                  & - d \; ∂_y ∧ dx^z \\
     - c \; ∂_z ∧ dx^t & - e \; ∂_z ∧ dx^x & + d \; ∂_z ∧ d^y &                   \\
   \end{bmatrix}
   \end{align}

.. }}}

The :math:`♭♯` Rotation Tensor
------------------------------

.. {{{

In this section, I flattne the first component using the :ref:`free matrix
representation <formalism_free_matrix_representation:The Free Matrix
Representation>`. The mixed tensor is obtained by applying the flatternig
operator :math:`\flat`:

.. math::

   \begin{equation}
   B^{♭♯}
   =
   \begin{bmatrix}
     a \; ∂_t ∧ ∂_x \\
     b \; ∂_t ∧ ∂_y \\
     c \; ∂_t ∧ ∂_z \\
     d \; ∂_y ∧ ∂_z \\
     e \; ∂_z ∧ ∂_x \\
     f \; ∂_x ∧ ∂_y \\
   \end{bmatrix}^{♭♯}
   =
   \begin{bmatrix}
     + a \; dx^x ∧ ∂_t \\
     + b \; dx^y ∧ ∂_t \\
     + c \; dx^z ∧ ∂_t \\
     - d \; dx^z ∧ ∂_y \\
     - e \; dx^x ∧ ∂_z \\
     - f \; dx^y ∧ ∂_x \\
   \end{bmatrix}
   \end{equation}

.. admonition:: Every calculation steps
   :class: dropdown

   .. {{{

   Apply the musical operator :math:`♭♯`

   .. math::

      \begin{equation}
      B^{♭♯} =
      \begin{bmatrix}
        a \; ∂_t ∧ ∂_x \\
        b \; ∂_t ∧ ∂_y \\
        c \; ∂_t ∧ ∂_z \\
        d \; ∂_y ∧ ∂_z \\
        e \; ∂_z ∧ ∂_x \\
        f \; ∂_x ∧ ∂_y \\
      \end{bmatrix}^{♭♯}
      \end{equation}

   Distribute the musical operators to each matrix elements:

   .. math::

      \begin{equation}
      B^{♭♯} =
      \begin{bmatrix}
        a \; (∂_t ∧ ∂_x)^{♭♯} \\
        b \; (∂_t ∧ ∂_y)^{♭♯} \\
        c \; (∂_t ∧ ∂_z)^{♭♯} \\
        d \; (∂_y ∧ ∂_z)^{♭♯} \\
        e \; (∂_z ∧ ∂_x)^{♭♯} \\
        f \; (∂_x ∧ ∂_y)^{♭♯} \\
      \end{bmatrix}
      \end{equation}

   Distribute the musical operators:

   .. math::

      \begin{equation}
      B^{♭♯} =
      \begin{bmatrix}
        a \; (∂_t^♭ ∧ ∂_x^♯) \\
        b \; (∂_t^♭ ∧ ∂_y^♯) \\
        c \; (∂_t^♭ ∧ ∂_z^♯) \\
        d \; (∂_y^♭ ∧ ∂_z^♯) \\
        e \; (∂_z^♭ ∧ ∂_x^♯) \\
        f \; (∂_x^♭ ∧ ∂_y^♯) \\
      \end{bmatrix}
      \end{equation}

   Apply the musical operators:

   .. math::

      \begin{equation}
      B^{♭♯} =
      \begin{bmatrix}
        a \; η_{tγ} dx^γ ∧ ∂_x^♯ \\
        b \; η_{tγ} dx^γ ∧ ∂_y^♯ \\
        c \; η_{tγ} dx^γ ∧ ∂_z^♯ \\
        d \; η_{yγ} dx^γ ∧ ∂_z^♯ \\
        e \; η_{zγ} dx^γ ∧ ∂_x^♯ \\
        f \; η_{xγ} dx^γ ∧ ∂_y^♯ \\
      \end{bmatrix}
      \end{equation}

   Identify the non-zero terms of the Minkowski metric:

   .. math::

      \begin{equation}
      B^{♭♯} =
      \begin{bmatrix}
        a \; η_{tt} dx^t ∧ ∂_x \\
        b \; η_{tt} dx^t ∧ ∂_y \\
        c \; η_{tt} dx^t ∧ ∂_z \\
        d \; η_{yy} dx^y ∧ ∂_z \\
        e \; η_{zz} dx^z ∧ ∂_x \\
        f \; η_{xx} dx^x ∧ ∂_y \\
      \end{bmatrix}
      \end{equation}

   Use the numerical values of the Minkowski metric:

   .. math::

      \begin{equation}
      B^{♭♯} =
      \begin{bmatrix}
        + a \; dx^t ∧ ∂_x \\
        + b \; dx^t ∧ ∂_y \\
        + c \; dx^t ∧ ∂_z \\
        - d \; dx^y ∧ ∂_z \\
        - e \; dx^z ∧ ∂_x \\
        - f \; dx^x ∧ ∂_y \\
      \end{bmatrix}
      \end{equation}

   .. }}}

Taking into account the symetric property of :math:`dx^t ∧ ∂_x`, :math:`dx^t
∧ ∂_y`, and :math:`dx^t ∧ ∂_z`, as well the antisymetric property of
:math:`dx^x ∧ ∂_y`, :math:`dx^y ∧ ∂_z`, and :math:`dx^z ∧ ∂_x`
demonstrated above, this results in:

.. math::

   \begin{align}
   B^{♭♯}
   &= \frac{1}{2}
   \begin{bmatrix}
                       & + a \; dx^t ∧ ∂_x & + b \; dx^t ∧ ∂_y & + c \; dx^t ∧ ∂_z \\
     + a \; dx^x ∧ ∂_t &                   & + f \; dx^x ∧ ∂_y & - e \; dx^x ∧ ∂_z \\
     + b \; dx^y ∧ ∂_t & - f \; dx^y ∧ ∂_x &                   & + d \; dx^y ∧ ∂_z \\
     + c \; dx^z ∧ ∂_t & + e \; dx^z ∧ ∂_x & - d \; dx^z ∧ ∂_y &                   \\
   \end{bmatrix}
   \end{align}

.. }}}

The :math:`\mathfrak{so}(1,3)` Lie Algegra of the Lorentz group
---------------------------------------------------------------

.. {{{

We thus obtain explicit expressions of the `Lorentz group
<https://en.m.wikipedia.org/wiki/Lorentz_group#Lie_algebra>`_.

.. math::

   \begin{align}
   B^{♯♭}
   &= \frac{1}{2}
   \begin{bmatrix}
         & + a & + b & + c \\
     + a &     & + d & + f \\
     + b & - d &     & + e \\
     + c & - f & - e &     \\
   \end{bmatrix}
   \end{align}

.. }}}
