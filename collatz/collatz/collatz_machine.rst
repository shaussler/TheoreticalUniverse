The Collatz machine
===================

Given that the inverse of bit :math:`\neg s = 1 \oplus s`, we can choose an
expression depending on the value of :math:`s`:

.. math::

  (1 \oplus s) \land b \oplus a \land s

Or in simplified notation:

.. math::

  (1 + s) \cdot b \oplus a \land s

Using the first bit :math:`A_0` to determine if the even machine or the odd
machine is to be used, we construct the collatz machine:


.. math::

   \begin{array}{llcl}
   \hline
   \textrm{Bit} & & & \\
   \hline
   0       & S_0     & =       & (A_0 + 1) \cdot A_1 + A_0 \cdot (A_0 + A_1 + 1)                   \\
           & C_0     & =       & A_0 \cdot A_1 + (A_0 + A_1) \cdot 1                               \\
                                                                                                   \\
   1       & S_1     & =       & (A_0 + 1) \cdot A_2 + A_0 \cdot (A_1 + A_2 + C_0)                 \\
           & C_1     & =       & A_1 \cdot A_2 + (A_1 + A_2) \cdot C_0                             \\
           &         & \vdots  &                                                                   \\
   i       & S_i     & =       & (A_0 + 1) \cdot A_{i+1} + A_0 \cdot (A_i + A_{i+1}+ C_{i-1})      \\
           & C_i     & =       & A_i \cdot A_{i+1} + (A_i + A_{i+1}) \cdot C_{i-1}                 \\
           &         & \vdots  &                                                                   \\
   n-3     & S_{n-3} & =       & (A_0 + 1) \cdot A_{n-2} + A_0 \cdot (A_{n-3} + A_{n-2} + C_{n-4}) \\
           & C_{n-3} & =       & A_{n-3} \cdot A_{n-2} + ( A_{n-3} + A_{n-2}) \cdot C_{n-4}        \\
                                                                                                   \\ 
   n-2     & S_{n-2} & =       & (A_0 + 1) \cdot A_{n-1} + A_0 \cdot (A_{n-2} + A_{n-1} + C_{n-3}) \\
           & C_{n-2} & =       & A_{n-2} \cdot A_{n-1} + ( A_{n-2} + A_{n-1}) \cdot C_{n-3}        \\
                                                                                                   \\ 
   n-1     & S_{n-1} & =       & (A_0 + 1) \cdot A_n + A_0 \cdot (1+ C_{n-2})                      \\
           & C_{n-1} & =       & C_{n-2}                                                           \\
                                                                                                   \\ 
   n       & S_n     & =       & C_{n-2}                                                           \\
           & C_n     & =       & 0                                                                 \\
   \hline
   \end{array}

Where by definition :math:`A_n=0` and :math:`A_{n-1}=0`.
