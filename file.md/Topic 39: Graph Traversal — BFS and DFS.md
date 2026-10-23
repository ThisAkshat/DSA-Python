# Topic 39: Graph Traversal — BFS and DFS

## 1. What It Does

Graph Traversal means visiting nodes in a graph systematically.

There are two main methods:

* **BFS (Breadth-First Search):** Visits nearby nodes first, level by level. It uses a **Queue**.
* **DFS (Depth-First Search):** Explores one path as deeply as possible before backtracking. It uses a **Stack** or recursion.

Both methods use a visited set to avoid repeatedly visiting nodes in a cyclic graph.

## 2. Diagram

Suppose we have this graph:

```text
          A
         / \
        B   C
       / \   \
      D   E   F
```

**BFS traversal:**

```text
        A
      /   \
     B     C
    / \     \
   D   E     F

Order: A → B → C → D → E → F
```

BFS visits each level before moving to the next.

**DFS traversal:**

```text
A → B → D → E → C → F
```

DFS explores one branch deeply, then returns to explore other branches.

*Note: Traversal order can change depending on the order in which neighbours are visited.*

## 3. Unique Point

* **BFS:** Finds the shortest path in an unweighted graph, when a path exists.
* **DFS:** Useful for exploring connectivity, detecting cycles, and solving maze-like problems.
* Both typically take `O(V + E)` time using an adjacency-list representation, where `V` is the number of vertices and `E` is the number of edges.

## 4. Main Purpose

| Task                                          | Suitable Method                    |
| --------------------------------------------- | ---------------------------------- |
| Find the shortest path in an unweighted graph | BFS                                |
| Explore all reachable nodes                   | BFS or DFS                         |
| Detect cycles                                 | BFS or DFS, depending on the graph |
| Explore a maze or backtrack through paths     | DFS                                |
| Visit nodes level by level                    | BFS                                |

## 5. Real-World Apps

**1. Google Maps:** BFS can find shortest paths in unweighted road networks; real route planning commonly uses weighted-graph algorithms.

**2. Social Networks:** BFS can identify people within a certain number of connection levels.

**3. Web Crawlers:** BFS can visit web pages level by level by following links from a starting page.

---
