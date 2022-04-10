import unittest

"""
Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 

Assume len(str) >= 2
str[0] and str[1] are uppercase letters
- 65 <= ord() <= 90

Only a list can be used, not a Python dictionary.
Store a list at each bucket, not just the string itself.
- example: @ index 8565: ["Udacity"]
"""

class HashTable:
    
    def __init__(self):
        self.table = [None]*10000
        self.buckets = 10000
        self.length = 0
        self.load_factor = 0.0


    def __len__(self):
        return self.length


    def update_load_factor(self):
        self.load_factor = self.length * 1.0 / self.buckets


    def store(self, string):
        """Input a string that's stored in the table
        """
        index = self.calculate_hash_value(string)
        if index >= 0:
            if self.table[index] != None:
                self.table[index].append(string)
            else:
                self.table[index] = [string]

        self.length += 1
        self.update_load_factor()


    def lookup(self, string):
        """Return the hash value if the string is already in the table.
        Return -1 otherwise.
        """
        index = self.calculate_hash_value(string)

        if self.table[index] and string in self.table[index]:
            return index
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calculate a hash value from a string.
        """
        return ord(string[0]) * 100 + ord(string[1])


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hashtable = HashTable()


    def test_hash_func(self):
        word = "UDACITY"
        value = self.hashtable.calculate_hash_value(word)
        self.assertEqual(value, 8568)


    def test_lookup(self):
        word = "UDACITY"
        value = self.hashtable.lookup(word)
        self.assertEqual(value, -1)


    def test_store(self):
        word = "UDACITY"
        self.hashtable.store(word)
        value = self.hashtable.lookup(word)
        self.assertEqual(value, 8568)


    def test_store_edge_case(self):
        word = "UDACITY"
        self.hashtable.store(word)
        value = self.hashtable.lookup(word)
        self.assertEqual(value, 8568)

        word = "UDACIOUS"
        self.hashtable.store(word)
        value = self.hashtable.lookup(word)
        self.assertEqual(value, 8568)


if __name__ == "__main__":
    hashtable_test = TestHashTable()
    unittest.main()