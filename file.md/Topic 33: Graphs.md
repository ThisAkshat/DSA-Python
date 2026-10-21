# Topic 33: Graphs 🕸️

## 1. What It Does

* A **Graph** is a data structure made of **Nodes (Vertices)** and **Edges**.
* Nodes represent objects, and edges represent connections between them.
* Graphs can be directed (one-way) or undirected (two-way).
* Edges can also have weights, such as distance, time, or cost.

## 2. Diagram

Imagine a social network:

```text
       Akshat
       /    \
      /      \
   Rahul ─── Priya
      |
      |
     Aman
```

* **Nodes:** Akshat, Rahul, Priya, Aman.
* **Edges:** Represent friendships.
* Akshat is connected to Rahul and Priya.
* Rahul is connected to Aman.

**Types of graphs:**

```text
Undirected:  A ─── B

Directed:    A ───→ B

Weighted:    A ──5── B
```

## 3. Unique Point 💡

Graphs can represent complex relationships that arrays and linked lists cannot naturally express.

Two important graph traversal algorithms are:

* **BFS (Breadth-First Search):** Explores nearby nodes first, level by level.
* **DFS (Depth-First Search):** Explores one path deeply before exploring another.

## 4. Main Purpose 🎯

Graphs are used to:

* **Find paths:** Discover routes between locations.
* **Represent relationships:** Connect people, devices, or web pages.
* **Detect connections:** Check whether two nodes are connected.
* **Optimise routes:** Find paths based on distance, time, or cost.

## 5. Real-World Apps 🌍

**1. Instagram:** Represents users and their follow relationships as a graph.

**2. Google Maps:** Represents locations as nodes and roads as edges to calculate routes.

**3. LinkedIn:** Represents professionals as nodes and their professional connections as edges.

---

