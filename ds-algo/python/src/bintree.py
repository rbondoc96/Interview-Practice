import unittest

class Node:
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def __str__(self):
        return f"Node: {self.value}"


class BinaryTree:

    def __init__(self, root_val):
        self.root = Node(root_val)


    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)


    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root)


    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""

        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

        return False


    def preorder_print(self, start, traversal=None):
        """Helper method - use this to create a 
        recursive print solution."""

        if start:
            if traversal:
                traversal += f"-{start.value}"
            else:
                traversal = str(start.value)

            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        
        return traversal



class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree(1)
        self.tree.root.left = Node(2)
        self.tree.root.right = Node(3)
        self.tree.root.left.left = Node(4)
        self.tree.root.left.right = Node(5)

    def test_value_exists(self):
        self.assertTrue(self.tree.search(4))

    def test_value_not_exists(self):
        self.assertFalse(self.tree.search(6))

    def test_print_output(self):
        output = self.tree.print_tree()
        self.assertEqual("1-2-4-5-3", output)        



if __name__ == "__main__":
    test1 = BinaryTreeTest()
    unittest.main()