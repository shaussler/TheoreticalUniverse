Basis vectors
=============

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning::

   Under construction

.. The differential of a function is:
.. 
.. .. math::
.. 
..    \begin{equation}
..    df = dx \frac{∂f}{∂x} + dy \frac{∂f}{∂y} + dz \frac{∂f}{∂z}
..    \end{equation}
.. 
.. That we rewrite with 
.. 
.. .. math::
.. 
..    \begin{equation}
..    df = dx \frac{∂}{∂x} f + dy \frac{∂}{∂y} f + dz \frac{∂}{∂z} f
..    \end{equation}
.. 
.. Considering :math:`f(x, y, z)=x`:
.. 
.. .. math::
.. 
..    \begin{equation}
..    dx = dx \frac{∂}{∂x} x + dy \frac{∂}{∂y} x + dz \frac{∂}{∂z} x
..    \end{equation}
.. 
.. And thus:
.. 
.. .. math::
.. 
..    \begin{equation}
..    dφ(x) = dx \frac{∂}{∂x} φ(x)
..    \end{equation}
.. 
.. .. math::
.. 
..    \begin{equation}
..    dφ(x) = α dx
..    \end{equation}
.. 
.. Taking the taylor serie of :math:`φ(x)`:
.. 
.. .. math::
.. 
..    \begin{equation}
..    φ(x) = φ(a) + x \frac{∂}{∂x} φ(x) + ...
..    \end{equation}
.. 
.. We get:
.. 
.. .. math::
.. 
..    \begin{equation}
..    dφ(x) = dx \frac{∂}{∂x} [φ(a) + x \frac{∂}{∂x} φ(x)]
..    \end{equation}
.. 
.. Then
.. 
.. .. math::
.. 
..    \begin{equation}
..    dφ(x) = dx \frac{∂}{∂x} [x α]
..    \end{equation}
.. 
.. .. math::
.. 
..    \begin{equation}
..    dx = dx \frac{∂}{∂x} x
..    \end{equation}
.. 
.. .. math::
.. 
..    \begin{equation}
..    dx \frac{∂}{∂x} = 1
..    \end{equation}
.. 
.. .. math::
.. 
..    \begin{equation}
..    dx \frac{∂}{∂y} = 0
..    \end{equation}
.. 
.. .. math::
.. 
..    \begin{equation}
..    dx \frac{∂}{∂z} = 0
..    \end{equation}
.. 
.. 
.. .. math::
.. 
..    \begin{equation}
..    dx^i ∂_j = δ^i_j
..    \end{equation}
