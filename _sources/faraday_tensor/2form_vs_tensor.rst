.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _relation between the faraday 2--form and the faraday tensor:

Relation between the Faraday 2--form and the Faraday tensor
===========================================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: under construction

In this page, I relate the Faraday 2--form to the electormagnetic field tensor,
and review the differences when rising or lowering and indices.

In abstract index notation, the doubly covariant Faraday tensor is expressed
without its tensor basis as:

.. math::

   F_{μν}

With explicit tensor basis and Einstein summation notation, this object is
written as:

.. math::

   F_{μν} \: dx^μ ⊗ dx^ν

The Faraday 2--form is expressed as:

.. math::

   F^{♭♭} = \frac{1}{2} F_{μν} \: dx^μ ∧ dx^ν

Where we can rewrite the exterior product as a tensor product:

.. math::

   F^{♭♭} = \frac{1}{2} F_{μν} \: \left( dx^μ ⊗ dx^ν - dx^ν ⊗ dx^μ \right)

Since the components of the Faraday tensor are antisymmetric
(:math:`F_{μν}=-F_{νμ}`), we have:

.. math::

   F^{♭♭} &= \frac{1}{2} F_{μν} \: dx^μ ⊗ dx^ν - \frac{1}{2} F_{νμ} \: dx^ν ⊗ dx^μ \\
          &= \frac{1}{2} F_{μν} \: dx^μ ⊗ dx^ν + \frac{1}{2} F_{μν} \: dx^μ ⊗ dx^ν \\
          &= F_{μν} \: dx^μ ⊗ dx^ν

The fundamental difference between the Faraday tensor and the Faraday 2-form is
that the Faraday tensor innerhently has 4 ⨯ 4 = 16 components, of which only 6
are independent when taking into account the symmetries. The Faraday tensor is
written with 16 components in row-column representation as:

.. topic:: Faraday tensor

   .. math::

      \begin{bmatrix}
                            & + \E^x \: dx ⊗ dt & + \E^y \: dy ⊗ dt & + \E^z \: dz ⊗ dt \\
          - \E^x \: dt ⊗ dx &                   & -  B^z \: dy ⊗ dx & +  B^y \: dz ⊗ dx \\
          - \E^y \: dt ⊗ dy & +  B^z \: dx ⊗ dy &                   & -  B^x \: dz ⊗ dy \\
          - \E^z \: dt ⊗ dz & -  B^y \: dx ⊗ dz & +  B^x \: dy ⊗ dz &                   \\
      \end{bmatrix}

In contrast, the Faraday 2--form inherently has 6 independent components and
can be written as a column of 6 elements:

.. topic:: Faraday 2--form

   .. math::

      \left[ \begin{aligned}
          - & \E^x \: dt ∧ dx \\
          - & \E^y \: dt ∧ dy \\
          - & \E^z \: dt ∧ dz \\
            &  B^x \: dy ∧ dz \\
            &  B^y \: dz ∧ dx \\
            &  B^z \: dx ∧ dy \\
      \end{aligned} \right]

From the Faraday 2--form to the doubly covariant Faraday tensor
---------------------------------------------------------------

We can decompose the exterior product into tensor products:

.. math::

   F^{♭♭} = \left[ \begin{alignedat}{2}
       - & \E^x \: ( dt ⊗ dx &-& dx ⊗ dt ) \\
       - & \E^y \: ( dt ⊗ dy &-& dy ⊗ dt ) \\
       - & \E^z \: ( dt ⊗ dz &-& dz ⊗ dt ) \\
         &  B^x \: ( dy ⊗ dz &-& dz ⊗ dy ) \\
         &  B^y \: ( dz ⊗ dx &-& dx ⊗ dz ) \\
         &  B^z \: ( dx ⊗ dy &-& dy ⊗ dx ) \\
   \end{alignedat} \right]

Rerorganizing the terms with a row/column representation, we get the Faraday
tensor:

.. math::

   F^{♭♭} = \begin{bmatrix}
                         & + \E^x \: dx ⊗ dt & + \E^y \: dy ⊗ dt & + \E^z \: dz ⊗ dt \\
       - \E^x \: dt ⊗ dx &                   & -  B^z \: dy ⊗ dx & +  B^y \: dz ⊗ dx \\
       - \E^y \: dt ⊗ dy & +  B^z \: dx ⊗ dy &                   & -  B^x \: dz ⊗ dy \\
       - \E^z \: dt ⊗ dz & -  B^y \: dx ⊗ dz & +  B^x \: dy ⊗ dz &                   \\
   \end{bmatrix}

Difference between tensor basis and bivector basis
--------------------------------------------------

It turns out that the row-column representation in the double covariant tensor
basis :math:`dx^μ ⊗ dx^ν` and the 2--form basis :math:`dx^μ ∧ dx^ν` is the
same. The 2--form basis is related to the double covariant tensor basis
through:

.. math::

   dx^μ ∧ dx^ν = dx^μ ⊗ dx^ν - dx^ν ⊗ dx^μ

Hence we can also write:

.. math::

  F^{♭♭} = \left[ \begin{aligned}
      - & \E^x \: dt ∧ dx \\
      - & \E^y \: dt ∧ dy \\
      - & \E^z \: dt ∧ dz \\
        &  B^x \: dy ∧ dz \\
        &  B^y \: dz ∧ dx \\
        &  B^z \: dx ∧ dy \\
  \end{aligned} \right]
  = \frac{1}{2} \left[ \begin{alignedat}{3}
      - & \E^x \: (dt ∧ dx &+& dt ∧ dx) \\
      - & \E^y \: (dt ∧ dy &+& dt ∧ dy) \\
      - & \E^z \: (dt ∧ dz &+& dt ∧ dz) \\
        &  B^x \: (dy ∧ dz &+& dy ∧ dz) \\
        &  B^y \: (dz ∧ dx &+& dz ∧ dx) \\
        &  B^z \: (dx ∧ dy &+& dx ∧ dy) \\
  \end{alignedat} \right]
  = \frac{1}{2} \left[ \begin{alignedat}{3}
      - & \E^x \: (dt ∧ dx &-& dx ∧ dt) \\
      - & \E^y \: (dt ∧ dy &-& dy ∧ dt) \\
      - & \E^z \: (dt ∧ dz &-& dz ∧ dt) \\
        &  B^x \: (dy ∧ dz &-& dz ∧ dy) \\
        &  B^y \: (dz ∧ dx &-& dx ∧ dz) \\
        &  B^z \: (dx ∧ dy &-& dy ∧ dx) \\
  \end{alignedat} \right]

Which can then be rearanged into a row-column form:

.. math::

   F^{♭♭} = \frac{1}{2} \begin{bmatrix}
                         & + \E^x \: dx ∧ dt & + \E^y \: dy ∧ dt & + \E^z \: dz ∧ dt \\
       - \E^x \: dt ∧ dx &                   & -  B^z \: dy ∧ dx & +  B^y \: dz ∧ dx \\
       - \E^y \: dt ∧ dy & +  B^z \: dx ∧ dy &                   & -  B^x \: dz ∧ dy \\
       - \E^z \: dt ∧ dz & -  B^y \: dx ∧ dz & +  B^x \: dy ∧ dz &                   \\
   \end{bmatrix}

The row-column repesentation with implicit basis is then exactly the same up to
a factor :math:`\frac{1}{2}`:

.. math::

   \begin{bmatrix}
              & + \E^x & + \E^y & + \E^z \\
       - \E^x &        & -  B^z & +  B^y \\
       - \E^y & +  B^z &        & -  B^x \\
       - \E^z & -  B^y & +  B^x &        \\
   \end{bmatrix}

I am laying this here because it personally cost me *a lot* of confusion, since
I expected the same behavoir when lowering or raising the indices, which is not
the case because we are dealing with different basis.

Calulating the mixed Faraday tensor, we have:

.. math::

   F^μ{}_ν = F_{λν} η^{λμ}
