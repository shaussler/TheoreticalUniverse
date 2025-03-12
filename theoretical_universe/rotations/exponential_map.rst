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

   R^{♭♭} = θ dx ∧ dy

We take the exponential map:

.. math::

   e^{R^{♭♭}} = \mathbb{1} + R^{♭♭} + \frac{1}{2!} \left( R^{♭♭} \right)^2 + \frac{1}{3!} \left( R^{♭♭} \right)^3 + \cdots

We have:

.. math::

   \newcommand{\⌟}{\:⌟\:}
   dx \⌟ \mathbb{1} = dx

.. math::

   \newcommand{\⌟}{\:⌟\:}
   dx \⌟ R^{♭♭} = dx \⌟ θ dx ∧ dy = θ dy

.. math::

   \newcommand{\⌟}{\:⌟\:}
   dx \⌟ \frac{1}{2!} \left(R^{♭♭} \right)^2 & = \frac{1}{2!} \left(dx \⌟ R^{♭♭} \right) \⌟ R^{♭♭} \\
                                             & = \frac{1}{2!} θ dy \⌟ R^{♭♭} \\
                                             & = \frac{1}{2!} θ dy \⌟ θ dx ∧ dy \\
                                             & = \frac{1}{2!} θ^2 dy \⌟ \left( - dy ∧ dx \right) \\
                                             & = - \frac{1}{2!} θ^2 dx \\

.. math::

   \newcommand{\⌟}{\:⌟\:}
   dx \⌟ \frac{1}{3!} \left(R^{♭♭} \right)^3 & = \frac{1}{3!} \left(dx \⌟ \left(R^{♭♭}\right)^2 \right) \⌟ R^{♭♭} \\
                                             & = \frac{1}{3!} \left( - θ^2 dx \right) \⌟ R^{♭♭} \\
                                             & = - \frac{1}{3!} θ^2 dx \⌟ θ dx ∧ dy \\
                                             & = - \frac{1}{3!} θ^3 dy

We then get:

.. math::

   dx ⌟ exp\left( θ dx ∧ dy \right) =
   \begin{bmatrix}
       \left( 1 - \frac{1}{2!} θ^2 + \cdots \right) dx \\
       \left( θ - \frac{1}{3!} θ^3 + \cdots \right) dy \\
   \end{bmatrix}
   = \begin{bmatrix}
      cos(θ) dx \\
      sin(θ) dy \\
   \end{bmatrix}
