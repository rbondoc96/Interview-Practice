# Hashing

## Introduction
Utilizing a data structure that uses a hashing function allows one to do look-ups in constant, O(1) time.

With everything so far, look-ups would happen in linear O(n) time. In a list or a set, you need to look through every element to find the one you're looking for.

Stacks let you look up the newest element immediately, while queues let you look up the oldest element. Priority queues will let you find the highest priority element quickly. But, if we want to look for any other element, we have to do a linear time search.

The ability to do constant time look-ups will make almost any algorithm you write instantly faster.

The concept of Hashing shows up constantly in technical interviews. You can always optimize an answer, or improve an answer with it, or reduce a complex question to, just use a hash function.


## Hash Functions
The purpose of a Hash function is to transform some value into one that can be stored and retrieved easily.

```
def my_hash_function(value): -> some_hash_value
    ...
```

The function is given some value. It converts the value based on some formula, and spits out a coded version of the value that's often the index in an array.


An example would be scanning barcode tickets at a concert. You need to be able to scan the barcode and find ticket numbers fast when people check in.

Storing the ticket number using a hash function would work great. It would convert the ticket number into a hash value so they can be stored easily.
    One common pattern in hash functions is to take the last few digits of a big number, divide it by some consistent number, and using the remainder from that division, find a place to store that number in an array.

An example would be:

Ticket # 0123456 --> 56 / 10 = 5, remainder 6

We would store 0123456 into an array at index 6.

Why use the last few digits? Because the last few digits are most likely to be random.
    If you're assigning numbers in numerical order, the first few digits really wouldn't be random. They're more likely to start with a 1, 2, 3, than later numbers like 7, 8, or 9.


## Collisions
There are times when a hash function will spit out the same hash value for two different inputs. This situation is called a **collision**.

There are 2 ways to fix a collision:
1. Change the value in your hash function, or change the hash function completely so that there are more than enough slots to store all potential values.
2. Keep the same hash function, but change the structure of the Array.
    - Instead of a single value at each slot, you can store some type of lists that contains all values hashed at that spot. The lists would be called "buckets" in this context. 

However, both ways have their pitfalls.
1. For #1, you can maintain constant look-up time, but by using a bigger number in the hash function, you're going to need a lot more space to store your values.
    - If this the number is changed reactively whenever there is a collision, moving all the data into a new array is going to increase the complexity in terms of both size and time.
2. With the bucket approach in #1, you'll need to iterate through some collection (though a smaller one) every time you're looking for something.


In the average case, hash functions have a constant lookup time. But because of the bucket system, every value could be stored in a single bucket and then you're essentially just iterating through a list. In the worst case, lookup time is O(n).


When done well, hashing is really fast and can save a ton of time, but all of these things are real concerns. There is no one perfect way to build a hash function.

Often, you'll have to choose between making a hash function that either:
1. Spreads out values nicely but uses a lot of space
2. One that uses less buckets, but might have to do some searching within each bucket.
    - Ideally, there are 1-3 elements in each bucket.


Another approach would be to use a 2nd hash function on the hash value output by the 1st hash function to split up the elements even more. 
- This works well if you know you're going to have well spaced out elements, but end up having a few really large buckets.


Hashing questions are popular because there's often not a perfect solution. You're expected to talk about the upsides and the downsides of whatever approach you choose. 
    Just do your best to optimize your hash function and make sure you're communicating with your interviewer well.


## Load Factor
A "load factor" is often discussed when talking about hash tables.

The load factor is a ratio of the # of entries vs the # of buckets:

<span>$\frac{NumEntries}{NumBuckets}$</span>

The purpose of the load factor is to give a sense of how "full" a hashtable is. 

For example, if we're trying to store 10 values in a hashtable with 1000 buckets,

<span>$LoadFactor = \frac{10}{1000} = 0.01$</span>

and the majority of the buckets in the table will be empty. We end up wasting memroy by having so many empty buckets, so we may want to rehash, or come up with a new hash function with less buckets.

We can use load factor as an indicator for when to rehash--as the load factor approaches 0, the more empty, or sparse, the hashtable is.

On the flip side, the closer load factor is to 1, it would be better to rehash and add more buckets. Any table with a load value greater than 1 is guaranteed to have collisions.


### Collisions and Load Factor
If turns out that collisions can be minimised in some common cases because math.

If the constant used in the hash for modulus and the # of buckets are coprime (meaning the only positive divisor for both numbers is 1), collisions are minimised.

This [link](https://stackoverflow.com/questions/1145217/why-should-hash-functions-use-a-prime-number-modulus) was useful


## Example Question
One of your coworkers comes to you with a hash function that divides a group of values by 100 and uses the remainder as a key:

<span>$key = value \% 100$</span>

The values are 100 numbers that are all multiples of 5. What is the load factor?

100 numbers that are multiples of 5

NumEntries = 100

0 % 100 = 0
1 % 100 = 1
...
99 % 100 = 99 --> 100 buckets

<span>$LoadFactor = \frac{100}{100} = 1$</span>


