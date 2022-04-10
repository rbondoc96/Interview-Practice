from time import sleep, perf_counter
from random import randint
from decorators import timer


@timer
def bubble_sort(array):
    if len(array) == 0 or len(array) == 1:
        return

    is_sorted = False
    iterations = 1

    while not is_sorted:
        is_sorted = True

        # No need to include last element in range since we look 1 element to the right
        for i in range(0, len(array) - 1):
            print(f" {iterations} ".center(10, "="))
            print(f"Comparison: {array[i]} > {array[i+1]}")
            print("At", i)
            print("Before:", array)
            if array[i] > array[i + 1]:
                is_sorted = False

                # Right is calculated first, then
                # the tuple is destructured for the assignment
                array[i], array[i + 1] = array[i + 1], array[i]

            print("After:", array)
            iterations += 1

        if not is_sorted:
            print("\n*** Not sorted, going again... ***\n")


@timer
def bubble(array):
    N = len(array)
    iterations = 0

    for i in range(N):

        # The largest elements in each iteration will "bubble" to the last position
        # So, we can decrease the window we're looking at since we know that
        # larger values will keep floating to the top.
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            iterations += 1

"""
array = [2, 1, 5, 4, 3]

#1 --> [1, 2, 4, 3, 5]
#2 --> [1, 2, 3, 4]
#3 --> [1, 2, 3]
#4 --> [1, 2]
#5 --> [1], return
#4 --> chunk = [1], append list(n-1)
#3 --> chunk = [1, 2], append list(n-1)
#2 --> chunk = [1, 2, 3], append list(n-1)
#1 --> chunk = [1, 2, 3, 4], append list(n-1)
DONE --> chunk = [1, 2, 3, 4, 5]
"""
def recursive_bubble(array):
    """

        return recursive_bubble(array[:N-1])
    """
    if len(array) == 1:
        return array
    else:

        # After loop, largest element is at the end
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        # Repeat with array minus the largest element
        chunk = recursive_bubble(array[:len(array)-1])
        chunk.append(array[-1])
        return chunk


def test():
    array = [8, 3, 1, 7, 0]
    target = [0, 1, 3, 7, 8]


    bubble_sort(array)
    assert array == target


    array2 = [randint(0, 1000) for i in range(5)]
    target2 = sorted(array2)
    bubble(array2)
    assert array2 == target2


    array3 = [8, 3, 1, 7, 0]
    start = perf_counter()
    array3 = recursive_bubble(array3)
    end = perf_counter()
    print(f"recursive_bubble() took {end-start}s.")
    assert array3 == target


    print("All tests passed.")    


if __name__ == "__main__":
    test()