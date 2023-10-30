Deriving the Faraday Tensor from the 1865 Maxwell Equations
===========================================================

In this article, I present a simple and elegant derivation of the
Faraday tensor. This derivation is strongly inspired by Minkowski's
1908 paper:
`The Fundamental Equations for Electromagnetic Processes in Moving
Bodies
<https://en.wikisource.org/wiki/Translation:The_Fundamental_Equations_for_Electromagnetic_Processes_in_Moving_Bodies>`_.

You may find the derivation obvious, but I do not think it is well known and I
have not seen it anywhere. If I am mistaken and you know of a textbook, youtube
video, article, or some place in the internet, please let me know and I will
add a reference. You can open an issue or directly correct and send a merge
request on my `github repository
<https://github.com/shaussler/electromagnetism/actions/runs/6444649784>`_.

Mr. Maxwell published in 1865 `A Dynamical Theory of the Electromagnetic Field
<https://en.m.wikipedia.org/wiki/A_Dynamical_Theory_of_the_Electromagnetic_Field>`_
(`pdf <https://www.jstor.org/stable/108892>`_).
The original formulation uses differential expressions, as opposed to the
modern vector formulation proposed by Mr. Heaviside. There was no concept of
vectors in 1865.

The Vector Formulation of Mr. Heaviside
---------------------------------------

Mr. Heaviside proposed the vector form of the Maxwell equations which is the
most widespread formulation today. I therefore start from there and unpack into
a form closer in spirit to the 1865 maxwell equation. The equations consist of
two inhomogenous vector equations (Gauss's law and Ampere's circuital law with
Maxwell addition):

.. math::

   \begin{align}
   \overrightarrow{\nabla} \cdot \overrightarrow{E} &= \rho / \epsilon_0 \\
   \overrightarrow{\nabla} \times \overrightarrow{B} &= \mu_0 \overrightarrow{J} + \frac{1}{c^2} \frac{\partial}{\partial t} \overrightarrow{E} \\
   \end{align}

As well as two homogenous equations (Gauss's law for magnetism and Faraday's law of induction):

.. math::

   \begin{align}
   \overrightarrow{\nabla} \cdot \overrightarrow{B} &= 0 \\
   \overrightarrow{\nabla} \times \overrightarrow{E} &= \frac{\partial}{\partial t} \overrightarrow{B} \\
   \end{align}

Unpacking the vector equations into their component form, we obtain in spirit
the 1865 Maxwell formulation, albeit with modern notation and conventions:

.. note::

   With the electric field
   :math:`\overrightarrow{E}=\begin{bmatrix} E^x \\ E^y \\ E^z \end{bmatrix}`,
   magnetic field
   :math:`\overrightarrow{B}=\begin{bmatrix} B^x \\ B^y \\ B^z \end{bmatrix}`, and operator
   :math:`\overrightarrow{\nabla}=\begin{bmatrix} \frac{\partial}{\partial x} \\ \frac{\partial}{\partial y} \\ \frac{\partial}{\partial z} \end{bmatrix}`

The Equations of Mr. Maxwell
----------------------------

**Inhomogenous equations**

Gauss's law

.. math::

   \begin{align}
   \frac{\partial}{\partial x} E^x + \frac{\partial}{\partial y} E^y + \frac{\partial}{\partial z} E^z &= \rho / \epsilon_0
   \end{align}

Ampere's circuital law

.. math::

   \begin{align}
   \frac{\partial}{\partial y} B^z - \frac{\partial}{\partial z} B^y &= \mu_0 J^x + \frac{1}{c^2} \frac{\partial}{\partial t} E^x \\
   \frac{\partial}{\partial z} B^x - \frac{\partial}{\partial x} B^z &= \mu_0 J^y + \frac{1}{c^2} \frac{\partial}{\partial t} E^y \\
   \frac{\partial}{\partial x} B^y - \frac{\partial}{\partial y} B^x &= \mu_0 J^z + \frac{1}{c^2} \frac{\partial}{\partial t} E^z \\
   \end{align}

**Homogenous equations**

Gauss's law for magnetism

.. math::

   \begin{align}
   \frac{\partial}{\partial x} B^x + \frac{\partial}{\partial y} B^y + \frac{\partial}{\partial z} B^z &= 0
   \end{align}

Faraday's law of induction

.. math::

   \begin{align}
   \frac{\partial}{\partial y} E^z - \frac{\partial}{\partial z} E^y &= - \frac{\partial}{\partial t} B^x \\
   \frac{\partial}{\partial z} E^x - \frac{\partial}{\partial x} E^z &= - \frac{\partial}{\partial t} B^y \\
   \frac{\partial}{\partial x} E^y - \frac{\partial}{\partial y} E^x &= - \frac{\partial}{\partial t} B^z \\
   \end{align}

The underlying structure of the equations
-----------------------------------------

Reordering the terms, a clear structures appear:

**Inhomogenous equations**

.. math::

   \begin{matrix}
                                                    & + \frac{\partial E^x}{\partial x} & + \frac{\partial E^y}{\partial_y} & + \frac{\partial E^z}{\partial z} & = & + \rho/\epsilon_0 \\
    + \frac{1}{c^2} \frac{\partial E^x}{\partial t} &                                   & - \frac{\partial B^z}{\partial_y} & + \frac{\partial B^y}{\partial z} & = & - \mu_0 J^x       \\
    + \frac{1}{c^2} \frac{\partial E^y}{\partial t} & + \frac{\partial B^z}{\partial x} &                                   & - \frac{\partial B^x}{\partial z} & = & - \mu_0 J^y       \\
    + \frac{1}{c^2} \frac{\partial E^z}{\partial t} & - \frac{\partial B^y}{\partial x} & + \frac{\partial B^x}{\partial y} &                                   & = & - \mu_0 J^z       \\
   \end{matrix}

**Homogenous equations**

.. math::

   \begin{matrix}
                                      & + \frac{\partial B^x}{\partial x} & + \frac{\partial B^y}{\partial_y} & + \frac{\partial B^z}{\partial z} & = & 0 \\
    + \frac{\partial B^x}{\partial t} &                                   & + \frac{\partial E^z}{\partial_y} & - \frac{\partial E^y}{\partial z} & = & 0 \\
    + \frac{\partial B^y}{\partial t} & - \frac{\partial E^z}{\partial x} &                                   & + \frac{\partial E^x}{\partial z} & = & 0 \\
    + \frac{\partial B^z}{\partial t} & + \frac{\partial E^y}{\partial x} & - \frac{\partial E^x}{\partial y} &                                   & = & 0 \\
   \end{matrix}

Reordered form
--------------

To take advantage of the structure, we see after a bit of struggle that the form is very nice when taking:

.. math::

   \begin{cases}
   \partial_t  &=& \frac{\partial}{\partial(ct)} \\
   \partial_x  &=& \frac{\partial}{\partial x}   \\
   \partial_y  &=& \frac{\partial}{\partial y}   \\
   \partial_z  &=& \frac{\partial}{\partial z}   \\
   \end{cases}

As well as:

.. math::

   \begin{cases}
   \tilde{E^x} &=& \frac{E^x}{c} \\
   \tilde{E^y} &=& \frac{E^y}{c} \\
   \tilde{E^z} &=& \frac{E^z}{c} \\
   \end{cases}

.. note::

   I also use :math:`c=\frac{1}{\sqrt{\epsilon_0 \mu_0}}` to get the constants right.

.. note::

   :math:`\frac{1}{c}\frac{\partial}{\partial t} =\frac{\partial}{\partial(ct)}`
   has the units of an inverse distance, exactly
   like the partial derivative with respect to the spatial dimensions
   :math:`\frac{\partial}{\partial x}, :math:`\frac{\partial}{\partial y}, and
   :math:`\frac{\partial}{\partial z}.

**Inhomogenous equations**

.. math::

   \begin{matrix}
                            & +\partial_x \tilde{E^x} & +\partial_y \tilde{E^y} & +\partial_y \tilde{E^z} & = & + \mu_0 c \rho  \\
    +\partial_t \tilde{E^x} &                         & +\partial_y        B^z  & -\partial_z        B^y  & = & - \mu_0 J^x     \\
    +\partial_t \tilde{E^y} & +\partial_x        B^z  &                         & -\partial_z        B^x  & = & - \mu_0 J^y     \\
    +\partial_t \tilde{E^z} & -\partial_x        B^y  & +\partial_y        B^x  &                         & = & - \mu_0 J^z     \\
   \end{matrix}

**Homogenous equations**

.. math::

   \begin{matrix}
                            & +\partial_x        B^x  & +\partial_y        B^y  & +\partial_z        B^z  & = & 0 \\
    +\partial_t        B^x  &                         & +\partial_y \tilde{E^z} & -\partial_z \tilde{E^y} & = & 0 \\
    +\partial_t        B^y  & -\partial_x \tilde{E^z} &                         & +\partial_z \tilde{E^x} & = & 0 \\
    +\partial_t        B^z  & +\partial_x \tilde{E^y} & -\partial_y \tilde{E^x} &                         & = & 0 \\
   \end{matrix}

Now the structure of the equations is obvious and we obtain in Matrix form:

.. math::

   \begin{bmatrix}
   \partial_t & \partial_x & \partial_y & \partial_z
   \end{bmatrix}
   \begin{bmatrix}
                 & +\tilde{E^x} & +\tilde{E^y} & + \tilde{E^z} \\
    +\tilde{E^x} &              & +       B^z  & -        B^y  \\
    +\tilde{E^y} & +       B^z  &              & -        B^x  \\
    +\tilde{E^z} & -       B^y  & +       B^x  &               \\
   \end{bmatrix}
   =
   \begin{bmatrix}
   + \mu_0 c \rho \\
   - \mu_0 J^x    \\
   - \mu_0 J^y    \\
   - \mu_0 J^z    \\
   \end{bmatrix}

.. math::

   \begin{bmatrix}
   \partial_t & \partial_x & \partial_y & \partial_z
   \end{bmatrix}
   \begin{bmatrix}
                 & +       B^x  & +       B^y  & +       B^z  \\
    +       B^x  &              & +\tilde{E^z} & -\tilde{E^y} \\
    +       B^y  & -\tilde{E^z} &              & +\tilde{E^x} \\
    +       B^z  & +\tilde{E^y} & -\tilde{E^x} &              \\
   \end{bmatrix}
   =
   \begin{bmatrix}
   0 \\
   0 \\
   0 \\
   0 \\
   \end{bmatrix}

Where the tensor form is also revealed:

.. math::

   \begin{matrix}
   \partial_{\mu} F^{\mu \nu} & = & J^{\nu} \\
   \partial_{\mu} G^{\mu \nu} & = & 0       \\
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

