Deriving the Faraday-Maxwell Tensor from the 1865 Maxwell Equations
===================================================================

.. warning:: Under construction

In this article, I present a simple and elegant derivation of the
Faraday-Maxwell tensor. This derivation is strongly inspired by Minkowski's
1908 paper: `The Fundamental Equations for Electromagnetic Processes in Moving
Bodies
<https://en.wikisource.org/wiki/Translation:The_Fundamental_Equations_for_Electromagnetic_Processes_in_Moving_Bodies>`_.

You may find the derivation obvious, but I do not think it is well known as I
could not find it anywhere. If I am mistaken and you know of a textbook,
youtube video, or some place in the internet, please let me know and I will add
a reference. You can open an issue or directly correct and send a merge request
on my `github repository
<https://github.com/shaussler/electromagnetism/actions/runs/6444649784>`_.

Mr. Maxwell published in 1865 `A Dynamical Theory of the Electromagnetic Field
<https://en.m.wikipedia.org/wiki/A_Dynamical_Theory_of_the_Electromagnetic_Field>`_
(`pdf <https://www.jstor.org/stable/108892>`_).
The original formulation uses differential expressions, as opposed to the
modern vector formulation proposed by Mr. Heaviside. We had no concept of
vectors in 1865!

Equations of Mr. Heaviside
--------------------------

Mr. Heaviside formulated the Maxwell equations in vector form is the most known
formulation. I thus start from there and unpack the euations to the original
maxwell equation. The well known equations in the form first laid down by Mr.
Heaviside is:

* Gauss's law: 
* Gauss's law for magnetism
* Faraday-Maxwell's equation
* Amp\'ere-Maxwell's equation

.. math::

   \begin{align}
   \overrightarrow{\nabla} \cdot \overrightarrow{E} &= \rho / \epsilon_0 \\
   \overrightarrow{\nabla} \cdot \overrightarrow{B} &= 0 \\
   \overrightarrow{\nabla} \times \overrightarrow{E} &= \partial_t \overrightarrow{B} \\
   \overrightarrow{\nabla} \times \overrightarrow{B} &= \mu_0 \overrightarrow{J} + \frac{1}{c^2} \partial_t \overrightarrow{E}
   \end{align}

This form corresponds to the 1865 Maxwell formulation, albeit with modern
notation and conventions. So by doing that we obtain:

.. todo::
  
   Here I would like to use :math:`\partial_t = \frac{1}{c} \frac{\partial}{\partial_t}` and :math:`\tilde{E^i}=\frac{E^i}{c}`

**Gauss's law**

.. math::

   \partial_x E^x + \partial_y E^y + \partial_z E^z = \rho / \epsilon_0

**Gauss's law for magnetism**

.. math::

   \partial_x B^x + \partial_y B^y + \partial_z B^z = 0

**Faraday-Maxwell equations**

.. math::

   \begin{align}
   \partial_y E^z - \partial_z E^y &= - \partial_t B^x \\
   \partial_z E^x - \partial_x E^z &= - \partial_t B^y \\
   \partial_x E^y - \partial_y E^x &= - \partial_t B^z \\
   \end{align}

**Ampere-Maxwell equations**

.. math::

   \begin{align}
   \partial_y B^z - \partial_z B^y &= \mu_0 J^x + \frac{1}{c^2} \partial_t E^x \\
   \partial_z B^x - \partial_x B^z &= \mu_0 J^y + \frac{1}{c^2} \partial_t E^y \\
   \partial_x B^y - \partial_y B^x &= \mu_0 J^z + \frac{1}{c^2} \partial_t E^z \\
   \end{align}


Taking inspiration from Mr. Minkowski, I reorder these equations in a manner
which may suddenly strike as extremely obvious. Note how the terms that are not
there are now as important as the terms which are there.


.. warning::

   to be deleted

   .. image:: _static/reordered_maxwell_equations.jpg
      :alt: Reordered Maxwell equations
      :scale: 50


Inhomogenous equations
----------------------

Gauss's law and Maxwell-Faraday equation

.. math::

   \begin{matrix}
                            & +\partial_x \tilde{E^x} & +\partial_y \tilde{E^y} & +\partial_y \tilde{E^z} & = & + \mu_0 c \rho  \\
    +\partial_t \tilde{E^x} &                         & +\partial_y        B^z  & -\partial_z        B^y  & = & - \mu_0 J^x     \\
    +\partial_t \tilde{E^y} & +\partial_x        B^z  &                         & -\partial_z        B^x  & = & - \mu_0 J^y     \\
    +\partial_t \tilde{E^z} & -\partial_x \      B^y  & +\partial_y        B^x  &                         & = & - \mu_0 J^z     \\
   \end{matrix}

Homogenous equations
--------------------

Gauss law for magnetism and Ampere equations

.. math::

   \begin{matrix}
                            & +                  B^x  & +                  B^y  & +                  B^z  & = & 0 \\
    +\partial_t        B^x  &                         & +\partial_y \tilde{E^z} & -\partial_z \tilde{E^y} & = & 0 \\
    +\partial_t        B^y  & -\partial_x \tilde{E^z} &                         & +\partial_z \tilde{E^x} & = & 0 \\
    +\partial_t        B^z  & +\partial_x \tilde{E^y} & -\partial_y \tilde{E^x} &                         & = & 0 \\
   \end{matrix}


.. todo::
  
   Just have a quick recal that :math:`\partial_{\mu} \eta^{\mu \nu}=\partial^{\nu}` and that we end up with:

   .. math::

      \begin{bmatrix}
      \partial_t & \partial_x & \partial_y & \partial_z
      \end{bmatrix}
      \begin{bmatrix}
       1 &  0 &  0 &  0 \\
       0 & -1 &  0 &  0 \\
       0 &  0 & -1 &  0 \\
       0 &  0 &  0 & -1
      \end{bmatrix}
      = 
      \begin{bmatrix}
        \partial_t \\
      - \partial_x \\
      - \partial_y \\
      - \partial_z \\
      \end{bmatrix}

**Homogenous equations**
(Gauss's law and Maxwel-Ampere equation)

And from there, to anyone familiar with matrix computation, the Farady-Maxwell
tensor as well as its hodge dual should appear.

.. note::

   This is a note
