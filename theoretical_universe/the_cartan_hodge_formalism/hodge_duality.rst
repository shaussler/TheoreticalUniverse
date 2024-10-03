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

The Hodge dual is, in my opinion, often presented with unnecessary complexity,
frequently involving from the outset a number of dimensions beyond three,
varying metric signatures, and a formal mathematical approach. However, the
concept is intuitive in the familiar three-dimensional space we live in, and
from there, extending it to four-dimensional Minkowski space may become easier.

In the first part of this article, I aim to simplify the presentation of the
Hodge dual by focusing initially on three dimensions, making the concept more
accessible. This discussion assumes the reader has a solid understanding of
vector calculus and is familiar with Élie Cartan's differential forms.

The second part presents a practical method for calculating the Hodge dual
using the Clifford product, which is then used to systematically calculated the
Hodge duals in Minkowski spacetime.

This article can be read independently, provided you are familiar with the
prerequisites above. In this work, I use a toolbox of concepts and notation
that I dub the Cartan-Hodge formalism. In this page the relevant bit of
notation from this formalism is that basis vectors :math:`\mathbf{e}_μ` are
noted with the partial derivative symbol :math:`∂_μ`:

.. math::

   \mathbf{e}_t & = ∂_t \\
   \mathbf{e}_x & = ∂_x \\
   \mathbf{e}_y & = ∂_y \\
   \mathbf{e}_z & = ∂_z \\

For our purpose, this is simply a matter of using a notation (that is both
widespread and standard). However, I don't necessarily expect all readers to
have ever considered partial derivatives as basis vectors.

.. }}}

Duality in Three Dimensions
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

Pseudo-vectors and Pseudo-scalars
---------------------------------

.. {{{

From the vector basis, we have obtained the following objects:

* Scalars.
* Vectors.
* Bivectors corresponding to surfaces, often called pseudo-vectors.
* Trivectors corresponding to volumes, often called pseudo-scalars.

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

Practical Caculations with the Clifford Product
-----------------------------------------------

.. warning:: Under Construction

Here, we map to the Clifford algebra. We have seen with that we can, through
the Hodge dual, associate a vector to all oriented surfaces. In particular this
is true when considering basis vectors and bivectors.

.. math::

   ∂_x ∧ ∂_y \rightarrow ∂_z \\
   ∂_y ∧ ∂_z \rightarrow ∂_x \\
   ∂_z ∧ ∂_x \rightarrow ∂_y \\

We map to the corresponding Clifford algebra. For Euclidean space, we have:

.. math::

   ∂_i ∨ ∂_i = 1

And is fully antisymmetric:

.. math::

   ∂_i ∨ ∂_j = - ∂_j ∨ ∂_i

From there, we note that the Hodge dual of a basis number :math:`\mathbf{1}`
is:

.. math::

   ⋆ \mathbf{1} = \mathbf{1} ∨ (∂_x ∨ ∂_y ∨ ∂_z) = ∂_x ∨ ∂_y ∨ ∂_z

We can either take the product with :math:`(∂_x ∨ ∂_y ∨ ∂_z)` or :math:`(∂_z ∨
∂_y ∨ ∂_x)`. To obtain the Hodge dual of a 3-vector, we apply the Clifford
product with:

.. math::

   ⋆ (∂_x ∨ ∂_y ∨ ∂_z) = (∂_x ∨ ∂_y ∨ ∂_z) ∨ (∂_z ∨ ∂_y ∨ ∂_x) = \mathbf{1}

The Hodge dual can then be calculated with:

.. math::

   ⋆ (∂_x ∨ ∂_y) = (∂_x ∨ ∂_y) ∨ (∂_z ∨ ∂_y ∨ ∂_x) = ∂_z \\
   ⋆ (∂_y ∨ ∂_z) = (∂_y ∨ ∂_z) ∨ (∂_z ∨ ∂_y ∨ ∂_x) = ∂_x \\
   ⋆ (∂_z ∨ ∂_x) = (∂_z ∨ ∂_x) ∨ (∂_z ∨ ∂_y ∨ ∂_x) = ∂_y \\

.. math::

   ⋆ ∂_x = ∂_x ∨ (∂_x ∨ ∂_y ∨ ∂_z) = ∂_y ∨ ∂_z \\
   ⋆ ∂_y = ∂_y ∨ (∂_x ∨ ∂_y ∨ ∂_z) = ∂_z ∨ ∂_x \\
   ⋆ ∂_z = ∂_z ∨ (∂_x ∨ ∂_y ∨ ∂_z) = ∂_x ∨ ∂_y \\

.. _duality_in_minkowski_space:
.. _Duality in Minkowski Space:

Duality in Minkowski Space
--------------------------

.. math::

   ⋆ (∂_x ∨ ∂_y) = (∂_x ∨ ∂_y) ∨ (∂_t ∨ ∂_x ∨ ∂_y ∨ ∂_z) = - ∂_t ∨ ∂_z \\
   ⋆ (∂_y ∨ ∂_z) = (∂_y ∨ ∂_z) ∨ (∂_t ∨ ∂_x ∨ ∂_y ∨ ∂_z) = - ∂_t ∨ ∂_x \\
   ⋆ (∂_z ∨ ∂_x) = (∂_z ∨ ∂_x) ∨ (∂_t ∨ ∂_x ∨ ∂_y ∨ ∂_z) = - ∂_t ∨ ∂_y \\

.. math::

   ⋆ (∂_x ∨ ∂_y) = (∂_x ∨ ∂_y) ∨ (∂_z ∨ ∂_y ∨ ∂_x ∨ ∂_t) = ∂_z ∨ ∂_t \\
   ⋆ (∂_y ∨ ∂_z) = (∂_y ∨ ∂_z) ∨ (∂_z ∨ ∂_y ∨ ∂_x ∨ ∂_t) = ∂_x ∨ ∂_t \\
   ⋆ (∂_z ∨ ∂_x) = (∂_z ∨ ∂_x) ∨ (∂_z ∨ ∂_y ∨ ∂_x ∨ ∂_t) = ∂_y ∨ ∂_t \\

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

