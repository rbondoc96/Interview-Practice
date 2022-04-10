# Python Lists

## Time Complexities - https://wiki.python.org/moin/TimeComplexity
- Copy: O(n)
- Insert Last: O(1)
- Insert: O(n)
- Remove Last: O(1)
- Remove middle: O(n)
- Get Element: O(1)
- Set Element: O(1)
- Iteration: O(n)
- Find element X: O(n)
- max()/min(): O(n)
- len(): O(1)

**For slices of data of length 'k'**
- Get slice: O(k)
- Remove slice: O(n)
- Set slice: O(k+n)


The `list` type/data structure contains the functionalities of some other list-based data structures.

## Behind the Scenes
A `list` is built as an array. Many of the list operations take only one line of Python code, but the code that built Python is doing more in the background to make that happen.
    With CPython (Python built using C), C code is being used to manipulate the `list`. Knowing C, think about how pointers and memory allocation works.


For example, inserting into a List is O(1). However, inserting into an Array is O(n), since element shifting may be needed to make space for the new element, or even copying everything into a new, larger array if you run out of space.