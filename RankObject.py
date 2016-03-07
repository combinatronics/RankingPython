'''
Abstract base class RankObject.
'''
from random import randrange

class RankObject(object):
    def __init__(self):
        self.name = "ranking object"

    def string(self, obj, blank=True):
        s = ""
        for x in obj:
            s += str(x)
            if blank: s += " "
        return s

    def total(self, n):
        raise NotImplementedError

    def rank(self, obj):
        raise NotImplementedError

    def unrank(index, n):
        raise NotImplementedError

    def is_valid_rank(self, index, n):
        return index >= 0 and index < self.total(n)

    def random(self, n):
        index = randrange(0, self.total(n))
        obj = self.unrank(index, n)
        return obj

    def listing(self, n):
        s = ""
        for index in range(self.total(n)):
            obj = self.unrank(index, n)
            assert(self.rank(obj) == index)
            s += str(index)
            s += ": "
            s += self.string(obj)
            s += "\n"
        return s

    def test_all(self, verbose=True):
        for n in range(1, 21):
            total = self.total(n)
            if total > 100000: break
            passed = self.test_n(n)
            if verbose: print("n =  " + str(n) + " " + str(passed))
            if passed == False: return False
        return True

    def test_n(self, n):
        # Test the unrank function by creating a list of all objects.
        object_list = []
        total = self.total(n)
        for i in range(total):
            next_object = tuple(self.unrank(i, n))
            object_list.append(next_object)
        object_set = set(object_list)
        if (len(object_set) != total):
            return False

        # Test the rank function for all of the signed permutations created above.
        for i, next_object in enumerate(object_list):
            pos = self.rank(next_object)
        if pos != i:
            return False

        return True
