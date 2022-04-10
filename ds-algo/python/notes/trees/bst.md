# Binary Search Trees (BSTs)


## Time Complexities
Insert, Search, Delete
- Average Case: O(log(n))
- Worst Case: O(n)



A Binary Search Tree (or BST) is a variant of a Binary Tree. There is a specific rule on how the values associated with each node are arranged. 

BSTs are sorted so that every node on the left of a particular node is smaller than it, and every value on the right of a particular node is to the right of it. 

Because of this rule, we can do operations like search, insert, and delete pretty quickly.

If we want to search for an element, the length of the search just becomes the height of the tree, which is log(n).

Inserting in a binary tree is pretty much the same process. You can start at the top and you can make quick decisions about where to look at each step by comparing to the element you want to add. Eventually, you'll hit that open spot on the Tree.
    As long as you compared your element correctly at each step, you can put your new element there and not violate the core BST properties.

Deleting a node is more complicated, but it's complicated in the same way that it was for the generic Binary Tree.  


## Complications
BSTs are nice to look at when they're full, but there's no rule that states that BSTs need to look that way. 

An **unbalanced* binary tree is a Binary Tree where the distribution of nodes is skewed to one side, like below:

```
5
 \
  10
    \
    15
      \
      20
```

It could start at the root, or in one of the subtrees. An unbalanced binary tree can be considered the worst case scenario for a BST. 

When a BST is unbalanced, search, insert, and delete all actually take **linear** time in the worst case. In the tree above, we would search through every element from the root to the leaf. 