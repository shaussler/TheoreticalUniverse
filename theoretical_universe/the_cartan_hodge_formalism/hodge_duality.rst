.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _hodge_duality:
.. _hodge duality:

Hodge Duality
=============

.. rst-class:: custom-author

   by Stéphane Haussler

.. {{{

The Hodge dual is in my opinion often presented with unnecessary complexity,
frequently involving from the outset a number of dimensions beyond three,
varying metric signatures, and a formal mathematical approach. However, the
concept is very intuitive in the familiar three-dimensional space we live in,
and from there, extending to four-dimensional Minkowski space may then be
easier.

In the first part of this article, I tentatively simplify the concept of the
Hodge dual by focusing on three dimensions. The second part presents the
systematical calculation of the Hodge duals in Minkowski spacetime. This
discussion assumes you, the reader, to have a solid understanding of vector
calculus and familiarity with Élie Cartan's differential forms.

I generally use a toolbox of concepts and notation that I dub the Cartan-Hodge
formalism. This article can however be read independently. In this page the
relevant bit of notation from this Cartan-Hodge formalism is that basis vectors
:math:`\mathbf{e}_μ` are noted with the partial derivative symbol :math:`∂_μ`:

.. math::

   \mathbf{e}_t & = ∂_t \\
   \mathbf{e}_x & = ∂_x \\
   \mathbf{e}_y & = ∂_y \\
   \mathbf{e}_z & = ∂_z \\

I don't necessarily expect all readers to have ever considered partial
derivatives as basis vectors. For our purpose, this is simply a matter of using
a notation, which is both widespread and standard.

.. }}}

Duality in three dimensions
---------------------------

.. {{{

First consider a coordinate basis in 3 dimensions corresponding to our
intuitive understanding of space :math:`∂_x`, :math:`∂_y` and :math:`∂_z`.
Observe that we did not merely define three unit vectors, but also three *unit
surfaces* that we name using the wedge symbol :math:`∧`. The surface along the
:math:`x` and :math:`y` axis is named :math:`∂_x ∧ ∂_y`, along the :math:`y`
and :math:`z` axis :math:`∂_y ∧ ∂_z`, and along the :math:`z` and :math:`x`
axis, :math:`∂_z ∧ ∂_x`:

.. image:: _static/hodge_dual_coordinates.png
   :align: center
   :width: 60%

The naming of the surfaces is carefully chosen counterclock wise. The reason is
that not only we can define a surface (a number) from two vectors but also
given a vector together with a surface, we can uniquely determine the second
vector needed to obtain that surface. The surface need be oriented and a sign
convention chosen (counterclockwise is positive). For example, :math:`∂_z ∧ ∂_x
= - ∂_x ∧ ∂_z`.

Each basis surface can be associated with a unique basis vector:

.. math::

   ∂_x ∧ ∂_y \rightarrow ∂_z \\
   ∂_y ∧ ∂_z \rightarrow ∂_x \\
   ∂_z ∧ ∂_x \rightarrow ∂_y \\

We note this relation with the star symbol :math:`⋆`:

.. math::

   ⋆ ∂_x ∧ ∂_y = ∂_z \\
   ⋆ ∂_y ∧ ∂_z = ∂_x \\
   ⋆ ∂_z ∧ ∂_x = ∂_y \\

This association defines a dual vector to every oriented surfaces and is called
the Hodge dual, noted with the star operator :math:`⋆` operator. The relation
holds in both direction:

.. math::

   ⋆ ∂_z = ∂_x ∧ ∂_y \\
   ⋆ ∂_x = ∂_y ∧ ∂_z \\
   ⋆ ∂_y = ∂_z ∧ ∂_x \\

The Hodge dual in three dimensions is the cross product. The cross product
defines a vector perpendicular to the surface whose length is proportional to
the amount of rotation:

.. math::

   ∂_x ⨯ ∂_y = ⋆ ∂_x ∧ ∂_y = ∂_z \\
   ∂_y ⨯ ∂_z = ⋆ ∂_y ∧ ∂_z = ∂_x \\
   ∂_z ⨯ ∂_x = ⋆ ∂_z ∧ ∂_x = ∂_y \\

This establishes the deep connection between the Hodge dual, rotations,
surfaces, and the cross product.

Going one step futher, we observe that we did not merely define unit surfaces,
but also unit volumes that we note :math:`∂_x ∧ ∂_y ∧ ∂_z`. We can associate
the unit volume with numbers:

.. math::

   ⋆ \mathbf{1} = ∂_x ∧ ∂_y ∧ ∂_z

As well as:

.. math::

   ⋆ ∂_x ∧ ∂_y ∧ ∂_z = \mathbf{1}

Where :math:`\mathbf{1}` is the unit number. In other words any number can be
expressed as a linear combination of :math:`1`.

.. }}}

.. _pseudo_vectors_and_pseudo_scalars:

Pseudo-vectors and pseudo-scalars
---------------------------------

.. {{{

From the vector basis, we have obtained the following objects:

* Scalars.
* Vectors.
* Bivectors corresponding to surfaces, and also called pseudo-vectors.
* Trivectors corresponding to volumes, and also called pseudo-scalars.

Placing the objects in front of a mirror:

* Scalars look the same.
* Vectors look the same.
* Surfaces are flipped and the sign changes.
* Volumes are flipped and the sign changes.

This is the reason behind the naming *pseudo-vector*. When placed in front of a
mirror, the sign of a positive oriented surface goes to negative. These objects
are associated to vectors through the hodge dual. These dual vectors flip their
directions with the image of the oriented surface.

This is also the reason behind the name *pseudo-scalar*. When placed in front
of a mirror, the sign of a positive oriented volume goes to negative. These
objects are associated to scalars through the hodge dual. This dual scalars
flip their signs with the image of the oriented volume.

.. }}}

Inner product of bivectors in 3-dimensional Euclidean space
-----------------------------------------------------------

.. {{{

.. warning:: Under construction, last modified |today|

In essence, the inner product can be understood as the concept of shadow. The
inner product between vectors is the one dimensional shadow of one onto the
other. The inner product between bivectors is the surface shadow of one surface
onto the other. The 2-dimensional surface can be calculated from the
determinant of a 2 by 2 matrix. This will permit to generalize to 3-dimensional
shadows, which can be calculated as the determinant of a 3 by 3 matrix, and
above. A k-dimensional shadow is then calculated using a k by k matrix. This
permits to find a meaningfull way to *lift* the inner product from vectors to
bivectors, trivectors, and k-vectors. This approach will finally lead to
generalizing the definition of the Hodge dual, applicable Minkowski space, and
here with metric signature :math:`(+,-,-,-)`. The inner product in
3-dimensional Euclidean space of the basis vectors is:

.. math::

   \braket{∂_i|∂_j} = δ_{ij}

Consequently, we obtain the following dot products:

.. math::

   \begin{array}{c|rrr}
           & ∂_x & ∂_y & ∂_z \\
       \hline
       ∂_x & 1   & 0   & 0   \\
       ∂_y & 0   & 1   & 0   \\
       ∂_z & 0   & 0   & 1   \\
   \end{array}

A hint that the inner product can be generalized to surfaces is that in 3
dimensions, we can associate a basis surface to each of the basis vectors
through the Hodge dual, as argued above. It may then *feels natural,* since
:math:`∂_x` is associated to :math:`∂_y ∧ ∂_z`, to expect that the inner
product of :math:`\braket{∂_x|∂_x}=1` implies that :math:`\braket{∂_y ∧ ∂_z |
∂_y ∧ ∂_z}=1`. Let us consider two vectors :math:`a^♯` and :math:`b^♯` in
3-dimensional Euclidean space, written in component form as:

* :math:`a^♯ = p \, ∂_x + q \, ∂_y + r \, ∂_z`
* :math:`b^♯ = u \, ∂_x + v \, ∂_y + w \, ∂_z`

Now consider the components of :math:`a^♯` and :math:`b^♯` along the unit
vectors :math:`∂_x` and :math:`∂_y`:

* :math:`p \, ∂_x + q \, ∂_y`
* :math:`u \, ∂_x + v \, ∂_y`

.. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Area_parallellogram_as_determinant.svg/891px-Area_parallellogram_as_determinant.svg.png
   :width: 250px
   :align: right

   Surfaces and the determinant of 2x2 matrices.

The magnitude of the surface shadow determined by :math:`a^♯` and :math:`b^♯`
on the :math:`∂_x ∧ ∂_y` plane is the inner product on bivectors. This lifts
the inner product from vectors to bivectors through the determinant:

.. math::

   \braket{α^♯ ∧ β^♯ | ∂_x ∧ ∂_y} =
   \begin{vmatrix}
       p & u \\
       q & v \\
   \end{vmatrix}
   = pv - qu

In the same manner we obtain:

.. math::

   \braket{α^♯ ∧ β^♯ | ∂_y ∧ ∂_z} =
   \begin{vmatrix}
       q & v \\
       r & w \\
   \end{vmatrix}
   = qw - rv

.. math::

   \braket{α^♯ ∧ β^♯ | ∂_z ∧ ∂_x} =
   \begin{vmatrix}
       r & w \\
       p & u \\
   \end{vmatrix}
   = ru - pw

With this quantities, we measure the amount of shadow from the surface
determined by :math:`a^♯` and :math:`b^♯` onto the unit surface :math:`∂_y ∧
∂_z`, :math:`∂_z ∧ ∂_x`, and :math:`∂_x ∧ ∂_y`, . We can modify the expression
slightly in order to express the inner product of bivectors in terms of the
inner products of vectors:

.. math::

   \braket{a^♯ ∧ b^♯ | ∂_y ∧ ∂_z} =
   \begin{vmatrix}
       q & v \\
       r & w \\
   \end{vmatrix} =
   \begin{vmatrix}
       \braket{a^♯ | ∂_y} & \braket{b^♯ | ∂_y} \\
       \braket{a^♯ | ∂_z} & \braket{b^♯ | ∂_z} \\
   \end{vmatrix}

.. math::

   \braket{a^♯ ∧ b^♯ | ∂_z ∧ ∂_x} =
   \begin{vmatrix}
       r & w \\
       p & u \\
   \end{vmatrix} =
   \begin{vmatrix}
       \braket{a^♯ | ∂_z} & \braket{b^♯ | ∂_z} \\
       \braket{a^♯ | ∂_x} & \braket{b^♯ | ∂_x} \\
   \end{vmatrix}

.. math::

   \braket{a^♯ ∧ b^♯ | ∂_x ∧ ∂_y} =
   \begin{vmatrix}
       p & u \\
       q & v \\
   \end{vmatrix} =
   \begin{vmatrix}
       \braket{a^♯ | ∂_x} & \braket{b^♯ | ∂_x} \\
       \braket{a^♯ | ∂_y} & \braket{b^♯ | ∂_y} \\
   \end{vmatrix}

Or in other words:

.. math::

   \braket{a^♯ ∧ b^♯ | ∂_k ∧ ∂_l} =
   \begin{vmatrix}
       \braket{a^♯ | ∂_k} & \braket{b^♯ | ∂_k} \\
       \braket{a^♯ | ∂_l} & \braket{b^♯ | ∂_l} \\
   \end{vmatrix}

With this, we have determined the surface of any arbitrary vector onto the
basis surfaces. We can replace :math:`a^♯` and :math:`b^♯` with any of the
basis vectors. For example, with :math:`a^♯=∂_y`  and :math:`b^♯=∂_z`, we get:
We now have a technique to determine the inner product of all 2-forms. In
3-dimensional Euclidean space, we substitute :math:`a^♯` by :math:`∂_i` and
:math:`b^♯` by :math:`∂_j` to obtain:

.. math::

   \braket{∂_i ∧ ∂_j | ∂_k ∧ ∂_l} =
   \begin{vmatrix}
       \braket{∂_i | ∂_k} & \braket{∂_j | ∂_k} \\
       \braket{∂_i | ∂_l} & \braket{∂_j | ∂_l} \\
   \end{vmatrix}

Which permits to perform calculations:

.. math::

   \braket{∂_y ∧ ∂_z | ∂_x ∧ ∂_y}
   =
   \begin{vmatrix}
       \braket{∂_y | ∂_x} & \braket{∂_z | ∂_x} \\
       \braket{∂_y | ∂_y} & \braket{∂_z | ∂_y} \\
   \end{vmatrix}
   =
   \begin{vmatrix}
       0 & 0 \\
       0 & 0 \\
   \end{vmatrix}
   =0

.. math::

   \braket{∂_x ∧ ∂_y | ∂_x ∧ ∂_y}
   =
   \begin{vmatrix}
       \braket{∂_x | ∂_x} & \braket{∂_y | ∂_x} \\
       \braket{∂_x | ∂_y} & \braket{∂_y | ∂_y} \\
   \end{vmatrix}
   =
   \begin{vmatrix}
       1 & 0 \\
       0 & 1 \\
   \end{vmatrix}
   =1

Doing this for all 9 possible bivector basis combinations, we obtain:

.. math::

   \begin{array}{c|cccc}
                 & ∂_y ∧ ∂_z & ∂_z ∧ ∂_x & ∂_x ∧ ∂_y \\
      \hline
       ∂_y ∧ ∂_z & 1         & 0         & 0         \\
       ∂_z ∧ ∂_x & 0         & 1         & 0         \\
       ∂_x ∧ ∂_y & 0         & 0         & 1         \\
   \end{array}

Finally, we can generalize by lifting the inner product to trivectors. In
3-dimensional Euclidean space, we get:

.. math::

   \braket{∂_x ∧ ∂_y ∧ ∂_z | ∂_x ∧ ∂_y ∧ ∂_z}
   =
   \begin{vmatrix}
       \braket{∂_x | ∂_x} & \braket{∂_y | ∂_x} & \braket{∂_z | ∂_x}\\
       \braket{∂_x | ∂_y} & \braket{∂_y | ∂_y} & \braket{∂_z | ∂_y}\\
       \braket{∂_x | ∂_z} & \braket{∂_y | ∂_z} & \braket{∂_z | ∂_z}\\
   \end{vmatrix}
   =
   \begin{vmatrix}
       1 & 0 & 0\\
       0 & 1 & 0\\
       0 & 0 & 1\\
   \end{vmatrix}
   =1

Also, with this, we can see how we can reasonably lift the innner product on
k-forms in Minkowski space in a manner that makes sense.

.. }}}

Inner product of k-vectors in Minkowski space
---------------------------------------------

.. {{{

.. warning:: Under construction, last modified |today|

The inner product in Minkowski space of the basis vectors is:

.. math::

   \braket{∂_μ|∂_ν} = η_{μν}

Fully expanded in table form we have:

.. math::

   \begin{array}{c|rrr}
           & ∂_t & ∂_x & ∂_y & ∂_z \\
       \hline
       ∂_t & +1  &  0  &  0  &  0  \\
       ∂_x &  0  & -1  &  0  &  0  \\
       ∂_y &  0  &  0  & -1  &  0  \\
       ∂_z &  0  &  0  &  0  & -1  \\
   \end{array}

We can use our formulation for lifting the inner product to bivectors:

.. math::

   \braket{∂_μ ∧ ∂_ν | ∂_ρ ∧ ∂_σ}
   =
   \begin{vmatrix}
       ∂_μ \cdot ∂_ρ & ∂_ν \cdot ∂_ρ \\
       ∂_μ \cdot ∂_σ & ∂_ν \cdot ∂_σ \\
   \end{vmatrix}


We get in table form:

.. math::

   \begin{array}{c|ccrrrr}
             & ∂_t ∧ ∂_x & ∂_t ∧ ∂_y & ∂_t ∧ ∂_z & ∂_y ∧ ∂_z & ∂_z ∧ ∂_x & ∂_x ∧ ∂_y \\
             \hline
   ∂_t ∧ ∂_x & -1        &  0        &  0        &   0       &  0        &  0        \\
   ∂_t ∧ ∂_y &  0        & -1        &  0        &   0       &  0        &  0        \\
   ∂_t ∧ ∂_z &  0        &  0        & -1        &   0       &  0        &  0        \\
   ∂_y ∧ ∂_z &  0        &  0        &  0        &  +1       &  0        &  0        \\
   ∂_z ∧ ∂_x &  0        &  0        &  0        &   0       & +1        &  0        \\
   ∂_x ∧ ∂_y &  0        &  0        &  0        &   0       &  0        & +1        \\
   \end{array}


.. admonition:: Systematic calculations of the inner product of basis bivectors
   :class: dropdown

   .. math::

      \braket{∂_t ∧ ∂_x | ∂_t ∧ ∂_x} =
      \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_x \cdot ∂_t \\
          ∂_t \cdot ∂_x & ∂_x \cdot ∂_x \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 & 0 \\
           0 & -1 \\
      \end{vmatrix}
      = -1

   .. math::

      \braket{∂_t ∧ ∂_y | ∂_t ∧ ∂_y} =
      \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_y \cdot ∂_t \\
          ∂_t \cdot ∂_y & ∂_y \cdot ∂_y \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 & 0 \\
           0 & -1 \\
      \end{vmatrix}
      = -1

   .. math::

      \braket{∂_t ∧ ∂_z | ∂_t ∧ ∂_z} =
      \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_z \cdot ∂_t \\
          ∂_t \cdot ∂_z & ∂_z \cdot ∂_z \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 & 0 \\
           0 & -1 \\
      \end{vmatrix}
      = -1

   .. math::

      \braket{∂_y ∧ ∂_z | ∂_y ∧ ∂_z} =
      \begin{vmatrix}
          ∂_y \cdot ∂_y & ∂_z \cdot ∂_y \\
          ∂_y \cdot ∂_z & ∂_z \cdot ∂_z \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 &  0 \\
           0 & +1 \\
      \end{vmatrix}
      = +1

   .. math::

      \braket{∂_z ∧ ∂_x | ∂_z ∧ ∂_x} =
      \begin{vmatrix}
          ∂_z \cdot ∂_z & ∂_x \cdot ∂_z \\
          ∂_z \cdot ∂_x & ∂_x \cdot ∂_x \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 &  0 \\
           0 & +1 \\
      \end{vmatrix}
      = +1

   .. math::

      \braket{∂_x ∧ ∂_y | ∂_x ∧ ∂_y} =
      \begin{vmatrix}
          ∂_x \cdot ∂_x & ∂_y \cdot ∂_x \\
          ∂_x \cdot ∂_y & ∂_y \cdot ∂_y \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 &  0 \\
           0 & +1 \\
      \end{vmatrix}
      = +1

As well as for trivectors:

.. math::

   \braket{∂_μ ∧ ∂_ν ∧ ∂_λ | ∂_ρ ∧ ∂_σ ∧ τ}
   =
   \begin{vmatrix}
       ∂_μ \cdot ∂_ρ & ∂_ν \cdot ∂_ρ & ∂_λ \cdot ∂_ρ \\
       ∂_μ \cdot ∂_σ & ∂_ν \cdot ∂_σ & ∂_λ \cdot ∂_σ \\
       ∂_μ \cdot ∂_τ & ∂_ν \cdot ∂_τ & ∂_λ \cdot ∂_τ \\
   \end{vmatrix}

.. }}}

Formal and natural definition
-----------------------------

.. {{{

.. warning:: Under construction, last modified |today|

In 3-dimensional Euclidean space, the Hodge dual is defined by the property
that for all k-vectors :math:`α` and :math:`β`, the following holds:

.. math::

   α ∧ ⋆ β = ∂_x ∧ ∂_y ∧ ∂_z

In essence, this asks: Given an m-vector, which k-vector fills the remaining
space to complete the full volume, as discussed at the beginning of this
article? I refer to this as the natural definition. To generalize this concept
to any metric signature, we utilize the dot product:

.. math::

   α ∧ ⋆ β = \braket{α | β} ∂_x ∧ ∂_y ∧ ∂_z

This reduces to the initial definition in 3-dimensional Euclidean space. In
Minkowski space, however, we seek the dual k-vector that fills the
4-dimensional space:

.. math::

   α ∧ ⋆ β = \braket{α | β} ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z

For example, if we seek the Hodge dual :math:`⋆(∂_t ∧ ∂_x)`, we know it will be
:math:`∂_y ∧ ∂_z` to complete the space, with the sign determined by the inner
product :math:`\braket{∂_t ∧ ∂_x | ∂_t ∧ ∂_x} = -1`. Thus, we obtain:

.. math::

   ⋆ ∂_t ∧ ∂_x = - ∂_y ∧ ∂_z

.. }}}

.. _duality_in_minkowski_space:
.. _Duality in Minkowski Space:

Hodge duality of k-vectors in Minkowski space
---------------------------------------------

.. {{{

.. warning:: Under construction, last modified |today|

With this, we can conclude and fully determine the Hodge dual of all k-vectors
in Minkowski space:

.. math::

   ⋆ (∂_t ∧ ∂_x) &= -& ∂_y ∧ ∂_z \\
   ⋆ (∂_t ∧ ∂_y) &= -& ∂_z ∧ ∂_x \\
   ⋆ (∂_t ∧ ∂_z) &= -& ∂_x ∧ ∂_y \\
   ⋆ (∂_y ∧ ∂_z) &=  & ∂_t ∧ ∂_x \\
   ⋆ (∂_z ∧ ∂_x) &=  & ∂_t ∧ ∂_y \\
   ⋆ (∂_x ∧ ∂_y) &=  & ∂_t ∧ ∂_z \\

.. admonition:: Full calculations
   :class: dropdown

   In order to obtain the volume element :math:`∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z`, the Hodge
   duals are proportional to:

   .. math::

      ⋆ (∂_t ∧ ∂_x) \propto ∂_y ∧ ∂_z \\
      ⋆ (∂_t ∧ ∂_y) \propto ∂_z ∧ ∂_x \\
      ⋆ (∂_t ∧ ∂_z) \propto ∂_x ∧ ∂_y \\
      ⋆ (∂_y ∧ ∂_z) \propto ∂_t ∧ ∂_x \\
      ⋆ (∂_z ∧ ∂_x) \propto ∂_t ∧ ∂_y \\
      ⋆ (∂_x ∧ ∂_y) \propto ∂_t ∧ ∂_z \\

   Indeed, taking the second entry as an example :math:`⋆ (∂_t ∧ ∂_y) \propto
   ∂_z ∧ ∂_x`, we have:

   .. math::

      ⋆ (∂_t ∧ ∂_y) \propto ∂_z ∧ ∂_x  & \rightarrow   & ∂_t ∧ ∂_y ∧ ∂_z ∧ ∂_x \\
                                       & \rightarrow - & ∂_t ∧ ∂_y ∧ ∂_x ∧ ∂_z \\
                                       & \rightarrow   & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\

   Taken all together and with the inner product:

   .. math::

      ⋆ (∂_t ∧ ∂_x) &= \braket{∂_t ∧ ∂_x|∂_t ∧ ∂_x} \, ∂_y ∧ ∂_z \\
      ⋆ (∂_t ∧ ∂_y) &= \braket{∂_t ∧ ∂_y|∂_t ∧ ∂_y} \, ∂_z ∧ ∂_x \\
      ⋆ (∂_t ∧ ∂_z) &= \braket{∂_t ∧ ∂_z|∂_t ∧ ∂_z} \, ∂_x ∧ ∂_y \\
      ⋆ (∂_y ∧ ∂_z) &= \braket{∂_y ∧ ∂_z|∂_y ∧ ∂_z} \, ∂_t ∧ ∂_x \\
      ⋆ (∂_z ∧ ∂_x) &= \braket{∂_z ∧ ∂_x|∂_z ∧ ∂_x} \, ∂_t ∧ ∂_y \\
      ⋆ (∂_x ∧ ∂_y) &= \braket{∂_x ∧ ∂_y|∂_x ∧ ∂_y} \, ∂_t ∧ ∂_z \\

   .. math::

      ⋆ (∂_t ∧ ∂_x) &= -& ∂_y ∧ ∂_z \\
      ⋆ (∂_t ∧ ∂_y) &= -& ∂_z ∧ ∂_x \\
      ⋆ (∂_t ∧ ∂_z) &= -& ∂_x ∧ ∂_y \\
      ⋆ (∂_y ∧ ∂_z) &=  & ∂_t ∧ ∂_x \\
      ⋆ (∂_z ∧ ∂_x) &=  & ∂_t ∧ ∂_y \\
      ⋆ (∂_x ∧ ∂_y) &=  & ∂_t ∧ ∂_z \\

.. math::

   ⋆ (dt ∧ dx) &= -& dy ∧ dz \\
   ⋆ (dt ∧ dy) &= -& dz ∧ dx \\
   ⋆ (dt ∧ dz) &= -& dx ∧ dy \\
   ⋆ (dy ∧ dz) &=  & dt ∧ dx \\
   ⋆ (dz ∧ dx) &=  & dt ∧ dy \\
   ⋆ (dx ∧ dy) &=  & dt ∧ dz \\

.. math::

   ⋆ dt &= - dx ∧ dy ∧ dz \\
   ⋆ dx &= - dt ∧ dy ∧ dz \\
   ⋆ dy &= - dt ∧ dz ∧ dx \\
   ⋆ dz &= - dt ∧ dx ∧ dy \\


To double-check the results, I recommend the video `Differential Forms | The
Minkowski metric and the Hodge operator
<https://m.youtube.com/watch?v=vDRfADusqYQ>`_ by Michale Penn.

.. }}}

Hodge duality of k-forms in Minkowski space
-------------------------------------------

.. {{{

.. warning:: Under construction, last modified |today|

As a final note, we can repeat the definition of the Hodge dual of k-vectors
to k-forms. Indeed the inner product is:

.. math::

   \braket{∂_μ | ∂_ν} = \braket{dx^μ | dx^ν}

We seek the dual k-form that fills the 4-dimensional space: the Hodge dual is
defined by the property that for all k-forms :math:`α` and :math:`β`, the
following holds:

.. math::

   α ∧ ⋆ β = \braket{α | β} dt ∧ dx ∧ dy ∧ dz

.. }}}

