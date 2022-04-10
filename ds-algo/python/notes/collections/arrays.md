# Arrays

## Time Complexity
- Insertion
    - Best Case: O(1) -- insertion at the end 
    - Worst Case: O(N) -- insertion at the beginning 
        - All elements must shift down 1 index
- Deletion
    - Best Case: O(1) -- deletion at the end 
    - Worst Case: O(N) -- deletion at the beginning
- Access an element at location i
    - O(1)


Arrays are the most common implementation of lists. Most programming languages have a core ability to create arrays.

An Array is a List with some added rules, so we already know it has some things in some order.
- Some languages restrict Arrays to have elements of the same type in the same array.
- Some languages allow Arrays to contain elements with different types.
- Some languages have a fixed size for Arrays, some don't.

The biggest thing that differentiates Arrays from Lists. Each Array has a location called an **index**. 
- **Index**: The number associated with that place/element in the array.
    - Normally, an index starts at 0.
    - An Array of length 5 has indexes 0, 1, 2, 3, and 4.


## When to Use Them
1. If you need to access a certain location in the middle frequently, using an array can be a great choice.


## Insertion and Deletion
Things get a bit more complicated with inserting and deletion.

**Insertion**
- Inserting at the end can be easy, unless the Array is full and has a set size.
- Inserting in the middle can be difficult. You'll need to shift elements down to add an element in a specific place.
    - Worse Case: O(n)


**Deletion**
Deletion is similar to insertion. If there's an empty box due to an element being deleted, elements may need to shift up to fill the empty space.
