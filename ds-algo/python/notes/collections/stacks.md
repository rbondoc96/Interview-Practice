# Stacks - The LIFO Structure

**LIFO**: Last In, First Out

## Time Complexities
- push(): O(1)
- pop(): O(1)


Also a List-based structure, Stacks are a bit different than Arrays and Linked Lists. A Stack is like an actual stack of things in real life.
- You have easy access to add to, remove from, or look at the top element in the stack.
- Even though the last pancake at the bottom might have the most chocolate, you can't get to it easily. You have to make your way through the stack.
- The earliest thing put in the stack is at the bottom!

# When to Use Them
1. When you only care about the most recent elements
2. When the order in which you see and save elements actually matters

**Social Media Example**: A list of comments on a News Feed. You typically will need to see the most recent one quickly and more frequently, but you have to scroll down to see the older comments.


## Insertion and Deletion
Think of it like a stack of plates in a spring-loaded dispenser at a buffet.

**Insertion** - push() function
Stacks receive elements at the top of their list. They "push" older elements down the structure as more elements are added.

**Deletion** - pop() function
Stacks remove elments from the top of their list. As items are removed, the older items rise up and "pop" the top element off the stack.

Since both of these actions just involve the top of the stack, their time complexities are O(1).


## Implementation
A Stack is pretty abstract. It can be implemented using other data structures, like a Linked List. 
- How the elements are connected doesn't matter
- Only the methods for push() and pop() are specified.

One implementation would be a Linked List. Just add elements to the beginning.