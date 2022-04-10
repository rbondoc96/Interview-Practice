# Sorting Algorithms

In a searching algorithm, we're given some sort of List, and we just looking at each element. In a sorting algorithm, we're changing the order of each element.

Typically, we asking 2 questions when sorting things:
1. Do we put the smallest value first or last?
2. What algorithm do we use to sort?

**Naive Approach**: Compare every element to every other element until everything is in order. 
- There's no real trick going on here. It's probably the first thing the brain thinks of when you see a new problem.
    - Hmm... I could do it this way, but there's probably a smarter way.

## In-Place Sorting Algorithms

An in-place sorting algorithm just rearranges the elements in the data structure they're already in without copying into another structure.
- Because of this, they have **low space complexity** since you don't need to recreate the data structure.

There's typically a trade-off between less space vs less time.