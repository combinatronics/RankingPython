'''
Ranking and unranking of signed permutations by multiplying two ranking algorithms:
 - lexicographic order for binary strings
 - "Ranking and unranking permutations in linear time" by Myrvold and Ruskey

The signed permutations are lists containing n values in {-1,1,-2,2,...,-n,n}.
The ranks are 0-based.
'''

from math import factorial
from rankPerm import rank, unrank as rank_perm, unrank_perm
from rankBinary import rank, unrank as rank_binary, unrank_binary

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
    binary = []
    perm = [abs(x) for x in signed]
    prank = rank_perm(perm)
    brank = rank_binary(binary)
    return prank*(2**n) + brank


'''
Return the signed permutation of n that has the given rank.
'''
def unrank(rank, n):
  if (n < 1 or n > 20 or rank < 0 or rank >= num_objects(n)):
    usage(n)
    return [-1]
  # TODO: Continue working from here.
  remainder = rank % (2**n)

  quotient = rank
  copy = list(range(1,n+1))
  for i in range(n, 1, -1):
    remainder = quotient % i
    quotient = quotient / i
    x = i-1
    y = remainder
    temp = copy[x]
    copy[x] = copy[y]
    copy[y] = temp
  perm = list(copy)
  return perm


if __name__ == "__main__":
  for n in range(1, 6):
    passed = test(n)
    assert(passed)
