# Topic 36: AVL Tree

## 1. What It Does

* An **AVL Tree** is a self-balancing Binary Search Tree (BST).
* It follows the BST rule: smaller values go left, larger values go right.
* Whenever insertion or deletion makes the tree unbalanced, it performs rotations to restore balance.
* This prevents the tree from becoming a long chain and keeps searching efficient.

## 2. Diagram

**Example: Insert `10, 20, 30`**

A normal BST becomes unbalanced:

```text
    10
      \
       20
         \
          30
```

The AVL Tree performs a rotation:

```text
       20
      /  \
    10    30
```

Now the tree is balanced! ✅

**Four AVL rotations:**

* **LL:** Right rotation
* **RR:** Left rotation
* **LR:** Left rotation, then right rotation
* **RL:** Right rotation, then left rotation

## 3. Unique Point 💡

* AVL trees use a **Balance Factor** to measure the height difference between the left and right subtrees.
* For every node, the balance factor must be `-1`, `0`, or `+1`.
* Searching, insertion, and deletion take **O(log n)** time because the tree maintains its balance.

## 4. Main Purpose 🎯

* **Fast searching:** Prevents the tree from becoming skewed.
* **Efficient insertion and deletion:** Restores balance using rotations.
* **Ordered data:** Maintains BST ordering.
* **Predictable performance:** Guarantees logarithmic time for basic operations.

## 5. Real-World Apps 🌍

**1. Database Systems:** Balanced search trees can maintain ordered indexes, although databases commonly use B-trees or B+ trees.

**2. In-Memory Applications:** AVL trees can maintain sorted records while supporting fast searching and insertion.

**3. Scheduling Systems:** They can manage tasks ordered by time or priority when efficient search and updates are needed.

---
