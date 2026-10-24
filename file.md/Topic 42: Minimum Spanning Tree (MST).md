# Topic 42: Minimum Spanning Tree (MST)

## 1. What It Does

A **Minimum Spanning Tree (MST)** connects all nodes in a weighted, undirected graph using the **minimum total edge weight**, without creating any cycles.

## 2. Diagram

Suppose we have this graph:

```text
       A
      / \
    2/   \4
    /     \
   B---1---C
    \     /
    5\   /3
      \ /
       D
```

One possible MST is:

```text
       A
      /
    2/
    /
   B---1---C
           \
           3\
             D
```

**Total weight = 2 + 1 + 3 = 6**

* All four nodes are connected.
* No cycle is formed.
* The MST uses exactly **V − 1 edges**, where V is the number of vertices.

## 3. Unique Point

There are two important algorithms for finding an MST:

* **Kruskal's Algorithm:** Sort edges by weight and select the smallest edge that does not create a cycle.
* **Prim's Algorithm:** Start from one node and repeatedly add the smallest edge connecting the current tree to a new node.

Both aim to find a minimum spanning tree, but they build it differently.

**Important:** MST minimizes the total weight needed to connect all nodes. It does not necessarily find the shortest path between every pair of nodes.

## 4. Main Purpose

The main purpose of MST is to **connect every location or node at the lowest possible total cost**.

For example, if a company needs to connect five offices using network cables, MST helps determine which connections to build while minimizing the total cable cost.

Remember:

* Every node must be connected.
* Cycles are not allowed.
* A connected graph with `V` vertices has `V − 1` edges in its MST.
* If multiple edges have equal weights, multiple valid MSTs may exist.

## 5. Real-World Apps

**1. Computer Networks**

Companies connect office computers using cables. MST helps minimize the total cable length while keeping every computer connected.

**2. Roads and Pipelines**

When planning roads between towns or pipelines between locations, MST helps minimize the total construction cost while connecting all locations.

**3. Clustering in Machine Learning**

MST can help identify groups of related data points by connecting nearby points and analyzing where the largest gaps occur.

---
