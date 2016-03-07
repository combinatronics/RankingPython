'''
Ranking and unranking of binary strings using standard lexicographic order.
'''

from RankObject import RankObject

class BinaryStrings(RankObject):
    def __init__(self):
        self.name = "binary string"

    def string(self, binary):
        return super(BinaryStrings, self).string(binary, blank=False)

    def total(self, n):
        return 2**n

    def rank(self, binary):
        n = len(binary)
        value = 0
        power = 1
        for bit in reversed(binary):
            value += power * bit
            power *= 2
        return value

    def unrank(self, rank, n):
        if not self.is_valid_rank(rank, n):
            return None
        binary = []
        for i in range(n):
            bit = rank % 2
            binary.append(bit)
            rank /= 2
        return list(reversed(binary))
