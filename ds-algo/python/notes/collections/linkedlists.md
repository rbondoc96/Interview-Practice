# Linked Lists

## Variations
- Singly Linked List (default version): Each node in the structure contains a pointer to the `next` element in the list.
- Doubly Linked List: In addition to a pointer to the `next` element, each node also has a pointer to the `previous` element.


## Time Complexities
- Insertion
    - Best Case: O(1) - Insert at beginning
    - Worst Case: O(n) - Insert at the end
- Deletion
    - Best Case: O(1) - Delete at the beginning
    - Worst Case: O(n) - Delete at the end
- Get Element
    - Best Case: O(1) - Head element
    - Worst Case: O(n) - Last element
- Find X in the list
    - Best Case: O(1) - Head element
    - Worst Case: O(n) - Last element


A Linked List an extension of a List, but it is not an array.
- There are things with order, but it has **no indicies**
- Each element is connected to the element after it.

Each element has a notion of what the next element is, but not necessarily where in the list it is, or how long the list is. 

The main distinction between an Array and a Linked List is that each element in the structure stores different information.

**Array Elements**: These store a value and the element's index.

**Linked List Nodes**: These store a value and a reference/memory address (`next`) to the next element in the list. 


## Insertion and Deletion
Insertion is simple. All you need to do is change the `next` references of some cells. 

When inserting an item between 2 elements, <span style="color:red">make sure to tie the `next` references such that you don't lose any references</span>


Deletion works similarly to insertion. It's just pointers moving around.

