# Quick Sort

# Time Complexity
- Best Case: O(n * log(n))
- Average Case: O(n * log(n))
- Worst Case: O(n^2)

# Space Complexity
This version of Quick Sort is in-place, so space complexity is O(1)


In many cases, Quick Sort is one of the most efficient sorting algorithms. 

To do a Quick Sort:
1. Pick one of the values in the array at random. (A pivot)
2. Move all values larger than it, above it and all values below it, lower than it.
3. Continue recursively, picking a pivot in the upper and lower sections of the array, sorting them similarly until the whole array is sorted.


## Example

array = [8, 3, 1, 7, 0, 10, 2]

How do we pick a pivot? The convention is to pick the last element as the pivot.

pivot = 2

Our first element `8` is larger than our pivot, so it needs to move behind the pivot. However, we're doing an in-place sort, so we need to move the element that's in front of the pivot to make room.

**Steps**
1. Move 8 to the last block
2. Move 2 where 10 is
3. Move 10 where 8 was (the first block)
`RESULT = [10, 3, 1, 7, 0, 2, 8]`

Now that we did our shift, we can make another comparison. Let's compare 10 and 2. 10 is bigger than 2.

**Steps**
1. Move 10 behind 2 
2. Move 2 where 0 is
3. Move 0 to where 10 was (the first block)
`RESULT = [0, 3, 1, 7, 2, 10, 8]`

We can compare 0 and 2. However, 0 is already less than 2 and to the left of 2, so we can move on to the 2nd element.

Let's compare 3 and 2. 3 is greater than 2.

**Steps**
1. Move 3 behind 2
2. Move 2 where 7 is
3. Move 7 where 3 was
`RESULT = [0, 7, 1, 2, 3, 10, 8]`

Since 7 is greater than 2, we need to swap again.

**Steps**
1. Move 7 behind 2
2. Move 2 where 1 is
3. Move 1 where 7 was
`RESULT = [0, 1, 2, 7, 3, 10, 8]`

Here, now that we know that everything to the left of 2 is actually less than 2 and everything above 2 is greater than 2, we know 2 is in the exact right place. 

At this point, we do the same process for everything smaller than the pivot and everything larger than the pivot. Let's start with the smaller part first, `[0, 1]`

We select our pivot and compare it to everything before. With `pivot = 1`, we compare it to 0. Since they are already sorted, we don't need to do anything.

Let's do the second half with `pivot = 8`. Since 7 and 3 are already smaller than 8, we just need to swap 10 and 8.

`RESULT = [0, 1, 2, 7, 3, 8, 10]`

Now, everything less than 8 is below it and everything greater than 8 is below it. Since only 10 is right of 8, we know it's in the right position. We only need to look at `[7, 3]

With `pivot = 3`, we can see that they need to switch, so:

`RESULT = [0, 1, 2, 3, 7, 8, 10]`


## Efficiency

The magic of this algorithm is that it cuts the number of comparisons needed by splitting the array in half pretty much every iteration. 

The effiency of a quick sort is fairly complicated. Let's start at worst case.

**Worst Case**
The worst case is if we couldn't split the array in half and had to do all of the comparisons every time. You'll end up doing all of the comparisons if the pivots are already in the right place!

```
array = [1, 8, 2, 5, 3, 9, 13]
pivot = 13
```
Here, 13 is already in the right place and we'd end up doing all n-1 comparisons. If we switch to 9, the same happens and we compare n-2 comparisons. 

Remember that in Bubble Sort, we'd compare each element to the one next to it, again and again and again. Eventually, we could leave off the ones that were at the end because we knew they were in the right place. The worst case for Quick Sort is exactly the same.

<span style="color:blue">Therefore, worst case is O(n^2)</span> 

<span>It's best not to use Quick Sort if we know that the already is already nearly sorted.</span>

**Average and Best Case**
For the average and best case, time complexity is O(n * log(n)).

**Best Case**
In the best case, the pivot ends up at the middle and we'll get to divide the array in half every time.
- This would cascade. The pivots for the left and right halves would move to their middles too.
- Since the pivots are sorted, we know everything else is sorted.
- We're cutting everything in half, so it ends up looking like a merge sort.

In the average case, the pivot ends up close to the middle, but not exactly.


## Optimizations
There are ways to make Quick Sort run faster. 

1. @hen you split your array, you can configure your program such that it runs both halves at the same time.
    - It'll end up using the same amount of computer power, but it'll take less time. 
2. Rather than selecting the last element as a pivot, you can look at the last few elements and take the median as a pivot. Selecing the median will give a better sense of the middle of the array overall. This gives a better chance of the pivot going right in the middle and having the best case scenario
    - Ex. `[..., 56, 13, 2]; pivot = 2`