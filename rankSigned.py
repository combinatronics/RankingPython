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
Test the ranking and unranking routines for all signed permutations of n.
Returns False and any test fails.
'''
def test(n):
  # Test the unrank function by creating a list of all signed permutations.
  object_list = []
  for i in range(num_objects(n)):
    next_object = tuple(unrank(i, n))
    object_list.append(next_object)
  object_set = set(object_list)
  if (len(object_set) != num_objects(n)):
    return False

  # Test the rank function for all of the signed permutations created above.
  for i, next_object in enumerate(object_list):
    pos = rank(next_object, n)
    if pos != i:
      return False

  return True

'''
Returns the number of signed permutations of n.
'''
def num_objects(n):
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
  if (n < 1 or n > 20 or rank < 0 or rank >= num_objects(n)):
    usage(n)
    return [-1]
  remainder = rank % (2**n)
  quotient = rank / (2**n)
  binary = unrank_binary(remainder, n)
  perm = unrank_perm(quotient, n)
  signs = [-2*b+1 for b in binary] # map 0 -> 1 and 1 to -1 
  signed = [signs[i]*perm[i] for i in range(n)]
  return signed


if __name__ == "__main__":
  for n in range(1, 5):
    passed = test(n)
    assert(passed)
