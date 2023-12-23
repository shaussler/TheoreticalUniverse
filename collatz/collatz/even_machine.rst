The even machine
================

.. tikz::
   :xscale: 60

   \tikzstyle{firstbox} = [
     draw, minimum size=4cm,
     label={[anchor=east]right:$s_\text{out}$},
     label={[anchor=south]below:$c_\text{in}$},
     label={[anchor=west]left:$a$},
   ]

   \tikzstyle{fullbox} = [
     draw, minimum size=4cm,
     label={[anchor=east]right:$s_\text{out}$},
     label={[anchor=south]below:$c_\text{in}$},
     label={[anchor=north]above:$c_\text{out}$},
     label={[anchor=west]left:$a$},
   ]

   \node[firstbox] (a) {};
   \node[fullbox, below={3cm}] (b) {};
   \node[fullbox, below={8cm}] (c) {};
   \node[fullbox, below={16cm}] (d) {};
   \node[fullbox, below={21cm}] (e) {};

   \draw[] (a.center) node {$0$}; %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (a.west)   --++(180:0.5cm) node [left]  {$A_0$=0};
   \draw[->] (a.east)   --++(  0:0.5cm) node [right] {$A_1$};

   \draw[<-] (a.south)  -- (b.north) node [midway,right]
   {$A_1$};

   \draw[] (b.center) node {$1$}; %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (b.west)   --++(180:0.5cm) node [left]  {$A_1$};
   \draw[->] (b.east)   --++(  0:0.5cm) node [right] {$A_2$};

   \draw[<-] (b.south)  --  (c.north) node [midway,right]
   {$A_2$};

   \draw[] (c.center) node {$2$}; %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (c.west)   --++(180:0.5cm) node [left]  {$A_2$};
   \draw[->] (c.east)   --++(  0:0.5cm) node [right] {$A_3$};

   \draw[dotted,<-] (c.south) -- (d.north) node [right, yshift=0.3cm]
   {$A_{n-2}$};

   \draw[] (d.center) node {$n-2$}; %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (d.west)    --++(180:0.5cm) node [left]  {$A_{n-2}$};
   \draw[->] (d.east)   --++(  0:0.5cm) node [right] {$A_{n-1}=1$};

   \draw[<-] (d.south)  --  (e.north) node [midway,right] {$A_{n-1}=1$};

   \draw[] (e.center) node {$n-1$}; %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   \draw[<-] (e.west)   --++(180:0.5cm) node [left]  {$1=A_{n-1}$};
   \draw[->] (e.east)   --++(  0:0.5cm) node [right] {$A_n=0$};
   \draw[<-] (e.south)  --++(-90:0.5cm) node [below] {$A_n=0$};

The *even machine* divides an even binary number by 2. In this section, the
*even machine* is built and the corresponding *even logic* is derived.
Dividing an even number :math:`A` by two corresponds to the `logical right
shift <https://en.wikipedia.org/wiki/Logical_shift>`_ operation
:math:`\texttt{>>}`.

**Input A**

:Index of first bit: :math:`0`
:Index of last significant bit: :math:`n-1` 
:Number of bits: :math:`n`

**Output O**

:Index of first bit: :math:`0`
:Index of last significant bit: :math:`n-2` 
:Number of bits: :math:`n-1`

The corresponding *even logic* for number :math:`O` corresponds to:

.. math::

   \begin{array}{lll}
   \hline
   S_0    & =  & A_1     \\
   S_1    & =  & A_2     \\
   S_2    & =  & A_3     \\
   \vdots & =  &         \\
   S_{n-3}& =  & A_{n-2} \\
   S_{n-2}& =  & 1       \\
   S_{n-1}& =  & 0       \\
   S_{n}  & =  & 0       \\
   \hline
   \end{array}


