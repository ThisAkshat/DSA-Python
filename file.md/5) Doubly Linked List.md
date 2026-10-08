# 5) Doubly Linked List

### 1) What it does

A doubly linked list is a linked list where each node has **two links**:

* One points to the **next** node.
* One points to the **previous** node.

This allows us to move through the list in **both directions**.

### 2) Diagram

```text
        next             next
[None ← 10 ↔ 20 ↔ 30 → None]
        prev             prev
   ↑
  HEAD
```

Each node:

```text
[ Previous | Data | Next ]
```

### 3) Unique Python line

Python has no built-in doubly linked list, but you can create one using two references:

```python
node.prev = previous_node
node.next = next_node
```

This makes deletion easier because the node already knows **both neighbours**.

### 4) Why we use it / Main purpose

The main purpose is **fast movement and insertion/deletion in both directions**.
You can move from `10 → 20 → 30` or `30 → 20 → 10`.
Deletion is efficient when you already have the node reference.
It is commonly used in things like **browser history, undo/redo systems, and LRU Cache**.
