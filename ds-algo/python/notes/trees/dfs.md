# Depth-First Traversals

## Pre-Order Traversal 
Look at a node as you see it before you traverse any further in the tree
1. Start at root, and immediately check off that we've seen it
2. Pick one of the children (normally left first by convention) and check it off too.
3. We continue traversing down the left most nodes until we had a leaf
4. Check off the leaf, then go back to the parent.
5. Go to its right child, check it off, and go back to its grandparent.
6. At the grandparent, now we can look down its right side. We do the same steps until we've seen everything

```
      D
    /   \
   B    E
 /  \    \
A    C    F
```

Result = D, B, A, C, E, F


## In-Order Traversal
We move through the nodes in the same order, since this is a DFS and we need to explore all its children first. However, this time, we check off the nodes in a different order.

We only check off a node after we've seen its left child and come back to it
1. Start at the root
2. Since we haven't seen its left child yet, we have to keep traversing down until we hit a Leaf.
3. Check off the leaf, then move up to the parent
4. Since we've seen the left child, we can check off that node.
5. Go to the right node. Since it doesn't have any children, we can check that off.
6. Go back up to the root, then repeat on the right side.

```
      D
    /   \
   B    E
 /  \    \
A    C    F
```
Result = A, B, C, D, E, F


Why is this called in-order though? It's because we went through the nodes "in order", from leftmost to the tight. We move up and down a lot, but if you just look strictly from left to right, we actually did go through everything in order.


## Post- Order Traversal
This time, we don't check off a node until we've visited all of its descendants, or we visited both of its children and returned.
1. Start at root
2. Continue down to a leaft
3. Check off the leaf, move back to the parent
4. This time, don't check off the parent, move on to the right node.
5. Once we've checked off the right side, we can go back to the parent and finally check it off too. 
6. Skip over the root node and move all the way down to the right
7. Once everything there is good, we can go back to the root node and get it.

```
      D
    /   \
   B    E
 /  \    \
A    C    F
```

Result = A, C, B, F, E, D