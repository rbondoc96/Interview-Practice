from random import randint


def merge(array, left, right):
    l = r = k = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            array[k] = left[l]
            l += 1
            k += 1
        else:
            array[k] = right[r]
            r += 1
            k += 1

    # There are no more elements in <right> to compare, append everything else
    while l < len(left):
        array[k] = left[l]
        l += 1
        k += 1

    # There are no more elements in <left> to compare, append everything else
    while r < len(right):
        array[k] = right[r]
        r += 1
        k += 1


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        print("Left", left)
        print("Right", right)

        merge(array, left, right)


def test():
    array = [15, 3, 9, 33, 0, 5]
    target = [0, 3, 5, 9, 15, 33]

    merge_sort(array)
    assert array == target
    print("Test 1 passed.")

    # array2 = [randint(0, 1000) for _ in range(100)]
    # target2 = sorted(array2)
    # merge_sort(array2)
    # assert array2 == target2

    # print("Test 2 passed.")


    print("All tests passed.")


if __name__ == "__main__":
    test()