"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    start_idx = 0
    end_idx = len(input_array) - 1

    # Loop until start passes end or end passes start
    while start_idx <= end_idx:
        mid_idx = int((start_idx + end_idx) / 2)
        
        if value == input_array[mid_idx]:
            return mid_idx
        elif value > input_array[mid_idx]:
            # Place start index to the right of the middle
            start_idx = mid_idx + 1
        else:
            # Place end index to the left of the middle
            end_idx = mid_idx - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print()
print(binary_search(test_list, 1))
print(binary_search(test_list, 3))
print(binary_search(test_list, 9))
print(binary_search(test_list, 11))
print(binary_search(test_list, 15))
print(binary_search(test_list, 19))
print(binary_search(test_list, 29))