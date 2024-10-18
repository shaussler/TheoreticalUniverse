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

In a nutshell, the inner product is the concept of a shadow. The inner product
of two vectors is the one dimensional shadow of one onto the other. The surface
can be calculated from the determinant of a 2 by 2 matrix. This permits to
generalize to 3 dimensions (volumes) and above. I show a meaningfull way to
*lift* the inner product from vectors to bivectors, trivectors, and k-vectors.
This permits to generalize the definition of the Hodge dual and apply to
4-dimensional Minkowski space. The inner product in 3-dimensional Euclidean
space of the basis vectors is:

.. math::

   \braket{∂_i|∂_j} = δ_{ij}

Fully expanded, with a notation that I hope obvious, we have:

.. math::

   \begin{array}{c|rrr}
           & ∂_x & ∂_y & ∂_z \\
       ∂_x & 1   & 0   & 0   \\
       ∂_y & 0   & 1   & 0   \\
       ∂_z & 0   & 0   & 1   \\
   \end{array}

A hint that the inner product can be generalized to surfaces is that in 3
dimensions, we can associate a basis surface to each basis vectors. it would
then *feel* natural, that since :math:`∂_x` is associated to :math:`∂_y ∧ ∂_z`
through Hodge duality, we could expect that the inner product of
:math:`\braket{∂_x|∂_x}=1` would imply that :math:`\braket{∂_y ∧ ∂_z | ∂_y ∧
∂_z}=1`. Consider two arbitrary vectors :math:`a^♯` and :math:`b^♯` in
3-dimensional Euclidean space:

* :math:`a^♯ = p \, ∂_x + q \, ∂_y + r \, ∂_z`
* :math:`b^♯ = u \, ∂_x + v \, ∂_y + w \, ∂_z`

Now consider the subspace determined by the unit vectors:

* :math:`∂_x`
* :math:`∂_y`

And the plane along these :math:`∂_x` and :math:`∂_y` unit vectors:

* :math:`∂_x ∧ ∂_y`

The components of :math:`a^♯` and :math:`b^♯` on the :math:`∂_x ∧ ∂_y` plane
are:

* :math:`p \, ∂_x + q \, ∂_y`
* :math:`u \, ∂_x + v \, ∂_y`

.. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Area_parallellogram_as_determinant.svg/891px-Area_parallellogram_as_determinant.svg.png
   :width: 250px
   :align: right

   This figure needs to be replaced by a better depiction

The magnitude of the surface determined by :math:`a^♯` and :math:`b^♯` along
the :math:`∂_x ∧ ∂_y` plane is the inner product on bivectors. This generalizes
the inner product of vectors. The inner product of vectors correspond to the
projection of vectors onto another, and the inner product of bivectors
correspond to the projection of surfaces onto another.

.. math::

   \braket{α^♯ ∧ β^♯ | ∂_x ∧ ∂_y} =
   \begin{vmatrix}
       p & u \\
       q & v \\
   \end{vmatrix}
   = pv - uq

With this quantity, we measure the amount of shadow from the surface determined
by :math:`a^♯` and :math:`b^♯` onto the plane determined by :math:`∂_x` and
:math:`∂_y` in term of the unit surface :math:`∂_x ∧ ∂_y`. So what we would
like to have for the inner product of two vectors is the projection of a vector
onto another. In the same manner, the inner product of two bivectors is the
projection of a surface onto another. We rewrite slightly in order to
generalize. The surface covered by :math:`a^♯` and :math:`b^♯` in the
:math:`∂_x ∧ ∂_y` unit plane is the inner product of surfaces (or 2-vectors)
:math:`\braket{a^♯ ∧ b^♯|∂_x ∧ ∂_y}`:

.. math::

   \braket{a^♯ ∧ b^♯ | ∂_x ∧ ∂_y}
   =
   \begin{vmatrix}
       p & u \\
       q & v \\
   \end{vmatrix}
   =
   \begin{vmatrix}
       \braket{a^♯ | ∂_x} & \braket{b^♯ | ∂_x} \\
       \braket{a^♯ | ∂_y} & \braket{b^♯ | ∂_y} \\
   \end{vmatrix}

We now have a technique to generalize and calculate the inner product to
2-forms. In 3-dimensional Euclidean space, we substitute :math:`a^♯` by
:math:`∂_i` and :math:`b^♯` by :math:`∂_j`:

.. math::

   \braket{a^♯ ∧ b^♯ | ∂_x ∧ ∂_y}
   =
   \begin{vmatrix}
       \braket{a^♯ | ∂_x} & \braket{b^♯ | ∂_x} \\
       \braket{a^♯ | ∂_y} & \braket{b^♯ | ∂_y} \\
   \end{vmatrix}

With this, we have determined the surface of any arbitrary vector onto the
basis surfaces. We can replace :math:`a^♯` and :math:`b^♯` with any of the
basis vectors. For example, with :math:`a^♯=∂_y`  and :math:`b^♯=∂_z`, we get:

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

with :math:`a^♯=∂_x`  and :math:`b^♯=∂_y`, we get:

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

Doing this for all possible bivector basis pairs, we obtain:

.. math::

   \begin{matrix}
                 & ∂_y ∧ ∂_z & ∂_z ∧ ∂_x & ∂_x ∧ ∂_y \\
       ∂_y ∧ ∂_z & 1         & 0         & 0         \\
       ∂_z ∧ ∂_x & 0         & 1         & 0         \\
       ∂_x ∧ ∂_y & 0         & 0         & 1         \\
   \end{matrix}

With this, we can generalize and lift the inner product to trivectors. In
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

Inner product of k-forms in Minkowski space
-------------------------------------------

.. {{{

.. warning:: Under construction, last modified |today|

The inner product in Minkowski space of the basis vectors is:

.. math::

   \braket{∂_μ|∂_ν} = η_{μν}

Fully expanded, with a notation that I hope obvious, we have:

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
       \braket{∂_μ | ∂_ρ} & \braket{∂_ν | ∂_ρ} \\
       \braket{∂_μ | ∂_σ} & \braket{∂_ν | ∂_σ} \\
   \end{vmatrix}

And also to trivectors:

.. math::

   \braket{∂_μ ∧ ∂_ν | ∂_ρ ∧ ∂_σ}
   =
   \begin{vmatrix}
       \braket{∂_μ | ∂_ρ} & \braket{∂_ν | ∂_ρ} \\
       \braket{∂_μ | ∂_σ} & \braket{∂_ν | ∂_σ} \\
   \end{vmatrix}

.. }}}

.. _duality_in_minkowski_space:
.. _Duality in Minkowski Space:

Duality in Minkowski Space
--------------------------

.. {{{

.. warning:: Under construction, last modified |today|

.. math::

   ⋆ dt &= - dx ∧ dy ∧ dz \\
   ⋆ dx &= - dt ∧ dy ∧ dz \\
   ⋆ dy &= - dt ∧ dz ∧ dx \\
   ⋆ dz &= - dt ∧ dx ∧ dy \\

.. math::

   ⋆ (dt ∧ dx) &= -& dy ∧ dz \\
   ⋆ (dt ∧ dy) &= -& dz ∧ dx \\
   ⋆ (dt ∧ dz) &= -& dx ∧ dy \\
   ⋆ (dy ∧ dz) &=  & dt ∧ dx \\
   ⋆ (dz ∧ dx) &=  & dt ∧ dy \\
   ⋆ (dx ∧ dy) &=  & dt ∧ dz \\

.. ifconfig:: draft in ('yes')

   .. warning:: Draft

   .. math::

      ⋆ (∂_t ∧ ∂_x) &= -& ∂_y ∧ ∂_z \\
      ⋆ (∂_t ∧ ∂_y) &= -& ∂_z ∧ ∂_x \\
      ⋆ (∂_t ∧ ∂_z) &= -& ∂_x ∧ ∂_y \\
      ⋆ (∂_x ∧ ∂_y) &=  & ∂_t ∧ ∂_z \\
      ⋆ (∂_y ∧ ∂_z) &=  & ∂_t ∧ ∂_x \\
      ⋆ (∂_z ∧ ∂_x) &=  & ∂_t ∧ ∂_y \\

To double-check the results, I recommend the video `Differential Forms | The
Minkowski metric and the Hodge operator
<https://m.youtube.com/watch?v=vDRfADusqYQ>`_ by Michale Penn.

.. }}}

