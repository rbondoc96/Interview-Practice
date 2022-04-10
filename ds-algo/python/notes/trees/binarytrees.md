# Binary Trees

Binary Trees are trees where parents have **at most two children**. This means nodes can have 0, 1, or 2 children. Those children can also be a null value (the case for leaf nodes)

## Search Operation
We could start by using any of the traversal algorithms we have to go through the Tree. Since there's no real order to the elements, we need to go through every single element in the Tree if the value we're looking for doesn't exist.

Since there's no tricks, we're stuck with O(n) search at worst case.


## Delete Operation
A delete operation often starts out with a search since you need the node you want to delete.

If you're deleting a leaf, you can simply delete it and move on. However, if you delete an internal node, you'll suddenly have a gap in the Tree. 
- If the node you deleted only has 1 child, you can actually just take it out, move the child up, and attach it to the old node's parent.
- If the node has 2 children, there are a few options
    1. Promote the child up like with 1 child, but what if both children also have 2 children? 
        - In the worst case, you'll need to keep traversing down the sub tree until a leaf is hit.
        - Since there's no order requirement, you can put the leaft where your deleted node was without a problem.

Since there's a search involved and some additional work to shift around the nodes, we get O(n) delete.


## Insertion Operation
If the Tree has no order, it's easy to add a new node to the Tree. We'll just tack on the node onto another node. 
    Maybe it's a leaf or maybe its a parent with only 1 child.

We just need to make sure we're obeying the 2 children rule. 
1. We're given the root at the beginning. 
2. Keep moving down the tree until we find an open spot. 
    - But how long will this take? The worst case is that we travel down the longest path until we find the farthest leaf. In that case, we travel the # of nodes == to the height of the Tree. 


### Finding the Height of a Binary Tree

**Perfect Tree**: Every node, except the leaves on the last level, has exactly 2 children.

As a three grows bigger, each new level has the capacity to hold a number of nodes equivalent to a power of 2. This means that each new Level can have twice as many nodes as the one before it


## Variants of a Binary Tree
Trees are inherently unorganized. When we use a tree, we know what the overall structure looks like, but we don't know where a specific element will be. 

We can add some rules to the ordering of elements in our Trees to accomplish certain tasks really fast. 