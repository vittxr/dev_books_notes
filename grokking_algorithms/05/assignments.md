It’s important for hash functions to have a good distribution. They should map items as broadly as possible. The worst case is a hash function that maps all items to the same slot in the hash table.

Suppose you have these four hash functions that work with strings:

1. **a.** Return “1” for all input.  

2. **b.** Use the length of the string as the index.  

3. **c.** Use the first character of the string as the index. So, all strings starting with *a* are hashed together, and so on.
  
4. **d.** Map every letter to a prime number:  
   - a = 2  
   - b = 3  
   - c = 5  
   - d = 7  
   - e = 11  
   - and so on.  

   For a string, the hash function is the sum of all the characters modulo the size of the hash. For example, if your hash size is 10, and the string is “bag”, the index is:


3 + 2 + 17 % 10 = 22 % 10 = 2


For each of these examples, which hash functions would provide a good distribution? Assume a hash table size of 10 slots.

1. **5.5** A phonebook where the keys are names and values are phone numbers. The names are as follows: Esther, Ben, Bob, and Dan.  

ans: c and d
   
2. **5.6** A mapping from battery size to power. The sizes are A, AA, AAA, and AAAA.  

ans: b and d
   
3. **5.7** A mapping from book titles to authors. The titles are Maus, Fun Home, and Watchmen.

ans: b, c and d