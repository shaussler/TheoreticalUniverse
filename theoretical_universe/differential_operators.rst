Differential operators as differential forms
============================================

Notation
--------

The vector field :math:`\mathbf{F}` is noted with the musical isomorphism
:math:`\sharp` as :math:`F^\sharp`, which either declare :math:`F` is a vector,
or transform a covector to a vector:

.. math::

   \mathbf{F}=F^\sharp=(F^\sharp)^\sharp=(F^\flat)^\sharp

The component of :math:`F^\sharp` are noted with upper indices consistently
with the rules of Ricci calculus and utilizing Einstein summation convention.

.. math::

   F^\sharp = F^i \partial_i = F_i \partial^i = g^{il} F_l \partial_i

Where :math:`g` is the metric tensor, and thus:

.. math::

   \begin{align}
   g_{ij} &= \partial_i \cdot \partial_j \\
   g^{ij} &= dx^i \cdot dx^j
   \end{align}

Finally, the basis vector :math:`\mathbf{e}_i` are:

.. math::

   \mathbf{e}_i = \partial_i

An the basis covectors are:

.. math::

   \mathbf{e}^i = dx^i

Curl
----

The full expression of the curl of a vector field is

.. math::

   \nabla^\sharp \times F^\sharp =
   \{ (\py F^z - \pz F^y) \px \\
      (\pz F^x - \px F^z) \py \\
      (\px F^y - \py F^x) \pz \}

We demonstrate this is also equal to:

.. math::

   \nabla^\sharp \times F^\sharp = (\star(dF^\flat))^\sharp

The vector field is:

.. math::

   F^\sharp = \{ F^x \px \\ F^y \py \\ F^z \pz \}
            = F^x \px + F^y \py + F^z \pz

Flattening the vector field result in:

.. math::

   F^\flat = \{ F^x dx \\ F^y dy \\ F^z dz \}
           = F^x dx + F^y dy + F^z dz

Taking the differential, we have: 

.. math::

   dF^\flat =
   \{ \partial_x F^x dx \wedge dx & \partial_y F^x dy \wedge dx & \partial_z F^x dz \wedge dx \\
      \partial_x F^y dx \wedge dy & \partial_y F^y dy \wedge dy & \partial_z F^y dz \wedge dy \\
      \partial_x F^z dx \wedge dz & \partial_y F^z dy \wedge dy & \partial_z F^z dz \wedge dz \}

Or with more natural row/column convention:

.. math::

   dF^\flat =
   \{ \partial_x F^x dx \wedge dx & \partial_x F^y dx \wedge dy & \partial_x F^z dx \wedge dz \\
      \partial_y F^x dy \wedge dx & \partial_y F^y dy \wedge dy & \partial_y F^z dy \wedge dy \\
      \partial_z F^x dz \wedge dx & \partial_z F^y dz \wedge dy & \partial_z F^z dz \wedge dz \}

Where :math:`dx^i \wedge dx^i = 0`:

.. math::

   dF^\flat =
   \{                             & \partial_x F^y dx \wedge dy & \partial_x F^z dx \wedge dz \\
      \partial_y F^x dy \wedge dx &                             & \partial_y F^z dy \wedge dy \\
      \partial_z F^x dz \wedge dx & \partial_z F^y dz \wedge dy &                             \}


And :math:`dx^i \wedge dx^j = -dx^j \wedge dx^i`:

.. math::

   dF^\flat =
   \{                              & +\partial_x F^y dx \wedge dy & -\partial_x F^z dz \wedge dx \\
      -\partial_y F^x dx \wedge dy &                              & +\partial_y F^z dy \wedge dy \\
      +\partial_z F^x dz \wedge dx & -\partial_z F^y dy \wedge dz &                              \}

That we reorder to:

.. math::

   dF^\flat =
   \{ +\partial_y F^z dy \wedge dy - \partial_z F^y dy \wedge dz \\
      +\partial_z F^x dz \wedge dx - \partial_x F^z dz \wedge dx \\
      +\partial_x F^y dx \wedge dy - \partial_y F^x dx \wedge dy \}

.. math::

   dF^\flat =
   \{ (\partial_y F^z - \partial_z F^y) dy \wedge dz \\
      (\partial_z F^x - \partial_x F^z) dz \wedge dx \\
      (\partial_x F^y - \partial_y F^x) dx \wedge dy \}

Where we can now take the star operator:

.. math::

   \star dF^\flat =
   \{ (\partial_y F^z - \partial_z F^y) \star dy \wedge dz \\
      (\partial_z F^x - \partial_x F^z) \star dz \wedge dx \\
      (\partial_x F^y - \partial_y F^x) \star dx \wedge dy \}

.. math::

   \star dF^\flat =
   \{ (\partial_y F^z - \partial_z F^y) dx \\
      (\partial_z F^x - \partial_x F^z) dy \\
      (\partial_x F^y - \partial_y F^x) dz \}


