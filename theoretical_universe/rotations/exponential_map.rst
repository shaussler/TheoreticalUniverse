.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Exponential map
===============

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: Draft

2D Euclidean space
------------------

Infinitesimal rotations in 2D Euclidean space are expressed as:

.. math::

   R^{♭♭} = θ \: dx ∧ dy

We take the exponential map:

.. math::

   e^{R^{♭♭}} = \mathbb{1} + R^{♭♭} + \frac{1}{2!} \left( R^{♭♭} \right)^2 + \frac{1}{3!} \left( R^{♭♭} \right)^3 + \cdots

We have:

.. math::

   dx \⌟ \mathbb{1} &= dx \\
   dy \⌟ \mathbb{1} &= dy \\

----

.. math::

   dx \⌟ R^{♭♭} = + θ dy \\
   dy \⌟ R^{♭♭} = - θ dx \\

.. admonition:: Calculations
   :class: dropdown

   .. rubric:: dx

   .. math::

      dx \⌟ R^{♭♭} &= dx \⌟ θ dx ∧ dy \\
                   &= θ dy

   .. rubric:: dy

   .. math::

      dy \⌟ R^{♭♭} &= dy \⌟ θ dx ∧ dy \\
                   &= - dy \⌟ θ dy ∧ dx \\
                   &= - θ dx

----

.. math::

   dx \⌟ \left(R^{♭♭}\right)^2 &= - θ^2 dx \\
   dy \⌟ \left(R^{♭♭}\right)^2 &= - θ^2 dy \\

.. admonition:: Calculations
   :class: dropdown

   .. rubric:: dx

   .. math::

      dx \⌟ \left(R^{♭♭} \right)^2 & = \left(dx \⌟ R^{♭♭} \right) \⌟ R^{♭♭} \\
                                   & = θ dy \⌟ R^{♭♭} \\
                                   & = θ dy \⌟ \left(θ dx ∧ dy\right) \\
                                   & = θ^2 dy \⌟ \left( - dy ∧ dx \right) \\
                                   & = - θ^2 dx \\

   .. rubric:: dy

   .. math::

      dy \⌟ \left(R^{♭♭} \right)^2 & = \left(dy \⌟ R^{♭♭} \right) \⌟ R^{♭♭} \\
                                   & = - θ dx \⌟ R^{♭♭} \\
                                   & = - θ dx \⌟ \left(θ dx ∧ dy\right) \\
                                   & = - θ^2 dx \⌟ \left( dx ∧ dy \right) \\
                                   & = - θ^2 dy \\
----

.. math::

   dx \⌟ \left(R^{♭♭}\right)^3 &= - θ^3 dy \\
   dy \⌟ \left(R^{♭♭}\right)^3 &= + θ^3 dx \\

.. admonition:: Calculations
   :class: dropdown

   .. rubric:: dx

   .. math::

      dx \⌟ \left(R^{♭♭} \right)^3 & = \left(dx \⌟ \left(R^{♭♭}\right)^2 \right) \⌟ R^{♭♭} \\
                                   & = \left( - θ^2 dx \right) \⌟ R^{♭♭} \\
                                   & = - θ^2 dx \⌟ \left(θ dx ∧ dy\right) \\
                                   & = - θ^3 dy

   .. rubric:: dy

   .. math::

      dy \⌟ \left(R^{♭♭} \right)^3 & = \left(dy \⌟ \left(R^{♭♭}\right)^2 \right) \⌟ R^{♭♭} \\
                                   & = \left( - θ^2 dy \right) \⌟ R^{♭♭} \\
                                   & = - θ^2 dy \⌟ \left(θ dx ∧ dy\right) \\
                                   & = - θ^3 dy \⌟ \left(- θ dy ∧ dx\right) \\
                                   & = + θ^3 dx
We then get:

.. math::

   dx \⌟ e^{θ dx ∧ dy}
   = \begin{bmatrix}
       \left( + 1 - \frac{1}{2!} θ^2 + \cdots \right) dx \\
       \left( + θ - \frac{1}{3!} θ^3 + \cdots \right) dy \\
   \end{bmatrix}
   = \begin{bmatrix}
      + cos(θ) dx \\
      + sin(θ) dy \\
   \end{bmatrix}

.. math::

   dy \⌟ e^{θ dx ∧ dy}
   = \begin{bmatrix}
       \left( - θ + \frac{1}{3!} θ^3 + \cdots) \right) dx \\
       \left( + 1 - \frac{1}{2!} θ^2 + \cdots) \right) dy \\
   \end{bmatrix}
   = \begin{bmatrix}
      - sin(θ) dx \\
      + cos(θ) dy \\
   \end{bmatrix}
