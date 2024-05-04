.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Differential Operators on Translations in Spacetime
===================================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: Under construction

This article present a systematic analysis of differential operators on vectors.

Spacetime Translations
----------------------

.. {{{

Tanslations in spacetime can occur in six independent directions. Any
translation can be decomposed into a linear combination of basis translations in
each direction:

.. topic:: Rotation in Minkowski Space

   .. math::

      T^♯ = \begin{bmatrix}
          a \; ∂_t \\
          b \; ∂_x \\
          c \; ∂_y \\
          d \; ∂_z \\
      \end{bmatrix}

.. }}}

Spacetime Translations in Differential Forms
--------------------------------------------

.. {{{

The generic translation above is contravariant, given in terms of vectors
corresponding to our physical understanding of space (and time). By flattening,
we obtain the associated covariant differential 1-form representative of the
translation:

.. topic:: Spacetime Translations in Differential Form

   .. math::

      T^♭ = \left[ \begin{aligned}
            & a \; dt \\
          - & b \; dx \\
          - & c \; dy \\
          - & d \; dz \\
      \end{aligned} \right]

.. admonition:: All Calculation Steps
   :class: dropdown

   .. {{{

   Apply the flat operator :math:`♭` to the sharp contravariant translation:

   .. math::

      T^♭ = \begin{bmatrix}
          a \; ∂_t \\
          b \; ∂_x \\
          c \; ∂_y \\
          d \; ∂_z \\
      \end{bmatrix}^♭

   Distribute the flat operator :math:`♭`:

   .. math::

      T^♭ = \begin{bmatrix}
          a \; ∂_t^♭ \\
          b \; ∂_x^♭ \\
          c \; ∂_y^♭ \\
          d \; ∂_z^♭ \\
      \end{bmatrix}

   Apply:

   .. math::

      T^♭ = \begin{bmatrix}
          a \; η_{tμ} \; dx^μ \\
          b \; η_{xμ} \; dx^μ \\
          c \; η_{yμ} \; dx^μ \\
          d \; η_{zμ} \; dx^μ \\
      \end{bmatrix}

   Identify the non-zero components:

   .. math::

      T^♭ = \begin{bmatrix}
          a \; η_{tt} \; dx^t \\
          b \; η_{xx} \; dx^x \\
          c \; η_{yy} \; dx^y \\
          d \; η_{zz} \; dx^z \\
      \end{bmatrix}

   Apply numerical values

   .. math::

      T^♭ = \begin{bmatrix}
          a \; (+1) dx^t \\
          b \; (-1) dx^x \\
          c \; (-1) dx^y \\
          d \; (-1) dx^z \\
      \end{bmatrix}

   Identify the basis covectors:

   .. math::

      dx^t = dt \\
      dx^x = dx \\
      dx^y = dy \\
      dx^z = dz \\

   Conclude:

   .. math::

      T^♭ = \left[ \begin{aligned}
             &a \; dt \\
           - &b \; dx \\
           - &c \; dy \\
           - &d \; dz \\
      \end{aligned} \right]


   .. }}}

Exterior Derivative of a Translation
------------------------------------

.. {{{

.. warning:: Under construction

.. }}}

Laplace-De Rahm
---------------

.. {{{

.. warning:: Under construction

.. }}}
