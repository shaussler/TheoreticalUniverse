The short odd machine
=====================

The odd machine :math:`(3X + 1)/2` can be rewritten as :math:`(2 X + X + 1 )/2`
and thus also using logical shift:

.. math::

   (X \texttt{<<} + X + 1) \texttt{>>}

**Input**

:Index of first bit: :math:`0`
:Index of last significant bit: :math:`n-1` 
:Number of bits: :math:`n`

**Output**

:Index of first bit: :math:`0`
:Minimal index of last significant bit: :math:`n-1` 
:Minimal number of bits: :math:`n`
:Maximal index of last significant bit: :math:`n` 
:Maximal number of bits: :math:`n+1`

By definition, the first bit and the last significant bit :math:`A_{n-1}` are
equal to :math:`1`.

.. tikz:: n-Bits Short Odd Machine
   :xscale: 80

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

   \node[fullbox, below={3cm}] (b) {};
   \node[fullbox, below={8cm}] (c) {};
   \node[fullbox, below={13cm}] (d) {};
   \node[fullbox, below={20cm}] (e) {};
   \node[fullbox, below={25cm}] (f) {};
   \node[fullbox, below={30cm}] (g) {};

   \draw[] (b.center) node {$0$}; % Bit 0 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (b.north)  --++(90:0.5cm)  node [above] {$1$};
   \draw[<-] (b.155)    --++(180:0.5cm) node [left]  {$1=A_0$};
   \draw[<-] (b.205)    --++(180:0.5cm) node [left]  {$A_1$};
   \draw[->] (b.east)   --++(  0:0.5cm) node [right] 
   {$S_0 = A_0 \oplus A_1 \oplus 1$};

   \draw[->] (b.south) --  (c.north) node [right, yshift=0.3cm]
   {$C_0 = A_0 \land A_1 \oplus (A_0 \oplus A_1) \land 1$};

   \draw[] (c.center) node {$1$}; % Bit 1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (c.155)    --++(180:0.5cm) node [left]  {$A_1$};
   \draw[<-] (c.205)    --++(180:0.5cm) node [left]  {$A_2$};
   \draw[->] (c.east)   --++(  0:0.5cm) node [right] 
   {$S_1 = A_1 \oplus A_2 \oplus C_0$};

   \draw[->] (c.south) --  (d.north) node [right, yshift=0.3cm]
   {$C_1 = A_1 \land A_2 \oplus (A_1 \oplus A_2) \land C_0$};

   \draw[] (d.center) node {$2$}; % Bit 2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (d.155)    --++(180:0.5cm) node [left]  {$A_2$};
   \draw[<-] (d.205)    --++(180:0.5cm) node [left]  {$A_3$};
   \draw[->] (d.east)   --++(  0:0.5cm) node [right]
   {$S_2 = A_2 \oplus A_3 \oplus C_2$};

   \draw[dotted,->] (d.south) --  (e.north) node [right, yshift=0.3cm]
   {$C_{n-3}=A_{n-3} \land A_{n-2} \oplus (A_{n-3} \oplus A_{n-2}) \land C_{n-4}$};

   \draw[] (e.center) node {$n-2$}; % Bit n-2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (e.155)    --++(180:0.5cm) node [left]  {$A_{n-2}$};
   \draw[<-] (e.205)    --++(180:0.5cm) node [left]  {$A_{n-1}$};
   \draw[->] (e.east)   --++(  0:0.5cm) node [right]
   {$S_{n-2} = A_{n-2} \oplus A_{n-1} \oplus C_{n-2}$};

   \draw[->] (e.south) --  (f.north) node [right, yshift=0.3cm]
   {$C_{n-2} = A_{n-2} \land A_{n-1} \oplus (A_{n-2} \oplus A_{n-1}) \land C_{n-3}$};

   \draw[] (f.center) node {$n-1$}; % Bit n-1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (f.155)    --++(180:0.5cm) node [left]  {$1=A_{n-1}$};
   \draw[<-] (f.205)    --++(180:0.5cm) node [left]  {$0=A_{n}$};
   \draw[->] (f.east)   --++(  0:0.5cm) node [right]
   {$S_{n-1} = 1 \oplus C_{n-2}$};

   \draw[->] (f.south) --  (g.north) node [right, yshift=0.3cm]
   {$C_{n-1} = C_{n-2}$};

   \draw[] (g.center) node {$n$}; % Bit n %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (g.155)    --++(180:0.5cm) node [left]  {$0$};
   \draw[<-] (g.205)    --++(180:0.5cm) node [left]  {$0$};
   \draw[->] (g.east)   --++(  0:0.5cm) node [right]
   {$S_{n} = C_{n-2}$};

   \draw[->] (g.south)  --++(-90:0.5cm) node [below]  {$0$};

Changing the convection of boolean operators :math:`(\land, \oplus)` for
multiplication and addition symbols :math:`(\cdot, +)` , logical *carry out* of
the n-Bits full adder can be written as:

.. math::

   \begin{array}{llcl}
   \hline
   \textrm{Bit} & & & \\
   \hline
   0       & S_0     & =       & A_0 + A_1 + 1                                              \\
           & C_0     & =       & A_0 \cdot A_1 + (A_0 + A_1) \cdot 1                        \\
                                                                                            \\
   1       & S_1     & =       & A_1 + A_2 + C_0                                            \\
           & C_1     & =       & A_1 \cdot A_2 + (A_1 + A_2) \cdot C_0                      \\
           &         & \vdots  &                                                            \\
   i       & S_i     & =       & A_i + A_{i+1}+ C_{i-1}                                     \\
           & C_i     & =       & A_i \cdot A_{i+1} + (A_i + A_{i+1}) \cdot C_{i-1}          \\
           &         & \vdots  &                                                            \\
   n-2     & S_{n-2} & =       & A_{n-2} + A_{n-1} + C_{n-3}                                \\
           & C_{n-2} & =       & A_{n-2} \cdot A_{n-1} + ( A_{n-2} + A_{n-1}) \cdot C_{n-3} \\
                                                                                            \\ 
   n-1     & S_{n-1} & =       & 1+ C_{n-2}                                                 \\
           & C_{n-1} & =       & C_{n-2}                                                    \\
                                                                                            \\ 
   n       & S_n     & =       & C_{n-2}                                                    \\
           & C_n     & =       & 0                                                          \\
   \hline
   \end{array}


