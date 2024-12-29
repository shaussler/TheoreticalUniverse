.. Theoretical Universe (c) by Stéphane Haussler

.. theoretical universe is licensed under a creative commons attribution 4.0
.. international license. you should have received a copy of the license along
.. with this work. if not, see <https://creativecommons.org/licenses/by/4.0/>.

Permutation operator
====================

.. rst-class:: custom-author

   by Stéphane Haussler

To shorten calculations, but at the cost of additional notation, I sometime use
an operator that I refer to as the *permutation operator* :math:`Π`. This
operator loops through all even permutations of the spatial dimensions
:math:`{x, y, z}`, enabling me to perform a single calculation instead of
repeating it for each specific ordering.

For example, rather than performing separate calculations for :math:`{x, y,
z}`, :math:`{y, z, x}`, and :math:`{z, x, y}`, the permutation operator
reduces these to a single iteration loop:

.. math::

   Π (y dx + x dy) = \left[ \begin{alignedat}{1}
       y dx & + x & dy \\
       z dy & + y & dz \\
       x dz & + z & dx \\
   \end{alignedat} \right]
