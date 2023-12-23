Introduction
============

Positive integers are represented in electronic devices by a collection of
arbitrarily large number of bits. Historically, the first widely available
computers were based on 8 bits, which was incementarly increased over the years
to 16, 32, and today 64 bits. 8 bits permit to represent 256 positive integers
from 0 to 255 as a sum of power of 2. For example, the number 17 can be
represented as :math:`00001001`. Operations on binary numbers are performed
throught the use of logic gates built upon transistors which can take the
values **off** and **on**, interpreted as **FALSE** and **TRUE** or
alternatively **zero** and **one**.  **Any integer number as well as associated
addition and multiplication operations** can be represented as logical
operations, and therefore **have an equivalent representation as boolean
operations**.

In electronics, simple (e.g. NAND gates) as well as more complex operations
(e.g. addition, registers) are built into chips which are then used as *black
boxes* in electronic circuits. The meaning of *black box* in this context
refers to the idea that the user of the electronic circuits only needs to know
the inputs and outputs of the chips, with no knowledge of how the transistors
within are set up to perform the operations. As of today, the most famous
example is certainly the `7400 series of integrated circuits
<https://en.m.wikipedia.org/wiki/List_of_7400-series_integrated_circuits>`_.

The collatz conjecture can be rewritten as an electronic device in terms of
*black box* chips which is named here the *collatz machine*. The collatz
conjecture can in turn be interpreted as boolean propositions.
