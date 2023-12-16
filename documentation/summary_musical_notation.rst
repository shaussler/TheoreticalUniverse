Musical notation extends the use of matrix multiplication, providing a compact
representation while distinctly differentiating between a sharp
(:math:`\sharp`) vector and a flat (:math:`\flat`) covector. This notation
serves dual purposes:

* explicitly and compactly represent tensor components, making symmetries
  evident and readily comprehensible
* streamline calculations by adhering to matrix multiplication rules, offering
  a familiar framework for computations.

.. rubric:: Vectors and covectors

.. math::

     \begin{matrix}
         v^{\sharp}=
         \begin{bmatrix}
         a \\
         b
         \end{bmatrix}
     ,&
         v^{\flat}=
         \begin{bmatrix}
         a & b
         \end{bmatrix}
     \end{matrix}

.. rubric:: Covector of vector, rows of columns, contravariant/covariant tensor of rank 2

.. math::

   A^{\sharp\flat}
   =
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}^{\sharp\flat}
   =
   \begin{bmatrix}
       \begin{bmatrix}
       a \\
       b \\
       \end{bmatrix}
       \begin{bmatrix}
       c \\
       d \\
       \end{bmatrix}
   \end{bmatrix}

.. rubric:: Vector of covectors, columns of rows, covariant/contravariant tensor of rank 2

.. math::

   A^{\flat\sharp}
   =                                                                                                                                                                                       \begin{bmatrix}
       a & c \\                                                                                                                                                                                b & d \\
   \end{bmatrix}^{\flat\sharp}
   =
   \begin{bmatrix}
       \begin{bmatrix} a & b \end{bmatrix} \\
       \begin{bmatrix} c & d \end{bmatrix} \\
   \end{bmatrix}

.. rubric:: Covectors of covectors, rows of rows, covariant/convariant tensor of rank 2

.. math::

   A^{\flat\flat}
   =
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}^{\flat\flat}
   =
   \begin{bmatrix}
       \begin{bmatrix} a & b \end{bmatrix} &
       \begin{bmatrix} c & d \end{bmatrix}
   \end{bmatrix}

.. rubric:: Vectors of vectors, columns of columns, contravariant/contravariant tensor of rank 2

.. math::

   A^{\sharp\sharp}
   =
   \begin{bmatrix}
       a & c \\
       b & d \\
   \end{bmatrix}^{\sharp\sharp}
   =
   \begin{bmatrix}
       \begin{bmatrix}
           a \\
           b \\
       \end{bmatrix} \\
       \begin{bmatrix}
           c \\
           d \\
       \end{bmatrix} \\
   \end{bmatrix}
