- Big O establishes a worst-case run **time**

- Common Big O notations: 
  - O(log n), also known as log time. Example: Binary
search.
  - O(n), also known as linear time. Example: Simple
search.
  - O(n * log n). Example: A fast sorting algorithm, like
quicksort (coming up in chapter 4).
  - O(n2). Example: A slow sorting algorithm, like selection
sort (coming up in chapter 2).
  - O(n!). Example: A really slow algorithm, like the
traveling salesperson (caixeiro-viajante)

- Main takeaways: 
  - Algorithm speed isn’t measured in seconds, but in
growth of the number of operations.
  - Instead of seconds, we talk about how quickly the run
time of an algorithm increases as the size of the input
increases.
  - Run time of algorithms is expressed in Big O notation.
  - O(log n) is faster than O(n), but it gets a lot faster as
the list of items you’re searching grows.