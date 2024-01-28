Differential operators in differential forms
============================================

.. warning::

   Under construction.

.. rst-class:: custom-author

   by Stéphane Haussler\

In this article, I use the language of differential forms to express the
derivative, the gradient, the divergence, the curl and the laplacian in the
language of differential forms.

I assume the reader possesses a strong grasp of vector calculus and a
functional understanding of differential forms. I personally learned
differential forms with yet another `great video serie by Michael Penn
<https://youtube.com/playlist?list=PL22w63XsKjqzQZtDZO_9s2HEMRJnaOTX7&si=4dDrAZ-oKa1rI7B8>`_.
I will simplify the concept of the Hodge dual, often presented in a needlessly
complex manner, making it more accessible. A basic comprehension of vectors,
covectors, and tensor calculus will enhance the discussion. Familiarity with
the concepts of Grassman Algebra, Clifford Algebra (AKA Geometric Algebra), Lie
Groups and Algebra will certainly be a sign that the reader understand
antisymmetry underlying differential forms

I will be using a pseudo-matrix notation which is not conventional, but that I
hope highlight symmetries and the reader will find obvious.

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

Finally, the basis vector :math:`\mathbf{e}_i` are.

Derivative
----------

The derivative is our basic vector:

.. math::

   \mathbf{e}_i = \partial_i

The basis covectors are the differentials:

.. math::

   \mathbf{e}^i = dx^i

Indeed get:

.. math::

   \mathbf{e}^i \cdot \mathbf{e}_j = dx^i \partial_j = \delta^i_j

Divergence
----------

.. admonition:: Proposition

   .. math::

      \star d \star F^\flat = \nabla^\sharp \cdot F^\sharp
                            = \mathbf{\nabla} \cdot \mathbf{F}

We begin with :math:`F` as a vector :math:`\mathbf{F} = F^\sharp = F^i
\partial_i` and flatten:

.. math::

   F^\flat = \{ F^x \partial_x \\
                F^y \partial_y \\
                F^z \partial_z \}^\flat
           = \{ F^x dx \\
                F^y dy \\
                F^z dz \}

Apply the :math:`\star` operator:

.. math::

   \star F^\flat = \{ F^x \star dx     \\ F^y \star dy     \\ F^z \star dz     \}
                 = \{ F^x dy \wedge dz \\ F^y dz \wedge dx \\ F^z dx \wedge dy \}

.. note::

   Since I have not seen anybody mentioning it or highlighting it, you can see
   the beautiful symmetry out of the Hodge start operator when ordering into
   row and columns of differential forms:

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

Apply the :math:`d` operator:

.. math::

   d \star F^\flat = d \{ F^x dy \wedge dz \\
                          F^y dz \wedge dx \\
                          F^z dx \wedge dy \}
   = \{ \partial_x F^x dx \wedge dy \wedge dz \\
        \partial_y F^y dy \wedge dz \wedge dx \\
        \partial_z F^z dz \wedge dx \wedge dy \}
   = \{ \partial_x F^x dx \wedge dy \wedge dz \\
        \partial_y F^y dx \wedge dy \wedge dz \\
        \partial_z F^z dx \wedge dy \wedge dz \}

Which can be brought back to a zero form by applying yet again the Hodge star: 

.. math::

   \star d \star F^\flat
   = \{ \partial_x F^x \star dx \wedge dy \wedge dz \\
        \partial_y F^y \star dx \wedge dy \wedge dz \\
        \partial_z F^z \star dx \wedge dy \wedge dz \}
   = \{ \partial_x F^x \mathbf{1} \\
        \partial_y F^y \mathbf{1} \\
        \partial_z F^z \mathbf{1} \}
   = \partial_x F^x + \partial_y F^y + \partial_z F^z


.. admonition:: Proposition

   .. math::

      \nabla^\flat F^\sharp = \mathbf{\nabla} \cdot \mathbf{F}

Curl
----

.. admonition:: Proposition

   .. math::
   
      (\star(dF^\flat))^\sharp = \nabla^\sharp \times F^\sharp


The full expression of the curl of a vector field is

.. math::

   \nabla^\sharp \times F^\sharp =
   \{ (\partial_y F^z - \partial F^y) \; \partial_x \\
      (\partial_z F^x - \partial F^z) \; \partial_y \\
      (\partial_x F^y - \partial F^x) \; \partial_z \}

We demonstrate this is also equal to:


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

We can then sharpen the covector to its vector form:

.. math::

   (\star dF^\flat)^\sharp
   =
   \{ (\partial_y F^z - \partial_z F^y) dx^\sharp \\
      (\partial_z F^x - \partial_x F^z) dy^\sharp \\
      (\partial_x F^y - \partial_y F^x) dz^\sharp \}

.. math::

   (\star dF^\flat)^\sharp
   =
   \{ (\partial_y F^z - \partial_z F^y) \px \\
      (\partial_z F^x - \partial_x F^z) \py \\
      (\partial_x F^y - \partial_y F^x) \pt \}

Divergence
----------

Laplacian
---------
