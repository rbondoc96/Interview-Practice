import unittest
from random import randint

class QuicksortTests(unittest.TestCase):
    def test_normal_list(self):
        test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        target = sorted(test)

        quicksort(test)
        self.assertEqual(test, target, "These lists should be equal.")


    def test_random_list(self):
        test = [randint(0, 1000) for _ in range(100)]
        target = sorted(test)

        quicksort(test)
        self.assertEqual(test, target, "These lists should be equal.")   


    def test_empty_list(self):
        test = []
        target = []

        quicksort(test)
        self.assertEqual(test, target, "These lists should be equal.")             


    def test_list_with_one_element(self):
        test = [1]
        target = [1]

        quicksort(test)
        self.assertEqual(test, target, "These lists should be equal.")          


# Use Recursion?
def quicksort(array):
    _quicksort(array, 0, len(array) - 1)


def _quicksort(array, lo, hi):
    if lo < hi and lo >= 0:
        p_idx = partition(array, lo, hi)

        _quicksort(array, lo, p_idx - 1)
        _quicksort(array, p_idx + 1, hi)


def partition(array, lo, hi):
    pivot = array[hi]
    i = lo
    for j in range(lo, hi):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[hi] = array[hi], array[i]
    return i


def test():
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    target = sorted(test)

    quicksort(test)
    assert test == target

    print("All tests passed.")


if __name__ == "__main__":
    unittest.main()