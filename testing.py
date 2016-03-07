from rankBinary import rank   as rank_binary
from rankBinary import unrank as unrank_binary
from rankBinary import total  as total_binary

from rankPerm   import rank   as rank_perm
from rankPerm   import unrank as unrank_perm
from rankPerm   import total  as total_perm

from rankSigned import rank   as rank_signed
from rankSigned import unrank as unrank_signed
from rankSigned import total  as total_signed

import sys

'''
Test the given ranking and unranking routines for the provided object.
'''
def test_rank_unrank(n, rank_fn, unrank_fn, total_fn):
  # Test the unrank function by creating a list of all objects.
  object_list = []
  total = total_fn(n)
  for i in range(total):
    next_object = tuple(unrank_fn(i, n))
    object_list.append(next_object)
  object_set = set(object_list)
  if (len(object_set) != total):
    return False

  # Test the rank function for all of the signed permutations created above.
  for i, next_object in enumerate(object_list):
    pos = rank_fn(next_object, n)
    if pos != i:
      return False

  return True


'''
Test each of the objects that are hard-coded below.
TODO figure out a nice object-oriented approach to this testing.
'''
def main():
  object_names = ["binary strings", "permutations", "signed permutations"]
  rank_fns     = [rank_binary, rank_perm, rank_signed]
  unrank_fns   = [unrank_binary, unrank_perm, unrank_signed]
  total_fns    = [total_binary, total_perm, total_signed]

  for i in range(len(rank_fns)):
    object_name = object_names[i]
    rank_fn = rank_fns[i]
    unrank_fn = unrank_fns[i]
    total_fn = total_fns[i]
    print("Testing " + object_name)
    for n in range(1, 21):
      total = total_fn(n)
      if total > 100000: 
        break
      sys.stdout.write("n =  " + str(n) + " ")
      passed = test_rank_unrank(n, rank_fn, unrank_fn, total_fn)
      print(passed)
      if passed == False:
        return
  print("Finished all tests")

if __name__ == "__main__":
  main()
