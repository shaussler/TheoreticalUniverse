.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _deriving_the_faraday_tensor_from_the_1865_maxwell_equations:
.. _deriving the Faraday tensor from the 1865 Maxwell equations:
.. _deriving the Faraday tensor from the 1865 Maxwell's equations:
.. _faraday tensor derivation:

Deriving the Faraday tensor from the 1865 Maxwell's equations
=============================================================

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

This page stands alone and can be understood without referencing other content
on this site. I assume the reader possesses a strong grasp of vector calculus,
including familiarity with the vector dot and cross products, as well as matrix
multiplication. While an understanding of Maxwell's equations and tensor
calculus certainly can enrich the content, they are not essential to follow
this derivation.

.. _vector_formulation_of_mr_heaviside:

Vector formulation of Mr. Heaviside
-----------------------------------

.. {{{

Mr. Maxwell's groundbreaking work in 1865, `A Dynamical Theory of the
Electromagnetic Field
<https://en.m.wikipedia.org/wiki/A_Dynamical_Theory_of_the_Electromagnetic_Field>`_
(`pdf <https://www.jstor.org/stable/108892>`_), utilized differential
expressions rather than the modern vector formulation proposed by Mr. Heaviside.
Indeed in 1865, the concept of vectors had not yet been introduced.

`Mr. Heaviside proposed both the concept of vectors as well as the vector form
of the Maxwell equations. <https://youtu.be/M12CJIuX8D4?si=nuOUEFmRu5Jx4jHJ>`_
This is the most widespread formulation today. I therefore start from there and
unpack into a form closer in spirit to the 1865 equation. The equations consist
of two inhomogeneous (Gauss's law and Ampère'circuital law) and two homogeneous
vector equations (Gauss's law for magnetism and Faraday's law of induction),
which is how I organize the equations.

While these equations are undoubtedly intriguing, within the context of this
derivation, a deep comprehension of the physics behind them is unnecessary. I
simply present them as the initial basis for the derivation. With the exception
of Maxwell's modification to Ampère's circuital law, these equations represent
the mathematical expression of empirical observations. Therefore, they can be
regarded as established experimental facts.

.. rubric:: Gauss's Law

.. math::

   \overrightarrow{∇} \cdot \overrightarrow{E}  = ρ / ε_0

.. rubric:: Ampère's Circuital Law

.. math::

   \overrightarrow{∇} \times \overrightarrow{B} =
   μ_0 \overrightarrow{J} + \frac{1}{c^2} \frac{∂}{∂t} \overrightarrow{E}

.. rubric:: Faraday's law of induction

.. math::

   \overrightarrow{∇} ⨯ \overrightarrow{E} = -\frac{∂}{∂t} \overrightarrow{B}

.. rubric:: Gauss's Law for Magnetism

.. math::

   \overrightarrow{∇} \cdot \overrightarrow{B} = 0

With the electric field :math:`\overrightarrow{E} = \begin{bmatrix} E^x \\ E^y
\\ E^z \end{bmatrix}`, magnetic field :math:`\overrightarrow{B} =
\begin{bmatrix} B^x \\ B^y \\ B^z \end{bmatrix}`, and operator
:math:`\overrightarrow{∇} = \begin{bmatrix} \frac{∂}{∂x} \\ \frac{∂}{∂y} \\
\frac{∂}{∂z} \end{bmatrix}`

.. }}}

The equations of Mr. Maxwell
----------------------------

.. {{{

Unpacking the vector equations into their component form, we obtain in spirit
the 1865 Maxwell formulation, albeit with modern notation and conventions.

.. rubric:: Gauss's Law

.. math::

   \frac{∂}{∂x} E^x + \frac{∂}{∂y} E^y + \frac{∂}{∂z} E^z = ρ / ε_0

.. rubric:: Ampère's Circuital Law

.. math::

   \frac{∂}{∂y} B^z - \frac{∂}{∂z} B^y = μ_0 J^x + \frac{1}{c^2} \frac{∂}{∂t} E^x \\
   \frac{∂}{∂z} B^x - \frac{∂}{∂x} B^z = μ_0 J^y + \frac{1}{c^2} \frac{∂}{∂t} E^y \\
   \frac{∂}{∂x} B^y - \frac{∂}{∂y} B^x = μ_0 J^z + \frac{1}{c^2} \frac{∂}{∂t} E^z \\

.. rubric:: Gauss's Law for Magnetism

.. math::

   \frac{∂}{∂x} B^x + \frac{∂}{∂y} B^y + \frac{∂}{∂z} B^z = 0

.. rubric:: Faraday's Law of Induction

.. math::

   \frac{∂}{∂y} E^z - \frac{∂}{∂z} E^y = - \frac{∂}{∂t} B^x \\
   \frac{∂}{∂z} E^x - \frac{∂}{∂x} E^z = - \frac{∂}{∂t} B^y \\
   \frac{∂}{∂x} E^y - \frac{∂}{∂y} E^x = - \frac{∂}{∂t} B^z \\

.. }}}

Underlying structure
--------------------

.. {{{

Gathering and reordering the terms, a clear structures becomes apparent:

.. rubric:: Inhomogenous equations: Gauss's law and Ampère's circuital law

.. math::

   \begin{alignedat}{4}
                                       & + \frac{∂E^x}{∂x} & + \frac{∂E^y}{∂y} & + \frac{∂E^z}{∂z} & = + ρ/ε_0   \\
       + \frac{1}{c^2} \frac{∂E^x}{∂t} &                   & - \frac{∂B^z}{∂y} & + \frac{∂B^y}{∂z} & = - μ_0 J^x \\
       + \frac{1}{c^2} \frac{∂E^y}{∂t} & + \frac{∂B^z}{∂x} &                   & - \frac{∂B^x}{∂z} & = - μ_0 J^y \\
       + \frac{1}{c^2} \frac{∂E^z}{∂t} & - \frac{∂B^y}{∂x} & + \frac{∂B^x}{∂y} &                   & = - μ_0 J^z \\
   \end{alignedat}

.. rubric:: Homogenous equations: Guauss's law and Faraday's law of induction

.. math::

   \begin{alignedat}{4}
                          & + \frac{∂B^x}{∂x} & + \frac{∂B^y}{∂y} & + \frac{∂B^z}{∂z} &= 0 \\
        + \frac{∂B^x}{∂t} &                   & + \frac{∂E^z}{y∂} & - \frac{∂E^y}{∂z} &= 0 \\
        + \frac{∂B^y}{∂t} & - \frac{∂E^z}{∂x} &                   & + \frac{∂E^x}{∂z} &= 0 \\
        + \frac{∂B^z}{∂t} & + \frac{∂E^y}{∂x} & - \frac{∂E^x}{∂y} &                   &= 0 \\
   \end{alignedat}

.. }}}

Ordered equations
-----------------

.. {{{

Recognizing the emerging structure, we slightly modify the expressions. These
modifications are not intricate. The objective is merely to present a compact
and symmetrical form, where all terms are aligned.

To eliminate the factor :math:`1/c`, we introduce :math:`\tilde{E}^x = E^x /
c`, :math:`\tilde{E}^y = E^y / c`, and :math:`\tilde{E}^z = E^z / c`.
Additionally, we define for the time dimension :math:`∂_t = \frac{∂}{∂(ct)}`,
and for the spatial dimensions :math:`∂_x = \frac{∂}{∂ x}`, :math:`∂_y =
\frac{∂}{∂y}`, as well as :math:`∂_z = \frac{∂}{∂z}`. The equations are now:

.. rubric:: Inhomogenous equations

.. _inc_beg_ordered_inhomogenous_equations:

.. math::

   \begin{alignedat}{4}
                  & + ∂_x \E^x & + ∂_y \E^y & + ∂_z \E^z & = + μ_0 c ρ \\
       + ∂_t \E^x &            & - ∂_y  B^z & + ∂_z  B^y & = - μ_0 J^x \\
       + ∂_t \E^y & + ∂_x  B^z &            & - ∂_z  B^x & = - μ_0 J^y \\
       + ∂_t \E^z & - ∂_x  B^y & + ∂_y  B^x &            & = - μ_0 J^z \\
   \end{alignedat}

.. _inc_end_ordered_inhomogenous_equations:

.. rubric:: Homogenous equations

.. _inc_beg_ordered_homogenous_equations:

.. math::

   \begin{alignedat}{4}
                  & + ∂_x  B^x & + ∂_y  B^y & + ∂_z  B^z & = 0 \\
       + ∂_t  B^x &            & + ∂_y \E^z & - ∂_z \E^y & = 0 \\
       + ∂_t  B^y & - ∂_x \E^z &            & + ∂_z \E^x & = 0 \\
       + ∂_t  B^z & + ∂_x \E^y & - ∂_y \E^x &            & = 0 \\
   \end{alignedat}

.. _inc_end_ordered_homogenous_equations:

For readers well-versed in the tensor formulation of electromagnetism, the
presence and nature of the Faraday tensor and its dual are likely evident.
Moreover, for those acquainted with matrix multiplication principles, it should
be apparent that we can employ matrices operations.

.. note::

   Although beyond our current discussion's scope, defining :math:`∂_μ` unifies
   all dimensions to a unit of inverse distance. :math:`\frac{1}{c}\frac{∂}{∂t}
   =\frac{∂}{∂(ct)}` has the units of an inverse distance, exactly like the
   partial derivative with respect to the spatial dimensions
   :math:`\frac{∂}{∂x}`, :math:`\frac{∂}{∂y}`, and :math:`\frac{∂}{∂z}`.

.. note::

   The experimental relation between the speed of light :math:`c`, the
   permitivity of free space :math:`ε_0`, and and the permeability of free
   space :math:`μ_0` is used:

   .. math:: c = \frac{1}{\sqrt{ε_0 μ_0}}

.. }}}

.. _the_tensor_of_mr_faraday:

Faraday tensor
--------------

.. {{{

From matrix multiplication rules, we infer the ordered equations are equivalent
to:

.. math::

   \begin{bmatrix} ∂_t & ∂_x & ∂_y & ∂_z \end{bmatrix}
   \begin{bmatrix}
              & + \E^x & +\E^y & + \E^z \\
       + \E^x &        & + B^z & -  B^y \\
       + \E^y & -  B^z &       & +  B^x \\
       + \E^z & +  B^y & - B^x &        \\
   \end{bmatrix}
   = \begin{bmatrix} + μ_0 c ρ & - μ_0 J^x  & - μ_0 J^y  & - μ_0 J^z \end{bmatrix}

.. math::

   \begin{bmatrix} ∂_t & ∂_x & ∂_y & ∂_z \end{bmatrix}
   \begin{bmatrix}
             & +  B^x & +  B^y & +  B^z \\
       + B^x &        & - \E^z & + \E^y \\
       + B^y & + \E^z &        & - \E^x \\
       + B^z & - \E^y & + \E^x &        \\
   \end{bmatrix}
   = \begin{bmatrix} 0 & 0 & 0 & 0 \end{bmatrix}

The flat left hand side is a covector, which we note in tensor notation with
lower indices :math:`∂_μ`. The right hand side is also flat and therefore a
covector :math:`J_ν`. The rank 2 tensors in the expressions are necessarily one
time contravariant and one time covariant. We multiply each column of :math:`∂`
with each row of :math:`F`, and repeat for all columns of :math:`F`. With the
first index :math:`μ` of :math:`F` to identify the rows, and the second index
:math:`ν` to indentify the columns, this means :math:`∂_μ F^μ{}_ν`. We then
write in tensor notation :math:`F^μ{}_ν` for the Faraday tensor, and
:math:`G^μ{}_ν` for its dual:

.. math::

   F^μ{}_ν = \begin{bmatrix}
              & + \E^x & + \E^y & + \E^z \\
       + \E^x &        & +  B^z & -  B^y \\
       + \E^y & -  B^z &        & +  B^x \\
       + \E^z & +  B^y & -  B^x &        \\
   \end{bmatrix}

.. math::

   G^μ{}_ν = \begin{bmatrix}
               & +  B^x & +  B^y & +  B^z \\
       +  B^x  &        & - \E^z & + \E^y \\
       +  B^y  & + \E^z &        & - \E^x \\
       +  B^z  & - \E^y & + \E^x &        \\
   \end{bmatrix}

We have thus obtained the Faraday tensor (inhomogenous equations) and its dual
(homogeneous equations). Maxwell's equations are then:

.. math::

   ∂_μ F^μ{}_ν &= J_{ν} \\
   ∂_μ G^μ{}_ν &= 0     \\

To double-check the result, you can have a look at `this alternative derivation
of the mixed electromagnetic tensor
<https://www.wikihow.life/Derive-the-Faraday-Tensor>`_. To triple-check the
result, you can also have a look at `these lecture notes from the Department of
Physics of the University of Oxford
<https://users.physics.ox.ac.uk/~palmerc/S8files/lectures.pdf>`_.

.. admonition:: Doubly contravariant form
   :class: dropdown

   .. {{{

   Another widespread expression of the Maxwell equations is written with a
   doubly contravariant tensor :math:`F^{μν}`. The derivation will be discussed
   here. Contrary to my ususal practice of performing systematic calculations,
   I consider in this note for simplicity only the inhomogenous equations. The
   argument and calculations can be apply to the homogenous equations in the
   same manner. Of course we can apply the Minkowski metric to raise or lower
   the indices, but the point here is to derive the tensor form using the
   doubly contravariant Faraday tensor, and from the ordered equations.

   You may have noticed that the sign in all equations can be flipped. In
   particular we can choose to express the ordered equations using the
   contravariant 4-current:

   .. math::

      J^ν = \begin{bmatrix}
          + μ_0 c ρ \\
          + μ_0 J^x \\
          + μ_0 J^y \\
          + μ_0 J^z \\
      \end{bmatrix}

   We would then reorder the inhomogenous equations as follows:

   .. math::

      \begin{alignedat}{4}
                     & + ∂_x \E^x & + ∂_y \E^y & + ∂_z \E^z & = + μ_0 c ρ \\
          - ∂_t \E^x &            & + ∂_y  B^z & - ∂_z  B^y & = + μ_0 J^x \\
          - ∂_t \E^y & - ∂_x  B^z &            & + ∂_z  B^x & = + μ_0 J^y \\
          - ∂_t \E^z & + ∂_x  B^y & - ∂_y  B^x &            & = + μ_0 J^z \\
      \end{alignedat}

   Following the same logic, we can use a column-column representation for the
   Faraday tensor, which permit to still follow matrix multiplication rules:

   .. math::

      \begin{bmatrix} ∂_t & ∂_x & ∂_y & ∂_z \end{bmatrix}
      \begin{bmatrix}
          \begin{bmatrix}
                 0   \\
              + \E^x \\
              + \E^y \\
              + \E^z \\
          \end{bmatrix} \\
          \begin{bmatrix}
              - \E^x \\
                 0   \\
              +  B^z \\
              -  B^y \\
          \end{bmatrix} \\
          \begin{bmatrix}
              -\E^y \\
              - B^z \\
                0   \\
              + B^x \\
          \end{bmatrix} \\
          \begin{bmatrix}
              - \E^z \\
              +  B^y \\
              -  B^x \\
                 0   \\
          \end{bmatrix} \\
      \end{bmatrix}
      = \begin{bmatrix}
          + μ_0 c ρ \\
          + μ_0 J^x \\
          + μ_0 J^y \\
          + μ_0 J^z \\
      \end{bmatrix}

   The doubly contravariant Faraday tensor can be written:

   .. math::

      F^{μν} = \begin{bmatrix}
          \begin{bmatrix}
                 0   \\
              + \E^x \\
              + \E^y \\
              + \E^z \\
          \end{bmatrix} \\
          \begin{bmatrix}
              - \E^x \\
                 0   \\
              +  B^z \\
              -  B^y \\
          \end{bmatrix} \\
          \begin{bmatrix}
              -\E^y \\
              - B^z \\
                0   \\
              + B^x \\
          \end{bmatrix} \\
          \begin{bmatrix}
              - \E^z \\
              +  B^y \\
              -  B^x \\
                 0   \\
          \end{bmatrix} \\
      \end{bmatrix}

   In this context, the first index :math:`μ` for selects the outer row, and
   the second index :math:`ν` selects the inner row. However, representing the
   Faraday tensor as a "row of rows" is unconventional. Typically a table form,
   and matrix multiplication rules not applied. This leads to the following
   expression for the doubly contravariant Faraday tensor:

   .. math::

      F^{μν} = \begin{bmatrix}
                & - \E^x & - \E^y & - \E^z \\
         + \E^x &        & -  B^z & +  B^y \\
         + \E^y & +  B^z &        & -  B^x \\
         + \E^z & -  B^y & +  B^x &        \\
      \end{bmatrix}

   Regardless whether we follow a row/row or row/column convention, the doubly
   contravariant Maxwell equations in tensor form are expressed as:

   .. math::

      ∂_μ F^{μν} = J^ν

   The discussion highlights some difficulties in using tensor notation, which
   makes it inconvenient when performing calculations algorithmically, without
   extensive thoughts. This is adressed by using the :ref:`the free matrix
   representation <the free matrix representation>` at the cost of extra
   symbols for the explicit basis. The advantage is that it allows for
   straightforward, "dumb" calculations.

   .. }}}

.. }}}
