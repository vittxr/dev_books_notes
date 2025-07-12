# Summary 

- **Greedy algorithms** optimize locally in the hope of reaching a global optimization.
- **NP-complete problems** do not have a fast solution.
- If you're trying to solve an NP-complete problem, the best thing to do is to use an **approximation algorithm**.
- Greedy algorithms are easy to write and have low execution time, so they make good approximation algorithms.

# How identify NP-complete problems

Here is the English translation:

- Your algorithm runs fast for a few items, but becomes very slow as the number of items increases.
- “All combinations of X” usually means an **NP-complete** problem.
- Do you have to calculate “every possible version” of X because you can’t break it into smaller subproblems? It might be an **NP-complete** problem.
- If your problem involves a **sequence** (like a sequence of cities, as in the **traveling salesman problem**) and is hard to solve, it could be **NP-complete**.
- If your problem involves a **set** (like a set of radio stations) and is hard to solve, it could be **NP-complete**.
- Can you rewrite your problem as the **set cover problem** or the **traveling salesman problem**? Then your problem is definitely **NP-complete**.

# How to solve it

You usually use a greedy algorithm (approximation algorithm). For example, in case of TSP (Traveling Salesman Problem) is select the nearest unvisited city at each step, although this does not always guarantee the optimal solution

