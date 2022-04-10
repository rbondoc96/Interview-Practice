# String Keys

The real beauty of hashing is that it can be used with string keys as well. 

You just need to come up with a hash function that converts letters into numbers. 
- Individual letters can easily be converted into ASCII values. Many languages have built in functions that do that.

We can combine the ASCII values with a formulat to get a unique hash for each letter. 

But, what should our hash function look like?
- Do we want every word in its own bucket?
- Okay with some collisions and a simple hash function? 

If you have 30 or less words, you could probably just use the ASCII value for the first letter of a string as a hash value.
- In Java, the standard hash code function for string keys favor a large hashtable over having any collisions. The formula looks something like: 

<span>$s[0]*31^{n-1} + s[1]*31^{n-2} + ... + s[n-1]*31^{0}$</span>

Why does it work though?

By multipying the ASCII value for each letter by a power of some number, like 31, we can guarantee that every number representation/hash value would be unique for that string. 
- However, strings with just 3 or 4 letters already have huge hash values. 
    - Example: "HASH" = 72 + 65 + 83 + 72 --> 2210062 (using the equation in Java)

The tradeoff is really important here. As long as you have the space for it, a unique hash value can be really useful. 

Another thing, why is 31 chosen? The earliest hash functions took advantage of some properties of the number 31. Research showed that 31 was good for this kind of string hashing.
- However, there's now more complex hash functions, so 31 is more of a convention than the best possible value. 