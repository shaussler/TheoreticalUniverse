Differential as a Covector
==========================

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
