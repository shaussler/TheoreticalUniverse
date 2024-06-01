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

.. figure:: _static/hodge_dual_coordinates.png
   :align: center
   :width: 60%

   Basis directions and surfaces

We order vectors and bivectors by the letters :math:`x`, :math:`y`, and
:math:`z`. Cycling directions counterclockwise, we can go from:

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
exactly through the permutations of the spatial directions. I personally had
difficulties with respect to :math:`∂_z ∧ ∂_x`. For a long time, as my natural
inclination was to always order the elements of the basis surfaces
alphabetically and thus take :math:`∂_x ∧ ∂_z`, which result in a negative sign
when flipping the surface :math:`-∂_z ∧ ∂_x`. Taking :math:`∂_z ∧ ∂_x` is the
superior choice.

The Equal Things
----------------

Directions, vectors, and dual covectors are representation of the same thing.

Sufaces, bivectors, and the dual or mixed tensor are representations of the
same object. Rotation matrices with :math:`A=A^T` are the same object as mixed
tensors and without explicit basis.

.. ifconfig:: draft in ('yes')

   .. warning:: Draft content

   Differential as a Covector
   --------------------------

   .. math:: dx^i ∂_j = \frac{∂x^i}{∂x^j} = δ^i_j

   .. math:: dx^i \frac{∂}{∂ x^j} x^l = dx^i δ_j^l

   .. math:: \frac{∂x^i}{∂x^j} x^l= δ^i_j x^l

   Considering a parametric 3surface in a space that can be of higher dimension:

   .. math:: f(x, y, z) = C

   where :math:`C` is a constant and therefore :math:`dC=0` The differential is:

   .. math:: df = dx \frac{∂f}{∂x} + dy \frac{∂f}{∂y} + dz \frac{∂f}{∂z} = 0

   That we rewrite with

   .. math:: df = dx \frac{∂}{∂x} f + dy \frac{∂}{∂y} f + dz \frac{∂}{∂z} f

   .. math:: df = \left(dx \frac{∂}{∂x} + dy \frac{∂}{∂y} + dz \frac{∂}{∂z}\right) f

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
