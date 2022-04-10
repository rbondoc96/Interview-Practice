# Bubble Sort


## Space Complexity
- O(1), we didn't need any extra structures in the whole process


## Time Complexities
- Worst Case: O(n^2)
- Average Case: O(n^2)
- Best Case: O(n)


## Example Question
If you were to perform a bubble sort on the following array, what would the third iteration look like (i. e. after bubbling all the way up 3 times)?
`[21, 4, 1, 3, 9, 20, 25, 6, 21, 14]`
1: [4, 1, 3, 9, 20, 21, 6, 21, 14, 25]
2: [1, 3, 4, 9, 20, 6, 21, 14, 21, 25]
3: [1, 3, 4, 9, 6, 20, 14, 21, 21, 25] * Answer
4: [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]



The Bubble Sort, or Sinking Sort, is a naive approach to sorting. You'll go through you array comparing elements side-by-side and switching them whenever necessary.

It is an in-place algorithm, since we didn't have to use any extra data structures to do the sort. 

Here's an example. We want to sort this list from least to greatest.

array = [8, 3, 1, 7, 0]

Let's start with the first element and compare to the next.
| # | Comparisons | List After Comparison | Comments |
| - | ----------- | --------------------- | -------- |
| 1 | 8 > 3? | [3, 8, 1, 7, 0] | 
| 2 | 8 > 1? | [3, 1, 8, 7, 0] |
| 3 | 8 > 7? | [3, 1, 7, 8, 0] |
| 4 | 8 > 0? | [3, 1, 7, 0, 8] | End of 1st iteration; O(n - 1) |
| 5 | 3 > 1? | [1, 3, 7, 0, 8] |
| 6 | 3 > 7? | [1, 3, 7, 0, 8] | No change!
| 7 | 7 > 0? | [1, 3, 0, 7, 8] | We switch to 7 since 3 was less than 7.
| 8 | 7 > 8? | [1, 3, 0, 7, 8] | No change! End 2nd iteration; O(n - 1)
| 9 | 1 > 3? | [1, 3, 0, 7, 8] | No change!
| 10 | 3 > 0? | [1, 0, 3, 7, 8] | 
| 11 | 3 > 7? | [1, 0, 3, 7, 8] | No change!
| 12 | 7 > 8? | [1, 0, 3, 7, 8] | No change! End 3rd iteration; O(n - 1)
| 13 | 1 > 0? | [0, 1, 3, 7, 8] | Array is sorted! But we have to keep going.
| 14 | 1 > 3? | [0, 1, 3, 7, 8] | No change!
| 15 | 3 > 7? | [0, 1, 3, 7, 8] | No change!
| 16 | 7 > 8? | [0, 1, 3, 7, 8] | No change! End 4th iteration; O(n - 1)


Notice that with each iteration, the largest element in the array will `bubble` on up to the top.

Note that the method used in the table could be simplified. After Iteration 8, we still compare 7 and 8 again in Iterations 12 and 16. Common versions of Bubble Sort leave out this repeated step. 
- After the 1st iteration, we know that 8 is in the right place, so you wouldn't need to check it against anything else later.
- This would save time, but would not change the complexity from O(n^2)


## Efficiency

Here's a table of what we did in the example:

| Iteration # | # of Comparisons |
| ----------- | ---------------- |
| 1 | n - 1 |
| 2 | n - 1 |
| 3 | n - 1 |
| 4 | n - 1 |

Note that the total # of iterations, 4, was n - 1 since `n = 5`.

Big O would be `iterations * comparisons` == (n - 1) * (n - 1).
- Which is n^2 - 2n + 1. This simplifies down to O(n^2)

However, in the best case, when the list is actually sorted or if only 1 number is out of place, the complexity is simply O(n).