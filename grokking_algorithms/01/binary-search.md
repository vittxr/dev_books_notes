- binary search only works for sorted array.
- IN THIS BOOK, log = log2

#### binary search operation times: 

log n elements

for a list of 8 elements, the max operation to find the target el is 3, because log 8 = 3 (2 ** 3 = 8):

if target 7:

```
[1, 2, 3, 4, 5, 6, 7, 8]
             |
[6, 7, 8]: 
    | 
```

found target with 2 executions, but if target was 8 it would be 3 that is the maximum execution possible.       

#### Big O 

linear alg: O(n)      
binary search: O(log n)