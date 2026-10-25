# Topic 43: Union-Find (Disjoint Set Union — DSU)

## 1. What It Does

**Union-Find** is a data structure that helps determine whether two elements belong to the same group.

It supports two main operations:

* **Find:** Checks which group an element belongs to.
* **Union:** Combines two different groups into one group.

## 2. Diagram

Suppose we have 5 nodes, initially in separate groups:

**Starting state:**

```text
A    B    C    D    E
```

**After Union(A, B) and Union(B, C):**

```text
    A          D    E
    |
    B
    |
    C
```

A, B and C now belong to the same group.

**Find(A) and Find(C):** Same group — Yes.

**Find(A) and Find(D):** Same group — No.

*Note: The diagram shows group membership, not necessarily the exact internal tree structure used by the implementation.*

## 3. Unique Point

Union-Find is commonly optimized using two techniques:

* **Path Compression:** During `Find`, it makes nodes point more directly to the group's representative, speeding up future operations.
* **Union by Rank/Size:** When combining groups, it attaches the smaller or shallower tree under the larger or shallower one to keep the structure efficient.

With both optimizations, operations are extremely fast in practice.

## 4. Main Purpose

The main purpose of Union-Find is to **track connected groups efficiently**.

For example, imagine a graph with several nodes and edges. You want to check whether two nodes are already connected before adding another edge.

* If both nodes belong to the same group, adding an edge between them creates a cycle.
* If they belong to different groups, connecting them joins those groups without creating a cycle.

This is why Union-Find is useful in **Kruskal's Minimum Spanning Tree algorithm**.

## 5. Real-World Apps

**1. Network Connectivity**

A network system can track which computers belong to the same connected network. When connections are added, Union-Find can combine their groups.

**2. Kruskal's MST Algorithm**

Kruskal uses Union-Find to check whether an edge would create a cycle before selecting it.

**3. Image Processing**

Some image-processing algorithms use connected-component labeling to group neighboring pixels that share a particular property, such as a similar color.

---
