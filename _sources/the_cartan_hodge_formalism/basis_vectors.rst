.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Basis vectors
=============

.. rst-class:: custom-author

   by Stéphane Haussler

Partial Derivatives
-------------------

.. {{{

In these pages, the basis vectors :math:`\mathbf{e}_μ` are noted with the
partial derivative symbol :math:`∂_μ`:

.. math::

   \mathbf{e}_t & = ∂_t \\
   \mathbf{e}_x & = ∂_x \\
   \mathbf{e}_y & = ∂_y \\
   \mathbf{e}_z & = ∂_z \\

If you have never seen or thought of partial derivatives as basis vectors, you
may be rightfully unsettled. However this is not central to any calculations or
arguments presented in this work. Therefore, I propose to *simply accept*, or
*just replace* the :math:`∂_μ` symbols with the :math:`\mathbf{e}_μ` symbols.
For learning and a deeper understanding, I recommend video `Vectors as
directional derivatives <https://youtu.be/vtPiROQUMhQ?si=_ZLQbP6nifSsGXYC>`_ by
`Robert Davie <https://www.youtube.com/@TensorCalculusRobertDavie>`_, and video
`Manifolds 22 | Coordinate Basis
<https://www.youtube.com/watch?v=BjU8-n4ixqo&list=PLHlTqVYmqunWXBoO3xZhQOAoc8oqd-2Su&index=48>`_
by `The Bright Side of Mathematics
<https://www.youtube.com/@brightsideofmaths>`_. As very broad justification and
without systematically laying down the properties of a vector space, notice how
partial derivatives indeed fulfill the definition for a `vector space
<https://en.m.wikipedia.org/wiki/Vector_space>`_. They behave like vectors; the
following linear relations hold:

.. math::

  a (∂_t + ∂_x) = a ∂_t + a ∂_x \\
  (a+b) ∂_y     = a ∂_y + b ∂_y \\

.. }}}

Differentials
-------------

.. {{{

Using the partial derivatives as basis vectors :math:`\mathbf{e}_μ`, the
associated covectors :math:`\mathbf{e}^ν` are the differential operators:

.. math::

   \mathbf{e}^t & = dt \\
   \mathbf{e}^x & = dx \\
   \mathbf{e}^y & = dy \\
   \mathbf{e}^z & = dz \\

With :math:`δ` being the Kronecher-delta, the differential operators
:math:`dx^ν` fulfill the definition for covectors, i.e. :math:`\mathbf{e}^μ
\mathbf{e}_ν = δ^μ_ν`:

.. math::

   dx^μ ∂_ν = δ^μ_ν

.. }}}

Indexing
--------

.. {{{

We adopt the Einstein summation convention, where any repeated indices imply
summation. In 3-dimensional Euclidean space, we use Latin letters for indices,
while in 4-dimensional Minkowski space, we use Greek letters. For example, the
following expression represents a vector in spacetime:

.. math::

   V^{♯} = V^μ ∂_μ = \sum_{μ} V^μ ∂_μ

The indices are :math:`(t,x,y,z)`, or equivalently :math:`0,1,2,3`. For the
basis vectors, we have:

.. math::

   ∂_t &= ∂_0  \\
   ∂_x &= ∂_1  \\
   ∂_y &= ∂_2  \\
   ∂_z &= ∂_3  \\

For the basis covectors, we have:

.. math::

   \begin{alignedat}{1}
   dt &= dx^0 &= dx^t \\
   dx &= dx^1 &= dx^x \\
   dy &= dx^2 &= dx^y \\
   dz &= dx^3 &= dx^z \\
   \end{alignedat}

.. }}}

.. _orientation_of_space:

Basis Elements
--------------

.. {{{

.. figure:: _static/hodge_dual_coordinates.png
   :align: center
   :width: 60%

   Basis elements and orientation of space

In 3-dimensional Euclidean space, we define more than *just* three directions:

* :math:`∂_x`
* :math:`∂_y`
* :math:`∂_z`

We notice we have also defined three planes:

* :math:`∂_y ∧ ∂_z`
* :math:`∂_z ∧ ∂_x`
* :math:`∂_x ∧ ∂_z`

Where the wedge symbol :math:`∧` denotes the surface spanned by two directions
:math:`∂_i ∧ ∂_j`. The naming of the surfaces is carefully chosen counterclock
wise. Taking this one step further, we notice that we have defined the volume
element as well:

* :math:`∂_x ∧ ∂_y ∧ ∂_z`

Indeed, the Euclidean space necessitate the dot product, which permits to not
only determine the projection of a vector onto another :math:`V^♯ \cdot W^♯ =
V^i W^j δ_{ji} cos(θ)`, but also the surface of the parallelogram defined by
these two vectors :math:`|V^♯ ∧ W^♯| = V^i W^j δ_{ji} sin(θ)`.

.. }}}

Orientation of Space
--------------------

.. {{{

We label and order vectors by the letters :math:`x`, :math:`y`, and :math:`z`.
Cycling counterclockwise, the sequences are:

* :math:`x` to :math:`y` to :math:`z`, or
* :math:`y` to :math:`z` to :math:`x`, or
* :math:`z` to :math:`x` to :math:`y`

=========== ================= =============
Direction   Surface           Permutation
=========== ================= =============
:math:`∂_x` :math:`∂_y ∧ ∂_z` :math:`x,y,z`
:math:`∂_y` :math:`∂_z ∧ ∂_x` :math:`y,z,x`
:math:`∂_z` :math:`∂_x ∧ ∂_z` :math:`z,x,y`
=========== ================= =============

Traversing the table above from left to right or top to bottom, we cycle
through all permutations of the spatial directions. For a long time, I had
difficulties with the term :math:`∂_z ∧ ∂_x`. My instinct was to order the
elements of the basis bivectors alphabetically and thus take :math:`∂_x ∧ ∂_z`,
but requires a negative sign when flipping the surface to :math:`-∂_z ∧ ∂_x`.
Both conventions are correct but as can be read from the table, taking
:math:`∂_z ∧ ∂_x` is ultimately the superior choice.

.. }}}
