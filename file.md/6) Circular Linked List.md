# 6) Circular Linked List

### 1) What it does

A circular linked list is a linked list where the **last node points back to the first node**.
There is no `None` at the end.
You can keep travelling through the nodes repeatedly.
It can be singly or doubly linked.
The most common version is a **singly circular linked list**.

### 2) Diagram

```text
       ┌──────────────────────────┐
       ↓                          │
HEAD → [10] → [20] → [30] → [40] ┘
```

Unlike a normal linked list:

```text
[10] → [20] → [30] → None
```

### 3) Unique Python line

In Python, you can create the circular connection simply by making the last node point to the head:

```python
last.next = head
```

The tricky part is traversal: **don't stop when `current` becomes `None`**, because it never will.

### 4) Why we use it / Main purpose

The main purpose is when data needs to be processed **repeatedly in a cycle**.
You can start at any node and eventually return to it.
A classic use case is **Round Robin scheduling**, where tasks get turns repeatedly.
It is also useful for cyclic playlists and turn-based systems.
