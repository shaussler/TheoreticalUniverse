Rotations in differential forms
===============================

.. rst-class:: custom-author

   by Stéphane Haussler

Since I have not seen anybody mentioning it or highlighting it, you can see the
symmetry pop out of the Hodge start operator when ordering into row and columns
of differential forms:

.. math::

   \begin{align}
   \star F^\flat &= \{                   & F^z dx \wedge dy &                  \\
                                         &                  & F^x dy \wedge dz \\
                        F^y dz \wedge dx &                  &                  \} \\
                 &= \frac{1}{2}
                    \{                   & +F^z dx \wedge dy & -F^y dx \wedge dz \\
                       -F^z dy \wedge dx &                   & +F^x dy \wedge dz \\
                       +F^y dz \wedge dx & -F^x dz \wedge dy &                   \}
   \end{align}

With implicit vector and surface basis vectors, we obtain:

.. math::

   \star F^\flat
   = \star \{ F^x \\ F^y \\ F^z \}^\flat
   = \frac{1}{2}
     \{      & +F^z & -F^y \\
        -F^z &      & +F^x \\
        +F^y & -F^x &      \}^\flat
