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
relevant bit of notation from the Cartan-Hodge formalism is that basis vectors
:math:`\mathbf{e}_μ` are noted with the partial derivative symbol :math:`∂_μ`:

.. math::

   \mathbf{e}_t & = ∂_t \\
   \mathbf{e}_x & = ∂_x \\
   \mathbf{e}_y & = ∂_y \\
   \mathbf{e}_z & = ∂_z \\

I don't necessarily expect all readers to have ever considered partial
derivatives as basis vectors. For our purpose, this is simply a matter of using
a notation, which is both widespread and standard. For readability, I use for
the inner product either the dot notation :math:`\cdot`, or the bra-ket
notation from quantum mechanics :math:`\braket{|}`, both of which are standard
and widely recognized.

I would here like to point out the work of `Michael Penn
<https://www.michael-penn.net>`_ for the quality of his content. In particular,
I recommend the following:

* `Differential Forms | The Hodge operator via an inner product
  <https://m.youtube.com/watch?v=iLlaFBMk_Bs&list=PLHlTqVYmqunWXBoO3xZhQOAoc8oq
  d-2Su&index=58&t=225s&pp=gAQBiAQB>`_.
* `Differential Forms | The Minkowski metric and the Hodge operator
  <https://m.youtube.com/watch?v=vDRfADusqYQ>`_.

These videos provide an alternative, yet equivalent, approach to the
conclusions presented in this article. There is also the added bonus that he
uses the same metric signature :math:`(+,-,-,-)`. I prefer my way, but I
learned and understood first his way.

I am currently revisiting this article and expanding its content, particularly
in relation to Minkowski space. As a result, some sections are still in draft
form, and despite my best efforts to ensure accuracy, there may be typos and
errors. This page was last updated on |today|.

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

Inner product of k-vectors
--------------------------

Surfaces, volumes, hypervolumes and the determinant of matrices
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

I expect you are very familiar with linear algebra, since you are interested in
the topic of the Hodge dual. I nonetheless recall the relationship between the
determinant of matrices and surfaces, volumes, and hypervolumes in k
dimensions, as it is central to understanding the procedure for lifting the
inner product on vectors to the innner product on bivectors, trivectos,
quadvectors, and in all generality on k-vectors.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/
   Area_parallellogram_as_determinant.svg/
   891px-Area_parallellogram_as_determinant.svg.png
   :width: 250px

   Surfaces and the determinant of 2x2 matrices.

The area of the surface :math:`S` spanned by a parallelogram defined by two
vectors :math:`a ∂_x + b ∂_y` and :math:`c ∂_x + d ∂_y` corresponds
to the determinant of the :math:`2 \times 2` matrice, where each column are the
entries of the components of the vectors.

.. math::

   S = \begin{vmatrix}
     a & c \\
     b & d \\
   \end{vmatrix}

Or in other words the magnitude of the bivector:

.. math::

   S ∂_x ∧ ∂_y &= a ∂_x + b ∂_y) ∧ (c ∂_x + d ∂_y) \\
               &= a ∂_x ∧ (c ∂_x + d ∂_y) + b ∂_y ∧ (c ∂_x + d ∂_y) \\
               &= a ∂_x ∧ c ∂_x + a ∂_x ∧ d ∂_y + b ∂_y ∧ c ∂_x + b ∂_y ∧ d ∂_y \\
               &= a ∂_x ∧ d ∂_y + b ∂_y ∧ c ∂_x \\
               &= a d ∂_x ∧ ∂_y + b c ∂_y ∧ ∂_x \\
               &= a d ∂_x ∧ ∂_y - b c ∂_x ∧ ∂_y \\
               &= (ad - bc) ∂_x ∧ ∂_y\\

Using the free matrix representation from the Cartan-Hodge formalism helps
organize the terms. The same calculation yields:

.. math::

   S ∂_x ∧ ∂_y
   &= \begin{bmatrix} a ∂_x \\ b ∂_y \end{bmatrix} ∧ \begin{bmatrix} c ∂_x \\ d ∂_y \\ \end{bmatrix} \\
   &= \begin{bmatrix} a ∂_x ∧ d∂_y \\ b ∂_y ∧ c ∂_x \end{bmatrix} \\
   &= \begin{bmatrix} + a d ∂_x ∧ ∂_y \\ - b c ∂_x ∧ ∂_y \end{bmatrix} \\
   &= (ad - bc) ∂_x ∧ ∂_y\\

The same can be done in three dimensions to calculate the volume of a
parallelepiped defined by three vectors in three dimensions.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/
   Determinant_parallelepiped.svg/912px-Determinant_parallelepiped.svg.png
   :width: 250px

   Volumes and the determinant of 3x3 matrices.

* :math:`r_1 = a ∂_x + b ∂_y + c ∂_z`
* :math:`r_2 = u ∂_x + v ∂_y + w ∂_z`
* :math:`r_3 = p ∂_x + q ∂_y + r ∂_z`

where each columns are the entry of the components of the vectors.

.. math::

   V &= \begin{vmatrix}
     a & u & p \\
     b & v & q \\
     c & w & r \\
   \end{vmatrix}

.. math::

   v= + a \begin{vmatrix}
     v & q \\
     w & r \\
   \end{vmatrix}
   - b \begin{vmatrix}
      u & p \\
      w & r \\
   \end{vmatrix}
   + c \begin{vmatrix}
      u & p \\
      v & q \\
     \end{vmatrix}

.. math::
   V = + avr - awq - bur + bwp + cuq - cvp

Using the free matrix representation of the Cartan-Hodge formalism, we reach
the same result. I like to think this approach replaces the algorithmic
structure of the previous calculation with meaningful computations. Although
the Cartan-Hodge formalism introduces additional notation, this is balanced by
the clarity ofthe operations.

First, we wedge the three vectors that define the volume:

.. math::

   V ∂_x ∧ ∂_y ∧ ∂_z = \begin{bmatrix} a ∂_x \\ b ∂_y \\ c ∂_z \end{bmatrix} ∧
                       \begin{bmatrix} u ∂_x \\ v ∂_y \\ w ∂_z \end{bmatrix} ∧
                       \begin{bmatrix} p ∂_x \\ q ∂_y \\ r ∂_z \end{bmatrix}

Expand the first two vectors:

.. math::

   V ∂_x ∧ ∂_y ∧ ∂_z = \begin{bmatrix}
                            av ∂_x ∧ ∂_y \\
                            aw ∂_x ∧ ∂_z \\
                            bu ∂_y ∧ ∂_x \\
                            bw ∂_y ∧ ∂_z \\
                            cu ∂_z ∧ ∂_x \\
                            cv ∂_z ∧ ∂_y
                        \end{bmatrix}
                        ∧ \begin{bmatrix}
                              p ∂_x \\
                              q ∂_y \\
                              r ∂_z
                          \end{bmatrix}

Expand with the third vector:

.. math::

   V ∂_x ∧ ∂_y ∧ ∂_z = \begin{bmatrix}
                            avr ∂_x ∧ ∂_y ∧ ∂_z \\
                            awq ∂_x ∧ ∂_z ∧ ∂_y \\
                            bur ∂_y ∧ ∂_x ∧ ∂_z \\
                            bwp ∂_y ∧ ∂_z ∧ ∂_x \\
                            cuq ∂_z ∧ ∂_x ∧ ∂_y \\
                            cvp ∂_z ∧ ∂_y ∧ ∂_x
                        \end{bmatrix}

Reorder the terms:

.. math::

   V ∂_x ∧ ∂_y ∧ ∂_z = \begin{bmatrix}
                            +avr ∂_x ∧ ∂_y ∧ ∂_z \\
                            -awq ∂_x ∧ ∂_y ∧ ∂_z \\
                            -bur ∂_x ∧ ∂_y ∧ ∂_z \\
                            +bwp ∂_x ∧ ∂_y ∧ ∂_z \\
                            +cuq ∂_x ∧ ∂_y ∧ ∂_z \\
                            -cvp ∂_x ∧ ∂_y ∧ ∂_z
                        \end{bmatrix}

And obtain the expected conclusion:

.. math::

   V ∂_x ∧ ∂_y ∧ ∂_z = (+avr -awq -bur +bwp +cuq -cvp) ∂_x ∧ ∂_y ∧ ∂_z

This can be generalized to hypervolumes constructed from k-vectors, where the
hypervolume is calculated with the determinant of a :math:`k \times k` matrice.

bivectors in 3-dimensional Euclidean space
''''''''''''''''''''''''''''''''''''''''''

.. {{{

In essence, the inner product can be understood as the concept of measuring a
shadow. The inner product between two vectors is the measure of the
1-dimensional shadow of one vector onto the other. Similarly, the inner product
between bivectors is the measure of the surface shadow of one surface onto the
other. This 2-dimensional surface can be calculated from the determinant of a
:math:`2 ⨯ 2` matrix. We then generalize to 3-dimensions by calculating the
determinant of :math:`3 ⨯ 3` matrices, corresponding to the volumes covered by
3-vectors. A k-dimensional shadow measure can then be calculated using :math:`k
⨯ k` matrices, corresponding to hypervolumes of dimension k. This permits to
find a meaningfull way to *lift* the inner product from vectors to bivectors,
trivectors, and k-vectors. Lifting the inner product will finally permit to
generalize the the Hodge dual to any metric signature, and apply to Minkowski
space with metric signature :math:`(+,-,-,-)`. In 3-dimensional Euclidean
space, the inner product of the basis vectors, denoted with with either the dot
symbol :math:`\cdot` or the bracket symbol :math:`\braket{|}` is given by:

.. math::

   ∂_i \cdot ∂_j = \braket{∂_i|∂_j} = δ_{ij}

Consequently, we obtain the following dot products:

.. math::

   \begin{array}{c|ccc}
           & ∂_x & ∂_y & ∂_z \\
       \hline
       ∂_x & 1   & 0   & 0   \\
       ∂_y & 0   & 1   & 0   \\
       ∂_z & 0   & 0   & 1   \\
   \end{array}

A hint that the inner product can be generalized to surfaces is that in 3
dimensions, we can associate a basis surface to each of the basis vectors
through the Hodge dual, as argued at the beginning of this article. It may then
*feel natural,* since :math:`∂_x` is associated to :math:`∂_y ∧ ∂_z`, to expect
that the inner product :math:`\braket{∂_x|∂_x}=1` implies that
:math:`\braket{∂_y ∧ ∂_z | ∂_y ∧ ∂_z}=1`. Let us consider two vectors
:math:`a^♯` and :math:`b^♯` in 3-dimensional Euclidean space, written in
component form as:

* :math:`a^♯ = p \, ∂_x + q \, ∂_y + r \, ∂_z`
* :math:`b^♯ = u \, ∂_x + v \, ∂_y + w \, ∂_z`

Now consider the components of :math:`a^♯` and :math:`b^♯` along the unit
vectors :math:`∂_x` and :math:`∂_y`:

* :math:`p \, ∂_x + q \, ∂_y`
* :math:`u \, ∂_x + v \, ∂_y`

The measure of the amount of shadow of the surface determined by vectors
:math:`a^♯` and :math:`b^♯` on the :math:`∂_x ∧ ∂_y` plane is the inner product
on bivectors. This lifts the inner product from vectors to bivectors through
the determinant:

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

With this quantities, we have measured the amount of shadow from the surface
determined by vectors :math:`a^♯` and :math:`b^♯` onto the unit surface
:math:`∂_y ∧ ∂_z`, :math:`∂_z ∧ ∂_x`, and :math:`∂_x ∧ ∂_y`, . We can modify
the expression slightly in order to express the inner product of bivectors in
terms of the inner products of vectors:

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

Or put together in condensed form:

.. math::

   \braket{a^♯ ∧ b^♯ | ∂_k ∧ ∂_l} =
   \begin{vmatrix}
       \braket{a^♯ | ∂_k} & \braket{b^♯ | ∂_k} \\
       \braket{a^♯ | ∂_l} & \braket{b^♯ | ∂_l} \\
   \end{vmatrix}

With this, we have determined the surface of any arbitrary vector onto the
basis surfaces. We can replace vectors :math:`a^♯` and :math:`b^♯` with any of
the basis vectors :math:`∂_x`, :math:`∂_y`, or :math:`∂_z`. We now have a
technique to determine the inner product of all 2-forms:

.. math::

   \braket{∂_i ∧ ∂_j | ∂_k ∧ ∂_l} =
   \begin{vmatrix}
       \braket{∂_i | ∂_k} & \braket{∂_j | ∂_k} \\
       \braket{∂_i | ∂_l} & \braket{∂_j | ∂_l} \\
   \end{vmatrix}

Which permits to obtain:

.. math::

   \braket{∂_y ∧ ∂_z | ∂_y ∧ ∂_z}
   =
   \begin{vmatrix}
       \braket{∂_y | ∂_y} & \braket{∂_z | ∂_y} \\
       \braket{∂_y | ∂_z} & \braket{∂_z | ∂_z} \\
   \end{vmatrix}
   =
   \begin{vmatrix}
       1 & 0 \\
       0 & 1 \\
   \end{vmatrix}
   =1

.. math::

   \braket{∂_z ∧ ∂_x | ∂_z ∧ ∂_x}
   =
   \begin{vmatrix}
       \braket{∂_z | ∂_z} & \braket{∂_x | ∂_z} \\
       \braket{∂_z | ∂_x} & \braket{∂_x | ∂_x} \\
   \end{vmatrix}
   =
   \begin{vmatrix}
       1 & 0 \\
       0 & 1 \\
   \end{vmatrix}
   =1

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

All other inner products are zero. For example:

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

Doing this systematically for all 9 possible combinations bivector basis, we
obtain:

.. math::

   \begin{array}{c|cccc}
                 & ∂_y ∧ ∂_z & ∂_z ∧ ∂_x & ∂_x ∧ ∂_y \\
      \hline
       ∂_y ∧ ∂_z & 1         & 0         & 0         \\
       ∂_z ∧ ∂_x & 0         & 1         & 0         \\
       ∂_x ∧ ∂_y & 0         & 0         & 1         \\
   \end{array}

Finally, we generalize lifting the inner product to trivectors. In
3-dimensional Euclidean space, we get for the unit trivector:

.. math::

   \braket{∂_x ∧ ∂_y ∧ ∂_z | ∂_x ∧ ∂_y ∧ ∂_z} =
   \begin{vmatrix}
       \braket{∂_x | ∂_x} & \braket{∂_y | ∂_x} & \braket{∂_z | ∂_x}\\
       \braket{∂_x | ∂_y} & \braket{∂_y | ∂_y} & \braket{∂_z | ∂_y}\\
       \braket{∂_x | ∂_z} & \braket{∂_y | ∂_z} & \braket{∂_z | ∂_z}\\
   \end{vmatrix}

.. math::

   \braket{∂_x ∧ ∂_y ∧ ∂_z | ∂_x ∧ ∂_y ∧ ∂_z} =
   \begin{vmatrix}
       1 & 0 & 0\\
       0 & 1 & 0\\
       0 & 0 & 1\\
   \end{vmatrix}

.. math::

   \braket{∂_x ∧ ∂_y ∧ ∂_z | ∂_x ∧ ∂_y ∧ ∂_z} = 1

With this, we remark we have found a meaningfull and reasonable way to extend
the inner product to k-forms in Minkowski space. This approach is meaningful,
as the inner product of the basis vectors inherently incorporates the metric
signature.

.. }}}

k-vectors in Minkowski space
''''''''''''''''''''''''''''

.. {{{

.. rubric:: Inner product of vectors

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

.. rubric:: Inner product of bivectors

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

   \begin{array}{c|rrrrrr}
             & ∂_t ∧ ∂_x & ∂_t ∧ ∂_y & ∂_t ∧ ∂_z & ∂_y ∧ ∂_z & ∂_z ∧ ∂_x & ∂_x ∧ ∂_y \\
             \hline
   ∂_t ∧ ∂_x & -1        &  0        &  0        &   0       &  0        &  0        \\
   ∂_t ∧ ∂_y &  0        & -1        &  0        &   0       &  0        &  0        \\
   ∂_t ∧ ∂_z &  0        &  0        & -1        &   0       &  0        &  0        \\
   ∂_y ∧ ∂_z &  0        &  0        &  0        &  +1       &  0        &  0        \\
   ∂_z ∧ ∂_x &  0        &  0        &  0        &   0       & +1        &  0        \\
   ∂_x ∧ ∂_y &  0        &  0        &  0        &   0       &  0        & +1        \\
   \end{array}

.. admonition:: Derivation of the inner product of all basis bivectors
   :class: dropdown

   .. {{{

   In this dropdown section, I extend the inner product to all non-zero
   bivector combinations and provide an example of a zero combination.

   .. rubric:: Basis bivectors involving the temporal dimension

   .. math::

      \braket{∂_t ∧ ∂_x | ∂_t ∧ ∂_x}
      = \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_x \cdot ∂_t \\
          ∂_t \cdot ∂_x & ∂_x \cdot ∂_x \\
      \end{vmatrix}
      = \begin{vmatrix}
            \begin{alignedat}{1}
              + & 1 & \;   & 0 \\
                & 0 & \; - & 1 \\
             \end{alignedat}
      \end{vmatrix}
      = -1

   .. math::

      \braket{∂_t ∧ ∂_y | ∂_t ∧ ∂_y} =
      \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_y \cdot ∂_t \\
          ∂_t \cdot ∂_y & ∂_y \cdot ∂_y \\
      \end{vmatrix}
      = \begin{vmatrix}
            \begin{alignedat}{1}
              + & 1 & \;   & 0 \\
                & 0 & \; - & 1 \\
             \end{alignedat}
      \end{vmatrix}
      = -1

   .. math::

      \braket{∂_t ∧ ∂_z | ∂_t ∧ ∂_z} =
      \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_z \cdot ∂_t \\
          ∂_t \cdot ∂_z & ∂_z \cdot ∂_z \\
      \end{vmatrix}
      = \begin{vmatrix}
            \begin{alignedat}{1}
              + & 1 & \;   & 0 \\
                & 0 & \; - & 1 \\
             \end{alignedat}
      \end{vmatrix}
      = -1

   .. rubric:: Basis bivectors involving the spatial dimensions

   .. math::

      \braket{∂_y ∧ ∂_z | ∂_y ∧ ∂_z} =
      \begin{vmatrix}
          ∂_y \cdot ∂_y & ∂_z \cdot ∂_y \\
          ∂_y \cdot ∂_z & ∂_z \cdot ∂_z \\
      \end{vmatrix}
      = \begin{vmatrix}
            \begin{alignedat}{1}
              - & 1 & \;   & 0 \\
                & 0 & \; - & 1 \\
             \end{alignedat}
      \end{vmatrix}
      = +1

   .. math::

      \braket{∂_z ∧ ∂_x | ∂_z ∧ ∂_x} =
      \begin{vmatrix}
          ∂_z \cdot ∂_z & ∂_x \cdot ∂_z \\
          ∂_z \cdot ∂_x & ∂_x \cdot ∂_x \\
      \end{vmatrix}
      = \begin{vmatrix}
            \begin{alignedat}{1}
              - & 1 & \;   & 0 \\
                & 0 & \; - & 1 \\
             \end{alignedat}
      \end{vmatrix}
      = +1

   .. math::

      \braket{∂_x ∧ ∂_y | ∂_x ∧ ∂_y} =
      \begin{vmatrix}
          ∂_x \cdot ∂_x & ∂_y \cdot ∂_x \\
          ∂_x \cdot ∂_y & ∂_y \cdot ∂_y \\
      \end{vmatrix}
      = \begin{vmatrix}
            \begin{alignedat}{1}
              - & 1 & \;   & 0 \\
                & 0 & \; - & 1 \\
             \end{alignedat}
      \end{vmatrix}
      = +1

   .. rubric:: Basis vectors resulting in zero inner products

   All other inner products are zero. I demonstrate one example calculation,
   assuming the remaining cases will be clear to the reader.

   .. math::

      \braket{∂_t ∧ ∂_x | ∂_x ∧ ∂_y} =
      \begin{vmatrix}
          ∂_t \cdot ∂_x & ∂_x \cdot ∂_x \\
          ∂_t \cdot ∂_y & ∂_x \cdot ∂_y \\
      \end{vmatrix}
      = \begin{vmatrix}
            \begin{alignedat}{1}
                & 0 & \; + & 1 \\
                & 0 & \;   & 0 \\
             \end{alignedat}
      \end{vmatrix}
      = 0

   .. }}}

.. rubric:: Inner product of trivectors

As well as for trivectors:

.. math::

   \braket{∂_μ ∧ ∂_ν ∧ ∂_λ | ∂_ρ ∧ ∂_σ ∧ ∂_τ}
   =
   \begin{vmatrix}
       ∂_μ \cdot ∂_ρ & ∂_ν \cdot ∂_ρ & ∂_λ \cdot ∂_ρ \\
       ∂_μ \cdot ∂_σ & ∂_ν \cdot ∂_σ & ∂_λ \cdot ∂_σ \\
       ∂_μ \cdot ∂_τ & ∂_ν \cdot ∂_τ & ∂_λ \cdot ∂_τ \\
   \end{vmatrix}

.. admonition:: Systematic calculations of the inner product of basis trivectors
   :class: dropdown

   .. math::

      \braket{∂_x ∧ ∂_y ∧ ∂_z | ∂_x ∧ ∂_y ∧ ∂_z} =
      \begin{vmatrix}
          ∂_x \cdot ∂_x & ∂_y \cdot ∂_x & ∂_z \cdot ∂_x \\
          ∂_x \cdot ∂_y & ∂_y \cdot ∂_y & ∂_z \cdot ∂_y \\
          ∂_x \cdot ∂_z & ∂_y \cdot ∂_z & ∂_z \cdot ∂_z \\
      \end{vmatrix}
      =  \begin{vmatrix}
          -1 &  0 &  0 \\
           0 & -1 &  0 \\
           0 &  0 & -1 \\
      \end{vmatrix}
      = -1

   .. math::

      \braket{∂_t ∧ ∂_y ∧ ∂_z | ∂_t ∧ ∂_y ∧ ∂_z} =
      \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_y \cdot ∂_t & ∂_z \cdot ∂_t \\
          ∂_t \cdot ∂_y & ∂_y \cdot ∂_y & ∂_z \cdot ∂_y \\
          ∂_t \cdot ∂_z & ∂_y \cdot ∂_z & ∂_z \cdot ∂_z \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 &  0 &  0 \\
           0 & -1 &  0 \\
           0 &  0 & -1 \\
      \end{vmatrix}
      = 1

   .. math::

      \braket{∂_t ∧ ∂_z ∧ ∂_x | ∂_t ∧ ∂_z ∧ ∂_x} =
      \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_z \cdot ∂_t & ∂_x \cdot ∂_t \\
          ∂_t \cdot ∂_z & ∂_z \cdot ∂_z & ∂_x \cdot ∂_z \\
          ∂_t \cdot ∂_x & ∂_z \cdot ∂_x & ∂_x \cdot ∂_x \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 &  0 &  0 \\
           0 & -1 &  0 \\
           0 &  0 & -1 \\
      \end{vmatrix}
      = 1

   .. math::

      \braket{∂_t ∧ ∂_x ∧ ∂_y | ∂_t ∧ ∂_x ∧ ∂_y} =
      \begin{vmatrix}
          ∂_t \cdot ∂_t & ∂_x \cdot ∂_t & ∂_y \cdot ∂_t \\
          ∂_t \cdot ∂_x & ∂_x \cdot ∂_x & ∂_y \cdot ∂_x \\
          ∂_t \cdot ∂_y & ∂_x \cdot ∂_y & ∂_y \cdot ∂_y \\
      \end{vmatrix}
      =  \begin{vmatrix}
          +1 &  0 &  0 \\
           0 & -1 &  0 \\
           0 &  0 & -1 \\
      \end{vmatrix}
      = 1

.. math::

   \begin{array}{c|rrrr}
                   & ∂_x ∧ ∂_y ∧ ∂_z & ∂_t ∧ ∂_y ∧ ∂_z & ∂_t ∧ ∂_z ∧ ∂_x & ∂_t ∧ ∂_x ∧ ∂_y \\
                   \hline
   ∂_x ∧ ∂_y ∧ ∂_z & -1              &  0              &   0             &   0             \\
   ∂_t ∧ ∂_y ∧ ∂_z &  0              & +1              &   0             &   0             \\
   ∂_t ∧ ∂_z ∧ ∂_x &  0              &  0              &  +1             &   0             \\
   ∂_t ∧ ∂_x ∧ ∂_y &  0              &  0              &   0             &  +1             \\
   \end{array}

.. rubric:: Inner product of quadvectors

In Minkowski space, all quadvectors are proportional to :math:`∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z`:

.. math::

   \braket{∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z | ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z}
   &= \begin{vmatrix}
       ∂_t \cdot ∂_t & ∂_x \cdot ∂_t & ∂_y \cdot ∂_t & ∂_y \cdot ∂_t \\
       ∂_t \cdot ∂_x & ∂_x \cdot ∂_x & ∂_y \cdot ∂_x & ∂_y \cdot ∂_x \\
       ∂_t \cdot ∂_y & ∂_x \cdot ∂_y & ∂_y \cdot ∂_y & ∂_y \cdot ∂_y \\
       ∂_t \cdot ∂_z & ∂_x \cdot ∂_z & ∂_y \cdot ∂_z & ∂_y \cdot ∂_z \\
   \end{vmatrix} \\
   &=  \begin{vmatrix}
       +1 &  0 &  0 &  0 \\
        0 & -1 &  0 &  0 \\
        0 &  0 & -1 &  0 \\
        0 &  0 &  0 & -1 \\
   \end{vmatrix} \\
   &= -1

.. }}}

Formal and natural definition
-----------------------------

.. {{{

In 3-dimensional Euclidean space, the Hodge dual of a k-vector :math:`β` is
uniquely defined by the property that for any other k-vector :math:`α`, the
following property holds:

.. math::

   α ∧ ⋆ β = \braket{α | β} \; ∂_x ∧ ∂_y ∧ ∂_z

In essence, this asks: Given a k-vector, which m-vector fills the remaining
space? Where the inner product :math:`\braket{α | β}` ensures that :math:`⋆ β`
is unique. This question can be viewed as a *natural definition*  and be used
for practical calculations. For 4-dimensional Minkowski space, the definition
is:

.. math::

   α ∧ ⋆ β = \braket{α | β} \; ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z

For instance, when seeking the Hodge dual :math:`⋆(∂_t ∧ ∂_x)`, we know that it
must be :math:`∂_y ∧ ∂_z` to complete the space, with the sign determined by
the inner product :math:`\braket{∂_t ∧ ∂_x | ∂_t ∧ ∂_x} = -1`. Therefore, in
this example, we obtain:

.. math::

   ⋆ ∂_t ∧ ∂_x = - ∂_y ∧ ∂_z

.. }}}

.. _duality_in_minkowski_space:
.. _Duality in Minkowski Space:

Duality in Minkowski space
--------------------------

k-vectors
'''''''''

.. {{{

With this, we can conclude and fully determine the Hodge dual of all k-vectors
in Minkowski space:

.. rubric:: vectors

.. math::

   ⋆ ∂_t & = ∂_x ∧ ∂_y ∧ ∂_z \\
   ⋆ ∂_x & = ∂_t ∧ ∂_y ∧ ∂_z \\
   ⋆ ∂_y & = ∂_t ∧ ∂_z ∧ ∂_x \\
   ⋆ ∂_z & = ∂_t ∧ ∂_x ∧ ∂_y \\

.. admonition:: Full calculation
   :class: dropdown

   .. rubric:: Determine the Hodge duals up to the sign

   To obtain the volume element :math:`∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z`, the Hodge duals
   must be proportional to:

   .. math::

      ⋆ ∂_t &\propto & ∂_x ∧ ∂_y ∧ ∂_z \\
      ⋆ ∂_x &\propto & ∂_t ∧ ∂_z ∧ ∂_y \\
      ⋆ ∂_y &\propto & ∂_t ∧ ∂_x ∧ ∂_z \\
      ⋆ ∂_z &\propto & ∂_t ∧ ∂_y ∧ ∂_x \\

   .. rubric:: Check the sign

   Since the above was mentally determined, we check by wedging the left part
   to the right part of the equations above in order to make sure the sign is
   positive when reordered into the volume element :math:`∂_t ∧ ∂_x ∧ ∂_y ∧
   ∂_z`.

   .. math::

      ⋆ ∂_t \propto ∂_x ∧ ∂_y ∧ ∂_z \rightarrow & \phantom{-}& ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\

   .. math::

      ⋆ ∂_x \propto ∂_t ∧ ∂_z ∧ ∂_y \rightarrow &   & ∂_x ∧ ∂_t ∧ ∂_z ∧ ∂_y \\
                                                & - & ∂_t ∧ ∂_x ∧ ∂_z ∧ ∂_y \\
                                                &   & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\
   .. math::

      ⋆ ∂_y \propto ∂_t ∧ ∂_x ∧ ∂_z \rightarrow &   & ∂_y ∧ ∂_t ∧ ∂_x ∧ ∂_z \\
                                                & - & ∂_t ∧ ∂_y ∧ ∂_x ∧ ∂_z \\
                                                & - & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\
   .. math::

      ⋆ ∂_z \propto ∂_t ∧ ∂_y ∧ ∂_x \rightarrow &   & ∂_z ∧ ∂_t ∧ ∂_y ∧ ∂_x \\
                                                & - & ∂_t ∧ ∂_z ∧ ∂_y ∧ ∂_x \\
                                                &   & ∂_t ∧ ∂_y ∧ ∂_z ∧ ∂_x \\
                                                & - & ∂_t ∧ ∂_y ∧ ∂_x ∧ ∂_z \\
                                                &   & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\

   .. rubric:: Use the definition of the Hodge dual

   .. math::

      ⋆ ∂_t & = \braket{∂_t | ∂_t} & ∂_x ∧ ∂_y ∧ ∂_z \\
      ⋆ ∂_x & = \braket{∂_x | ∂_x} & ∂_t ∧ ∂_z ∧ ∂_y \\
      ⋆ ∂_y & = \braket{∂_y | ∂_y} & ∂_t ∧ ∂_x ∧ ∂_z \\
      ⋆ ∂_z & = \braket{∂_z | ∂_z} & ∂_t ∧ ∂_y ∧ ∂_x \\

   .. rubric:: Reorder

   .. math::

      ⋆ ∂_t & = \braket{∂_t | ∂_t} & (+1) & ∂_x ∧ ∂_y ∧ ∂_z \\
      ⋆ ∂_x & = \braket{∂_x | ∂_x} & (-1) & ∂_t ∧ ∂_y ∧ ∂_z \\
      ⋆ ∂_y & = \braket{∂_y | ∂_y} & (-1) & ∂_t ∧ ∂_z ∧ ∂_x \\
      ⋆ ∂_z & = \braket{∂_z | ∂_z} & (-1) & ∂_t ∧ ∂_x ∧ ∂_y \\

   .. rubric:: Apply the values of the inner products

   .. math::

      ⋆ ∂_t & = (+1) & (+1) & ∂_x ∧ ∂_y ∧ ∂_z \\
      ⋆ ∂_x & = (-1) & (-1) & ∂_t ∧ ∂_y ∧ ∂_z \\
      ⋆ ∂_y & = (-1) & (-1) & ∂_t ∧ ∂_z ∧ ∂_x \\
      ⋆ ∂_z & = (-1) & (-1) & ∂_t ∧ ∂_x ∧ ∂_y \\

   .. rubric:: Conclude

   .. math::

      ⋆ ∂_t & = ∂_x ∧ ∂_y ∧ ∂_z \\
      ⋆ ∂_x & = ∂_t ∧ ∂_y ∧ ∂_z \\
      ⋆ ∂_y & = ∂_t ∧ ∂_z ∧ ∂_x \\
      ⋆ ∂_z & = ∂_t ∧ ∂_x ∧ ∂_y \\

   If you feel more comfortable with a more *mechanical approach* I redirect
   you to the video by Michael Penn: `Differential Forms | The Minkowski metric
   and the Hodge operator <https://m.youtube.com/watch?v=vDRfADusqYQ>`_.

.. rubric:: bivectors

.. math::

   ⋆ (∂_t ∧ ∂_x) &= -& ∂_y ∧ ∂_z \\
   ⋆ (∂_t ∧ ∂_y) &= -& ∂_z ∧ ∂_x \\
   ⋆ (∂_t ∧ ∂_z) &= -& ∂_x ∧ ∂_y \\
   ⋆ (∂_y ∧ ∂_z) &=  & ∂_t ∧ ∂_x \\
   ⋆ (∂_z ∧ ∂_x) &=  & ∂_t ∧ ∂_y \\
   ⋆ (∂_x ∧ ∂_y) &=  & ∂_t ∧ ∂_z \\

.. admonition:: Full calculations of the Hodge dual of bivectors
   :class: dropdown

   To obtain the volume element :math:`∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z`, the Hodge duals
   must be proportional to:

   .. math::

      ⋆ (∂_t ∧ ∂_x) \propto ∂_y ∧ ∂_z \\
      ⋆ (∂_t ∧ ∂_y) \propto ∂_z ∧ ∂_x \\
      ⋆ (∂_t ∧ ∂_z) \propto ∂_x ∧ ∂_y \\
      ⋆ (∂_y ∧ ∂_z) \propto ∂_t ∧ ∂_x \\
      ⋆ (∂_z ∧ ∂_x) \propto ∂_t ∧ ∂_y \\
      ⋆ (∂_x ∧ ∂_y) \propto ∂_t ∧ ∂_z \\

   For example, taking the second entry as an example :math:`⋆ (∂_t ∧ ∂_y) \propto
   ∂_z ∧ ∂_x`, we have:

   .. math::

      ⋆ (∂_t ∧ ∂_y) \propto ∂_z ∧ ∂_x  & \rightarrow   & ∂_t ∧ ∂_y ∧ ∂_z ∧ ∂_x \\
                                       & \rightarrow - & ∂_t ∧ ∂_y ∧ ∂_x ∧ ∂_z \\
                                       & \rightarrow   & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\

   Taken all together and with the inner product, we have:

   .. math::

      ⋆ (∂_t ∧ ∂_x) &= \braket{∂_t ∧ ∂_x|∂_t ∧ ∂_x} \, ∂_y ∧ ∂_z \\
      ⋆ (∂_t ∧ ∂_y) &= \braket{∂_t ∧ ∂_y|∂_t ∧ ∂_y} \, ∂_z ∧ ∂_x \\
      ⋆ (∂_t ∧ ∂_z) &= \braket{∂_t ∧ ∂_z|∂_t ∧ ∂_z} \, ∂_x ∧ ∂_y \\
      ⋆ (∂_y ∧ ∂_z) &= \braket{∂_y ∧ ∂_z|∂_y ∧ ∂_z} \, ∂_t ∧ ∂_x \\
      ⋆ (∂_z ∧ ∂_x) &= \braket{∂_z ∧ ∂_x|∂_z ∧ ∂_x} \, ∂_t ∧ ∂_y \\
      ⋆ (∂_x ∧ ∂_y) &= \braket{∂_x ∧ ∂_y|∂_x ∧ ∂_y} \, ∂_t ∧ ∂_z \\

   Which simplifies to:

   .. math::

      ⋆ (∂_t ∧ ∂_x) &= -& ∂_y ∧ ∂_z \\
      ⋆ (∂_t ∧ ∂_y) &= -& ∂_z ∧ ∂_x \\
      ⋆ (∂_t ∧ ∂_z) &= -& ∂_x ∧ ∂_y \\
      ⋆ (∂_y ∧ ∂_z) &=  & ∂_t ∧ ∂_x \\
      ⋆ (∂_z ∧ ∂_x) &=  & ∂_t ∧ ∂_y \\
      ⋆ (∂_x ∧ ∂_y) &=  & ∂_t ∧ ∂_z \\

.. rubric:: trivectors

.. math::

   ⋆ ∂_x ∧ ∂_y ∧ ∂_z &= ∂_t \\
   ⋆ ∂_t ∧ ∂_y ∧ ∂_z &= ∂_x \\
   ⋆ ∂_t ∧ ∂_z ∧ ∂_x &= ∂_y \\
   ⋆ ∂_t ∧ ∂_x ∧ ∂_y &= ∂_z \\

.. admonition:: Full calculations of the Hodge dual of trivectors
   :class: dropdown

   To obtain the volume element :math:`∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z`, the Hodge duals
   must be proportional to:

   .. math::

      ⋆ ∂_x ∧ ∂_y ∧ ∂_z &\propto - & ∂_t \\
      ⋆ ∂_t ∧ ∂_y ∧ ∂_z &\propto   & ∂_x \\
      ⋆ ∂_t ∧ ∂_z ∧ ∂_x &\propto   & ∂_y \\
      ⋆ ∂_t ∧ ∂_x ∧ ∂_y &\propto   & ∂_z \\

   Indeed, we check this for all entries:

   .. math::

      ⋆ ∂_x ∧ ∂_y ∧ ∂_z \propto ∂_t & \rightarrow   & ∂_x ∧ ∂_y ∧ ∂_z ∧ ∂_t \\
                                    & \rightarrow - & ∂_x ∧ ∂_y ∧ ∂_t ∧ ∂_z \\
                                    & \rightarrow   & ∂_x ∧ ∂_t ∧ ∂_y ∧ ∂_z \\
                                    & \rightarrow - & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\

   .. math::

      ⋆ ∂_t ∧ ∂_y ∧ ∂_z \propto ∂_x & \rightarrow   & ∂_t ∧ ∂_y ∧ ∂_z ∧ ∂_x \\
                                    & \rightarrow - & ∂_t ∧ ∂_y ∧ ∂_x ∧ ∂_z \\
                                    & \rightarrow   & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\

   .. math::

      ⋆ ∂_t ∧ ∂_z ∧ ∂_x \propto ∂_y & \rightarrow   & ∂_t ∧ ∂_z ∧ ∂_x ∧ ∂_y \\
                                    & \rightarrow - & ∂_t ∧ ∂_x ∧ ∂_z ∧ ∂_y \\
                                    & \rightarrow   & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\

   .. math::

      ⋆ ∂_t ∧ ∂_x ∧ ∂_y \propto ∂_z & \rightarrow \phantom{-} & ∂_t ∧ ∂_x ∧ ∂_y ∧ ∂_z \\


   Taken all together and with the inner product:

   .. math::

      ⋆ ∂_x ∧ ∂_y ∧ ∂_z &= \braket{∂_x ∧ ∂_y ∧ ∂_z | ∂_x ∧ ∂_y ∧ ∂_z}- & ∂_t \\
      ⋆ ∂_t ∧ ∂_y ∧ ∂_z &= \braket{∂_t ∧ ∂_y ∧ ∂_z | ∂_t ∧ ∂_y ∧ ∂_z}  & ∂_x \\
      ⋆ ∂_t ∧ ∂_z ∧ ∂_x &= \braket{∂_t ∧ ∂_z ∧ ∂_x | ∂_t ∧ ∂_z ∧ ∂_x}  & ∂_y \\
      ⋆ ∂_t ∧ ∂_x ∧ ∂_y &= \braket{∂_t ∧ ∂_x ∧ ∂_y | ∂_t ∧ ∂_x ∧ ∂_y}  & ∂_z \\

   .. math::

      ⋆ ∂_x ∧ ∂_y ∧ ∂_z &= ∂_t \\
      ⋆ ∂_t ∧ ∂_y ∧ ∂_z &= ∂_x \\
      ⋆ ∂_t ∧ ∂_z ∧ ∂_x &= ∂_y \\
      ⋆ ∂_t ∧ ∂_x ∧ ∂_y &= ∂_z \\

.. }}}

k-forms
'''''''

.. {{{

As a final note, we can repeat the definition of the Hodge dual of k-vectors to
k-forms. Indeed the inner product is:

.. math::

   \braket{∂_μ | ∂_ν} = \braket{dx^μ | dx^ν}

We seek the dual k-form that fills the 4-dimensional space: the Hodge dual is
defined by the property that for all k-forms :math:`α` and :math:`β`, the
following holds:

.. math::

   α ∧ ⋆ β = \braket{α | β} dt ∧ dx ∧ dy ∧ dz

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

.. }}}

