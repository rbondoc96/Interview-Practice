# Self-Balancing Trees

In the Tree world, a Balanced Tree has nodes condensed to only a few levels. An Unbalanced Tree has nodes spread out among many levels. 

The most extreme type of Unbalanced Tree is really just a Linked List, where every Node has only 1 child. 

A **Self-Balancing** Tree is one that tries to minimize the # of levels that it uses. It does some algorithm during insertion and deletion to keep itself balanced. The nodes themselves might have some additional properties. 


## Red-Black Tree

### Time Complexity
- Best Case: O(1)
- Average Case: O(log(n))
- Worst Case: O(log(n))



### Rules
1. Each node has a `color` property that is either Red or Black
2. All null leaf nodes are Black
3. If a node is Red, both of its children must be Black. 
4. (Optional) The root node must be black
5. Every path from a node to its descendent null nodes must have the same # of Black nodes 

These rules ensure that the Tree never gets too unbalanced.

A Red-Black Tree is an extension of a BST. In this type of Tree, nodes are assigned an additional color property where the values must either be Red or Black. 
    The use of Red or Black is just a convention. It's just a way to distinguish between 2 different Nodes. 

Another property of an RBT is the existence null leaf nodes. 
    Every node in the Tree that doesn't otherwise have 2 leaves must have null children. All null leaf nodes must be colored Black. 

If a node is Red, both of its children must be Black.


### Insertion
There are several different states of the Tree and the node you're inserting that require different courses of action. 

Remember that the resultant Tree needs to follow both the Red-Black Tree and BST rules. 

One overall rule of insertion is that you should try to insert a node as a Red node and then change its color as needed. 

#### Case 1 - Inserting the First Node into a Tree
Since it's the root, the node can be changed to Black if obeying the `root must be Black` rule. Otherwise, you'll have nothing to do. 


#### Case 2
If the new parent node is Black, you don't need to do any work. Since we're adding a Red node, we haven't upset the balance of Black nodes in any path or violated any of the other rules.

```
    9b
  /
 6r 
```


#### Case 3 - Parent is Red
We added `13`.

If the parent is Red, there are several cases with more complicated solutions. 

If the parent and its sibling are both red, then they should be changed to Black. 
- Their parent, the grandparent of the node you're inserting, becomes red. 
- Node colors are switched in this way to maintain the # of Black nodes in a given path. 

Howver, we could've violated another property by changing the grandparent. We can treat the grandparent as a newly inserted node and change it, or its ancestors according to the same cases and rules. 

We can treat it as Case 1 and change it back to Black since we still want the route to be Black. 

```
Tree A                  Tree B

    9b                      9b
  /    \                  /    \
 6r    19r  ----->      6b     19b
      /                       /
     13r                    13r
```

Look through all the paths in Tree B. The # of Black nodes in each path is still 2. 
    Remember that null leaf children are Black nodes!


#### Case 4 & 5 - Node's Parent is Red, Parent's Sibling is Black

```
    9b
   /  \
  6r  19b
      /
     13r
        \
         16r    <---inserted node 
```
16r's parent is 13r, and 13r's sibling is a Black (null) node.

In both cases, we'll need to perform a rotation. In a rotation, we shift a group of nodes around in a way that changes the structure of the Tree, but not the order of the nodes. 
    Remember that we still have a BST, so we need to keep our elements in strict order. 

**In Case 4**, the Red node and its Red parent are **not**on the same side of their parents
    Our node (16r) is a right child, and its parent (13r) is a left child.
    Here, we'll perform a Left Rotation, since the nodes shift one place to the Left while maintaining their order. 

```
    9b
   /  \
  6r  19b
      /
     16r
    /
   13r      
```
Result after left rotation

The above result after a left rotation is **Case 5**. Here, both the Red Node and its Red parent are on the same side of their parents.
    In the case for (16r) and (13r), they're both left children.
    Now, we'll do a Right Rotation, but this time we involve the grandparent and both of its children. We'll need to swap the colors of the nodes as well. 

```
    9b
   /  \
  6r  16b
      /  \
     13r  19r
```    
Result after right rotation

We have now rearranged the nodes without changing the # of Black nodes in any path. 

These are all of the cases that could arise in Insertion. We just needed to do some rearranging to keep the rules for Red-Black Trees and BSTs satisfied. 
    In doing the rotations, we kept any one subtree from getting much larger than the others. 

Insertion, like search and delete, is O(log(n)) in the average and worst cases. 