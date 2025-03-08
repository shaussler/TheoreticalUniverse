.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Relation between the Faraday tensor and the Faraday 2-form
==========================================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: under construction

In abstract index notation, the doubly covariant Faraday tensor is expressed without its tensor
basis as:

.. math::

   F_{μν}

The same, explicitely writing the tensor basis, is:

.. math::

   F_{μν} \: dx^μ ⊗ dx^ν

The expression of the Faraday tensor as a 2-form is:

.. math::

   F^{♭♭} = \frac{1}{2} F_{μν} \: dx^μ ∧ dx^ν

We can rewrite the exterior product as a tensor product:

.. math::

   F^{♭♭} = \frac{1}{2} F_{μν} \: \left( dx^μ ⊗ dx^ν - dx^ν ⊗ dx^μ \right)

Since the components of the Faraday tensor are antisymmetric (:math:`F_{μν}=-F_{νμ}`),
we have:

.. math::

   F^{♭♭} &= \frac{1}{2} F_{μν} \: dx^μ ⊗ dx^ν - \frac{1}{2} F_{νμ} \: dx^ν ⊗ dx^μ \\
          &= \frac{1}{2} F_{μν} \: dx^μ ⊗ dx^ν + \frac{1}{2} F_{μν} \: dx^μ ⊗ dx^ν \\
          &= F_{μν} \: dx^μ ⊗ dx^ν

The fundamental difference between the Faraday tensor and the Faraday 2-form is
that the Faraday tensor innerhently has :math:`4 ⨯ 4 = 16` components, of which
only 6 are independent when taking into account the symmetries. Hence the
Faraday tensor is written with 16 components as:

.. math::

   \frac{1}{2} \begin{bmatrix}
                         & + \E^x \: dx ⊗ dt & + \E^y \: dy ⊗ dt & + \E^z \: dz ⊗ dt \\
       - \E^x \: dt ⊗ dx &                   & -  B^z \: dy ⊗ dx & +  B^y \: dz ⊗ dx \\
       - \E^y \: dt ⊗ dy & +  B^z \: dx ⊗ dy &                   & -  B^x \: dz ⊗ dy \\
       - \E^z \: dt ⊗ dz & -  B^y \: dx ⊗ dz & +  B^x \: dy ⊗ dz &                   \\
   \end{bmatrix}

In contrast, the Faraday two form simply has 6 components and can be written
as a column of 6 elements:

.. math::

   \left[ \begin{aligned}
       - & \E^x \; dt ∧ dx \\
       - & \E^y \; dt ∧ dy \\
       - & \E^z \; dt ∧ dz \\
         &  B^x \; dy ∧ dz \\
         &  B^y \; dz ∧ dx \\
         &  B^z \; dx ∧ dy \\
   \end{aligned} \right]

Calulating the mixed Faraday tensor, we have:

.. math::

   F^μ{}_ν = F_{λν} η^{λμ}
