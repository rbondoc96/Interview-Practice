from collections import deque

"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)


def deque_test():
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")   # Enqueue
    queue.append("Graham")

    assert queue.popleft() == "Eric"    # Dequeue
    assert queue.popleft() == "John"
    assert queue == deque(["Michael", "Terry", "Graham"])

    print("All deque tests passed.")
    

def test():
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    # Should be 1
    assert q.peek() == 1

    # Test dequeue
    # Should be 1
    assert q.dequeue() == 1

    # Test enqueue
    q.enqueue(4)
    # Should be 2
    assert q.dequeue() == 2
    # Should be 3
    assert q.dequeue() == 3
    # Should be 4
    assert q.dequeue() == 4
    q.enqueue(5)
    # Should be 5
    assert q.dequeue() == 5

    print("All tests passed.")


if __name__ == "__main__":
    test()
    deque_test()