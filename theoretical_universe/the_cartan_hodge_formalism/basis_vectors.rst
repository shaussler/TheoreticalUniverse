.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Basis vectors
=============

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: Under construction

.. _orientation_of_space:

Orientation of space
--------------------

.. image:: _static/hodge_dual_coordinates.png
   :align: center
   :width: 60%

.. ifconfig:: draft in ('yes')

   .. warning:: Draft

   Differential as a covector
   --------------------------

   .. {{{

   The differential of a function is:

   .. math:: df = dx \frac{∂f}{∂x} + dy \frac{∂f}{∂y} + dz \frac{∂f}{∂z}

   That we rewrite with

   .. math:: df = dx \frac{∂}{∂x} f + dy \frac{∂}{∂y} f + dz \frac{∂}{∂z} f

   Considering :math:`f(x, y, z)=x`:

   .. math:: dx = dx \frac{∂}{∂x} x + dy \frac{∂}{∂y} x + dz \frac{∂}{∂z} x

   And thus:

   .. math:: dφ(x) = dx \frac{∂}{∂x} φ(x)

   .. math:: dφ(x) = α dx

   Taking the taylor serie of :math:`φ(x)`:

   .. math:: φ(x) = φ(a) + x \frac{∂}{∂x} φ(x) + ...

   We get:

   .. math:: dφ(x) = dx \frac{∂}{∂x} [φ(a) + x \frac{∂}{∂x} φ(x)]

   Then

   .. math:: dφ(x) = dx \frac{∂}{∂x} [x α]

   .. math:: dx = dx \frac{∂}{∂x} x

   .. math:: dx \frac{∂}{∂x} = 1

   .. math:: dx \frac{∂}{∂y} = 0

   .. math:: dx \frac{∂}{∂z} = 0

   .. math:: dx^i ∂_j = δ^i_j

   .. }}}
