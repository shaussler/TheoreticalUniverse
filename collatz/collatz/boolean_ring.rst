Boolean ring
============

Booleans is the set of elements **FALSE** or **TRUE**, equivalently denoted
**0** and *1*. Selecting the two operations:

* *exclusive or* (denoted :math:`\oplus`) together with,
* *logical and* (denoted :math:`\land`)

Booleans together with the above operations behave like numbers, which
intuitively allows to perform operations on booleans

Abelian group under *exclusive or* :math:`\oplus`
-------------------------------------------------

https://en.wikipedia.org/wiki/Abelian_group#Definition

**Associativity**

.. math::

   (A \oplus B) \oplus C = ( A \oplus B ) \oplus C

**Identity element**

There exist :math:`E` such that :math:`E \oplus A = A \oplus E`. Identifying
the identity element with :math:`E=0`.

.. math::

   0 \oplus A = 0 \oplus A 

**Inverse Element**

For each :math:`A` there exist :math:`B` such that :math:`A \oplus B = B \oplus
A = E`. The inverse element of :math:`A` is :math:`\neg A`:

.. math::

   A \oplus \neg A = A \oplus \neg A = 0

**Commutativity**

.. math::

   A \oplus B = B \oplus A

Ring under *exclusive or* :math:`\oplus` and *logical and* :math:`\land`
------------------------------------------------------------------------

https://en.wikipedia.org/wiki/Ring_(mathematics)#Definition

Booleans under *exclusive or* :math:`\oplus` for *addition* and *logical and*
:math:`\land` for *multiplication* is a ring.

**Group under addition**

The set of booleans is a group under addition as shown above.

**Multiplicative associativity**

.. math::

   (A \land B) \land C = ( A \land B ) \land C

**Multiplicative identity** 

There exist :math:`E` such that :math:`E \land A = A \land E = A`. Identifying
:math:`E` with truth :math:`E=1`:

.. math::

   1 \land A = A \land 1 = A

**Distributivity**

Multiplication is distributive with respect to addition:

.. math::

   (A \oplus B) \land C = ( A \land C ) \oplus ( B \land C)

This can be proven with a truth table:

.. math::

   \begin{array}{llllllll}
   \hline
   a & b & c & a \oplus b & a \land c & b \land c & (a \land c) \oplus (b \land c) & (a \oplus b) \land c \\
   \hline
   1 & 1 & 1 & 0          & 1         & 1         & 0                              & 0                    \\ 
   1 & 1 & 0 & 0          & 0         & 0         & 0                              & 0                    \\ 
   1 & 0 & 1 & 1          & 1         & 0         & 1                              & 1                    \\ 
   1 & 0 & 0 & 1          & 0         & 0         & 0                              & 0                    \\ 
   0 & 1 & 1 & 1          & 0         & 1         & 1                              & 1                    \\ 
   0 & 1 & 0 & 1          & 0         & 0         & 0                              & 0                    \\ 
   0 & 0 & 1 & 0          & 0         & 0         & 0                              & 0                    \\ 
   0 & 0 & 0 & 0          & 0         & 0         & 0                              & 0                    \\ 
   \hline
   \end{array}

Identities
----------

The *exclusive or* operator :math:`\oplus` is replaced by :math:`+` and the
*logical and* by :math:`\cdot`. Basic properties are then:

.. math::

  1 \cdot a = a

.. math::

  0 \cdot a = 0

.. math::

  1 + a = \bar{a}

.. math::

  0 + a = a

.. math::

  a \cdot a = a

And  the following identities hold:

.. math::

  (a + b) \cdot c = (a \cdot b) + (b + c)

.. math::

  (a + b) \cdot (a + b) = a + b + a \cdot b

Inverse relations

.. math::

   - a = \bar{a} =1 + a

.. math::

   1 \cdot a  = a


:math:`a^{-1}` does not exist because if :math:`a=1`, then :math:`a^{-1}=1`.
But if :math:`a=0`, there is no number such that :math:`0 \cdot a^{-1} = 1`.



