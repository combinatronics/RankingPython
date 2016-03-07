'''
Ranking and unranking permutations using the order given by Ruskey and Myrvold
in "Ranking and unranking permutations in linear time".
Note: The order used here is *not* lexicographic order.
'''

from RankObject import RankObject
from math import factorial

class Permutations(RankObject):
    def __init__(self):
        self.name = "permutation"

    def total(self, n):
        return factorial(n)

    def rank(self, perm):
        def recursive(m, copy, inv_perm):
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
            return s + m * recursive(m-1, copy, inv_perm)
        n = len(perm)
        perm = list(perm)
        copy = list(perm)
        inv_perm = n * [-1]
        for i in range(n):
            inv_perm[perm[i]-1] = i+1
        rank = recursive(n, copy, inv_perm)
        return rank


    def unrank(self, rank, n):
        if not self.is_valid_rank(rank, n):
            return None
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
