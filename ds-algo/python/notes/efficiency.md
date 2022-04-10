# Lesson 1 - Introduction and Efficiency

## Algorithm Effiency

Efficiency or Complexity: How well are you using your computer's resources to get a particular job done?
- Time complexity: How long does the code take to run?
- Space complexity: How much storage space do you need?

### Big O Notation
O(n) - where 'n' is the length of input to the algorithm/function

O(1) or O(0n + 1) - Constant time

```
function decode(input):
    create out_str
    for char in input:
        get new_letter from letter's location in cipher
        add new_letter to out_str
    return out_str
```
**Time Complexity** = O(2n + 2)

For the pseudocode above, we put together the Big O by looking at the # of lines of code and amount of repetitions.
- `create out_str` and `return out_str` run just twice for the duration of the entire function. 
    - That puts complexity at O(2).
- The `for` loop has 2 lines of code and runs for the entire length of the input, which is 'n'.
    - Added to O(2), we get O(2n + 2).
    - 2n because the 2 lines of code run 'n' times.

**BUT! A line may be more complex than others...**
For the line below:
`get new_letter from letter's location in cipher`
- This line could take a different # of computations based on the cipher's data structure.


### Approximations
Since the amount of computations can vary, we can approximate the exact Big O notation based on the highest order of n.
- O(2n + 2), O(3n + 2), O(29n + 2) can be approxmated by O(n)
- O(n^2 + n + 2) can be approximated by O(n^2)

In terms of efficiency, it is typically looked at in the Worst Case. It can also be looked at in the Best Case and in the Average Case.

**For example, if we are looking for some letter in the English alphabet (26 letters)**
- Finding letter 'A' (1st letter) gives us the best case
- Finding letter 'M' (13th letter) gives us the average case
- Finding letter 'Z' (26th letter) gives us the worst case

<b><span style="color:red">In an interview, you must specify if you are talking about best case, average case, worst case.</span></b>


### Space Efficiency
Big O can also be used for space efficiency.

**For example, if you needed to copy the input string in your code 3 times, Big O would be something like O(3n)**


### Effiency Practice
```python
"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

"""
manatees = list of manatee dictionaries
manatee:dict = {
    name,
    age,
    ...,
}
n = len(manatees)
m = len( manatee.keys() )
"""

# O(N)
def example1(manatees):
    for manatee in manatees:
        # Accessing is O(1)
        print manatee['name']

# O(2) --> O(1)
def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']

# O(N*M)
def example3(manatees):
    # O(N)
    for manatee in manatees:
        # O(M)
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

# O(3N^2 + 2) = O(N^2)
def example4(manatees):
    # Space: O(1)
    oldest_manatee = "No manatees here!"

    # O(N*3N)
    for manatee1 in manatees:
        # O(3N)
        for manatee2 in manatees:
            # O(1)
            if manatee1['age'] < manatee2['age']:
                # O(1)
                oldest_manatee = manatee2['name']
            else:
                # O(1)
                oldest_manatee = manatee1['name']
    
    # O(1)
    print oldest_manatee
```