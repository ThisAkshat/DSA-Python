# Topic 34: Trees

## 1. What It Does

* A **Tree** is a hierarchical data structure made of nodes connected by edges.
* The top node is called the **Root**.
* Nodes below another node are its **Children**; a node with no children is a **Leaf**.
* Trees are used when data has a parent-child relationship.

## 2. Diagram 🌿

```text
             A          ← Root
           /   \
          B     C        ← Children of A
         / \     \
        D   E     F      ← Leaf nodes

A = Root
B, C = Children of A
D, E, F = Leaf nodes
```

**Common tree types:**

* **Binary Tree:** Each node has at most two children.
* **Binary Search Tree (BST):** Smaller values go left, larger values go right.
* **Balanced Tree:** Keeps its height controlled for efficient operations.

## 3. Unique Point 💡

Trees have no cycles, and each child node has only one parent (except the root, which has none).

Tree traversal methods include:

* **Preorder:** Root → Left → Right
* **Inorder:** Left → Root → Right
* **Postorder:** Left → Right → Root
* **Level Order:** Visit nodes level by level.

In a BST, inorder traversal visits values in sorted order.

## 4. Main Purpose 🎯

Trees help us:

* **Organise hierarchical data:** Parent-child relationships.
* **Search efficiently:** Balanced search trees can search in `O(log n)` time.
* **Sort data:** BST inorder traversal produces sorted values.
* **Represent decisions:** Decision trees help evaluate different choices.

## 5. Real-World Apps 🌍

**1. File Explorer:** Folders contain subfolders and files in a tree structure.

**2. HTML / Web Browsers:** HTML documents are represented as a DOM tree, where elements contain child elements.

**3. Database Indexing:** B-trees and B+ trees help databases find records efficiently.

---
