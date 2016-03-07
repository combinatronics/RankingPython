'''
Ranking and unranking of signed permutations by multiplying two ranking algorithms:
 - lexicographic order for binary strings
 - "Ranking and unranking permutations in linear time" by Myrvold and Ruskey

The signed permutations are lists containing n values in {-1,1,-2,2,...,-n,n}.
The ranks are 0-based.
'''

from math import factorial
from rankPerm import rank as rank_perm
from rankPerm import unrank as unrank_perm
from rankBinary import rank as rank_binary
from rankBinary import unrank as unrank_binary


'''
Returns the number of signed permutations of n.
'''
def total(n):
    return 2**n * factorial(n)


'''
Simple usage message.
'''
def usage(n):
  print("The value of n must be between 0 and 20.")
  print("When ranking the signed permutation is a reordering of list(range(1,n+1)).")
  print("When unrakning the provided ranks are 0-based.")


'''
Returns the rank of the signed permutation of n.
'''
def rank(signed, n):
    binary = [int(x < 0) for x in signed]
    perm = [abs(x) for x in signed]
    prank = rank_perm(perm, n)
    brank = rank_binary(binary, n)
    return prank*(2**n) + brank


'''
Return the signed permutation of n that has the given rank.
'''
def unrank(rank, n):
  if (n < 1 or n > 20 or rank < 0 or rank >= total(n)):
    usage(n)
    return [-1]
  remainder = rank % (2**n)
  quotient = rank / (2**n)
  binary = unrank_binary(remainder, n)
  perm = unrank_perm(quotient, n)
  signs = [-2*b+1 for b in binary] # map 0 -> 1 and 1 to -1 
  signed = [signs[i]*perm[i] for i in range(n)]
  return signed

