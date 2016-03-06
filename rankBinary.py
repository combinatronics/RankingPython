'''
Ranking and unranking of binary strings using standard lexicographic order.

The binary strings of length n contain 0s and 1s, and the ranks are computed starting from 0.
'''

'''
Test the ranking and unranking routines for all binary strings of length n.
Returns False and any test fails.
'''
def test(n):
  # Test the unrank function by creating a list of all objects.
  num_objects = 2**n
  object_list = []
  for i in range(num_objects):
    next_object = tuple(unrank(i, n))
    object_list.append(next_object)
  object_set = set(object_list)
  if (len(object_set) != num_objects):
    return False

  # Test the rank function for all of the objects created above.
  for i, next_object in enumerate(object_list):
    pos = rank(next_object, n)
    if pos != i:
      return False

  return True


'''
Simple usage message.
'''
def usage(n):
  print("The value of n must be between 0 and 63.")
  print("When ranking the binary string is a list of 0s and 1s.")
  print("When unrakning the provided ranks are 0-based.")


'''
Returns the rank of the binary string of length n.
'''
def rank(binary, n):
  if n < 1 or n > 63 or len(binary) != n:  # TODO also test that all symbols are 0 or 1
    usage(n)
    return -1
  value = 0
  power = 1
  for bit in reversed(binary):
    value += power * bit
    power *= 2
  return value


'''
Return the binary string of length n that has the given rank.
'''
def unrank(rank, n):
  if (n < 1 or n > 63 or rank < 0 or rank >= 2**n):
    usage(n)
    return [-1]
  binary = []
  for i in range(n):
    bit = rank % 2
    binary.append(bit)
    rank /= 2
  return reversed(binary)


if __name__ == "__main__":
  for n in range(1, 11):
    passed = test(n)
    assert(passed)
