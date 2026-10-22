# Topic 35: Binary Search Tree (BST)

## 1. What It Does

* A **Binary Search Tree (BST)** is a special type of tree used to store and search data efficiently.
* Each node can have a maximum of **two children**: left and right.
* **Left subtree:** Contains values smaller than the node.
* **Right subtree:** Contains values larger than the node.
* This ordering makes searching, inserting, and deleting values easier.

## 2. Diagram

Insert these values: `50, 30, 70, 20, 40, 60, 80`

```text
              50
            /    \
          30      70
         /  \    /  \
        20  40  60   80

       LEFT       RIGHT
     Smaller      Larger
```

**Example: Search for 60**

```text
60 > 50  → Go RIGHT
60 < 70  → Go LEFT
60 = 60  → FOUND!
```

BST search takes **O(log n)** on average when the tree is reasonably balanced, but **O(n)** in the worst case when it becomes skewed.

## 3. Unique Point 💡

* Inorder traversal visits BST values in **ascending order**.
* A BST is not automatically balanced; inserting sorted values can turn it into a chain.
* AVL trees and Red-Black trees help maintain balance.

## 4. Main Purpose 🎯

* **Searching:** Find a value using the ordering of nodes.
* **Insertion:** Place a new value in the correct position.
* **Deletion:** Remove a value while maintaining BST rules.
* **Sorted output:** Retrieve values in ascending order through inorder traversal.

## 5. Real-World Apps 🌍

**1. Database Systems:** Tree-based indexes help search and retrieve records efficiently. Databases commonly use B-trees or B+ trees rather than ordinary BSTs.

**2. Dictionary Applications:** Ordered search trees can help store words and retrieve them efficiently.

**3. File and Data Management Tools:** Ordered trees can organise searchable data and support operations such as finding the smallest or largest value.

---
