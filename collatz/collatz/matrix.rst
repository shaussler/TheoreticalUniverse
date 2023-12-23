Matrix representation
=====================


Shift operator
--------------

The *left shift* operator << (Multiplication by two) is:

.. math::

   \begin{pmatrix}
   0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
   1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
   0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
   \end{pmatrix}
   \cdot
   \begin{pmatrix}
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   \end{pmatrix}
   = 
   \begin{pmatrix}
   0 \\
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   \end{pmatrix}

The *right shift* operator >> (Division by two) is:

.. math::

   \begin{pmatrix}
   0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
   0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
   0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
   \end{pmatrix}
   \cdot
   \begin{pmatrix}
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   \end{pmatrix}
   = 
   \begin{pmatrix}
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   0   \\
   \end{pmatrix}

Building the carry-over matrix

.. math::

   \begin{pmatrix}
   1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
   0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
   0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
   \end{pmatrix}
   \cdot
   \begin{pmatrix}
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   \end{pmatrix}
   +
   \begin{pmatrix}
   0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
   1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
   0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
   \end{pmatrix}
   \cdot
   \begin{pmatrix}
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   \end{pmatrix}


.. math::

   \begin{pmatrix}
   1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
   1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
   0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
   0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 \\
   0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 \\
   0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 \\
   0 & 0 & 0 & 0 & 0 & 1 & 1 & 0 \\
   0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
   \end{pmatrix}
   \cdot
   \begin{pmatrix}
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   \end{pmatrix}
   =
   \begin{pmatrix}
   A_0 & 0   &   0 &   0 &   0 &   0 &   0 &   0 \\
   A_0 & A_1 &   0 &   0 &   0 &   0 &   0 &   0 \\
   0   & A_1 & A_2 &   0 &   0 &   0 &   0 &   0 \\
   0   & 0   & A_2 & A_3 &   0 &   0 &   0 &   0 \\
   0   & 0   &   0 & A_3 & A_4 &   0 &   0 &   0 \\
   0   & 0   &   0 &   0 & A_4 & A_5 &   0 &   0 \\
   0   & 0   &   0 &   0 &   0 & A_5 & A_6 &   0 \\
   0   & 0   &   0 &   0 &   0 &   0 & A_6 & A_7 \\
   \end{pmatrix}
   \cdot
   \begin{pmatrix}
   1 \\
   1 \\
   1 \\
   1 \\
   1 \\
   1 \\
   1 \\
   1 \\
   \end{pmatrix}
   =
   \begin{pmatrix}
   A_0 \\
   A_0+A_1 \\
   A_1+A_2 \\
   A_2+A_3 \\
   A_3+A_4 \\
   A_4+A_5 \\
   A_5+A_6 \\
   A_6+A_7 \\
   \end{pmatrix}

.. math::

   \begin{pmatrix}
   A_0 & 0             &             0 &             0 &             0 &             0 &             0 &             0  \\
   0   & A_0 \cdot A_1 &             0 &             0 &             0 &             0 &             0 &             0  \\
   0   & 0             & A_1 \cdot A_2 &             0 &             0 &             0 &             0 &             0  \\
   0   & 0             &             0 & A_2 \cdot A_3 &             0 &             0 &             0 &             0  \\
   0   & 0             &             0 &             0 & A_3 \cdot A_4 &             0 &             0 &             0  \\
   0   & 0             &             0 &             0 &             0 & A_4 \cdot A_5 &             0 &             0  \\
   0   & 0             &             0 &             0 &             0 &             0 & A_5 \cdot A_6 &             0  \\
   0   & 0             &             0 &             0 &             0 &             0 &             0 & A_6 \cdot A_7  \\
   \end{pmatrix}


.. math::

   \begin{pmatrix}
   1   & 0             &             0 &             0 &             0 &             0 &             0 &             0  \\
   0   & A_0           &             0 &             0 &             0 &             0 &             0 &             0  \\
   0   & 0             & A_1           &             0 &             0 &             0 &             0 &             0  \\
   0   & 0             &             0 & A_2           &             0 &             0 &             0 &             0  \\
   0   & 0             &             0 &             0 & A_3           &             0 &             0 &             0  \\
   0   & 0             &             0 &             0 &             0 & A_4           &             0 &             0  \\
   0   & 0             &             0 &             0 &             0 &             0 & A_5           &             0  \\
   0   & 0             &             0 &             0 &             0 &             0 &             0 & A_6            \\
   \end{pmatrix}
   \cdot
   \begin{pmatrix}
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   \end{pmatrix}

test

.. math::

   (
   S^{<<}
   \cdot
   A
   +
   e_0
   )
   \cdot
   (
   S^{<<}
   \cdot
   A
   +
   e_0
   )^{T}
   =
   \begin{pmatrix}
   1   & 0             &             0 &             0 &             0 &             0 &             0 &             0  \\
   0   & A_0           &             0 &             0 &             0 &             0 &             0 &             0  \\
   0   & 0             & A_1           &             0 &             0 &             0 &             0 &             0  \\
   0   & 0             &             0 & A_2           &             0 &             0 &             0 &             0  \\
   0   & 0             &             0 &             0 & A_3           &             0 &             0 &             0  \\
   0   & 0             &             0 &             0 &             0 & A_4           &             0 &             0  \\
   0   & 0             &             0 &             0 &             0 &             0 & A_5           &             0  \\
   0   & 0             &             0 &             0 &             0 &             0 &             0 & A_6            \\
   \end{pmatrix}
   \cdot
   \begin{pmatrix}
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   \end{pmatrix}

.. math::

   (e_0 \cdot e_0^{T} + S^{<<}) \cdot A

.. math::

   (e_0 \cdot e_0^{T} + S^{<<})
   \cdot
   \begin{pmatrix}
   A_0 \\
   A_1 \\
   A_2 \\
   A_3 \\
   A_4 \\
   A_5 \\
   A_6 \\
   A_7 \\
   \end{pmatrix}
   =
   \begin{pmatrix}
   A_0           \\
   A_0 \cdot A_1 \\
   A_1 \cdot A_2 \\
   A_2 \cdot A_3 \\
   A_3 \cdot A_4 \\
   A_4 \cdot A_5 \\
   A_5 \cdot A_6 \\
   A_6 \cdot A_7 \\
   \end{pmatrix}

Carray over is:

.. math::

   C = (e_0 \cdot e_0^{T} + S^{<<}) \cdot A + [(I + S^{<<}) \cdot A]^T \cdot C


