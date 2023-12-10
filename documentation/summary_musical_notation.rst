The utilization of musical notation extends the conventional rules of matrix
multiplication, providing a compact representation while distinctly
differentiating between a sharp (:math:`\sharp`) vector and a flat
(:math:`\flat`) covector. This notation serves dual purposes: first, it
explicitly delineates tensors, making their symmetries evident and readily
comprehensible; second, it streamlines calculations by adhering to matrix
multiplication rules, offering a familiar framework for computations.

This notation aids in explicitely expressing the nature of geometric objects
involved in tensor analysis. Its use of symbols such as sharp and flat not only
clarifies the distinction between vectors and covectors but also highlights the
inherent symmetries within tensor expressions. Furthermore, the use of matrix
multiplication rules simplifies tensor operations, providing an intuitive and
efficient methodology for complex and lengthy calculations.

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

.. rubric:: covector of vector, rows of columns, contravariant/covariant tensor of rank 2

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

.. rubric:: vector of covectors, columns of rows, covariant/contravariant tensor of rank 2

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

.. rubric:: covectors of covectors, rows of rows, covariant/convariant tensor of rank 2

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

.. rubric:: vectors of vectors, columns of columns, contravariant/contravariant tensor of rank 2

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
