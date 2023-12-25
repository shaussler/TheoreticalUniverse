The musical notation presents a notable difference with the widespread
row/column representation of a doubly contravariant tensor. Concretely, the
doubly contravariant electromagnetic tensor is generally written as a
row/column matrix where the indices :math:`\mu` and :math:`\nu` represent the
row and column respectively. The Faraday tensor with metrix signature
:math:`(+,-,-,-)` is then expressed as:

.. math::

   F^{\mu\nu}=
   \{
            & -\Ex & -\Ey & -\Ez \\
       +\Ex &      & -\Bz & +\By \\
       +\Ey & +\Bz &      & -\Bx \\
       +\Ez & -\By & +\Bx &      \\
   \}

You will find this form in `the wikipedia article on the electromagnetic tensor
<https://en.wikipedia.org/wiki/Electromagnetic_tensor>`_.
In musical notation, the doubly contravariant tensor is expressed as a row of
rows. The indices :math:`\mu` and :math:`\nu` represent the indices of the
first and seconds rows respectively. The doubly contravariant Faraday tensor is
then expressed as:

.. math::

   F^{\sharp\sharp}=
   \{
            & +\Ex & +\Ey & +\Ez \\
       -\Ex &      & +\Bz & -\By \\
       -\Ey & -\Bz &      & +\Bx \\
       -\Ez & +\By & -\Bx &      \\
   \}^{\sharp\sharp}

The relation between the row/column and the row/row representations is a
transpose:

.. math::

   \{
            & -\Ex & -\Ey & -\Ez \\
       +\Ex &      & -\Bz & +\By \\
       +\Ey & +\Bz &      & -\Bx \\
       +\Ez & -\By & +\Bx &      \\
   \}^{T}
   =
   \{
            & +\Ex & +\Ey & +\Ez \\
       -\Ex &      & +\Bz & -\By \\
       -\Ey & -\Bz &      & +\Bx \\
       -\Ez & +\By & -\Bx &      \\
   \}^{\sharp\sharp}
