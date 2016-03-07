import random
import BinaryStrings
import Permutations
import SignedPermutations

def main():
    # Create a list of GenerateObjects.
    GenerateObjects = []
    GenerateObjects.append(BinaryStrings.BinaryStrings())
    GenerateObjects.append(Permutations.Permutations())
    GenerateObjects.append(SignedPermutations.SignedPermutations())

    # Do some random tests on each GenerateObject.
    n = 4
    for GenerateObject in GenerateObjects:

        # Print out the name of this GenerateObject.
        print("Testing of " + GenerateObject.name)
        print("")

        # Get a random object and rank it.
        obj = GenerateObject.random(n)
        index = GenerateObject.rank(obj)
        print("Random object: " + GenerateObject.string(obj))
        print("Rank: " + str(index))
        print("")

        # Get a random index and unrank it.
        index = random.randrange(0, GenerateObject.total(n))
        obj = GenerateObject.unrank(index, n)
        print("Random index: " + str(index))
        print("Object: " + GenerateObject.string(obj))
        print("")

        # List out all objects for this value of n.
        L = GenerateObject.listing(n)
        print(L)

        # Test objects for larger values of n.
        GenerateObject.test_all()
        print("")
        print("")


if __name__ == "__main__":
    main()
