import random
import BinaryStrings
import Permutations
import SignedPermutations

def main():
    # Create a list of RankObjects.
    RankObjects = []
    RankObjects.append(BinaryStrings.BinaryStrings())
    RankObjects.append(Permutations.Permutations())
    RankObjects.append(SignedPermutations.SignedPermutations())

    # Do some random tests on each RankObject.
    n = 4
    for RankObject in RankObjects:

        # Print out the name of this RankObject.
        print("Testing of " + RankObject.name)
        print("")

        # Get a random object and rank it.
        obj = RankObject.random(n)
        index = RankObject.rank(obj)
        print("Random object: " + RankObject.string(obj))
        print("Rank: " + str(index))
        print("")

        # Get a random index and unrank it.
        index = random.randrange(0, RankObject.total(n))
        obj = RankObject.unrank(index, n)
        print("Random index: " + str(index))
        print("Object: " + RankObject.string(obj))
        print("")

        # List out all objects for this value of n.
        L = RankObject.listing(n)
        print(L)

        # Test objects for larger values of n.
        RankObject.test_all()
        print("")
        print("")


if __name__ == "__main__":
    main()
