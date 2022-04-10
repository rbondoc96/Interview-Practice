# Merge Sort - "Divide and Conquer"

## Time Complexity
- Worst Case: O(n * log(n))

## Space Complexity
- Worst Case: O(n)



The idea behind a Merge Sort is that you split a huge array down as much as possible and then over time build it back up, doing comparisons and sorting at each step along the way.
- This idea of breaking up an array, sorting all the parts of it, and putting it back together is called **Divide and Conquer**.


# An Example
array = [8, 3, 1, 7, 0, 10, 2]

**Step 1**
In its smallest pieces, they are individual elements. Building them together, they can be put in pairs of 2:

p1 = [8]        # Whether or not the single cell is from the end or start depends on the implementation.
p2 = [3, 1]
p3 = [7, 0]
p4 = [10, 2]

We'll compare these elements to see which one is smaller. Keep track of how many comparisons we do.
p1 = [8]
p2 = [1, 3]     # Was 3 > 1? Yes, so switch
p3 = [0, 7]     # Was 7 > 0? Yes, so switch
p4 = [2, 10]    # Was 10 > 2? yes, so switch

We did 3 comparisons. 

**Step 2**
Now, we'll examine p1 + p2 and p3 + p4
pA = [8] + [1, 3]
We're comparing an array of 1 element to an array with 2 elements. We know the array with 2 elements is already sorted. The first element of pA will either come from p1 or p2.

pA = [1]        # 8 > 1? - Add 1
pA = [1, 3]     # 8 > 3? - Add 3
pA = [1, 3, 8]  # Since p2 has been added, just tack in what's in p1.


pB = [0, 7] + [2, 10]
We'll start with comparing the first element for each array, 0 and 2.

pB = [0]            # 0 > 2? - No, add 0
pB = [0, 2]         # 2 > 7? - No, add 2
pB = [0, 2, 7]      # 7 > 10? - No, add 7
pB = [0, 2, 7, 10]

With pA and pB, we did a total of 5 comparisons. 

**Step 3**
We're not done yet though, just one more round to get to the sorted array.

It's the same as the last round, we start off by comparing the first 2 elements of the 2 arrays that we have.
pA = [1, 3, 8]
pB = [0, 2, 7, 10]
1. 1 > 0? - Yes, add 0 [0]
2. 2 > 1? - yes, add 1 [0, 1]
3. 3 > 2? - Yes, add 2 [0, 1, 2]
4. 3 > 7? - No, add 3 [0, 1, 2, 3]
5. 7 > 8? - No, add 7 [0, 1, 2, 3, 7]
6. 8 > 10? - No, add 8 [0, 1, 2, 7, 8]
7. Add 10! 
result = [0, 1, 2, 3, 7, 8, 10]

To get to the result from pA and pB, we had to do 6 comparisons.


## Efficency
Here's the arrays we got at each step:
- Step 1 - 3 comparisons
    - p1 = [8]                          # 0 comparisons
    - p2 = [1, 3]                       # 1 comparison
    - p3 = [0, 7]     
    - p4 = [2, 10]
- Step 2 - 5 comparisons
    - pA = [1, 3, 8]                    # 2 comparisons
    - pB = [0, 2, 7, 10]                # 3 comparisons
- Step 3 - 6 comparisons
    - result = [0, 1, 2, 3, 7, 8, 10]   # 6 comparisons

It looks like that in each step, we did one less comparison than the array we were building. In step 3, we were building an array of 7, so we only did 6 comparisons. Let's denote the length of an array as `m`, then the # of comparisons would be `m - 1`.
- It's hard to get an exact amount of how many comparisons there would be, but we can approximate.
    - Since every iteration just cycles through the same 7 elements over and over, we know the size of all arrays will always be 7, or `m` again.
    - We're just dividing and conquering. We can approximate and say we're going to do 7 comparisons at each step.
        - 7 is an upper bound, we're never going to do more than 7 comparisons, but we can get close to it.


To get the runtime of a sorting algorithm, we can normally multiply the number of overall iterations by the number of comparisons at each iteration.
- In the examples above, `3 iterations` and `3 + 5 + 6 (24) comparisons`. The # of elements `n = 7`. At most, we're doing `n` comparisons at every step
    - In Bubble Sort, we were doing `n` comparisons and `n` steps.

In this table, we get the # of iterations/steps from our example.

| Array Size | # Iterations |
| ---------- | ------------ |
| 1 | 0 | 
| 2 | 1 |
| 3 | 2 | 
| 4 | 2 | 
| 5 | 3 | 
| 6 | 3 | 
| 7 | 3 |
| 8 | 3 | 
| 9 | 4 | 

The table actually looks similar to the table from a Binary Search!
- The # of iterations increases at roughly every power of 2 (really the next number after a power of 2). 
    - This gives us N = 2^i + 1 --> N - 1 = 2^i, i = log(N - 1)
    - Here, i is the # of iterations.

So... Big O = # of iterations * # of comparisons = log(n - 1) * n
O(n) = n * log(n - 1), or simply O(n) = n * log(n). An approximation is fine!


## Comparing to Bubble Sort
Compared to the Bubble Sort that was O(n^2), O(n*log(n)) is better!
- log(n) is generally going to be less than n, but its never going to be greater than n.

However, the **space efficiency** of merge sort is actually worse than bubble sort! Remember that Bubble Sort was O(1) in space because it was an in-place sorting algorithm. Here, we frequently copied our values into new arrays. The # of elements still was N, so we can say:
`The auxillary (extra) space = O(n)`

...as long as we got rid of the old ones at the end of each step so we don't use a ton of new arrays every time.


## Example
If you were to perform a merge sort on the following array, which is a possibility for what the second iteration might look like (i.e.) after bubbling all the way up 2 times?

[21, 4, 1, 3, 9, 20, 25]

**Step 1**
p1 = [21]
p2 = [4, 1] --> [1, 4]
p3 = [3, 9]
p4 = [20, 25]

end = [21, 1, 4, 3, 9, 20, 25]

**Step 2**
pA = [1, 4, 21]
pB = [3, 9, 20, 25]

**Step 3**
end = [1, 3, 4, 9, 20, 21, 25]

