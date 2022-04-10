

class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)



class LinkedList:
    def __init__(self, node=None):
        self.head = node 
        self.tail = node  
        self.length = 1 if node else 0


    def __str__(self):
        chars = []
        current = self.head
        while current:
            chars.append(str(current.value))
            current = current.next

        return "[" + ", ".join(chars) + "]"


    def __len__(self):
        return self.length

    
    def append(self, node):
        """Adds an item to the end of the list."""

        if not self.head:
            self.head = self.tail = node
        elif not self.head.next:
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1
        

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        current = self.head
        cursor = 0
        while current and position >= 0 and cursor <= position:
            if cursor == position:
                return current

            current = current.next
            cursor += 1

        return None
    

    def insert(self, node, position):
        """Insert a new node at the given position.
        Assume the first position is "0".
        Inserting at position 2 means between
        the 2nd and 3rd elements."""

        if position == 0:
            node.next = self.head
            self.head = node
        elif position == len(self) - 1:
            self.tail.next = node
            self.tail = node
        elif position > 0:
            current = self.head
            previous = None
            cursor = 0

            while current and cursor <= position:
                
                if cursor == position:
                    node.next = current
                    previous.next = node
                    break
                # If position is higher than len()-1, append 
                elif current == self.tail:
                    current.next = node
                    self.tail = node
                    break
                
                previous = current
                current = current.next
                cursor += 1

        self.length += 1
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    self.tail = previous
                    self.tail.next = None
                else:
                    previous.next = current.next

                self.length -= 1
                break

            previous = current
            current = current.next



def test():
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    assert len(ll) == 3

    # Test get_position
    assert ll.head.next.next.value == e3.value
    assert ll.get_position(2).value == e3.value

    # Test insert
    ll.insert(e4, 3)
    assert ll.get_position(3).value == e4.value
    assert len(ll) == 4

    ll.insert(Element(11), 1)
    assert ll.get_position(1).value == 11
    assert len(ll) == 5

    # Add past the end of the list
    pos = 33
    ll.insert(Element(24), 33)
    assert len(ll) == 6
    assert ll.get_position(33) == None
    assert ll.get_position(len(ll) - 1).value == 24
    print(ll)

    # Test delete
    ll.delete(1)
    ll.delete(11)
    print(ll)
    assert ll.get_position(0).value == e2.value
    assert ll.get_position(2).value == e4.value
    assert ll.get_position(3).value == 24
    assert len(ll) == 4

    ll.delete(24)
    print("New tail", ll.tail)
    print(ll)

    e5 = Element(5)
    ll.append(e5)
    print(ll)
    assert ll.get_position(len(ll) - 1).value == e5.value

    ll.insert(Element(122), 1)
    print(ll)
    ll.insert(Element(122), 0)
    print(ll)
    ll.insert(Element(123), 100)
    print(ll)    

    ll.delete(123)
    print(ll)

    print("All tests passed.")


if __name__ == "__main__":
    test()