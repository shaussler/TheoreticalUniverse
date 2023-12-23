Lagrangian
==========

Derivation
----------

The form of the Lagragian can be derived from the Work performed on a test particle.

The work performed by a force :math:`\vec{F}` along a path :math:`\mathcal{C}`
parameterized with time :math:`t` is:

.. math::

   W 
   = \int_{\mathcal{C}} dW 
   = \int_{\mathcal{C}} \vec{F} \cdot \vec{dr}
   = \int_{t_i}^{t_f} \vec{F}(t) \cdot \vec{v}(t) \cdot dt

Newtown's second law states that the force is equals to the mass multiplied by
the seconds derivative of displacement (acceleration), or equivalently the
first derivative of the velocity:

.. math::

   \vec{F} &= m \frac{d^2\vec{r}}{dt^2} \\

The work the force shall perform over path :math:`\mathcal{C}` in order to
modify velocity is:

.. math::

   W_K = \int_{t_a}^{t_b} m \frac{d^2\vec{r}}{dt^2} d\vec{r}

.. warning::
 
   The formula below is wrong

.. math::

   W_K =  \int_{v(t_a)}^{v(t_b)} m \frac{dv}{dt} \cdot v \cdot dt

.. math::

   W_K =  \int_{\partial \gamma} \frac{1}{2} m \cdot \vec{v}^2

Where :math:`\partial \gamma` is understood as the evalution at the endpoints
of the trajectory in phase space. The work depends only on initial and final
velocities hence :math:`\partial \gamma=\partial \gamma [\vec{v}(t_i);
\vec{v}(t_f)]`. The force resulting from a potential :math:`U(\vec{r})` and
corresponding work is:

.. math::
  
   \vec{F}= - \vec{\nabla} U(\vec{r})

.. math::

   W_U = \int_{\mathcal{C}} - \vec{\nabla} U(\vec{r}) d\vec{r}

The negative sign results from the convention that work done against a force
field increases the potential energy. A conservative force depends only on the
initial and final positions, independent of the path taken:

.. math::

   W_U = \int_{\partial \gamma} - U(\vec{r}) 

Where :math:`\partial \gamma` is understood as the evalution at the endpoints
of the trajectory in phase space. The work depends only on initial and final
positions hence :math:`\partial \gamma=\partial \gamma [\vec{r}(t_i);
\vec{r}(t_f)]`. 

:math:`\partial \gamma` for both :math:`W_K` and :math:`W_U` are: 

.. math::

   \begin{cases}
   W_K: \partial \gamma=\partial \gamma [\vec{v}(t_i); \vec{v}(t_f)] \\ 
   W_U: \partial \gamma=\partial \gamma [\vec{r}(t_i); \vec{r}(t_f)] 
   \end{cases}

Thus we have:

.. math::

   \partial \gamma = \partial \gamma [\vec{r}(t_i), \vec{v}(t_i); \vec{r}(t_f), \vec{v}(t_f)]

With :math:`K` being the kinetic energy, :math:`T` the potential energy and
:math:`\mathcal{L}` the lagrangian, we have:



.. math::

   \begin{cases}
   K=\frac{1}{2} m \cdot \left( \frac{d\vec{r}}{dt} \right)^2 \\
   T=U(\vec{r}) 
   \end{cases}

   W_K + W_U &= \int_{\partial \gamma} K - T\\
   W_K + W_U &= \int_{\partial \gamma} \mathcal{L}

Assuming that the force due to the potential is the same as the force due to
the second law is the same as minimizing the functional. 

.. math::

   \int_{t_i}^{t_f} \mathcal{L(t, q_i, \dot{q_i})}dt

Thus we look to solve the Euler-Lagrange equation:

.. math::

   \frac{\partial}{\partial q_i} \mathcal{L} - \frac{d}{dt} \frac{ \partial \mathcal{L}}{ \partial \dot{q_i}}
   = 0

with :math:`\mathcal{L}:M \times TM \times \mathbb{R} \to \mathbb{R}``

Free fall from height
---------------------

.. math::

   W  &= \int_{t_a}^{t_b} \left( m \frac{d^2 z}{dt^2} - mg \right)  dz \\
      &= \int_{t_a}^{t_b}  m \frac{d v}{dt} v dt - \int_{t_a}^{t_b} mg v dt \\
      &= \frac{1}{2} m v^2 - mgh


.. math::

   \vec{r} = \vec{r}(t, q_i(t), \dot{q_i}(t))

