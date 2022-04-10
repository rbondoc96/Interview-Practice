import unittest


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def __str__(self):
        return f"Node {self.value}"



class BST:

    def __init__(self, root_val):
        self.root = Node(root_val)


    def insert(self, new_val):
        self._insert(self.root, new_val)


    def _insert(self, start, new_val):
        if start:
            if start.value > new_val:
                if start.left:
                    self._insert(start.left, new_val)
                else:
                    start.left = Node(new_val)
            elif start.value < new_val:
                if start.right:
                    self.insert(start.right, new_val)
                else:
                    start.right = Node(new_val)


    def search(self, find_val):
        return self._search(self.root, find_val)


    def _search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif find_val < start.value:
                return self._search(start.left, find_val)
            else:
                return self._search(start.right, find_val)
        return False


    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root)    

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


class BSTTest(unittest.TestCase):

    def setUp(self):
        self.tree = BST(4)

        # Insert elements
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(3)
        self.tree.insert(5)

        print(self.tree.print_tree())

    def test_value_exists(self):
        self.assertTrue(self.tree.search(4))

    def test_value_not_exists(self):
        self.assertFalse(self.tree.search(6))


if __name__ == "__main__":
    test = BSTTest()
    unittest.main()