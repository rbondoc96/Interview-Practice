# Trees: Basics and Terminology

A Tree data structure starts from a place called a **root**. Data is added to it, called branches. 
    A big tree will fan out with lots of different branches in lots of different directions, just like a real tree.

Trees are basically an extension of a Linked List. 
- A Linked List has one head element at the front. Each element has a `next` pointer to another element.

A Tree has a `root` element, which is the first element in the collection. Instead of each node just having 1 next element, a Tree Node can have several.


A Linked List is usually drawn horizontally, but a Tree is normally drawn vertically.


## Properties of Trees
Each Tree must have the following properties:
1. Have a root element
2. Each node in the Tree has a pointer or reference to its children
3. Be completely connected.
    - That means, if you're starting from the root, there must be some way to reach every node in the tree.
4. No cycles in the tree.
    - A cycle occurs when there's a way for you to encounter the same node twice.
    - If the edges of a tree have arrows, ignore them. The edges still shouldn't form a cycle.


## Terminology
1. Level: The # of connections it takes to reach the root, plus 1.
    - Trees can be described in terms of levels
    - The root node is at Level 1, its children at Level 2 and its grandchildren at Level 3.
2. Tree Nodes are often described as having a **parent-child** relationship.
    - The node at the lower level is a parent, while the nodes connected to it at a higher level is a child.
    - A node in the middle can be both a parent and a child, depending on what it's being compared to. 
    - Though keep in mind, its not like a family tree, where children have 2 parents. Children are only allowed to have 1 parent. 
    - If a parent has multiple children, those children are considered siblings of each other.
3. Trees can be thought of in an ancestry-like way.
    - A node at a lower level can be called an ancestor of a node at a higher level, which is called a descendent.
4. Nodes at the end without any children are called **leaves**, or external nodes.
    - A parent node is called an internal node.
5. The lines connecting 2 nodes can be called **edges**.
4. A group of connections taken together is called a **path**.
5. Height of a Node is the # of edges between it and the *furthest* leaf on the tree.
    - A Leaf has a height of 0, but the parent of a leaf has a height of 1.
6. Height of the Tree is the Height of the root node
7. **Depth** of a Node is the # of edges to the *root*.
    - Height and Depth should be inversely
    - If a node is closert to a leaf, then it's ruther from the root


## Tree Traversal
Compared to List data structures, traversal was straightforward. The List was gone through, in order, to make sure that we looked at every element.

Trees aren't linear, so there's no clear way to traverse through everything.

We can't search or sort elements unless we have a way to make sure we can visit all elements first. 

**Depth First Search (DFS)**: The philosphy is that if there are children nodes to explore, exploring them is the priority.

**Breadth First Search (BFS)**: The priority is vising every node on the same Level we're currently on before visiting child nodes.


These traversal methods are somewhat vaguely defined since we can apply their principles but actually traverse the tree in several different ways. 

For a tree, a **level order traversal** is a BFS with a mre exact algorithm to implement.
1. Start at the root
2. then visit its children on the second level
3. Then all of their children on the third level
4. Repeat until you've visited every single leaf

By convention, we start from left -> right on each level

```
      D
    /   \
   B    E
 /  \    \
A    C    F
```
Result = D, B, E, A, C, F