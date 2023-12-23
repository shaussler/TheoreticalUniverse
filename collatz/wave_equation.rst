Wave equation
=============

Analysis of the harmonic oscillator and the wave equation.

Harmonic oscillator
-------------------

Derivation
''''''''''

Spring harmonic oscillator

.. math::

   F &= - k \cdot x

   F &= m \frac{d^2 x}{dt^2}

Result in the harmonic oscillator equation:

.. math::

   \frac{d^2 x}{dt^2} + \frac{k}{m} \cdot x(t)= 0

Where the solutions are:

.. math::

   x(t) &= A \cdot cos(\omega \cdot t + \varphi) \\
        &= A \cdot cos(\sqrt{\frac{k}{m}} \cdot t + \varphi) 

since:

.. math::

   \frac{d^2x(t)}{dt^2}=A \cdot \omega^2 \cdot u(x)


Energy of the harmonic oscillator
'''''''''''''''''''''''''''''''''

.. note::

   To be completed

Complex representation
----------------------

.. math::

   e^{i \theta} = cos(\theta) + i \cdot sin(\theta)

Then:

.. math::

   cos(\theta) &= \Re(e^{i \theta}) \\
   cos(\theta) &= \frac{e^{i \theta} + e^{-i \theta}}{2}

The result of the harmonic oscillator is:

.. math::

   x(t) &= A \cdot \Re(e^{i (\omega \cdot t + \varphi) }) \\
   x(t) &= \frac{A}{2} \cdot \left[ e^{i(\omega \cdot t + \varphi)} + e^{-i( \omega \cdot t + \varphi)}\right]

Wave equation
-------------

Derivation
''''''''''

.. math::

   \frac{\partial^2 \vec{u}}{\partial t^2} - \nabla^2 \vec{u} = 0

Where the operation on :math:`\vec{u}` can be rewritten as:

.. math::

   \frac{\partial^2 }{\partial t^2} - \nabla^2 =
   \left[\frac{\partial }{\partial t} - \nabla \right] \cdot
   \left[\frac{\partial }{\partial t} + \nabla \right]
   
The solutions in a reference frame chosen orientated along the direction of
movement :math:`\vec{k}` are of the form:

.. math::
  
   F(\vec{k} \cdot \vec{u} - v \cdot t) + G(\vec{k} \cdot \vec{u} + v \cdot t)

Where :math:`F` and :math:`G` can be any function, and in particular can be the
harmonic oscillator. Or, with the :math:`\mathcal{x}` axis oriented along
propagation:

.. math::

   F(x - c\cdot t) + G(x + c \cdot t) + \text{const.}


Momentum
''''''''

.. note::

   Is the equation above enough to define and calculate momentum of a
   propagating string?

Angular momentum
''''''''''''''''

.. note::

   Is the equation above enough to define and calculate the angular momentum of
   a propagating string? or is the harminic necessary?

Harmonic wave equation
----------------------

The harmonic wave equation is a solution of both:

.. math::

   \frac{d^2 \vec{u}}{dt^2} + \omega \cdot \vec{u} = 0

and 

.. math::

   \frac{\partial^2 \vec{u}}{\partial t^2} - \nabla^2 \vec{u} = 0

And therefore also a solution to:

.. math::

   2 \frac{\partial^2 \vec{u}}{\partial t^2} - \nabla^2 \vec{u} + \omega \cdot \vec{u} = 0

We know from the harmonic oscillator equation and the wave equation the
solutions are combinations of:

.. math::

   x(t) &= A \cdot \Re\left[e^{i (\omega \cdot t + \varphi \pm v \cdot t)} \right] + \text{const}\\
   x(t) &= \frac{A}{2} \cdot \left[ e^{i(\omega \cdot t + \varphi \pm v \cdot t)} + 
                                    e^{-i( \omega \cdot t + \varphi \pm v \cdot t)}
                             \right] + \text{const}

The constant is separated in a term depending on the initial phase :math:`A
\cdot cos(\varphi)` and a further constant :math:`const.`. For simplicity, we
concentrate on:

.. math::

   x(t) &= A \cdot \Re\left[e^{i (\omega \cdot t + \varphi - v \cdot t)} \right] \\
   x(t) &= \frac{A}{2} \cdot \left[ e^{i(\omega \cdot t + \varphi - v \cdot t)} + 
                                    e^{-i( \omega \cdot t + \varphi - v \cdot t)}
                             \right]


.. note::

   Identification with special relativity

.. math::

   \frac{\partial^2 y}{\partial t^2} - v^2 y = - (2 \pi f_{min})^2 y

.. math::

   f^2=\left( \frac{c}{\lambda}\right)^2+f_{min}^2

.. math::

   E = h \cdot f

.. math::

   E^2 = \left( \frac{h \cdot c }{\lambda} \right) + \left( h \cdot f_{min} \right)^2

.. math::

   E^2 = p^2 \cdot c^2 + (m \cdot c^2)^2

.. math::

   p=\frac{h}{\lambda}



