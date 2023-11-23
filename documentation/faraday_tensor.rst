Deriving the Faraday Tensors from the 1865 Maxwell Equations
============================================================

In this article, I present a straightforward and elegant derivation of the
Faraday tensor. This derivation draws strong inspiration from Minkowski's 1908
paper, 
`The Fundamental Equations for Electromagnetic Processes in Moving Bodies
<https://en.wikisource.org/wiki/Translation:The_Fundamental_Equations_for_Electromagnetic_Processes_in_Moving_Bodies>`_.
What sets this derivation apart is that it avoids the often-seen backward proof
that the tensor formulation is equivalent to the Maxwell equations. Notably, it
doesn't rely on the widespread vector formulation introduced by Mr. Heaviside,
but rather adheres to the original 1865 formulation by Mr. Maxwell, albeit
presented with modern notation and the benefit of hindsight.

While the derivation may seem quite obvious, it might not be widely known. If I
am mistaken, and you are aware of a textbook, YouTube video, article, or any
other online resource covering this topic, please don't hesitate to inform me.
You can either open an issue or directly provide corrections by sending a merge
request to my
`Github repository
<https://github.com/shaussler/electromagnetism/actions/runs/6444649784>`_.

The Vector Formulation of Mr. Heaviside
---------------------------------------

Mr. Maxwell's groundbreaking work in 1865,
`A Dynamical Theory of the Electromagnetic Field
<https://en.m.wikipedia.org/wiki/A_Dynamical_Theory_of_the_Electromagnetic_Field>`_
(`pdf <https://www.jstor.org/stable/108892>`_)
, utilized differential expressions rather than the modern vector formulation
proposed by Mr. Heaviside. It's essential to note that in 1865, the concept of
vectors had not yet been introduced.

Mr. Heaviside proposed the vector form of the Maxwell equations which is the
most widespread formulation today. I therefore start from there and unpack into
a form closer in spirit to the 1865 maxwell equation. The equations consist of
two inhomogenous and two homogenous vector equations:

Inhomogenous equations
''''''''''''''''''''''

**Gauss's law**

.. math::

   \overrightarrow{\nabla} \cdot \overrightarrow{E}  &= \rho / \epsilon_0 \\

**Ampère's circuital law with Maxwell addition**

.. math::

   \overrightarrow{\nabla} \times \overrightarrow{B} &= \mu_0 \overrightarrow{J} + \frac{1}{c^2} \frac{\partial}{\partial t} \overrightarrow{E} \\

Homogenous equations
''''''''''''''''''''

As well as two homogenous equations:

**Gauss's law for magnetism**

.. math::

   \overrightarrow{\nabla} \cdot \overrightarrow{B}  &= 0 \\

**Faraday's law of induction**

.. math::

   \overrightarrow{\nabla} \times \overrightarrow{E} &= \frac{\partial}{\partial t} \overrightarrow{B} \\

From there, the equations often are unpacked. In the following, I will argue
that in lots of sense, the original Maxwell equations from 1865 result in a
more *computable* representation.

.. note::

   With the electric field
   :math:`\overrightarrow{E}=\begin{bmatrix} E^x \\ E^y \\ E^z \end{bmatrix}`,
   magnetic field
   :math:`\overrightarrow{B}=\begin{bmatrix} B^x \\ B^y \\ B^z \end{bmatrix}`, and operator
   :math:`\overrightarrow{\nabla}=\begin{bmatrix} \frac{\partial}{\partial x} \\ \frac{\partial}{\partial y} \\ \frac{\partial}{\partial z} \end{bmatrix}`

The Equations of Mr. Maxwell
----------------------------

Unpacking the vector equations into their component form, we obtain in spirit
the 1865 Maxwell formulation, albeit with modern notation and conventions.

Inhomogenous equations
''''''''''''''''''''''

**Gauss's law**

.. math::

   \begin{align}
   \frac{\partial}{\partial x} E^x + \frac{\partial}{\partial y} E^y + \frac{\partial}{\partial z} E^z &= \rho / \epsilon_0
   \end{align}

**Ampère's circuital law**

.. math::

   \begin{align}
   \frac{\partial}{\partial y} B^z - \frac{\partial}{\partial z} B^y &= \mu_0 J^x + \frac{1}{c^2} \frac{\partial}{\partial t} E^x \\
   \frac{\partial}{\partial z} B^x - \frac{\partial}{\partial x} B^z &= \mu_0 J^y + \frac{1}{c^2} \frac{\partial}{\partial t} E^y \\
   \frac{\partial}{\partial x} B^y - \frac{\partial}{\partial y} B^x &= \mu_0 J^z + \frac{1}{c^2} \frac{\partial}{\partial t} E^z \\
   \end{align}

Homogenous equations
''''''''''''''''''''

**Gauss's law for magnetism**

.. math::

   \begin{align}
   \frac{\partial}{\partial x} B^x + \frac{\partial}{\partial y} B^y + \frac{\partial}{\partial z} B^z &= 0
   \end{align}

**Faraday's law of induction**

.. math::

   \begin{align}
   \frac{\partial}{\partial y} E^z - \frac{\partial}{\partial z} E^y &= - \frac{\partial}{\partial t} B^x \\
   \frac{\partial}{\partial z} E^x - \frac{\partial}{\partial x} E^z &= - \frac{\partial}{\partial t} B^y \\
   \frac{\partial}{\partial x} E^y - \frac{\partial}{\partial y} E^x &= - \frac{\partial}{\partial t} B^z \\
   \end{align}

The underlying structure
------------------------

Reordering the terms, a clear structures appear:

Inhomogenous equations
''''''''''''''''''''''

.. math::

   \begin{matrix}
                                                    & + \frac{\partial E^x}{\partial x} & + \frac{\partial E^y}{\partial y} & + \frac{\partial E^z}{\partial z} & = & + \rho/\epsilon_0 \\
    + \frac{1}{c^2} \frac{\partial E^x}{\partial t} &                                   & - \frac{\partial B^z}{\partial y} & + \frac{\partial B^y}{\partial z} & = & - \mu_0 J^x       \\
    + \frac{1}{c^2} \frac{\partial E^y}{\partial t} & + \frac{\partial B^z}{\partial x} &                                   & - \frac{\partial B^x}{\partial z} & = & - \mu_0 J^y       \\
    + \frac{1}{c^2} \frac{\partial E^z}{\partial t} & - \frac{\partial B^y}{\partial x} & + \frac{\partial B^x}{\partial y} &                                   & = & - \mu_0 J^z       \\
   \end{matrix}

Homogenous equations
''''''''''''''''''''

.. math::

   \begin{matrix}
                                      & + \frac{\partial B^x}{\partial x} & + \frac{\partial B^y}{\partial y} & + \frac{\partial B^z}{\partial z} & = & 0 \\
    + \frac{\partial B^x}{\partial t} &                                   & + \frac{\partial E^z}{\partial y} & - \frac{\partial E^y}{\partial z} & = & 0 \\
    + \frac{\partial B^y}{\partial t} & - \frac{\partial E^z}{\partial x} &                                   & + \frac{\partial E^x}{\partial z} & = & 0 \\
    + \frac{\partial B^z}{\partial t} & + \frac{\partial E^y}{\partial x} & - \frac{\partial E^x}{\partial y} &                                   & = & 0 \\
   \end{matrix}

The ordered equations
---------------------

To take advantage of the structure, we can use what at first sight may be
considered sytaxing sugar (and to some extent is). We define
:math:`\partial_t`, :math:`\partial_x`, :math:`\partial_y`:math:`\partial_z`:

.. math::

   {\small
   \begin{matrix}
   \partial_t  &=& \frac{\partial}{\partial(ct)} \\
   \partial_x  &=& \frac{\partial}{\partial x}   \\
   \partial_y  &=& \frac{\partial}{\partial y}   \\
   \partial_z  &=& \frac{\partial}{\partial z}   \\
   \end{matrix}
   }

To avoid taking with us a :math:`\frac{1}{c}`, we also define:

.. math::

   {\small
   \begin{matrix}
   \tilde{E^x} &= \frac{E^x}{c} \\
   \tilde{E^y} &= \frac{E^y}{c} \\
   \tilde{E^z} &= \frac{E^z}{c} \\
   \end{matrix}
   }

.. note::

   :math:`\frac{1}{c}\frac{\partial}{\partial t} =\frac{\partial}{\partial(ct)}`
   has the units of an inverse distance, exactly
   like the partial derivative with respect to the spatial dimensions
   :math:`\frac{\partial}{\partial x}`, :math:`\frac{\partial}{\partial y}`, and
   :math:`\frac{\partial}{\partial z}`.

.. note::

   The experimental relation between the speed of light :math:`c`, the
   permittivity of free space :math:`\epsilon_0`, and and the permeability of
   free space :math:`\mu_0` is used:

   .. math::

      c=\frac{1}{\sqrt{\epsilon_0 \mu_0}}

But really there is nothing involved at that step. The goal is to write the
Maxwell equations in the most pleasant form possible. And pleasant in the form
the equations are.

Inhomogenous equations
''''''''''''''''''''''

.. math::

   \begin{matrix}
                            & +\partial_x \tilde{E^x} & +\partial_y \tilde{E^y} & +\partial_y \tilde{E^z} & = & + \mu_0 c \rho  \\
    +\partial_t \tilde{E^x} &                         & -\partial_y        B^z  & +\partial_z        B^y  & = & - \mu_0 J^x     \\
    +\partial_t \tilde{E^y} & +\partial_x        B^z  &                         & -\partial_z        B^x  & = & - \mu_0 J^y     \\
    +\partial_t \tilde{E^z} & -\partial_x        B^y  & +\partial_y        B^x  &                         & = & - \mu_0 J^z     \\
   \end{matrix}

Homogenous equations
''''''''''''''''''''

.. math::

   \begin{matrix}
                            & +\partial_x        B^x  & +\partial_y        B^y  & +\partial_z        B^z  & = & 0 \\
    +\partial_t        B^x  &                         & +\partial_y \tilde{E^z} & -\partial_z \tilde{E^y} & = & 0 \\
    +\partial_t        B^y  & -\partial_x \tilde{E^z} &                         & +\partial_z \tilde{E^x} & = & 0 \\
    +\partial_t        B^z  & +\partial_x \tilde{E^y} & -\partial_y \tilde{E^x} &                         & = & 0 \\
   \end{matrix}

It should be already clear to readers already familiar with the tensor
formulation of electromagnetism that the Faraday tensor as well as its dual are
already fully apparent. For any reader familiar with Matrix multiplications
rules, it should also be clear at this stage that we are dealing here with the
application of covectors to matrices.

The electromagnetic tensor
--------------------------

Now the structure of the equations is obvious and we obtain in Matrix form
where musical notation is used for compactness.

Inhomogenous equations
''''''''''''''''''''''

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


Homogenous equations
''''''''''''''''''''

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

.. note::

   The musical notation here is to explicitely declare whether we are dealing
   with a sharp :math:`\sharp` vector or a :math:`\flat` covector

   .. math::

        \begin{matrix}
            v^{\sharp}=
            \begin{bmatrix}
            a \\
            b
            \end{bmatrix}
        ,&
            v^{\flat}=
            \begin{bmatrix}
            a & b
            \end{bmatrix}
        \end{matrix}

   For all practical purposes, a covector is merely the
   transpose of a vector :math:`\begin{bmatrix} a & b
   \end{bmatrix}=\begin{bmatrix} a \\ b \end{bmatrix}^T`.

   For the matrices, it permits to explicitely define if we are dealing with
   rows of columns, columns of rows, rows of rows, or columns of columns. 

.. note::
    
   An alternative to the musical notation is to explicitely sharpen
   :math:`\sharp` or flatten :math:`\flat` the vectors. The equations then take
   this form which is strictly equivalent.

   .. math::
    
      {\small
      \begin{bmatrix}
      \partial_t     & \partial_x   & \partial_y   & \partial_z    \\
      \end{bmatrix}
      \begin{bmatrix}
          \begin{bmatrix}
                       \\
          +\tilde{E^x} \\
          +\tilde{E^y} \\
          +\tilde{E^z} \\
          \end{bmatrix}
          \begin{bmatrix}
          +\tilde{E^x} \\
                       \\
          -       B^z  \\
          +       B^y  \\
          \end{bmatrix}
          \begin{bmatrix}
          +\tilde{E^y} \\
          +       B_z  \\
                       \\
          -       B^x  \\
          \end{bmatrix}
          \begin{bmatrix}
          +\tilde{E^z} \\
          -       B^y  \\
          +       B^x  \\
                       \\
          \end{bmatrix}
      \end{bmatrix}
      =
      \begin{bmatrix}
      + \mu_0 c \rho & - \mu_0 J^x  & - \mu_0 J^y  & - \mu_0 J^z   \\
      \end{bmatrix}
      }

   .. math::
    
      {\small
      \begin{bmatrix}
      \partial_t     & \partial_x   & \partial_y   & \partial_z    \\
      \end{bmatrix}
      \begin{bmatrix}
          \begin{bmatrix}
                       \\
          +\tilde{B^x} \\
          +\tilde{B^y} \\
          +\tilde{B^z} \\
          \end{bmatrix}
          \begin{bmatrix}
          +\tilde{B^x} \\
                       \\
          +       E^z  \\
          -       E^y  \\
          \end{bmatrix}
          \begin{bmatrix}
          +\tilde{B^y} \\
          -       E_z  \\
                       \\
          +       E^x  \\
          \end{bmatrix}
          \begin{bmatrix}
          +\tilde{B^z} \\
          +       E^y  \\
          -       E^x  \\
                       \\
          \end{bmatrix}
      \end{bmatrix}
      =
      \begin{bmatrix}
      0 & 0 & 0 & 0 \\
      \end{bmatrix}
      }

The Faraday Tensors
-------------------

Inhomogenous equations
''''''''''''''''''''''

.. math::

   {\small
   F^{\sharp\flat}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x} &              & -       B^z  & +        B^y  \\
    +\tilde{E^y} & +       B^z  &              & -        B^x  \\
    +\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}^{\sharp\flat}
   }

From there, we can obtain all other forms of the Faraday tensors by applying
the Minkowski metric:

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
   \end{bmatrix}
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x} &              & +       B^z  & -        B^y  \\
    +\tilde{E^y} & -       B^z  &              & +        B^x  \\
    +\tilde{E^z} & +       B^y  & -       B^x  &               \\
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    -\tilde{E^x} &              & -       B^z  & +        B^y  \\
    -\tilde{E^y} & +       B^z  &              & -        B^x  \\
    -\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}
   }

.. math::
 
   {\scriptsize
   F^{\flat\sharp}
   =
   F^{\flat\flat} \eta
   =
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    -\tilde{E^x} &              & -       B^z  & +        B^y  \\
    -\tilde{E^y} & +       B^z  &              & -        B^x  \\
    -\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & -\tilde{E^x} & -\tilde{E^y} & - \tilde{E^z} \\
    -\tilde{E^x} &              & +       B^z  & -        B^y  \\
    -\tilde{E^y} & -       B^z  &              & +        B^x  \\
    -\tilde{E^z} & +       B^y  & -       B^x  &               \\
   \end{bmatrix}
   }

Homogenous equations
''''''''''''''''''''

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

.. math::

   {\small
   G^{\sharp\sharp}
   =
   G^{\sharp\flat} \eta
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & -       B^x  & -       B^y  & -       B^z  \\
    +       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    +       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    +       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}
   }

.. math::

   {\small
   G^{\flat\flat}
   =
   \eta G^{\sharp\flat}
   =
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    -       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    -       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    -       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}
   }

.. math::

   {\small
   G^{\flat\sharp}
   =
   \eta G^{\flat\flat}
   =
   \begin{bmatrix}
    1 &  0 &  0 &  0 \\
    0 & -1 &  0 &  0 \\
    0 &  0 & -1 &  0 \\
    0 &  0 &  0 & -1
   \end{bmatrix}
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    -       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    -       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    -       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}
   =
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & -\tilde{E^z} & +\tilde{E^y} \\
    +       B^y  & +\tilde{E^z} &              & -\tilde{E^x} \\
    +       B^z  & -\tilde{E^y} & +\tilde{E^x} &              \\
   \end{bmatrix}
   }

The Tensor Formulations
-----------------------

With that, we have obtained all tensor formulations of the Maxwell equations.

Inhomogenous equations
''''''''''''''''''''''

The homogenous equations can take one of four equivalent form. The full and
explicit matrix representation in musical notation can be found above. One can
go from one representation to the other by applying the metric tensor.

.. math::

   \partial_{\mu} F^\mu{}_\nu = J_{\nu}

.. math::

   \partial_{\mu} F^{\mu\nu} = J^{\nu}

.. math::

   \partial^{\mu} F_{\mu\nu} = J_{\nu}

.. math::

   \partial^{\mu} F_\mu{}^\nu = J^{\nu}

Homogenous equations
''''''''''''''''''''

The exact same can be done

.. math::

   \partial_{\mu} G^\mu{}_\nu = 0

.. math::

   \partial_{\mu} G^{\mu\nu} = 0

.. math::

   \partial^{\mu} G_{\mu\nu} = 0

.. math::

   \partial^{\mu} G_\mu{}^\nu = 0

Summary
-------

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

