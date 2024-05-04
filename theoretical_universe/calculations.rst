Calculations
============

Rotations
---------

.. rubric:: Divergence ⋆ d ⋆

.. {{{

.. code:: python

   R.hodge_star().d.hodge_star().math_output()

.. code:: python

   '- ∂_x a - ∂_y b - ∂_z c dt  +  - ∂_t a - ∂_z e + ∂_y f dx  +  - ∂_t b + ∂_z d - ∂_x f dy  +  - ∂_t c - ∂_y d + ∂_x e dz'

.. math::

   ⋆ d ⋆ R = \begin{bmatrix}\begin{alignat*}{1}
       (&         & - ∂_x a & - ∂_y b & - ∂_z c &) \; dt \\
       (& - ∂_t a &         & + ∂_y f & - ∂_z e &) \; dx \\
       (& - ∂_t b & - ∂_x f &         & + ∂_z d &) \; dy \\
       (& - ∂_t c & + ∂_x e & - ∂_y d &         &) \; dz \\
   \end{alignat*}\end{bmatrix}

.. }}}

Translations
------------

.. rubric:: Gradient d

.. {{{

.. code:: python

   T.d.math_output()

.. code:: python

   '- ∂_x a - ∂_t b dt∧dx  +  - ∂_y a - ∂_t c dt∧dy  +  - ∂_z a - ∂_t d dt∧dz  +  ∂_y b - ∂_x c dx∧dy  +  ∂_z b - ∂_x d dx∧dz  +  ∂_z c - ∂_y d dy∧dz'

.. math::

   d T = \begin{alignat*}{1}
       (& - ∂_t b & - ∂_x a &         &         &) \; dt∧dx \\
       (& - ∂_t c &         & - ∂_y a &         &) \; dt∧dy \\
       (& - ∂_t d &         &         & - ∂_z a &) \; dt∧dz \\
       (&         &         & - ∂_y d & + ∂_z c &) \; dy∧dz \\
       (&         & + ∂_x d &         & - ∂_z b &) \; dz∧dx \\
       (&         & - ∂_x c & + ∂_y b &         &) \; dx∧dy \\
   \end{alignat*}

.. }}}

.. rubric:: Divergence ⋆ d ⋆

.. {{{

.. code:: python

   T.hodge_star().d.hodge_star().math_output()

.. code:: python

   '0'

.. math::

   ⋆ d ⋆ T = 0

.. }}}

.. rubric:: Curl ⋆ d

.. {{{

.. code:: python

   T.d.hodge_star().math_output()

.. code:: python

   '∂_z c - ∂_y d dt∧dx  +  - ∂_z b + ∂_x d dt∧dy  +  ∂_y b - ∂_x c dt∧dz  +  ∂_z a + ∂_t d dx∧dy  +  - ∂_y a - ∂_t c dx∧dz  +  ∂_x a + ∂_t b dy∧dz'

.. math::

   ⋆ d T = \begin{bmatrix}
   \begin{alignat*}{1}
       (&        &         & - ∂_y d & + ∂_z c &) \; dt∧dx \\
       (&        & + ∂_x d &         & - ∂_z b &) \; dt∧dy \\
       (&        & - ∂_x c & + ∂_y b &         &) \; dt∧dz \\
       (&+ ∂_t b & + ∂_x a &         &         &) \; dy∧dz \\
       (&+ ∂_t c &         & + ∂_y a &         &) \; dz∧dx \\
       (&+ ∂_t d &         &         & + ∂_z a &) \; dx∧dy \\
   \end{alignat*}
   \end{bmatrix}

.. }}}
