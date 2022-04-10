# Recursive Algorithms

A recursive function is a function that calls itself.
```pseudocode
function recursive(input):
    if input <= 0
        return input
    else
        output = recursive(input - 1)
        return output
```
It's a very simple example, but it shows the main parts of a recursive function:
1. The function must call itself at some point.
2. The function needs a base case.
    - This is similar to an exit condition for a `while` loop.
    - Without a proper base case, you can get infinite recursion.
3. The function needs to alter the input parameter at some point.
    - Without giving a condition for changing every time the function iterates, the function will never know where to stop.

Here's an example using the first pseudocode function
```
recursive(2) --> {
    output = recursive(1) --> {
        output = recursive(0) --> return 0
        --> output = 0
        return 0
    }
    --> output = 0
    return 0
}
```
We can see that `recursive(input)` will return 0 for all positive inputs and the same input for all negative inputs.

<span style="color:red">When writing a recursive function, remember to think about all the different input values the statement could have.</span>


## Example: Fibonacci Sequence

The most popular example of recursion is the Fibonacci sequence.
`seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...]`

The first 2 values are 0 and 1. The following numbers are the sum of the previous 2 numbers. Below is the Fibonacci sequence in Python:
```python
def fib(position):
    if position < 0:
        return -1
    if position == 0 or position == 1:
        return position
    return fib(position - 1) + fib(position - 2)
```
Notice that the solution computes the values for some inputs more than once. For example, `fib(3)` calls `fib(2)` and `fib(1)`, and `fib(2)` calls `fib(1)` and `fib(0)`. <span style="color: red">The number of recursive calls grows exponentially with `n`.</span>

In practice, if recursion is used to solve the Fibonacci sequence, we should use a Hashtable to store and fetch previously calculated results. This will increase the space needed, but will drastically improve the runtime efficiency.