(breadth-first-serach: pesquisa em largura)

- **Breadth-first search** tells you if there’s a path from A to B.
- If there’s a path, breadth-first search will find the **shortest path**.
- If you have a problem like **“find the shortest X,”** try modeling your problem as a **graph**, and use **breadth-first search** to solve it.
- A **directed graph** has arrows, and the relationship follows the direction of the arrow (e.g., `rama -> adit` means “Rama owes Adit money”).
- **Undirected graphs** don’t have arrows, and the relationship goes both ways (e.g., `ross - rachel` means “Ross dated Rachel and Rachel dated Ross”).
- **Queues** are **FIFO** (First In, First Out).
- **Stacks** are **LIFO** (Last In, First Out).
- You need to check people in the **order they were added** to the search list, so the search list needs to be a **queue**. Otherwise, you won’t get the shortest path.
- Once you check someone, make sure you **don’t check them again**. Otherwise, you might end up in an **infinite loop**.
