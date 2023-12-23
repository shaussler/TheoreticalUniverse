The odd machine
===============

Logical shift
-------------

In binary number, multiplication by two consist of a logical left shift noted
:math:`\texttt{<<}`. For example, the bits of the number :math:`5=0101` are
shifted to the left (:math:`10=1010`) in order to multiply by two. Dividing an
even number likewise correspond to a logical right shift :math:`\texttt{>>}`. 

The full odd machine :math:`(3X + 1)` can be rewritten as :math:`(2 X + X + 1
)`:

.. math::

   (X \texttt{<<} + X + 1)

**Input**

:Index of first bit: :math:`0`
:Index of last significant bit: :math:`n-1` 
:Number of bits: :math:`n`

**Output**

:Index of first bit: :math:`0`
:Minimal index of last significant bit: :math:`n` 
:Minimal number of bits: :math:`n+1`
:Maximal index of last significant bit: :math:`n+1` 
:Maximal number of bits: :math:`n+2`

By definition, the first bit and the last significant bit math:`A_{n-1}` are
equal to :math:`1`.

.. tikz:: n-Bits Full Odd Machine
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
   \node[fullbox, below={13cm}] (d) {};
   \node[fullbox, below={20cm}] (e) {};
   \node[fullbox, below={25cm}] (f) {};
   \node[fullbox, below={30cm}] (g) {};

   \draw[] (a.center) node {$0$};
   \draw[<-] (a.155)    --++(180:0.5cm) node [left]  {$1$};
   \draw[<-] (a.205)    --++(180:0.5cm) node [left]  {$1=A_0$};
   \draw[->] (a.east)   --++(  0:0.5cm) node [right]
   {$S_0 = 0$};

   \draw[->] (a.south)  -- (b.north) node [right, yshift=0.3cm]
   {$C_0 = 1$};

   \draw[] (b.center) node {$1$};
   \draw[<-] (b.155)    --++(180:0.5cm) node [left]  {$1=A_0$};
   \draw[<-] (b.205)    --++(180:0.5cm) node [left]  {$A_1$};
   \draw[->] (b.east)   --++(  0:0.5cm) node [right] 
   {$S_1 = 1 \oplus A_1 \oplus 1$};

   \draw[->] (b.south) --  (c.north) node [right, yshift=0.3cm]
   {$C_1 = 1 \land A_1 \oplus (1 \oplus A_1) \land 1$};

   \draw[] (c.center) node {$2$};
   \draw[<-] (c.155)    --++(180:0.5cm) node [left]  {$A_1$};
   \draw[<-] (c.205)    --++(180:0.5cm) node [left]  {$A_2$};
   \draw[->] (c.east)   --++(  0:0.5cm) node [right] 
   {$S_2 = A_1 \oplus A_2 \oplus C_1$};

   \draw[->] (c.south) --  (d.north) node [right, yshift=0.3cm]
   {$C_2 = A_1 \land A_2 \oplus (A_1 \oplus A_2) \land C_1$};

   \draw[] (d.center) node {$3$};
   \draw[<-] (d.155)    --++(180:0.5cm) node [left]  {$A_2$};
   \draw[<-] (d.205)    --++(180:0.5cm) node [left]  {$A_3$};
   \draw[->] (d.east)   --++(  0:0.5cm) node [right]
   {$S_2 = A_2 \oplus A_3 \oplus C_2$};

   \draw[dotted,->] (d.south) --  (e.north) node [right, yshift=0.3cm]
   {$C_{n-2}=A_{n-3} \land A_{n-2} \oplus (A_{n-3} \oplus A_{n-2}) \land C_{n-3}$};

   \draw[] (e.center) node {$n-1$};
   \draw[<-] (e.155)    --++(180:0.5cm) node [left]  {$A_{n-2}$};
   \draw[<-] (e.205)    --++(180:0.5cm) node [left]  {$A_{n-1}$};
   \draw[->] (e.east)   --++(  0:0.5cm) node [right]
   {$S_{n-1} = A_{n-2} \oplus A_{n-1} \oplus C_{n-2}$};

   \draw[->] (e.south) --  (f.north) node [right, yshift=0.3cm]
   {$C_{n-1} = A_{n-2} \land A_{n-1} \oplus (A_{n-2} \oplus A_{n-1}) \land C_{n-2}$};

   \draw[] (f.center) node {$n$};
   \draw[<-] (f.155)    --++(180:0.5cm) node [left]  {$1=A_{n-1}$};
   \draw[<-] (f.205)    --++(180:0.5cm) node [left]  {$0=A_{n}$};
   \draw[->] (f.east)   --++(  0:0.5cm) node [right]
   {$S_{n} = 1 \oplus C_{n-1}$};

   \draw[->] (f.south) --  (g.north) node [right, yshift=0.3cm]
   {$C_n = C_{n-1}$};

   \draw[] (g.center) node {$n+1$};
   \draw[<-] (g.155)    --++(180:0.5cm) node [left]  {$0$};
   \draw[<-] (g.205)    --++(180:0.5cm) node [left]  {$0$};
   \draw[->] (g.east)   --++(  0:0.5cm) node [right]
   {$S_{n} = C_{n-1}$};

   \draw[->] (g.south)  --++(-90:0.5cm) node [below]  {$C_{n+1}=0$};


