'''
Ranking and unranking of permutations according to the following paper:
  "Ranking and unranking permutations in linear time" by Myrvold and Ruskey

The permutations are lists of {1,2,...,n} and the ranks are computed starting from 0.
'''

from math import factorial


'''
Test the ranking and unranking routines for all permutations of n.
Returns False and any test fails.
'''
def test(n):
  # Test the unrank function by creating a list of all permutations.
  num_objects = factorial(n)
  object_list = []
  for i in range(num_objects):
    next_object = tuple(unrank(i, n))
    object_list.append(next_object)
  object_set = set(object_list)
  if (len(object_set) != num_objects):
    return False

  # Test the rank function for all of the permutations created above.
  for i, next_object in enumerate(object_list):
    pos = rank(next_object, n)
    if pos != i:
      return False

  return True


'''
Simple usage message.
'''
def usage(n):
  print("The value of n must be between 0 and 20.")
  print("When ranking the permutation is a reordering of list(range(1,n+1)).")
  print("When unrakning the provided ranks are 0-based.")


'''
Returns the inverse of a permutation as a list.
'''
def inverse(perm, n):
  inv_perm = n * [-1]
  for i in range(n):
    inv_perm[perm[i]-1] = i+1
  return inv_perm


'''
Returns the rank of the permutation of n.
'''
def rank(perm, n):
  if (n < 1 or n > 20 or sorted(perm) != list(range(1,n+1))):
    usage(n)
    return -1
  perm = list(perm)
  copy = list(perm)
  inv_perm = inverse(perm, n)
  rank = rankCopy(n, copy, inv_perm)
  return rank


'''
Recursive part of the rank routine.
'''
def rankCopy(m, copy, inv_perm):
  if m == 1: return 0
  s = copy[m-1]-1
  x = m-1
  y = inv_perm[m-1]-1
  temp = copy[x]
  copy[x] = copy[y]
  copy[y] = temp
  x = s
  y = m-1
  temp = inv_perm[x]
  inv_perm[x] = inv_perm[y]
  inv_perm[y] = temp
  return s + m * rankCopy(m-1, copy, inv_perm)


'''
Return the permutation of n that has the given rank.
'''
def unrank(rank, n):
  if (n < 1 or n > 20 or rank < 0 or rank >= factorial(n)):
    usage(n)
    return [-1]
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
  for n in range(1, 8):
    passed = test(n)
    assert(passed)
