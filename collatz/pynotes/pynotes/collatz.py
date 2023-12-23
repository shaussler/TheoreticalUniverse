
def orbit(x, **kwargs):

    """
    Collatz orbit

    Args:

      bit_length (int): Bit length

      method (str):
        either skip or None. if *skip* is used, then the collatz sequence is
        calculated using directly ``x/2`` and ``(3*x+1)/2``

    """

    #{{{

    gen = col_gen(x, **kwargs)

    return list(gen)

    #}}}

def has_converged(orbit):

    """
    Determines if the orbit has converged

    Args:

        orbit (ls): list of integers

    Returns:
        True if the orbit has converged, false otherwise

    """
    return orbit[-1]==1

def orbits(bit_length=8, method=None, stop_at_bit_length=True):

    """
    Determine all orbits for a given bit length

        bit_length (int): bit length
        method (str): None, skip, flush
    """

    #{{{

    orbits=[]

    for n in range(1, 2**bit_length):
      
       # Do not consider number divisible by 2 when method is flushed
       # ------------------------------------------------------------

       if method in ['flush'] and (n % 2) == 0:
           continue

       if stop_at_bit_length is True:
           orb = orbit(n, bit_length=bit_length, method=method)
       else:
           orb = orbit(n, bit_length=None, method=method)

       if has_converged(orb):
           orbits.append(orb)

    return orbits

    #}}}

def col_gen(x, **kwargs):

    """
    Collatz number generator

    Args:

      bit_length (int): Bit length

      method (str):
        either skip or None. if *skip* is used, then the collatz sequence is
        calculated using directly ``x/2`` and ``(3*x+1)/2``

    """

    #{{{

    yield x

    while x != 1 and x != None:

        x = col_next(x, **kwargs)
   
        if x is not None:
            yield x

    #}}}

def col_next(x, bit_length=None, method=None):

    """
    Next collatz number

    Args:

      x (int): Initial number

      bit_length (int): Bit length

      method (str):
        either skip or None. if *skip* is used, then the collatz sequence is
        calculated using directly ``x/2`` and ``(3*x+1)/2``
    """

    #{{{   

    x_next = -1

    match method:

        case None:
            x_next = col_next_classic(x)

        case 'skip':
            x_next = col_next_skip(x)

        case 'flush':
            x_next = col_next_flush(x)

    # Set to none if the resulting number if above the maximal bit length
    # -------------------------------------------------------------------

    if bit_length is not None and x_next.bit_length() > bit_length:
        x_next = None

    return x_next

    #}}}

def col_next_classic(x, bit_length=None):

    """
    Next collatz number with the classic method

    Args:
      x (int): Initial number
      bit_length (int): Bit length
    """

    #{{{   

    if x % 2 == 0:
       x_next = int(x/2)

    else:
       x_next = x*3+1

    return x_next

    #}}}

def col_next_skip(x, bit_length=None):

    """
    Next collatz number with the skip method

    Args:
      x (int): Initial number
      bit_length (int): Bit length
    """

    #{{{   

    if x % 2 == 0:
       x_next = x//2

    else:
       x_next = (x*3+1)//2

    return x_next

    #}}}

def col_next_flush(x, bit_length=None):

    """
    Next collatz number with the flush method

    Args:
      x (int): Initial number
      bit_length (int): Bit length

    """

    #{{{   

    x_next=x

    while (x_next % 2) == 0:
        x_next=x_next // 2

    x_next = (x_next*3+1) // 2

    while (x_next % 2) == 0:
        x_next=x_next // 2

    return x_next

    #}}}


def col_previous_flush(x):

    """
    Previous collatz number with the flush method

    Args:
      x (int): Initial number
      bit_length (int): Bit length

    """

    #{{{   

    #x_prev = x
    #while x_prev % 3 != 0:
    #    x_prev = x_prev*2

    x_prev = (2*x - 1) // 3
    print(f"{(2*x - 1) // 3}")
    print(f"{(2*x - 1) / 3}")

    return x_prev

    #}}}



def int2bin(ls, bit_length=None):

    """
    Convert list of integer to list of binary numbers

    Args:
      ls (list):  List of integers
      bit_length (int): binary number bit length. Defaults to None.
    """

    if bit_length is not None:

        for el in int2bin(ls, bit_length=None):
            if len(el) > bit_length:
                raise Exception("Number larger than specified bit length")

        return [format(x, f"0{bit_length}b") for x in ls]

    if bit_length is None:
        return [format(x,'0b') for x in ls]

def testY():

    import sympy
    bit_length=8
 
    sequence = col_lst(
        7,
        bit_length=None,
        method='skip'
    )

    bin_sequence=[bin(x).replace('0b','') for x in sequence]
    nones_sequence=[d.count('1') for d in [ binary_number for binary_number in bin_sequence ]]
    nzeros_sequence=[d.count('0') for d in [ binary_number for binary_number in bin_sequence ]]
    nbits_sequence=[len(d) for d in [ binary_number for binary_number in bin_sequence ]]

    for idx, num in enumerate(sequence):
      print('-----------------------------')
      #print(f"{sympy.isprime(sequence[idx])=}")
      print(f"{sequence[idx]=}")
      print(f"{bin_sequence[idx]=}")
      print(f"{nbits_sequence[idx]=}")
      print(f"{nones_sequence[idx]=}")
      #print(f"{nzeros_sequence[idx]=}")
      #print(f"{nzeros_sequence[idx]/nones_sequence[idx]=}")


#    print(f"{bit_length=} {n=} {bin_sequence_size=}")
#    print(f"{bit_length=} {n=} {bin_sequence=}")



def testZ():

    """
    """

    import sys

    print('Sequence length')

    for bit_length in range(3, 5):
        # Prepare list of sequences
        # -------------------------

        ls_sequences = []

        for n in range(0, 2**bit_length):
          
           if n == 0:
              continue

           #print(f"{n=} {col_lst(n, bit_length=bit_length)}")

           sequence = col_lst(n, bit_length=None)
           #sequence.remove(n)
           #print(f"{bit_length=} {sequence=}")
           if 1 in sequence:
               ls_sequences.append(sequence)

        # Get unique numbers
        # ------------------

        st_sequences = list( {x for l in ls_sequences for x in l} )
        st_sequences.sort()

        # Get all possible numbers
        # ------------------------
  
        ls_all = list(range(1, 2**bit_length))

        # Get all numbers not in collatz numbers
        # --------------------------------------

        ls_not = list(set(ls_all) - set(st_sequences))
        #print(f"{bit_length=} {len(st_sequences)} {st_sequences}")
        print(f"{bit_length=} {len(st_sequences)} {1+len(ls_all)} {len(st_sequences)/len(ls_all)}")
        #test=len(st_sequences) - 2**(bit_length-1)
        #print(f"{bit_length=} {len(st_sequences)} {test=} {len(ls_all)} {len(st_sequences)/len(ls_all)}")
        #print(f"{bit_length=} {len(st_sequences)}")



def main():
    testY()

if __name__ == "__main__":
    main()
