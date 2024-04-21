.. Theoretical Universe (c) by Stéphane Haussler
.. 
.. Theoretical Universe is licensed under a Creative Commons Attribution 4.0
.. International License. You should have received a copy of the license along
.. with this work. If not, see <https://creativecommons.org/licenses/by/4.0/>.

.. _differential_operators_in_differential_form:

Differential Operators in Differential Form
===========================================

The exterior derivative permits to express and generalize all differential
operators. In this serie of articles, I systematically translate the
differential operators in the :ref:`Cartan-Hodge formalism
<the_cartan_hodge_formalism>` to obtain:

.. rubric:: Gradiant

.. math::

   \begin{equation}
   (df)^{♯} = \mathbf{∇} f
   \end{equation}

.. rubric:: Divergence

.. math::

   \begin{equation}
   ⋆ d ⋆ F^♭t = \mathbf{∇} \cdot \mathbf{F}
   \end{equation}

.. rubric:: Curl

.. math::

   \begin{equation}
   (⋆(dF^♭))^♯ = ∇^♯ ⨯ F^♯
   \end{equation}

.. rubric:: Laplacian

.. math::

   \begin{equation}
   ⋆ d ⋆ d f = \mathbf{∇}^2 f
   \end{equation}

Going towards the expression of the Maxwell equations in differential form, I
apply the exterior derivative :math:`d` to a spacetime rotation expressed in
differential form, as well as its Hodge dual :math:`⋆` to obtain:

.. rubric:: Exterior Derivative of Rotations in Differential Form

.. math::

   \begin{equation}\
   \newcommand{\phan}{\phantom{∂_m m}} % Phantom for alignment
   ⋆(dR^{♭♭}) =
   \begin{bmatrix}
     ( \; \phan   & - ∂_x d & - ∂_y e & - ∂_z f \; ) \; dt \\
     ( \; - ∂_t d & \phan   & - ∂_y c & + ∂_z b \; ) \; dx \\
     ( \; - ∂_t e & + ∂_x c & \phan   & - ∂_z a \; ) \; dy \\
     ( \; - ∂_t f & - ∂_x b & + ∂_y a & \phan   \; ) \; dz \\
   \end{bmatrix}
   \end{equation}

.. rubric:: Exterior Derivative of the Hodge Dual of a Rotation in Differential
   Form

.. math::

   \begin{equation}
   \newcommand{\_}{\phantom{∂_m m}} % Phantom for alignment
   ⋆d(⋆R^{♭♭})
   =
   \begin{bmatrix}
   (   \_    & - ∂_x a & - ∂_y b & - ∂_z c ) dt \\
   ( - ∂_t a &   \_    & + ∂_y f & - ∂_z e ) dx \\
   ( - ∂_t b & - ∂_x f &   \_    & + ∂_z d ) dy \\
   ( - ∂_t c & + ∂_x e & - ∂_y d &   \_    ) dz \\
   \end{bmatrix}
   \end{equation}

Readers well versed in the formulation of electromagnetism will already have
recognized the Faraday tensor, its dual, and the Maxwell equations.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   differential_operators.rst
   the_exterior_derivative_of_rotations.rst
