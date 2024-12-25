.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Exterior Derivative of Translations in Spacetime
================================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: Under construction

Translation in spacetime
------------------------

A generic translation in spacetime expressed as a vector is:

.. math::

   T^♯ = \left[ \begin{alignedat}{2}
       & φ   & ∂_t \\
       & A^x & ∂_x \\
       & A^y & ∂_y \\
       & A^z & ∂_z \\
   \end{alignedat} \right]

Flattened, the translation expressed in differential form is:

.. math::

   T^♭ = \left[ \begin{alignedat}{2}
       & φ   & dt \\
     - & A^x & dx \\
     - & A^y & dy \\
     - & A^z & dz \\
   \end{alignedat} \right]

.. admonition:: Calculations
   :class: dropdown

   Flatten the translation vector:

   .. math::

      T^♭ = \left(T^♯\right)^♭

   Expand:

   .. math::

      T^♭ = \left[ \begin{alignedat}{2}
          & φ   & ∂_t \\
          & A^x & ∂_x \\
          & A^y & ∂_y \\
          & A^z & ∂_z \\
      \end{alignedat} \right]^♭

   Distribute the flat operator to the basis vectors:

   .. math::

      T^♭ = \left[ \begin{alignedat}{2}
          & φ   &  ∂_t^♭ \\
          & A^x &  ∂_x^♭ \\
          & A^y &  ∂_y^♭ \\
          & A^z &  ∂_z^♭ \\
      \end{alignedat} \right]

   Apply the flat operators to each basis vectors:

   .. math::

      T^♭ = \left[ \begin{alignedat}{3}
          & φ   &  η_{tμ} & dx^μ \\
          & A^x &  η_{xμ} & dx^μ \\
          & A^y &  η_{yμ} & dx^μ \\
          & A^z &  η_{zμ} & dx^μ \\
      \end{alignedat} \right]

   Identify non-zero terms:

   .. math::

      T^♭ = \left[ \begin{alignedat}{3}
          & φ   & η_{tt} & dx^t \\
          & A^x & η_{xx} & dx^x \\
          & A^y & η_{yy} & dx^y \\
          & A^z & η_{zz} & dx^z \\
      \end{alignedat} \right]

   Apply numerical values:

   .. math::

      T^♭ = \left[ \begin{alignedat}{2}
          & φ   & dx^t \\
        - & A^x & dx^x \\
        - & A^y & dx^y \\
        - & A^z & dx^z \\
      \end{alignedat} \right]

   Conclude:

   .. math::

      T^♭ = \left[ \begin{alignedat}{2}
          & φ   & dt \\
        - & A^x & dx \\
        - & A^y & dy \\
        - & A^z & dz \\
      \end{alignedat} \right]

Laplace-De Rham
---------------

The Laplace-De Rham operator in Minkowski spacetime is:

.. math::

   d ⋆ d ⋆ + ⋆ d ⋆ d

:math:`dT^♭`
-----------

.. math::

  d T^♭ = d \left[ \begin{alignedat}{2}
       & φ   & dt \\
     - & A^x & dx \\
     - & A^y & dy \\
     - & A^z & dz \\
   \end{alignedat} \right]

.. math::

  d T^♭ = \left[ \begin{alignedat}{2}
     + ∂_x A^t dx ∧ dt & + ∂_y A^t dy ∧ dt & + ∂_z A^t dz ∧ dt \\
     - ∂_t A^x dt ∧ dx & - ∂_y A^x dy ∧ dx & - ∂_z A^x dz ∧ dx \\
  \end{alignedat} \right]

:math:`⋆dT^♭` - Curl
--------------------

.. math::

  ⋆ d T^♭ = ⋆ \left[ \begin{alignedat}{5}
     + & ∂_x A^t dx ∧ dt & + & ∂_y A^t dy ∧ dt & + & ∂_z A^t dz ∧ dt \\
     - & ∂_t A^x dt ∧ dx & - & ∂_y A^x dy ∧ dx & - & ∂_z A^x dz ∧ dx \\
     - & ∂_t A^y dt ∧ dy & - & ∂_z A^y dz ∧ dy & - & ∂_x A^y dx ∧ dy \\
     - & ∂_t A^z dt ∧ dz & - & ∂_x A^z dx ∧ dz & - & ∂_y A^z dy ∧ dz \\
  \end{alignedat} \right]

.. math::

  ⋆ d T^♭ = \left[ \begin{alignedat}{5}
     + & ∂_x A^t dy ∧ dz & + & ∂_y A^t dz ∧ dx & + & ∂_z A^t dx ∧ dy \\
     + & ∂_t A^x dy ∧ dz & + & ∂_y A^x dt ∧ dz & - & ∂_z A^x dt ∧ dy \\
     + & ∂_t A^y dz ∧ dx & + & ∂_z A^y dt ∧ dx & - & ∂_x A^y dt ∧ dz \\
     + & ∂_t A^z dx ∧ dy & + & ∂_x A^z dt ∧ dy & - & ∂_y A^z dt ∧ dx \\
  \end{alignedat} \right]

.. math::

  ⋆ d T^♭ = \left[ \begin{alignedat}{4}
     (+ & ∂_z A^y & - & ∂_y A^z &) \; dt ∧ dx \\
     (+ & ∂_x A^z & - & ∂_z A^x &) \; dt ∧ dy \\
     (+ & ∂_y A^x & - & ∂_x A^y &) \; dt ∧ dz \\
     (+ & ∂_x A^t & + & ∂_t A^x &) \; dy ∧ dz \\
     (+ & ∂_y A^t & + & ∂_t A^y &) \; dz ∧ dx \\
     (+ & ∂_z A^t & + & ∂_t A^z &) \; dx ∧ dy \\
  \end{alignedat} \right]

:math:`d⋆dT^♭` - Divergence
---------------------------

.. math::

  d ⋆ d T^♭ = d \left[ \begin{alignedat}{4}
     (+ & ∂_z A^y & - & ∂_y A^z &) \; dt ∧ dx \\
     (+ & ∂_x A^z & - & ∂_z A^x &) \; dt ∧ dy \\
     (+ & ∂_y A^x & - & ∂_x A^y &) \; dt ∧ dz \\
     (+ & ∂_x A^t & + & ∂_t A^x &) \; dy ∧ dz \\
     (+ & ∂_y A^t & + & ∂_t A^y &) \; dz ∧ dx \\
     (+ & ∂_z A^t & + & ∂_t A^z &) \; dx ∧ dy \\
  \end{alignedat} \right]

With :math:`Π` denoting all permutations over :math:`{x, y, z}`.

.. math::

  d ⋆ d T^♭ = Π d \left[ \begin{alignedat}{4}
     (+ & ∂_z A^y & - & ∂_y A^z &) \; dt ∧ dx \\
     (+ & ∂_x A^t & + & ∂_t A^x &) \; dy ∧ dz \\
  \end{alignedat} \right]

Apply the exterior derivative

.. math::

  d ⋆ d T^♭ = Π d \left[ \begin{alignedat}{4}
     ∂_y (+ & ∂_z A^y & - & ∂_y A^z &) \; dy ∧ dt ∧ dx \\
     ∂_z (+ & ∂_z A^y & - & ∂_y A^z &) \; dz ∧ dt ∧ dx \\
     ∂_t (+ & ∂_x A^t & + & ∂_t A^x &) \; dt ∧ dy ∧ dz \\
     ∂_x (+ & ∂_x A^t & + & ∂_t A^x &) \; dx ∧ dy ∧ dz \\
  \end{alignedat} \right]

Rearange:

.. math::

  d ⋆ d T^♭ = Π d \left[ \begin{alignedat}{4}
     (- & ∂_y^2   A^z & + & ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
     (- & ∂_z^2   A^y & + & ∂_y ∂_z A^z & ) \; dt ∧ dz ∧ dx \\
     (+ & ∂_t^2   A^x & + & ∂_t ∂_x A^t & ) \; dt ∧ dy ∧ dz \\
     (+ & ∂_x^2   A^t & + & ∂_t ∂_x A^x & ) \; dx ∧ dy ∧ dz \\
  \end{alignedat} \right]

Rearange:

.. math::

  d ⋆ d T^♭ = Π d \left[ \begin{alignedat}{4}
     (+ & ∂_x^2   A^t & + & ∂_t ∂_x A^x & ) \; dx ∧ dy ∧ dz \\
     (+ & ∂_t^2   A^x & + & ∂_t ∂_x A^t & ) \; dt ∧ dy ∧ dz \\
     (- & ∂_z^2   A^y & + & ∂_y ∂_z A^z & ) \; dt ∧ dz ∧ dx \\
     (- & ∂_y^2   A^z & + & ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
  \end{alignedat} \right]

Expand permutations:

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

Simplify and conclude:

.. math::

  d ⋆ d T^♭ = \left[ \begin{alignedat}{7}
     ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; dx ∧ dx ∧ dy \\
     ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; dt ∧ dy ∧ dz \\
     ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; dt ∧ dz ∧ dx \\
     ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
  \end{alignedat} \right]

:math:`⋆d⋆dT^♭`
---------------

.. math::

  ⋆ d ⋆ d T^♭ = ⋆ \left[ \begin{alignedat}{7}
     ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; dx ∧ dx ∧ dy \\
     ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; dt ∧ dy ∧ dz \\
     ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; dt ∧ dz ∧ dx \\
     ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; dt ∧ dx ∧ dy \\
  \end{alignedat} \right]

Conclude:

.. math::

  ⋆ d ⋆ d T^♭ = \left[ \begin{alignedat}{7}
     ( & + ∂_x^2 A^t & + ∂_y^2 A^t & + ∂_z^2 A^t & + ∂_t ∂_x A^x & + ∂_t ∂_y A^y & + ∂_t ∂_z A^z & ) \; dt \\
     ( & + ∂_t^2 A^x & - ∂_y^2 A^x & - ∂_z^2 A^x & + ∂_t ∂_x A^t & + ∂_x ∂_y A^y & + ∂_z ∂_x A^z & ) \; dx \\
     ( & + ∂_t^2 A^y & - ∂_x^2 A^y & - ∂_z^2 A^y & + ∂_t ∂_y A^t & + ∂_y ∂_z A^z & + ∂_x ∂_y A^x & ) \; dy \\
     ( & + ∂_t^2 A^z & - ∂_x^2 A^z & - ∂_y^2 A^z & + ∂_t ∂_z A^t & + ∂_z ∂_x A^x & + ∂_y ∂_z A^y & ) \; dz \\
  \end{alignedat} \right]


