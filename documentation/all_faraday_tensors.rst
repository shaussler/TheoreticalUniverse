All Faraday Tensors
===================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

In a :ref:`former post <faraday_tensor_derivation:Deriving the Faraday Tensor
from the 1865 Maxwell Equations>`, I derived the Faraday tensor and its Hodge
dual from the 1865 Maxwell equations. I also introdue a musical notation to
facilitate calculations. In this post, I derive all possible variants of the
Faraday together with more details and example of the musical notation.

Inhomogenous equations
----------------------

.. rubric:: Contravariant-covariant

.. {{{

.. math::

   {\small
   F^{\sharp\flat}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x} &              & +       B^z  & -        B^y  \\
    +\tilde{E^y} & -       B^z  &              & +        B^x  \\
    +\tilde{E^z} & +       B^y  & -       B^x  &               \\
   \end{bmatrix}^{\sharp\flat}
   }

From there, we can obtain all other forms of the Faraday tensors by applying
the Minkowski metric.

.. }}}

.. rubric:: Contravariant-contravariant

.. {{{

.. math::

   {\scriptsize
   F^{\sharp\sharp}
   =
   F^{\sharp\flat} \eta^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x} &              & +       B^z  & -        B^y  \\
    +\tilde{E^y} & -       B^z  &              & +        B^x  \\
    +\tilde{E^z} & +       B^y  & -       B^x  &               \\
   \end{bmatrix}^{\sharp\flat}
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & -\tilde{E^x} & -\tilde{E^y} & - \tilde{E^z} \\
    +\tilde{E^x} &              & -       B^z  & +        B^y  \\
    +\tilde{E^y} & +       B^z  &              & -        B^x  \\
    +\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}^{\sharp\sharp}
   }

.. note::

   An alternative to the musical notation is to explicitely sharpen
   :math:`\sharp` or flatten :math:`\flat` the vectors. The equations then take
   this form which is equivalent.

   .. math::

      {\small
      F^{\sharp\sharp}
      =
      F^{\sharp\flat} \eta^{\sharp\sharp}
      =
      \begin{bmatrix}
                    & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
       +\tilde{E^x} &              & +       B^z  & -        B^y  \\
       +\tilde{E^y} & -       B^z  &              & +        B^x  \\
       +\tilde{E^z} & +       B^y  & -       B^x  &               \\
      \end{bmatrix}^{\sharp\flat}
      \begin{bmatrix}
          \begin{bmatrix}
          \phantom{+} 1 \\
          \phantom{+} 0 \\
          \phantom{+} 0 \\
          \phantom{+} 0 \\
          \end{bmatrix} \\
          \begin{bmatrix}
          \phantom{+} 0 \\
          -1 \\
          \phantom{+} 0 \\
          \phantom{+} 0 \\
          \end{bmatrix} \\
          \begin{bmatrix}
          \phantom{+} 0 \\
          \phantom{+} 0 \\
          -1 \\
          \phantom{+} 0 \\
          \end{bmatrix} \\
          \begin{bmatrix}
          \phantom{+} 0 \\
          \phantom{+} 0 \\
          \phantom{+} 0 \\
          -1 \\
          \end{bmatrix}
      \end{bmatrix}
      =
      \begin{bmatrix}
          \begin{bmatrix}
                       \\
          +\tilde{E^x} \\
          +\tilde{E^y} \\
          +\tilde{E^z} \\
          \end{bmatrix} \\
          \begin{bmatrix}
          -\tilde{E^x} \\
                       \\
          +       B^z  \\
          -       B^y  \\
          \end{bmatrix} \\
          \begin{bmatrix}
          -\tilde{E^y} \\
          -       B^z  \\
                       \\
          +       B^x  \\
          \end{bmatrix} \\
          \begin{bmatrix}
          -\tilde{E^z} \\
          +       B^y  \\
          -       B^x  \\
                       \\
          \end{bmatrix}
      \end{bmatrix}
      }

.. }}}

.. rubric:: Covariant-covariant

.. {{{

.. math::
 
   {\scriptsize
   F^{\flat\flat}
   =
   \eta{\flat\flat} F^{\sharp\flat}
   =
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}^{\flat\flat}
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x} &              & +       B^z  & -        B^y  \\
    +\tilde{E^y} & -       B^z  &              & +        B^x  \\
    +\tilde{E^z} & +       B^y  & -       B^x  &               \\
   \end{bmatrix}^{\sharp\flat}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    -\tilde{E^x} &              & -       B^z  & +        B^y  \\
    -\tilde{E^y} & +       B^z  &              & -        B^x  \\
    -\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}^{\flat\flat}
   }

.. }}}

..rubric:: Covariant-contravariant

.. {{{

.. math::
 
   {\scriptsize
   F^{\flat\sharp}
   =
   F^{\flat\flat} \eta^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    -\tilde{E^x} &              & -       B^z  & +        B^y  \\
    -\tilde{E^y} & +       B^z  &              & -        B^x  \\
    -\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}^{\flat\flat}
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & +\tilde{E^z} \\
    +\tilde{E^x} &              & +       B^z  & -       B^y  \\
    +\tilde{E^y} & -       B^z  &              & +       B^x  \\
    +\tilde{E^z} & +       B^y  & -       B^x  &              \\
   \end{bmatrix}^{\flat\sharp}
   }

.. note::

   Without musical notation, the expression can be explicitely sharpened
   :math:`\sharp` (respectivelty flattened :math:`\flat`) like so:

   .. math::

      \begin{bmatrix}
                    & +\tilde{E^x} & +\tilde{E^y} & +\tilde{E^z} \\
       +\tilde{E^x} &              & +       B^z  & -       B^y  \\
       +\tilde{E^y} & -       B^z  &              & +       B^x  \\
       +\tilde{E^z} & +       B^y  & -       B^x  &               \\
      \end{bmatrix}^{\flat\sharp}
      =
      \begin{bmatrix}
        \begin{bmatrix} \phantom{+X^x} & +\tilde{E^x}   & +\tilde{E^y}   & +\tilde{E^z}   \end{bmatrix} \\
        \begin{bmatrix} +\tilde{E^x}   & \phantom{+X^x} & +       B^z    & -       B^y    \end{bmatrix} \\
        \begin{bmatrix} +\tilde{E^y}   & -       B^z    & \phantom{+X^x} & +       B^x    \end{bmatrix} \\
        \begin{bmatrix} +\tilde{E^z}   & +       B^y    & -       B^x    & \phantom{+X^x} \end{bmatrix} \\
      \end{bmatrix}

.. }}}

Homogenous equations
--------------------

..rubric:: Contravariant-covariant

.. {{{

.. math::

   {\small
   G^{\sharp\flat}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\flat}
   }

.. }}}

.. rubric:: Contravariant-contravariant

.. {{{

.. math::

   {\scriptsize
   G^{\sharp\sharp}
   =
   G^{\sharp\flat} \eta^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\flat}
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & -       B^x  & -       B^y  & -       B^z  \\
    +       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    +       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    +       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\sharp}
   }

.. }}}

.. rubric:: Covariant-covariant

.. {{{

.. warning::

   I have not doubled check that one.

.. math::

   {\scriptsize
   G^{\flat\flat}
   =
   \eta^{\flat\flat} G^{\sharp\flat}
   =
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}^{\flat\flat}
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\flat}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    -       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    -       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    -       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}^{\flat\flat}
   }

.. }}}

..rubric:: Covariant-contravariant

.. {{{

.. warning::

   I have not checked that one.

.. math::

   {\scriptsize
   G^{\flat\sharp}
   =
   G^{\flat\flat} \eta^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    -       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    -       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    -       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}^{\flat\flat}
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\flat\sharp}
   }

.. }}}

The Tensor Formulations
-----------------------

.. {{{

With that, we have obtained all tensor formulations of the Maxwell equations.

The homogenous equations can take one of four equivalent form. The full and
explicit matrix representation in musical notation can be found above. One can
go from one representation to the other by applying the metric tensor.

Contravariant-covariant
'''''''''''''''''''''''

.. math::

   \partial_{\mu} F^\mu{}_\nu = J_{\nu}

.. math::

   \partial_{\mu} G^\mu{}_\nu = 0

Contravariant-contravariant
'''''''''''''''''''''''''''

.. math::

   \partial_{\mu} F^{\mu\nu} = J^{\nu}

.. math::

   \partial_{\mu} G^{\mu\nu} = 0

Covariant-covariant
'''''''''''''''''''

.. math::

   \partial^{\mu} F_{\mu\nu} = J_{\nu}

.. math::

   \partial^{\mu} G_{\mu\nu} = 0

Covariant-contravariant
'''''''''''''''''''''''

.. math::

   \partial^{\mu} F_\mu{}^\nu = J^{\nu}

.. math::

   \partial^{\mu} G_\mu{}^\nu = 0

.. }}}

Explicit formulation of Maxwell equations
-----------------------------------------

.. {{{

Contravariant-covariant
'''''''''''''''''''''''

.. math::

   \begin{bmatrix}
   \partial_t \\
   \partial_x \\
   \partial_y \\
   \partial_z \\
   \end{bmatrix}^{\flat} &
   \begin{bmatrix}
                  & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x}  &              & +       B^z  & -        B^y  \\
    +\tilde{E^y}  & -       B^z  &              & +        B^x  \\
    +\tilde{E^z}  & +       B^y  & -       B^x  &               \\
   \end{bmatrix}^{\sharp\flat}
   =
   \begin{bmatrix}
   + \mu_0 c \rho \\
   - \mu_0 J^x    \\
   - \mu_0 J^y    \\
   - \mu_0 J^z    \\
   \end{bmatrix}^{\flat}

.. math::

   \begin{bmatrix}
   \partial_t \\
   \partial_x \\
   \partial_y \\
   \partial_z
   \end{bmatrix}^{\flat}
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp \flat}
   =
   \begin{bmatrix}
   0 \\
   0 \\
   0 \\
   0 \\
   \end{bmatrix}^{\flat}

Contravariant-contravariant
'''''''''''''''''''''''''''

.. math::

   \begin{bmatrix}
   \partial_t \\
   \partial_x \\
   \partial_y \\
   \partial_z \\
   \end{bmatrix}^{\flat} &
   \begin{bmatrix}
                 & -\tilde{E^x} & -\tilde{E^y} & - \tilde{E^z} \\
    +\tilde{E^x} &              & -       B^z  & +        B^y  \\
    +\tilde{E^y} & +       B^z  &              & -        B^x  \\
    +\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
   \mu_0 c \rho \\
   \mu_0 J^x    \\
   \mu_0 J^y    \\
   \mu_0 J^z    \\
   \end{bmatrix}^{\sharp}

.. math::

   \begin{bmatrix}
   \partial_t \\
   \partial_x \\
   \partial_y \\
   \partial_z \\
   \end{bmatrix}^{\flat}
   \begin{bmatrix}
                 & -       B^x  & -       B^y  & -       B^z  \\
    +       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    +       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    +       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
   0 \\
   0 \\
   0 \\
   0 \\
   \end{bmatrix}^{\sharp}

Covariant-covariant
'''''''''''''''''''

Covariant-contravariant
'''''''''''''''''''''''

.. }}}

Summary
-------

.. {{{

The derivatives are flat and therefore represent a covector with lower indices
in tensor notation :math:`\partial_\mu` While the left-hand side is sharp and
therefore represent a vector with high indices :math:`J^\nu`. The tensors in
the expressions above are necessarily one time contravariant and one time
covariant :math:`F^{\mu\nu}`.

.. math::

   F^{\sharp\flat}
   =
   \begin{bmatrix}
   F^\mu{}_\nu
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x} &              & -       B^z  & +        B^y  \\
    +\tilde{E^y} & +       B^z  &              & -        B^x  \\
    +\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}

.. math::

   G^{\sharp\flat}
   =
   \begin{bmatrix}
   G^\mu{}_\nu
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}

.. math::

   \begin{matrix}
   \partial_{\mu} F^\mu{}_\nu & = & J_{\nu} \\
   \partial_{\mu} G^\mu{}_\nu & = & 0       \\
   \end{matrix}

.. math::

   \begin{matrix}
   \partial^{\flat} F^{\sharp\flat} & = & J^{\flat} \\
   \partial^{\flat} G^{\sharp\flat} & = & 0^{\flat} \\
   \end{matrix}

.. note::

   Recall that :math:`\partial_{\mu} \eta^{\mu \nu}=\partial^{\nu}`. In matrix
   form, this is:

   .. math::

      \begin{bmatrix}
      \partial_t & \partial_x & \partial_y & \partial_z
      \end{bmatrix}
      \begin{bmatrix}
       1 &  0 &  0 &  0 \\
       0 & -1 &  0 &  0 \\
       0 &  0 & -1 &  0 \\
       0 &  0 &  0 & -1
      \end{bmatrix}
      = 
      \begin{bmatrix}
      + \partial_t \\
      - \partial_x \\
      - \partial_y \\
      - \partial_z \\
      \end{bmatrix}

In a next article, I show how the two tensors obtained in that manner are
related as one being the Hodge dual of the other.

.. }}}
