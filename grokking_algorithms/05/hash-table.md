- You can make a hash table by combining a hash function with an array.
- Collisions are bad. You need a hash function that minimizes collisions.
- Hash tables have really fast search, insert, and delete. - O(1)
  - O(1) denotes constant time complexity: the execution time remains the same regardless of the size of the hash table (it isn’t necessarily instantaneous, but it does not grow with the hash table size).
- Hash tables are good for modeling relationships from one item to another item.
- Once your load factor is greater than 0.7, it’s time to resize your hash table. (load factor = n of items in hash table / total number of slots)
- Hash tables are used for caching data (for example,
with a web server).
- Hash tables are great for catching duplicates.