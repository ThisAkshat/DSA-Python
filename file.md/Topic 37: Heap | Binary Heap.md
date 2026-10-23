# Topic 37: Heap / Binary Heap 🌳

## 1. What It Does

* A **Heap** is a tree-based data structure used to quickly access the highest- or lowest-priority element.
* **Max Heap:** The parent is greater than or equal to its children.
* **Min Heap:** The parent is smaller than or equal to its children.
* A Binary Heap is a **Complete Binary Tree**, meaning its levels are filled from left to right, except possibly the last level.
* Unlike a BST, a heap does not keep all values sorted.

## 2. Diagram 📊

**Max Heap: Largest value stays at the top.**

```text
             90
           /    \
         70      80
        /  \    /  \
       20  40  50  60

        Parent ≥ Children
```

**Min Heap: Smallest value stays at the top.**

```text
             10
           /    \
         20      15
        /  \    /  \
       40  30  50  60

        Parent ≤ Children
```

For example, in a Max Heap, the largest value (`90`) is available immediately at the root.

## 3. Unique Point 💡

* A heap is commonly stored in an **array**, without requiring separate node objects.
* For a zero-indexed array, the children of index `i` are at `2i + 1` and `2i + 2`.
* Getting the root takes `O(1)` time; insertion and removing the root take `O(log n)` time.

## 4. Main Purpose 🎯

Heaps are mainly used when we repeatedly need the **smallest or largest element**.

* **Priority Queue:** Process the highest-priority task first.
* **Top K Elements:** Find the largest or smallest `K` values.
* **Scheduling:** Select the next task based on priority.
* **Heap Sort:** Sort elements in `O(n log n)` time.

## 5. Real-World Apps 🌍

**1. Operating Systems:** Priority queues can help schedule tasks according to their priority.

**2. Online Shopping:** A product system can use a heap to retrieve the top-rated or cheapest `K` products efficiently.

**3. Navigation Systems:** Priority queues using heaps help algorithms such as Dijkstra's algorithm select the next closest node.

---
