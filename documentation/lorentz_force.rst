Lorentz Force
=============

.. math::

   \bv{F} = q (\bv{E} + \bv{v} \times \bv{B})

.. math::

   \frac{1}{q}\frac{d^2 \bv{r}}{dt^2} = \bv{E} + \frac{d\bv{r}}{dt} \times \bv{B}

.. math::

   \begin{align} 
   \frac{1}{q} \frac{d v^x}{dt} & = E^x + v^y B^z - v^z B^y \\
   \frac{1}{q} \frac{d v^y}{dt} & = E^y + v^z B^x - v^x B^z \\
   \frac{1}{q} \frac{d v^z}{dt} & = E^z + v^x B^y - v^z B^x \\
   \end{align}


.. math::

   \begin{align} 
   \frac{1}{q} \frac{d^2 x}{dt^2} & = E^x + \frac{dy}{dt} B^z - \frac{dz}{dt} B^y \\
   \frac{1}{q} \frac{d^2 y}{dt^2} & = E^y + \frac{dz}{dt} B^x - \frac{dx}{dt} B^z \\
   \frac{1}{q} \frac{d^2 z}{dt^2} & = E^z + \frac{dx}{dt} B^y - \frac{dy}{dt} B^x \\
   \end{align}

Things to think about:

.. math::

   f_\nu = q u^\mu F_{\mu\nu}
