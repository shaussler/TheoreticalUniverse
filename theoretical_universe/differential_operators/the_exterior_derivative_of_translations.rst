.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Translations in Minkowski space
===============================

.. rst-class:: custom-author

   by Stéphane Haussler

Translations
------------

.. {{{

A generic translation in spacetime is expressed with a 4-vector:

.. math::

   T^♯ = \left[ \begin{alignedat}{1}
       A^t & ∂_t \\
       A^x & ∂_x \\
       A^y & ∂_y \\
       A^z & ∂_z \\
   \end{alignedat} \right]

Flattened, the translation expressed in differential form is:

.. math::

   T^♭ = \left[ \begin{alignedat}{2}
         & A^t & dt \\
       - & A^x & dx \\
       - & A^y & dy \\
       - & A^z & dz \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: References

   * :ref:`basis vectors`
   * :ref:`musicality`

   .. rubric:: Flatten the translation vector

   .. math::

      T^♭ = \left(T^♯\right)^♭

   .. rubric:: Expand

   .. math::

      T^♭ = \left[ \begin{alignedat}{1}
          A^t & ∂_t \\
          A^x & ∂_x \\
          A^y & ∂_y \\
          A^z & ∂_z \\
      \end{alignedat} \right]^♭

   .. rubric:: Distribute the flat operator to the basis vectors

   .. math::

      T^♭ = \left[ \begin{alignedat}{1}
          A^t & ∂_t^♭ \\
          A^x & ∂_x^♭ \\
          A^y & ∂_y^♭ \\
          A^z & ∂_z^♭ \\
      \end{alignedat} \right]

   .. rubric:: Apply the flat operators to each basis vectors

   .. math::

      T^♭ = \left[ \begin{alignedat}{2}
          A^t & η_{tμ} & dx^μ \\
          A^x & η_{xμ} & dx^μ \\
          A^y & η_{yμ} & dx^μ \\
          A^z & η_{zμ} & dx^μ \\
      \end{alignedat} \right]

   .. rubric:: Identify non-zero terms

   .. math::

      T^♭ = \left[ \begin{alignedat}{2}
          A^t & η_{tt} & dx^t \\
          A^x & η_{xx} & dx^x \\
          A^y & η_{yy} & dx^y \\
          A^z & η_{zz} & dx^z \\
      \end{alignedat} \right]

   .. rubric:: Apply numerical values

   .. math::

      T^♭ = \left[ \begin{alignedat}{2}
          A^t &     & dx^t \\
          A^x & (-) & dx^x \\
          A^y & (-) & dx^y \\
          A^z & (-) & dx^z \\
      \end{alignedat} \right]

   .. rubric:: Rearange and conclude

   .. math::

      T^♭ = \left[ \begin{alignedat}{2}
          & A^t & dt \\
        - & A^x & dx \\
        - & A^y & dy \\
        - & A^z & dz \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`⋆ T^♭`
-------------

.. {{{

.. math::

   ⋆ T^♭ = \left[ \begin{alignedat}{2}
         & A^t & dx ∧ dy ∧ dz \\
       - & A^x & dt ∧ dy ∧ dz \\
       - & A^y & dt ∧ dz ∧ dx \\
       - & A^z & dt ∧ dx ∧ dy \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: References

   * :ref:`Hodge dual tables`

   .. rubric:: Apply the Hodge star to all

   .. math::

      ⋆ T^♭ = ⋆ \left[ \begin{alignedat}{2}
            & A^t & dt \\
          - & A^x & dx \\
          - & A^y & dy \\
          - & A^z & dz \\
      \end{alignedat} \right]

   .. rubric:: Distribute the Hodge star to each

   .. math::

      ⋆ T^♭ = \left[ \begin{alignedat}{3}
            & A^t & ⋆ & dt \\
          - & A^x & ⋆ & dx \\
          - & A^y & ⋆ & dy \\
          - & A^z & ⋆ & dz \\
      \end{alignedat} \right]

   .. rubric:: Apply the Hodge star and conclude

   .. math::

      ⋆ T^♭ = \left[ \begin{alignedat}{2}
            & A^t & dx ∧ dy ∧ dz \\
          - & A^x & dt ∧ dy ∧ dz \\
          - & A^y & dt ∧ dz ∧ dx \\
          - & A^z & dt ∧ dx ∧ dy \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`d T^♭`
-------------

.. {{{

.. math::

   d T^♭ = \left[ \begin{alignedat}{1}
       ( & - & ∂_t A^x & - & ∂_x A^t) & \; dt ∧ dx \\
       ( & - & ∂_t A^y & - & ∂_y A^t) & \; dt ∧ dy \\
       ( & - & ∂_t A^z & - & ∂_z A^t) & \; dt ∧ dz \\
       ( & - & ∂_y A^z & + & ∂_z A^y) & \; dy ∧ dz \\
       ( & - & ∂_z A^x & + & ∂_x A^z) & \; dz ∧ dx \\
       ( & - & ∂_x A^y & + & ∂_y A^x) & \; dx ∧ dy \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Take the exterior derivative

   .. math::

      d T^♭ = d \left[ \begin{alignedat}{2}
            & A^t & dt \\
          - & A^x & dx \\
          - & A^y & dy \\
          - & A^z & dz \\
      \end{alignedat} \right]

   .. rubric:: Apply the exterior derivative

   .. math::

      d T^♭ = \begin{bmatrix}
          + ∂_x A^t dx ∧ dt & + ∂_y A^t dy ∧ dt & + ∂_z A^t dz ∧ dt \\
          - ∂_t A^x dt ∧ dx & - ∂_y A^x dy ∧ dx & - ∂_z A^x dz ∧ dx \\
          - ∂_t A^y dt ∧ dy & - ∂_z A^y dz ∧ dy & - ∂_x A^y dx ∧ dy \\
          - ∂_t A^z dt ∧ dz & - ∂_x A^z dx ∧ dz & - ∂_y A^z dy ∧ dz \\
      \end{bmatrix}

   .. rubric:: Rearrange and conclude

   .. math::

      d T^♭ = \left[ \begin{alignedat}{1}
          ( & - & ∂_t A^x & - & ∂_x A^t) & \; dt ∧ dx \\
          ( & - & ∂_t A^y & - & ∂_y A^t) & \; dt ∧ dy \\
          ( & - & ∂_t A^z & - & ∂_z A^t) & \; dt ∧ dz \\
          ( & - & ∂_y A^z & + & ∂_z A^y) & \; dy ∧ dz \\
          ( & - & ∂_z A^x & + & ∂_x A^z) & \; dz ∧ dx \\
          ( & - & ∂_x A^y & + & ∂_y A^x) & \; dx ∧ dy \\
      \end{alignedat} \right]

   .. }}}

.. }}}

:math:`d⋆ T^♭`
--------------

.. {{{

.. math::

   d ⋆ T^♭ = \left( ∂_t A^t + ∂_x A^x + ∂_y A^y + ∂_z A^z \right) \; dt ∧ dx ∧ dy ∧ dz

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: References

   * :ref:`Hodge dual tables`

   .. rubric:: Apply the exterior derivative

   .. math::

      d ⋆ T^♭ = d \left[ \begin{alignedat}{2}
            & A^t & dx ∧ dy ∧ dz \\
          - & A^x & dt ∧ dy ∧ dz \\
          - & A^y & dt ∧ dz ∧ dx \\
          - & A^z & dt ∧ dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Expand the exterior derivative

   .. math::

      d ⋆ T^♭ = \left[ \begin{alignedat}{2}
            & ∂_t A^t & dt ∧ dx ∧ dy ∧ dz \\
          - & ∂_x A^x & dx ∧ dt ∧ dy ∧ dz \\
          - & ∂_y A^y & dy ∧ dt ∧ dz ∧ dx \\
          - & ∂_z A^z & dz ∧ dt ∧ dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Reorder the exterior products

   .. math::

      d ⋆ T^♭ = \left[ \begin{alignedat}{2}
          ∂_t A^t & dt ∧ dx ∧ dy ∧ dz \\
          ∂_x A^x & dt ∧ dx ∧ dy ∧ dz \\
          ∂_y A^y & dt ∧ dx ∧ dy ∧ dz \\
          ∂_z A^z & dt ∧ dx ∧ dy ∧ dz \\
      \end{alignedat} \right]

   .. rubric:: Conclude

   .. math::

      d ⋆ T^♭ = \left( ∂_t A^t + ∂_x A^x + ∂_y A^y + ∂_z A^z \right) \; dt ∧ dx ∧ dy ∧ dz

   .. }}}

.. }}}

:math:`⋆d T^♭`
--------------

.. {{{

.. math::

  ⋆ d T^♭ = \left[ \begin{alignedat}{4}
     (+ & ∂_z A^y & - & ∂_y A^z & ) & \; dt ∧ dx \\
     (+ & ∂_x A^z & - & ∂_z A^x & ) & \; dt ∧ dy \\
     (+ & ∂_y A^x & - & ∂_x A^y & ) & \; dt ∧ dz \\
     (+ & ∂_x A^t & + & ∂_t A^x & ) & \; dy ∧ dz \\
     (+ & ∂_y A^t & + & ∂_t A^y & ) & \; dz ∧ dx \\
     (+ & ∂_z A^t & + & ∂_t A^z & ) & \; dx ∧ dy \\
  \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: References

   * :ref:`Hodge dual tables`

   .. rubric:: Take the Hodge star

   .. math::

      ⋆ d T^♭ = ⋆ \left[ \begin{alignedat}{1}
          ( & - & ∂_t A^x & - & ∂_x A^t & ) & \; dt ∧ dx \\
          ( & - & ∂_t A^y & - & ∂_y A^t & ) & \; dt ∧ dy \\
          ( & - & ∂_t A^z & - & ∂_z A^t & ) & \; dt ∧ dz \\
          ( & - & ∂_y A^z & + & ∂_z A^y & ) & \; dy ∧ dz \\
          ( & - & ∂_z A^x & + & ∂_x A^z & ) & \; dz ∧ dx \\
          ( & - & ∂_x A^y & + & ∂_y A^x & ) & \; dx ∧ dy \\
      \end{alignedat} \right]

   .. rubric:: Distribute the Hodge star

   .. math::

      ⋆ d T^♭ = \left[ \begin{alignedat}{1}
          ( & - & ∂_t A^x & - & ∂_x A^t) & \; ⋆ \left( dt ∧ dx \right) \\
          ( & - & ∂_t A^y & - & ∂_y A^t) & \; ⋆ \left( dt ∧ dy \right) \\
          ( & - & ∂_t A^z & - & ∂_z A^t) & \; ⋆ \left( dt ∧ dz \right) \\
          ( & - & ∂_y A^z & + & ∂_z A^y) & \; ⋆ \left( dy ∧ dz \right) \\
          ( & - & ∂_z A^x & + & ∂_x A^z) & \; ⋆ \left( dz ∧ dx \right) \\
          ( & - & ∂_x A^y & + & ∂_y A^x) & \; ⋆ \left( dx ∧ dy \right) \\
      \end{alignedat} \right]

   .. rubric:: Apply the Hodge star

   .. math::

      ⋆ d T^♭ = \left[ \begin{alignedat}{1}
          ( & - & ∂_t A^x & - & ∂_x A^t) & \; & - & \left( dy ∧ dz \right) \\
          ( & - & ∂_t A^y & - & ∂_y A^t) & \; & - & \left( dz ∧ dx \right) \\
          ( & - & ∂_t A^z & - & ∂_z A^t) & \; & - & \left( dx ∧ dy \right) \\
          ( & - & ∂_y A^z & + & ∂_z A^y) & \; &   & \left( dt ∧ dx \right) \\
          ( & - & ∂_z A^x & + & ∂_x A^z) & \; &   & \left( dt ∧ dy \right) \\
          ( & - & ∂_x A^y & + & ∂_y A^x) & \; &   & \left( dt ∧ dz \right) \\
      \end{alignedat} \right]

   .. rubric:: Reorder and conclude

   .. math::

     ⋆ d T^♭ = \left[ \begin{alignedat}{4}
        ( + & ∂_z A^y & - & ∂_y A^z & ) & \; dt ∧ dx \\
        ( + & ∂_x A^z & - & ∂_z A^x & ) & \; dt ∧ dy \\
        ( + & ∂_y A^x & - & ∂_x A^y & ) & \; dt ∧ dz \\
        ( + & ∂_x A^t & + & ∂_t A^x & ) & \; dy ∧ dz \\
        ( + & ∂_y A^t & + & ∂_t A^y & ) & \; dz ∧ dx \\
        ( + & ∂_z A^t & + & ∂_t A^z & ) & \; dx ∧ dy \\
     \end{alignedat} \right]

   .. }}}

.. }}}

:math:`⋆d⋆ T^♭`
---------------

.. {{{

.. math::

   ⋆d⋆ T^♭ = ∂_t A^t + ∂_x A^x + ∂_y A^y + ∂_z A^z

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the Hodge star

   .. math::

      ⋆ d ⋆ T^♭ = ⋆ \left( ∂_t A^t + ∂_x A^x + ∂_y A^y + ∂_z A^z \right) \; dt ∧ dx ∧ dy ∧ dz

   .. rubric:: Conclude

   .. math::

      ⋆ d ⋆ T^♭ = ∂_t A^t + ∂_x A^x + ∂_y A^y + ∂_z A^z

   .. }}}

.. }}}

:math:`d⋆d T^♭`
---------------

.. {{{

.. math::

  d⋆d T^♭ = \left[ \begin{alignedat}{7}
     ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; dx ∧ dx ∧ dy \\
     ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; dt ∧ dy ∧ dz \\
     ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; dt ∧ dz ∧ dx \\
     ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
  \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the exterior derivative to all

   .. math::

     d ⋆ d T^♭ = d \left[ \begin{alignedat}{4}
        (+ & ∂_z A^y & - & ∂_y A^z &) \; dt ∧ dx \\
        (+ & ∂_x A^z & - & ∂_z A^x &) \; dt ∧ dy \\
        (+ & ∂_y A^x & - & ∂_x A^y &) \; dt ∧ dz \\
        (+ & ∂_x A^t & + & ∂_t A^x &) \; dy ∧ dz \\
        (+ & ∂_y A^t & + & ∂_t A^y &) \; dz ∧ dx \\
        (+ & ∂_z A^t & + & ∂_t A^z &) \; dx ∧ dy \\
     \end{alignedat} \right]

   .. rubric:: Collapse permutations

   .. math::

     d ⋆ d T^♭ = Π d \left[ \begin{alignedat}{4}
        (+ & ∂_z A^y & - & ∂_y A^z &) \; dt ∧ dx \\
        (+ & ∂_x A^t & + & ∂_t A^x &) \; dy ∧ dz \\
     \end{alignedat} \right]

   .. rubric:: Apply the exterior derivative

   .. math::

     d ⋆ d T^♭ = Π d \left[ \begin{alignedat}{4}
        ∂_y (+ & ∂_z A^y & - & ∂_y A^z &) \; dy ∧ dt ∧ dx \\
        ∂_z (+ & ∂_z A^y & - & ∂_y A^z &) \; dz ∧ dt ∧ dx \\
        ∂_t (+ & ∂_x A^t & + & ∂_t A^x &) \; dt ∧ dy ∧ dz \\
        ∂_x (+ & ∂_x A^t & + & ∂_t A^x &) \; dx ∧ dy ∧ dz \\
     \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

     d ⋆ d T^♭ = Π d \left[ \begin{alignedat}{4}
        (- & ∂_y^2 A^z & + & ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
        (- & ∂_z^2 A^y & + & ∂_y ∂_z A^z & ) \; dt ∧ dz ∧ dx \\
        (+ & ∂_t^2 A^x & + & ∂_t ∂_x A^t & ) \; dt ∧ dy ∧ dz \\
        (+ & ∂_x^2 A^t & + & ∂_t ∂_x A^x & ) \; dx ∧ dy ∧ dz \\
     \end{alignedat} \right]

   .. rubric:: Rearange

   .. math::

     d ⋆ d T^♭ = Π d \left[ \begin{alignedat}{4}
        (+ & ∂_x^2 A^t & + & ∂_t ∂_x A^x & ) \; dx ∧ dy ∧ dz \\
        (+ & ∂_t^2 A^x & + & ∂_t ∂_x A^t & ) \; dt ∧ dy ∧ dz \\
        (- & ∂_z^2 A^y & + & ∂_y ∂_z A^z & ) \; dt ∧ dz ∧ dx \\
        (- & ∂_y^2 A^z & + & ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
     \end{alignedat} \right]

   .. rubric:: Expand permutations

   .. math::

     d ⋆ d T^♭ = \left[ \begin{alignedat}{4}
        (+ & ∂_x^2 A^t & + & ∂_t ∂_x A^x & ) \; dx ∧ dy ∧ dz \\
        (+ & ∂_y^2 A^t & + & ∂_t ∂_y A^y & ) \; dx ∧ dz ∧ dx \\
        (+ & ∂_z^2 A^t & + & ∂_t ∂_z A^z & ) \; dx ∧ dx ∧ dy \\
        %
        (+ & ∂_t^2 A^x & + & ∂_t ∂_x A^t & ) \; dt ∧ dy ∧ dz \\
        (+ & ∂_t^2 A^y & + & ∂_t ∂_y A^t & ) \; dt ∧ dz ∧ dx \\
        (+ & ∂_t^2 A^z & + & ∂_t ∂_z A^t & ) \; dt ∧ dx ∧ dy \\
        %
        (- & ∂_z^2 A^y & + & ∂_y ∂_z A^z & ) \; dt ∧ dz ∧ dx \\
        (- & ∂_x^2 A^z & + & ∂_z ∂_x A^x & ) \; dt ∧ dx ∧ dy \\
        (- & ∂_y^2 A^x & + & ∂_x ∂_y A^y & ) \; dt ∧ dy ∧ dz \\
        %
        (- & ∂_y^2 A^z & + & ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
        (- & ∂_z^2 A^x & + & ∂_z ∂_x A^z & ) \; dt ∧ dy ∧ dz \\
        (- & ∂_x^2 A^y & + & ∂_x ∂_y A^x & ) \; dt ∧ dz ∧ dx \\
     \end{alignedat} \right]

   .. rubric:: Simplify and conclude

   .. math::

     d ⋆ d T^♭ = \left[ \begin{alignedat}{7}
        ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; dx ∧ dx ∧ dy \\
        ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; dt ∧ dy ∧ dz \\
        ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; dt ∧ dz ∧ dx \\
        ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
     \end{alignedat} \right]

   .. }}}

.. }}}

:math:`d⋆d⋆ T^♭`
----------------

.. {{{

.. math::

   d⋆d⋆ T^♭ = \left[ \begin{alignedat}{7}
       ( & ∂_t ∂_x A^x & + & ∂_t ∂_y A^y & + & ∂_t ∂_z A^z & ) & \; dt \\
       ( & ∂_t ∂_x A^t & + & ∂_x ∂_y A^y & + & ∂_z ∂_z A^z & ) & \; dx \\
       ( & ∂_t ∂_y A^t & + & ∂_y ∂_z A^z & + & ∂_x ∂_y A^x & ) & \; dy \\
       ( & ∂_t ∂_z A^t & + & ∂_z ∂_x A^x & + & ∂_y ∂_z A^y & ) & \; dz \\
  \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the exterior derivative

   .. math::

      d ⋆ d ⋆ T^♭ = d (∂_t A^t + ∂_x A^x + ∂_y A^y + ∂_z A^z)

   .. rubric:: Reorder

   .. math::

      d ⋆ d ⋆ T^♭ = \left[ \begin{alignedat}{7}
          d (∂_t A^t) \\
          d (∂_x A^x) \\
          d (∂_y A^y) \\
          d (∂_z A^z) \\
     \end{alignedat} \right]

   .. rubric:: Apply the exterior derivative

   .. math::

      d ⋆ d ⋆ T^♭ = \left[ \begin{alignedat}{7}
          ∂_x ∂_t A^t dx & + & ∂_y ∂_t A^t dy & + & ∂_z ∂_t A^t dz \\
          ∂_t ∂_x A^x dt & + & ∂_y ∂_x A^x dy & + & ∂_z ∂_x A^x dz \\
          ∂_t ∂_y A^y dt & + & ∂_x ∂_y A^y dx & + & ∂_z ∂_y A^y dz \\
          ∂_t ∂_z A^z dt & + & ∂_x ∂_z A^z dx & + & ∂_y ∂_z A^z dy \\
     \end{alignedat} \right]

   .. rubric:: Reorder, simplify and conclude

   .. math::

      d ⋆ d ⋆ T^♭ = \left[ \begin{alignedat}{7}
          ( & ∂_t ∂_x A^x & + & ∂_t ∂_y A^y & + & ∂_t ∂_z A^z & ) & \; dt \\
          ( & ∂_x ∂_t A^t & + & ∂_x ∂_y A^y & + & ∂_x ∂_z A^z & ) & \; dx \\
          ( & ∂_y ∂_t A^t & + & ∂_y ∂_z A^z & + & ∂_y ∂_x A^x & ) & \; dy \\
          ( & ∂_z ∂_t A^t & + & ∂_z ∂_x A^x & + & ∂_z ∂_y A^y & ) & \; dz \\
     \end{alignedat} \right]

   .. }}}

.. }}}

:math:`⋆d⋆d T^♭`
----------------

.. {{{

.. math::

  ⋆d⋆d T^♭ = \left[ \begin{alignedat}{7}
     ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; dt \\
     ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; dx \\
     ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; dy \\
     ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; dz \\
  \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   .. {{{

   .. rubric:: Apply the Hodge star to all

   .. math::

     ⋆ d ⋆ d T^♭ = ⋆ \left[ \begin{alignedat}{7}
        ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; dx ∧ dx ∧ dy \\
        ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; dt ∧ dy ∧ dz \\
        ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; dt ∧ dz ∧ dx \\
        ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
     \end{alignedat} \right]

   .. rubric:: Apply the Hodge star to each

   .. math::

     ⋆ d ⋆ d T^♭ = \left[ \begin{alignedat}{7}
        ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; ⋆ (dx ∧ dx ∧ dy) \\
        ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; ⋆ (dt ∧ dy ∧ dz) \\
        ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; ⋆ (dt ∧ dz ∧ dx) \\
        ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; ⋆ (dt ∧ dx ∧ dy) \\
     \end{alignedat} \right]

   .. rubric:: Conclude

   .. math::

     ⋆ d ⋆ d T^♭ = \left[ \begin{alignedat}{7}
        ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; dt \\
        ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; dx \\
        ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; dy \\
        ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; dz \\
     \end{alignedat} \right]

   .. }}}

.. }}}

:math:`(⋆d⋆d - d⋆d⋆) T^♭`
-------------------------

.. {{{

.. math::

  (⋆ d ⋆ d - d ⋆ d ⋆) T^♭ = \left[ \begin{alignedat}{7}
     ( &             & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & ) \; dt \\
     ( & + ∂_t^2 A^x &             & - ∂_y^2 A^x & - ∂_z^2 A^x & ) \; dx \\
     ( & + ∂_t^2 A^y & - ∂_x^2 A^y &             & - ∂_z^2 A^y & ) \; dy \\
     ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z &             & ) \; dz \\
  \end{alignedat} \right]

.. }}}
