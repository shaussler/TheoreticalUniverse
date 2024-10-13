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

Pseudo-Vectors and Pseudo-Scalars
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

The inner product on multivectors
---------------------------------

.. {{{

.. warning:: Under construction

The inner product in 3-dimensional Euclidean space of basis vectors is:

.. math::

   \braket{∂_i, ∂_j} = δ_{ij}

Fully expanded, with a notation that I hope obvious, we have:

.. math::

   \begin{matrix}
           & ∂_x & ∂_y & ∂_z \\
       ∂_x & 1   & 0   & 0   \\
       ∂_y & 0   & 1   & 0   \\
       ∂_z & 0   & 0   & 1   \\
   \end{matrix}

Since we associate through the Hodge dual in 3-dimensional Euclidean space we
can relate the inner product from vector to bivectors:

.. math::

   \begin{matrix}
                   & ⋆ ∂_y ∧ ∂_z & ⋆ ∂_z ∧ ∂_x & ⋆ ∂_x ∧ ∂_y \\
       ⋆ ∂_y ∧ ∂_z & 1           & 0           & 0           \\
       ⋆ ∂_z ∧ ∂_x & 0           & 1           & 0           \\
       ⋆ ∂_x ∧ ∂_y & 0           & 0           & 1           \\
   \end{matrix}

With :math:`α^♯ = a \, ∂_x + b \, ∂_y + c \, ∂_z` and :math:`β^♯ = u \, ∂_x + v
\, ∂_y + w \, ∂_z`, the magnitude of the surface along the :math:`∂_x ∧ ∂_y` is
the determinant. With

* :math:`∂_x ∧ ∂_y` the plane along the :math:`∂_x` abd :math:`∂_y` unit
  vectors.
* :math:`α^♯_{∂_x ∧ ∂_y} = a \, ∂_x + b \, ∂_y` the :math:`α^♯` vector on the
  :math:`∂_x ∧ ∂_y` plane.
* :math:`β^♯_{∂_x ∧ ∂_y} = u \, ∂_x + v \, ∂_y` the :math:`β^♯` vector on the
  :math:`∂_x ∧ ∂_y` plane.

.. math::

   \|α^♯ ∧ β^♯\|_{∂_x ∧ ∂_y} =
   \begin{vmatrix}
       a & u \\
       b & v \\
   \end{vmatrix}
   = av - ub

So what we would like to have for the inner product of two vectors is the
projection of a vector onto another. In the same manner, the inner product of
two bivectors is the projection of a surface onto another.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Area_parallellogram_as_determinant.svg/891px-Area_parallellogram_as_determinant.svg.png
   :width: 250px
   :align: center

Now rewrite slightly to be able to generalize. The surface covered by
:math:`α^♯` and :math:`β^♯` in the :math:`∂_x ∧ ∂_y` unit plane is the inner
product on surfaces (or 2-forms) :math:`\braket{α^♯ ∧ β^♯|∂_x ∧ ∂_y}`:

.. math::

   \braket{α^♯ ∧ β^♯ | ∂_x ∧ ∂_y}
   \begin{vmatrix}
       a & u \\
       b & v \\
   \end{vmatrix}
   =
   \begin{vmatrix}
       α^♯ \cdot ∂_x & β^♯ \cdot ∂_x \\
       α^♯ \cdot ∂_y & β^♯ \cdot ∂_y \\
   \end{vmatrix}

We now have a technique to generalize and calculate the inner product to
2-forms. In 3-dimensional Euclidean space, we substitute :math:`α^♯` by
:math:`∂_i` and :math:`β^♯` by :math:`∂_j`

.. math::

   \braket{α^♯ ∧ β^♯ | ∂_x ∧ ∂_y}
   =
   \begin{vmatrix}
       α^♯ \cdot ∂_x & β^♯ \cdot ∂_x \\
       α^♯ \cdot ∂_y & β^♯ \cdot ∂_y \\
   \end{vmatrix}

.. math::

   \begin{matrix}
                 & ∂_y ∧ ∂_z & ∂_z ∧ ∂_x & ∂_x ∧ ∂_y \\
       ∂_y ∧ ∂_z & 1         & 0         & 0         \\
       ∂_z ∧ ∂_x & 0         & 1         & 0         \\
       ∂_x ∧ ∂_y & 0         & 0         & 1         \\
   \end{matrix}

.. }}}

.. _duality_in_minkowski_space:
.. _Duality in Minkowski Space:

Duality in Minkowski Space
--------------------------

.. {{{

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

