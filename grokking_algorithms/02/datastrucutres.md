- array
  - store a fixed and contiguous blocks in the memory (elements stored side by side) 
  - better for random reading, because you can use the index to access any element of the array.
  - all elements must be of the same type (e.g., int, str, etc.), because each data structure type has a different size. With dynamic types, it's not possible to determine the size precisely.
- linked list
  - store elements randomly, each element has the memory address of the next element.
  - better for insertions and deletions, but bad for reading because you always start from the first element. 
  
Big O comparing table 

        
|           |Arrays   | Linked list  
|-----------|---------|-----------|
|READ       |O(1)     | O(n)      |
|INSERTION  |O(n)     | O(1)      |
|DELETION   |O(n)     | O(1)      |  

It’s worth mentioning that insertions and deletions are O(1)
time only if you can instantly access the element to be
deleted. It’s a common practice to keep track of the first
and last items in a linked list, so it would take only O(1)
time to delete those.

