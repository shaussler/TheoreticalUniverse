.. Theoretical Universe (c) by Stéphane Haussler

.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

Potential formulation via differential forms
============================================

.. rst-class:: custom-author

   by Stéphane Haussler

.. warning:: This is a very first draft

In this page, I derive the potential formulation of the equations of Mr.
Maxwell via differential form. This article in its current form is a first
draft and may contain errors.

.. rubric:: Inhomogenous Maxwell equations via differential forms

.. math::

   d\:⋆ \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right]
   = \begin{bmatrix}
     + μ_0 c ρ \; dx ∧ dy ∧ dz\\
     - μ_0 J^x \; dt ∧ dy ∧ dz\\
     - μ_0 J^y \; dt ∧ dz ∧ dx\\
     - μ_0 J^z \; dt ∧ dx ∧ dy\\
   \end{bmatrix}

.. rubric:: Homogenous Maxwell equations via differential forms

.. math::

   d \left[ \begin{aligned}
     - & \E^x \; dt ∧ dx \\
     - & \E^y \; dt ∧ dy \\
     - & \E^z \; dt ∧ dz \\
       &  B^x \; dy ∧ dz \\
       &  B^y \; dz ∧ dx \\
       &  B^z \; dx ∧ dy \\
   \end{aligned} \right]
   = 0

.. math::

   d F^{♭♭} = 0

.. rubric:: Potential formulation

Taking the exterior derivative of any differential form :math:`A` twice is zero

.. math::

   ddA = 0

Since :math:`dA = F^{♭♭}`, we can infer that :math:`A` is a one-form
:math:`A=A^{♭}`. From the Homogenous equations we obtain:

.. math::

   d\:d \left[ \begin{alignedat}{2}
     - & φ   & dt \\
       & A^x & dx \\
       & A^y & dy \\
       & A^z & dz \\
   \end{alignedat} \right]
   = 0

Now from the inhomogenous equations:

.. math::

   d\:⋆ d\left[ \begin{alignedat}{2}
     - & φ   \; & dt \\
       & A^x \; & dx \\
       & A^y \; & dy \\
       & A^z \; & dz \\
   \end{alignedat} \right]
   = \begin{bmatrix}
     + μ_0 c ρ \; dx ∧ dy ∧ dz \\
     - μ_0 J^x \; dt ∧ dy ∧ dz \\
     - μ_0 J^y \; dt ∧ dz ∧ dx \\
     - μ_0 J^z \; dt ∧ dx ∧ dy \\
   \end{bmatrix}

Maxwell Equations are in short form:

.. math::

   d ⋆ d A^♭ = J^{♭♭♭}

As expected, we can add a term do A of the form :math:`dα` since this is
guaranteed to be zero and :math:`α` can be any form:

.. math::

   α = number + \left[ \begin{aligned}
      α^t \; dt \\
      α^x \; dx \\
      α^y \; dy \\
      α^z \; dz \\
   \end{aligned} \right]
   + \left[ \begin{aligned}
         α^? \; d? ∧ d? \\
         α^? \; d? ∧ d? \\
         α^? \; d? ∧ d? \\
         α^? \; d? ∧ d? \\
   \end{aligned} \right]
   + \left[ \begin{aligned}
         α^? \; dx ∧ dy ∧ dz \\
         α^? \; dt ∧ dy ∧ dz \\
         α^? \; dt ∧ dz ∧ dx \\
         α^? \; dt ∧ dx ∧ dy \\
   \end{aligned} \right]




