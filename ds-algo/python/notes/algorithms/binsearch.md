# Binary Search Algorithm


## Time Complexity: O(log(n))


## Motivation
Let's say we have an <span style="color:blue">**Array sorted in increasing order**</span>:
```python
array = [1, 3, 9, 11, 15, 19, 29]
```
and we want to see if a number 'X' exists in the Array. 

If you start at the front or back of the Array and check every number, time complexity could be O(n) if 'X' is large. This would be called a **Linear Search**.

Instead, if we started in the middle of the Array, we could see if 'X' is larger than the middle. 
- For example, if `x = 25` and the middle value of the `array` is 11, we just have to look at the second half of the array `[15, 19, 29]`


## Effiency
The time efficiency is really just the # of steps needed to finish the algorithm. Keeping track of each iteration of the algorithm helps!

For example, with an array size of 8 and choosing to compare to the lower side:
```python
X = 10
array = [1, 2, 3, 4, 5, 6, 7, 8]
```
It would take **4** iterations to complete the algorithm
1. 10 > 4?
2. 10 > 6?
3. 10 > 7?
4. 10 > 8?

| Measure    |   |   |   |   |   |   |   |   |   |
| ---------- | - | - | - | - | - | - | - | - | - |
| Array Size | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| Iterations | 0 | 1 | 2 | 2 | 3 | 3 | 3 | 3 | 4 | 


If we cut the array size in half through each iteration, that also means if we double the array size, an extra iteration needs to happen.
In the table above, we can see that every time the array size doubles, the # of iterations goes up by 1. (See array size at 1, 2, 4, 8)

Looking at the exponential form of those sizes (2^0, 2^1, 2^2, 2^3), we can see that the exponent is 1 less than the # of iterations.

2^3 = 8 ----> log2(8) = 3

O(log2(n) + 1) --> O(log2(n)) **Ding!** That's our time complexity.

People tend to know the effiency of algorithms in 1 of 3 ways:
1. Rote memorization
2. Proofs - A new problem and you don't know the efficiency of the algorithm already
3. Try a results table like the Array Size vs. Iterations table is useful!
    - This will help you notice patterns and helps you start thinking of effieincy as Array Size vs. # of Iterations of the algorithm




## Example
```python
"""
This list has an even # of elements
Decide if you want to err on the lower side or the higher side when there is no real middle.
"""

X = 10
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

middle = floor(len(my_list) / 2)
left = my_list[0:middle]    # [1, 2, 3, 4]
right = my_list[middle:]    # [5, 6, 7, 8]

# Let's err on the lower side and check the greatest value in `left`
"""
10 > 4? - Yes, so we repeat the with `right` array
"""
if X > left[middle]:
    my_list = right
else:
    my_list = left

middle = floor(len(my_list) / 2)
left = my_list[0:middle]    # [5, 6]
right = my_list[middle:]    # [7, 8]

"""
10 > 6?
"""
if X > left[middle]:
    my_list = right
else:
    my_list = left

middle = floor(len(my_list) / 2)
left = my_list[0:middle]    # [7]
right = my_list[middle:]    # [8]

if X == left[0]:
    return True
elif X == right[0]:
    return True
else:
    return False
```