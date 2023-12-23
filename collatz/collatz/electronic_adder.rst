Electronic Adder
================

In this section, the building of adders as found in electronic circuit is
explained. We detail how a n-bits adder is built `from one half adder and n-1
full adders <https://en.wikipedia.org/wiki/Adder_(electronics)>`_. 

.. sidebar:: One Bit Adders

  .. tikz::
     :xscale: 100
  
     \tikzstyle{fullbox} = [
       draw, minimum size=4cm,
       label={[anchor=east]right:$s_\text{out}$},
       label={[anchor=south]below:$c_\text{out}$},
       label={[anchor=west]155:$a$},
       label={[anchor=west]205:$b\vphantom{a}$},
     ]
  
     \node[fullbox] (a) {};
  
     \draw[<-] (a.155)    --++(180:0.5cm) node [left]  {};
     \draw[<-] (a.205)    --++(180:0.5cm) node [left]  {};
     \draw[->] (a.east)   --++(  0:0.5cm) node [right] 
     {$a \oplus b \oplus c_{in}$};
     \draw[->] (a.south)   --++(-90:0.5cm) node [right] 
     {$a \land b$};

  **Half Adder**

  .. tikz::
     :xscale: 100
  
     \tikzstyle{fullbox} = [
       draw, minimum size=4cm,
       label={[anchor=east]right:$s_\text{out}$},
       label={[anchor=south]below:$c_\text{out}$},
       label={[anchor=north]above:$c_\text{in}$},
       label={[anchor=west]155:$a$},
       label={[anchor=west]205:$b\vphantom{a}$},
     ]
  
     \node[fullbox] (a) {};
  
     \draw[<-] (a.north)  --++(90:0.5cm) node [right] {}; 
     \draw[<-] (a.155)    --++(180:0.5cm) node [left]  {};
     \draw[<-] (a.205)    --++(180:0.5cm) node [left]  {};
     \draw[->] (a.east)   --++(  0:0.5cm) node [right] 
     {$a \oplus b \oplus c_{in}$};
     \draw[->] (a.south)   --++(-90:0.5cm) node [right] 
     {$a \land b \oplus (a \oplus b) \land c_{in}$};

  **Full Adder**

Half Adder
----------

The half adder takes in two input bits :math:`a` and :math:`b`, and outputs two
bits for the sum (:math:`s_{out}`) as well as the *carry out* (:math:`c_{out}`).
The truth table of the half adder is:

.. math::

  \begin{array}{llll}
  \hline
  a & b & c_{out} & s_{out} \\
  \hline
  1 & 1 & 1       & 0       \\ 
  1 & 0 & 0       & 1       \\ 
  0 & 1 & 0       & 1       \\ 
  0 & 0 & 0       & 0       \\ 
  \hline
  \end{array}

The logical half adder is:

.. math::

   \begin{flalign*}
   s_{out} &= a \oplus b \\
   c_{out} &= a \land b
   \end{flalign*}

Full Adder
----------

The full adder takes in two bits :math:`a` and :math:`b`, a *carry in*
:math:`c_{in}`, and outputs the sum :math:`s_{out}` as well as the *carry out*
:math:`c_{out}`. The truth table of the full adder is:

.. math::

   \begin{array}{lllll}
   \hline
   a & b & c_{in} & s_{out} & c_{out} \\
   \hline
   1 & 1 &      1 &       1 &       1 \\ 
   1 & 1 &      0 &       0 &       1 \\ 
   1 & 0 &      1 &       0 &       1 \\ 
   1 & 0 &      0 &       0 &       0 \\ 
   0 & 1 &      1 &       0 &       1 \\ 
   0 & 1 &      0 &       1 &       0 \\ 
   0 & 0 &      1 &       1 &       0 \\ 
   0 & 0 &      0 &       0 &       0 \\ 
   \hline
   \end{array}

The logical full adder can be written with boolean addition :math:`\oplus` and
boolean multiplication :math:`\land` as:

.. math::

   \begin{flalign*}
   s_{out} &= a \oplus b \oplus c_{in}\\
   c_{out} &= a \land b \oplus ( a \oplus b) \land c_{in}
   \end{flalign*}

The logical expression for the *carry out* bit :math:`c_{out}` is non trivial
and is therefore demonstrated below by means of truth table expansions:

.. math::

   \begin{array}{ccc|c|c|c|c|c}
   a & b & c_{in} & a \land b & a \oplus b & (a \oplus b) \land c_{in}& a \land b \oplus ( a \oplus b) \land c_{in}& c_{out} \\
   \hline
   1 & 1 &      1 &         1 &          0 &                         0 &                                           1 &       1 \\ 
   1 & 1 &      0 &         1 &          0 &                         0 &                                           1 &       1 \\ 
   1 & 0 &      1 &         0 &          1 &                         1 &                                           1 &       1 \\ 
   1 & 0 &      0 &         0 &          1 &                         0 &                                           0 &       0 \\ 
   0 & 1 &      1 &         0 &          1 &                         1 &                                           1 &       1 \\ 
   0 & 1 &      0 &         0 &          1 &                         0 &                                           0 &       0 \\ 
   0 & 0 &      1 &         0 &          0 &                         0 &                                           0 &       0 \\ 
   0 & 0 &      0 &         0 &          0 &                         0 &                                           0 &       0 \\ 
   \end{array}

N-Bits Adder
------------

**Input A and B**

:Index of first bit: :math:`0`
:Index of last significant bit: :math:`n-1` 
:Number of bits: :math:`n`

**Output S**

:Index of first bit: :math:`0`
:Index of last significant bit: :math:`n` 
:Number of bits: :math:`n+1`

.. tikz:: N-Bits Full Adder
   :xscale: 100

   \tikzstyle{firstbox} = [
     draw, minimum size=4cm,
     label={[anchor=east]right:$s_\text{out}$},
     label={[anchor=south]below:$c_\text{out}$},
     label={[anchor=west]155:$a$},
     label={[anchor=west]205:$b\vphantom{a}$},
   ]

   \tikzstyle{fullbox} = [
     draw, minimum size=4cm,
     label={[anchor=east]right:$s_\text{out}$},
     label={[anchor=south]below:$c_\text{out}$},
     label={[anchor=north]above:$c_\text{in}$},
     label={[anchor=west]155:$a$},
     label={[anchor=west]205:$b\vphantom{a}$},
   ]

   \node[firstbox] (a) {};
   \node[fullbox, below={3cm}] (b) {};
   \node[fullbox, below={8cm}] (c) {};
   \node[fullbox, below={16cm}] (d) {};
   \node[fullbox, below={21cm}] (e) {};

   \draw[] (a.center) node {$0$};
   \draw[<-] (a.155)    --++(180:0.5cm) node [left]  {$A_0$};
   \draw[<-] (a.205)    --++(180:0.5cm) node [left]  {$B_0$};
   \draw[->] (a.east)   --++(  0:0.5cm) node [right]
   {$S_0 = A_0 \oplus B_0$};

   \draw[->] (a.south)  -- (b.north) node [right, yshift=0.3cm]
   {$C_0 = A_0 \land B_0$};

   \draw[] (b.center) node {$1$};
   \draw[<-] (b.155)    --++(180:0.5cm) node [left]  {$A_1$};
   \draw[<-] (b.205)    --++(180:0.5cm) node [left]  {$B_1$};
   \draw[->] (b.east)   --++(  0:0.5cm) node [right] 
   {$S_1 = A_1 \oplus B_1 \oplus C_0$};

   \draw[->] (b.south) --  (c.north) node [right, yshift=0.3cm]
   {$C_1 = A_1 \land B_1 \oplus (A_1 \oplus B_1) \land C_0$};


   \draw[] (c.center) node {$2$};
   \draw[<-] (c.155)    --++(180:0.5cm) node [left]  {$A_2$};
   \draw[<-] (c.205)    --++(180:0.5cm) node [left]  {$B_2$};
   \draw[->] (c.east)   --++(  0:0.5cm) node [right]
   {$S_2 = A_2 \oplus B_2 \oplus C_1$};

   \draw[dotted,->] (c.south) --  (d.north) node [right, yshift=0.3cm]
   {$C_{n-2}=A_{n-2} \land B_{n-2} \oplus (A_{n-2} \oplus B_{n-2}) \land C_{n-3}$};

   \draw[] (d.center) node {$n-1$};
   \draw[<-] (d.155)    --++(180:0.5cm) node [left]  {$A_{n-1}$};
   \draw[<-] (d.205)    --++(180:0.5cm) node [left]  {$B_{n-1}$};
   \draw[->] (d.east)   --++(  0:0.5cm) node [right]
   {$S_{n-1} = A_{n-1} \oplus B_{n-1} \oplus C_{n-2}$};

   \draw[->] (d.south) --  (e.north) node [right, yshift=0.3cm]
   {$C_{n-1} = A_{n-1} \land B_{n-1} \oplus (A_{n-1} \oplus B_{n-1}) \land C_{n-2}$};

   \draw[] (e.center) node {$n$};
   \draw[<-] (e.155)    --++(180:0.5cm) node [left]  {$0=A_{n}$};
   \draw[<-] (e.205)    --++(180:0.5cm) node [left]  {$0=B_{n}$};
   \draw[->] (e.east)   --++(  0:0.5cm) node [right]
   {$S_{n} = C_{n-1}$};
   \draw[->] (e.south)  --++(-90:0.5cm) node [below]  {$C_{n}=0$};

Changing the convection of boolean operators :math:`(\land, \oplus)` for
multiplication and addition symbols :math:`(\cdot, +)` , logical *carry out* of
the n-Bits full adder can be written as:

.. math::

   \begin{array}{ll}
   \hline
   C_0 &  A_0 \cdot B_0 \\
   C_1 &  A_1 \cdot B_1 + (A_1 + B1) \cdot C_0 \\
   C_2 &  A_2 \cdot B_2 + (A_2 + B2) \cdot C_1 \\
   \vdots & \\
   C_{n-2} & A_{n-2} \cdot B_{n-2} + (A_{n-2} + B_{n-2}) \cdot C_{n-3}\\
   C_{n-1} & A_{n-1} \cdot B_{n-1} + (A_{n-1} + B_{n-1}) \cdot C_{n-2}\\
   C_n & 0 \\
   \hline
   \end{array}

The corresponding output bits are:

.. math::

   \begin{array}{ll}
   \hline
   S_0 & A_0 + B_0 \\
   S_1 & A_1 + B_1 + C_0 \\
   S_2 & A_2 + B_2 + C_1 \\
   \vdots & \\
   S_{n-2} & A_{n-2} + B_{n-2} + C_{n-1} \\
   S_{n-1} & A_{n-1} + B_{n-1} + C_{n-2} \\
   S_n & C_n-1 \\
   \hline
   \end{array}
