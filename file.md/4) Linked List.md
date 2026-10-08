# 4) Linked List

### 1) What it does

A linked list stores data in separate **nodes**.
Each node contains the **data** and a link to the next node.
Unlike an array, elements don't need to be stored next to each other in memory.
You move through the list by following these links.
The first node is called the **head**.

### 2) Diagram

```text
HEAD
 ↓
[10 | ●] → [20 | ●] → [30 | ●] → [40 | None]
```

Each node:

```text
[ Data | Next ]
```

### 3) Unique Python line

Python does **not have a built-in Linked List** like Java's `LinkedList`. You normally create one using your own `Node` class.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### 4) Why we use it / Main purpose

The main purpose is **efficient insertion and deletion** when you already have the required node position.
Adding/removing a node can be **O(1)** when inserting at the beginning or after a known node.
However, finding a particular element takes **O(n)** because you must traverse the nodes.
It is mainly useful for understanding pointer/reference-based data structures and building structures like stacks and queues.
