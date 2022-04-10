# Heaps

A Heap is another variant of a Tree with some additional rules. Heaps don't need to be binary trees, so parents can have any number of children.

Elements are arranged in increasing or decreasing order, such that the root is either the maximum or minimum element in the tree.
    There are 2 different types of heaps that capture those situtations, Max Heaps and Min Heaps.

## Max and Max Heaps
In this type of Heap, a parent must always have a greater value than its child, so the root ends up being the biggest element:

```
    7
   / \
  5   3
 / \
2  1
```

The opposite is true for Min Heaps, a parent has a lower value than its child, so the root ends up being the smallest element:

```
    1
   / \
  2   3
 / \
5  7
```

Operations like search, insert, and delete can vary a lot based on the type of heap we're discussing. 


## Max Binary Heaps
A Binary Heap must be a **complete** tree.

```
    7
   / \
  5   3
 / \
2  1
```

**Complete Tree**: All levels, except the last one, are completely full.

If the last level isn't totally full, values are added from left to right. The right-most leaf will be empty until the whole row has been filled. 

### peek() - Finding the Maximum Value
The peek() operation in a Max Binary Heap gets the maximum value, which is the root node. This operation takes O(1) time. 


### Search
In the diagram above, we're going to look for `2`. But should we start searching left or right? In a BST, we knew which direction to look by doing comparisons, but in a Max Binary Heap, there's no guarantee.
    Thus, searching ends up being a linear time operation O(n) since we normally can't rely on tricks and we'll end up searching the entire tree. 

However, we can use the Max Heap properties as an advantage. For example, we can quit our search immediately if the element we're searching for is bigger than the root. 
    In general, if our node value is bigger than the one we're comparing to, we don't need to check anything in its subtree, since we know that its the biggest. 

The Worst Case remains that search is O(n), but in the average case, it's about `O(n/2) = ~O(n)`


## Heapify - Inserting an Element
We could take the approach with BSTs: start at the root, then move down the tree 1 level at a time and do comparisons until we find an open spot. 

However, if our element is bigger than most of the parent nodes or even the root, we'll need to shuffle the tree around a lot. 
    Instead, we can insert the new element `21` in an open spot in the Tree. Then, we "heapify".

**Heapify**: The operation in which we reorder a tree based on the Heap property. 

Since we care that our parent element is bigger than its child, we just need to keep comparing the new element with its parent and swapping them when the child is bigger.

```
     30
   /    \
  25     20
 / \     /  \
15  10  5   *21*
```


## Heapify - Extract the Root
A similar approach happens with an Extract operation, where the root is removed from the Tree. We stick the rightmost leaf in the root spot, then just compare it to its children and swap where necessary.

The Worst Case for Insertion and Delete, a more general case of Extract, ends up being O(log(n)). 
    The Worst Case involves moving an element all the way up or down a tree, and would roughly be as many operations as the Height of the Tree. 


## Implementation
Though Heaps are represented as Trees, their implementations are often Arrays.

Since we know how many children each parent has, `2`, and thus how many nodes will be at each level, we can use a little math to figure out where the next node will fall in the Array, and then traverse the Tree.

```     
     30             1 node
   /    \
  25     20         2 nodes
 / \     /  \
15  10  5   21      4 nodes
```

### Array to Heap Representation Example
Let's convert this sorted Array into a Tree

sortedArray = [19, 17, 13, 11, 7, 5, 3, 2, 1]
- 19 will be the `root` since it's the biggest.
- The next 2 elements in the Array are the children of the root
    - By convention, insertion happens from Left to Right, but it doesn't really matter as long as they're on the second level. 
- **Again**, each level on the tree is double the size of the one before it, so we know the next level has 4 elements.
    - This can be done programmatically by tracking the size of the each level in a variable, then doubling it each time we move to a new level.
- Everything left over fills in the left side of the last level

```
        19             
      /    \
     17     13         
    /  \     /  \
  11    7   5    3
  / \
 2   1 
```

<span style="color:red">However, not every Array can be represented as a Heap.</span> The example could because the Array was sorted in descending order. 

In general, the numbers need to be in an order that will make sense on a Heap. Storing data in an Array can save some space.
    If we use an Array, we just need to store the Node value and the index in the Array slot. 
    But in a Tree, we need the value, left child pointer, right child pointer, and possibly a parent pointer. 
Since the Array saves us the pointers, it saves us space. 