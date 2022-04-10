# Hash Maps

Hash maps are one of the main places where hash functions show up.


Before, a hash function was being used to find a place in an Array to store a key.

```
key = ...
hash = hash_function(key)

array[hash] = key
```

But Maps are made up of key:value pairs. For a HashMap, you can use the keys as inputs to a hash function, then store the key value pair in the bucket of the hash value producted by the function.

```
elem = (key, value)
hash = hash_function(key)

array[hash] = (key, value)
```

We know that each key in the Map is unique since they belong to a Set. Therefore, we could use a hash function to give them each their own unique buckets.

The hash function could also be designed to allow for collisions

In an interview, you'll often be asked to create a hash table to show that you understand hashing. Also that you know the upsides and downsides of designing a hash function.


HashMaps are very useful to integrate into algorithms, since they make code run much faster. Always think if you can use these first. 