'''
Ranking and unranking signed permutations using by multiplying two orders:
 - The lexicographic order of binary strings.
 - The permutation order by Ruskey and Myrvold in the following paper:
   "Ranking and unranking permutations in linear time".
Note: The order used here is *not* lexicographic order.
'''

from GenerateObject import GenerateObject
from BinaryStrings import BinaryStrings
from Permutations import Permutations
from math import factorial

class SignedPermutations(GenerateObject):
    def __init__(self):
        self.name = "signed permutation"
        self.B = BinaryStrings()
        self.P = Permutations()

    def string(self, signed):
        s = ""
        for x in signed:
            if x > 0:
                s += "+"
            s += str(x)
        return s

    def total(self, n):
        return (2**n) * factorial(n)

    def rank(self, signed):
        n = len(signed)
        binary = [int(x < 0) for x in signed]
        perm = [abs(x) for x in signed]
        brank = self.B.rank(binary)
        prank = self.P.rank(perm)
        return prank*(2**n) + brank

    def unrank(self, rank, n):
        if not self.is_valid_rank(rank, n):
            return None
        remainder = rank % (2**n)
        quotient = rank / (2**n)
        binary = self.B.unrank(remainder, n)
        perm = self.P.unrank(quotient, n)
        signs = [-2*b+1 for b in binary] # map 0 -> 1 and 1 to -1
        signed = [signs[i]*perm[i] for i in range(n)]
        return signed
