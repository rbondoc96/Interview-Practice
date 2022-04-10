# Queues - The FIFO Structure


## Time Complexity
- enqueue(): O(1)
- dequeue(): O(1)


The best analogy is a line of people looking to get pancakes! The first person in line gets pancakes first.
- "Head" is the 1st element
- "Tail" is the last element


## Implementation
A Queue, like a Stack, can be implemented using a Linked List. Except this time, a new variable, `tail`, is needed to track the end of the structure.
- The `tail` is needed so that both the front and back are accessed in constant time.


## Insertion and Deletion

**Insertion** - the enqueue() function
Elements are inserted at the back of the line/tail.

**Deletion** -- the dequeue() function
Elements are deleted at the front of the line/head.


## Accessing Elements
For a Queue, there is a peek() function to simply return the element at the head of the Queue without removing it.


## Some Special, Common Types of Queues

### Deque - "Double Ended" Queue
A dequeue (pronounded 'deck') is a Queue that goes both ways. You can enqueue() or dequeue() from both ends.

It's kind of a generalized version of both Stacks and Queues. You could represent either a Stack or a Queue with a Dequeue.


### Priority Queue
Each element in the Queue is given a numerical priority when it is inserted into the Queue. On dequeue(), the element with the HIGHEST priority is removed first.
- If elements have the same priority, the oldest element is the one that is dequeued first.