
- Dynamic programming is useful when you're trying to optimize something within a constraint.
- You can use dynamic programming when the problem can be divided into discrete subproblems.
- All dynamic programming solutions involve a table.
- The values in the cells are usually what you're trying to optimize.
- Each cell represents a subproblem, so think about how this subproblem can be broken down into smaller ones.
- There is no single formula for solving a dynamic programming problem.

## Knapsack DP 

Given a set of items, each with a weight and a value, determine which items to include in the collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

guitar: 1kg  -> 1500$
radio: 4kg   -> 3000$
laptop: 3kg -> 2000$
iphone: 1kg -> 2000$
mp3: 1kg     -> 1000$

|            | 1kg  | 2kg          | 3kg              | 4kg                            |
| ---------- | ---- | ------------ | ---------------- | ------------------------------ |
| guitar (g) | 1500 | 1500         | 1500             | 1500                           |
| radio (r)  | 1500 | 1500         | 1500             | 3000                           |
| laptop (l) | 1500 | 1500         | 2000             | 3500 (laptop 3kg + guitar 1kg) |
| iphone(i)  | 2000 | 3500 (g + i) | 3500 (g+ i)      | 4000 (i + l)                   |
| mp3 (m)    | 1500 | 3500 (g + i) | 4500 (g + i + m) | 4500 (g + i + m)               |
formula: 
![[Pasted image 20250713213630.png]]

We've already seen a dynamic programming problem so far. What were the characteristics that helped identify this type of problem?

- Dynamic programming is useful when you're trying to optimize within a constraint. In the knapsack problem, it was necessary to maximize the value of the stolen items, limited by the capacity of the knapsack.
- You can use dynamic programming when the problem can be broken down into discrete subproblems that do not depend on each other.

It can be difficult to find a solution using dynamic programming, and that's what this section will focus on. Some general tips are:

- Every dynamic programming solution involves a table.
- The values in the cells are usually what you're trying to optimize. For the knapsack problem, the values in the cells were the item values.
- Each cell is a subproblem, so think about how you can divide it into other subproblems, as that will help you discover what your axes are.

## refs
https://en.wikipedia.org/wiki/Knapsack_problem#Quantum_approximate_optimization
