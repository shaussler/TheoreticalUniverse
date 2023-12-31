Deriving the Faraday Tensor from the 1865 Maxwell Equations
===========================================================

.. rst-class:: custom-author

   by Stéphane Haussler

In this article, I present a straightforward and natural derivation of the
electromagnetic field tensor. This derivation draws strong inspiration from
Minkowski's 1908 paper, `The Fundamental Equations for Electromagnetic
Processes in Moving Bodies <https://en.wikisource.org/wiki/Translation:
The_Fundamental_Equations_for_Electromagnetic_Processes_in_Moving_Bodies>`_.
What sets this derivation apart is that it avoids the often-seen backward proof
that the tensor formulation is equivalent to the Maxwell equations. Notably, it
doesn't rely on the widespread vector formulation introduced by Mr. Heaviside,
but rather adheres to the original 1865 formulation by Mr. Maxwell, albeit
presented with modern notation and the benefit of hindsight.

This derivation might not be widely known. If I am mistaken and you are aware
of freely available resources, open an issue and I will include a reference. If
you find mistakes, don't hesitate to open an issue or directly provide
corrections by sending a merge request to my `Github repository
<https://github.com/shaussler/TheoreticalUniverse/>`_.

I assume the reader possesses a strong grasp of vector calculus, including
familiarity with the vector dot and cross products, as well as matrix
multiplication. While an understanding of Maxwell's equations and tensor
calculus certainly can enrich the content, they are not essential to follow
this derivation.

The Vector Formulation of Mr. Heaviside
---------------------------------------

.. {{{

Mr. Maxwell's groundbreaking work in 1865,
`A Dynamical Theory of the Electromagnetic Field
<https://en.m.wikipedia.org/wiki/A_Dynamical_Theory_of_the_Electromagnetic_Field>`_
(`pdf <https://www.jstor.org/stable/108892>`_)
, utilized differential expressions rather than the modern vector formulation
proposed by Mr. Heaviside. Indeed in 1865, the concept of vectors had not yet
been introduced.

`Mr. Heaviside proposed both the concept of vectors as well as the vector form
of the Maxwell equations.
<https://youtu.be/M12CJIuX8D4?si=nuOUEFmRu5Jx4jHJ>`_
This is the most widespread formulation today. I therefore start from there and
unpack into a form closer in spirit to the 1865 equation. The equations consist
of two inhomogenous (Gauss's law and Ampère'circuital law) and two homogenous
vector equations (Gauss's law for magnetism and Faraday's law of induction),
which is how I organize the equations.

While these equations are undoubtedly intriguing, within the context of this
derivation, a deep comprehension of the physics behind them is unnecessary. I
simply present them as the initial basis for the derivation. With the exception
of Maxwell's modification to Ampère's circuital law, these equations represent
the mathematical expression of empirical observations. Therefore, they can be
regarded as established experimental facts.

.. rubric:: Gauss's law

.. math::

   \vect{\nabla} \cdot \vect{E}  = \rho / \epsilon_0


.. rubric:: Ampère's circuital

.. math::

   \vect{\nabla} \times \vect{B}
   = \mu_0 \vect{J} + \frac{1}{c^2} \frac{\partial}{\partial t} \vect{E}

.. rubric:: Gauss's law for magnetism

.. math::

   \vect{\nabla} \cdot \vect{B} = 0

.. rubric:: Faraday's law of induction

.. math::

   \vect{\nabla} \times \vect{E} = -\frac{\partial}{\partial t} \vect{B}

With the electric field :math:`\vect{E}=\{ E^x \\ E^y \\ E^z \}`, magnetic
field :math:`\vect{B}=\{ B^x \\ B^y \\ B^z \}`, and operator
:math:`\vect{\nabla}=\{ \frac{\partial}{\partial x} \\ \frac{\partial}{\partial
y} \\ \frac{\partial}{\partial z} \}`

.. }}}


The Equations of Mr. Maxwell
----------------------------

.. {{{

Unpacking the vector equations into their component form, we obtain in spirit
the 1865 Maxwell formulation, albeit with modern notation and conventions.

.. rubric:: Gauss's law

.. math::

   \frac{\partial}{\partial x} E^x +
   \frac{\partial}{\partial y} E^y +
   \frac{\partial}{\partial z} E^z
   = \rho / \epsilon_0

.. rubric:: Ampère's circuital law

.. math::

    \frac{\partial}{\partial y} B^z - \frac{\partial}{\partial z} B^y
    = \mu_0 J^x + \frac{1}{c^2} \frac{\partial}{\partial t} E^x \\

    \frac{\partial}{\partial z} B^x - \frac{\partial}{\partial x} B^z
    = \mu_0 J^y + \frac{1}{c^2} \frac{\partial}{\partial t} E^y \\

    \frac{\partial}{\partial x} B^y - \frac{\partial}{\partial y} B^x
    = \mu_0 J^z + \frac{1}{c^2} \frac{\partial}{\partial t} E^z

.. rubric:: Gauss's law for magnetism

.. math::

   \frac{\partial}{\partial x} B^x +
   \frac{\partial}{\partial y} B^y +
   \frac{\partial}{\partial z} B^z
   = 0

.. rubric:: Faraday's law of induction

.. math::

    \frac{\partial}{\partial y} E^z - \frac{\partial}{\partial z} E^y
    = - \frac{\partial}{\partial t} B^x \\

    \frac{\partial}{\partial z} E^x - \frac{\partial}{\partial x} E^z
    = - \frac{\partial}{\partial t} B^y \\

    \frac{\partial}{\partial x} E^y - \frac{\partial}{\partial y} E^x
    = - \frac{\partial}{\partial t} B^z \\

.. }}}


The Underlying Structure
------------------------

.. {{{

Gathering and reordering the terms, a clear structures becomes apparent:

.. rubric:: Inhomogenous equations

.. math::

   \begin{matrix}
                                                       &
       +               \frac{\partial E^x}{\partial x} &
       +               \frac{\partial E^y}{\partial y} &
       +               \frac{\partial E^z}{\partial z} &
       = & + \rho/\epsilon_0 \\
       + \frac{1}{c^2} \frac{\partial E^x}{\partial t} &
                                                       &
       -               \frac{\partial B^z}{\partial y} &
       +               \frac{\partial B^y}{\partial z} &
       = & - \mu_0 J^x \\
       + \frac{1}{c^2} \frac{\partial E^y}{\partial t} &
       +               \frac{\partial B^z}{\partial x} &
                                                       &
       -               \frac{\partial B^x}{\partial z} &
       = & - \mu_0 J^y \\
       + \frac{1}{c^2} \frac{\partial E^z}{\partial t} &
       -               \frac{\partial B^y}{\partial x} &
       +               \frac{\partial B^x}{\partial y} &
                                                       &
       = & - \mu_0 J^z \\
   \end{matrix}

.. rubric:: Homogenous equations

.. math::

   \begin{matrix}
                                     &
   + \frac{\partial B^x}{\partial x} &
   + \frac{\partial B^y}{\partial y} &
   + \frac{\partial B^z}{\partial z} &
   = & 0 \\
   + \frac{\partial B^x}{\partial t} &
                                     &
   + \frac{\partial E^z}{\partial y} &
   - \frac{\partial E^y}{\partial z} &
   = & 0 \\
   + \frac{\partial B^y}{\partial t} &
   - \frac{\partial E^z}{\partial x} &
                                     &
   + \frac{\partial E^x}{\partial z} &
   = & 0 \\
   + \frac{\partial B^z}{\partial t} &
   + \frac{\partial E^y}{\partial x} &
   - \frac{\partial E^x}{\partial y} &
                                     &
   = & 0 \\
   \end{matrix}

.. }}}


The Ordered Equations
---------------------

.. {{{

Recognizing the emerging structure, we slightly modify the expressions. These
modifications are not intricate. The objective is merely to present a compact
and symmetrical form, where all terms are aligned.

To eliminate the factor :math:`1/c`, we introduce :math:`\tilde{E^x} = E^x /
c`, :math:`\tilde{E^y} = E^y / c`, and :math:`\tilde{E^z} = E^z / c`.
Additionally, we define for the time dimension :math:`\partial_t =
\frac{\partial}{\partial(ct)}`, and for the spatial dimensions
:math:`\partial_x = \frac{\partial}{\partial x}`, :math:`\partial_y =
\frac{\partial}{\partial y}`, as well as :math:`\partial_z =
\frac{\partial}{\partial z}`. The equations are now:

.. rubric:: Inhomogenous equations

.. math::

   \begin{matrix}
                       & +\partial_x \Ex & +\partial_y \Ey & +\partial_y \Ez & = & + \mu_0 c \rho  \\
       +\partial_t \Ex &                 & -\partial_y \Bz & +\partial_z \By & = & - \mu_0 J^x     \\
       +\partial_t \Ey & +\partial_x \Bz &                 & -\partial_z \Bx & = & - \mu_0 J^y     \\
       +\partial_t \Ez & -\partial_x \By & +\partial_y \Bx &                 & = & - \mu_0 J^z
   \end{matrix}

.. rubric:: Homogenous equations

.. math::

   \begin{matrix}
                       & +\partial_x \Bx & +\partial_y \By & +\partial_z \Bz & = & 0 \\
       +\partial_t \Bx &                 & +\partial_y \Ez & -\partial_z \Ey & = & 0 \\
       +\partial_t \By & -\partial_x \Ez &                 & +\partial_z \Ex & = & 0 \\
       +\partial_t \Bz & +\partial_x \Ey & -\partial_y \Ex &                 & = & 0
   \end{matrix}

For readers well-versed in the tensor formulation of electromagnetism, the
presence and nature of the Faraday tensor and its dual are likely evident.
Moreover, for those acquainted with matrix multiplication principles, it should
be apparent that we can employ matrices operations.

.. note::

   Although beyond our current discussion's scope, defining
   :math:`\partial_\mu` unifies all dimensions to a unit of inverse distance.
   :math:`\frac{1}{c}\frac{\partial}{\partial t}
   =\frac{\partial}{\partial(ct)}` has the units of an inverse distance,
   exactly like the partial derivative with respect to the spatial dimensions
   :math:`\frac{\partial}{\partial x}`, :math:`\frac{\partial}{\partial y}`,
   and :math:`\frac{\partial}{\partial z}`.

.. note::

   The experimental relation between the speed of light :math:`c`, the
   permittivity of free space :math:`\epsilon_0`, and and the permeability of
   free space :math:`\mu_0` is used:

   .. math::

      c=\frac{1}{\sqrt{\epsilon_0 \mu_0}}

.. }}}


The Tensor of Mr. Faraday
-------------------------

.. {{{


From matrix multiplication rules, we deduct the ordered equations are
equivalent to:

.. math::

   \begin{bmatrix}
       \partial_t & \partial_x & \partial_y & \partial_z \\
   \end{bmatrix}
   \begin{bmatrix}
            & +\Ex & +\Ey & +\Ez \\
       +\Ex &      & +\Bz & -\By \\
       +\Ey & -\Bz &      & +\Bx \\
       +\Ez & +\By & -\Bx &      \\
   \end{bmatrix}
   =
   \begin{bmatrix}
       + \mu_0 c \rho & - \mu_0 J^x  & - \mu_0 J^y  & - \mu_0 J^z \\
   \end{bmatrix}

.. math::

   \begin{bmatrix}
       \partial_t & \partial_x & \partial_y & \partial_z \\
   \end{bmatrix}
   \begin{bmatrix}
            & +\Bx & +\By & +\Bz \\
       +\Bx &      & -\Ez & +\Ey \\
       +\By & +\Ez &      & -\Ex \\
       +\Bz & -\Ey & +\Ex &      \\
   \end{bmatrix}
   =
   \begin{bmatrix}
       0 & 0 & 0 & 0 \\
   \end{bmatrix}

We have thus obtained the Faraday tensor (inhomogenous equations) and its dual
(homogenous equations).

.. }}}


The Tensor Equations
--------------------

.. {{{

The flat left hand side is a covector, which we note in tensor notation with
lower indices :math:`\partial_\mu`. The right hand side is also flat and
therefore is a covector :math:`J_\nu`. The rank 2 tensors in the expressions
are necessarily one time contravariant and one time covariant. We multiply each
column of :math:`\partial` with each row of :math:`F`, and repeat for all
columns of :math:`F`. With the first index of :math:`F` being the row
:math:`\mu`, and :math:`\nu`, this means :math:`\partial_\mu F^\mu{}_\nu`. We
then write in tensor notation :math:`F^\mu{}_\nu` for the Faraday tensor, and
:math:`G^\mu{}_\nu` for its dual:

.. math::

   \{ F^\mu{}_\nu \}
   =
   \begin{bmatrix}
            & +\Ex & +\Ey & +\Ez \\
       +\Ex &      & +\Bz & -\By \\
       +\Ey & -\Bz &      & +\Bx \\
       +\Ez & +\By & -\Bx &      \\
   \end{bmatrix}

.. math::

   \{ G^\mu{}_\nu \}
   =
   \begin{bmatrix}
             & +\Bx & +\By & +\Bz \\
       +\Bx  &      & -\Ez & +\Ey \\
       +\By  & +\Ez &      & -\Ex \\
       +\Bz  & -\Ey & +\Ex &      \\
   \end{bmatrix}

Maxwell's equations are then:

.. math::

   \partial_{\mu} F^\mu{}_\nu & = J_{\nu} \\
   \partial_{\mu} G^\mu{}_\nu & = 0

To double-check the result, you can have a look at `this alternative derivation
of the mixed electromagnetic tensor
<https://www.wikihow.life/Derive-the-Faraday-Tensor>`_.

.. }}}
