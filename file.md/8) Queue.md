# 8) Queue

### 1) What it does

A queue is a data structure that follows **FIFO (First In, First Out)**.
The first element added is the first element removed.
You add elements at the **rear** and remove them from the **front**.
Think of people standing in a line: the person who arrives first gets served first.

### 2) Diagram

```text
  REMOVE                          ADD
  (Front)                        (Rear)
     ↓                              ↓
   [10]  →  [20]  →  [30]  →  [40]
    First                         Last

  Remove → 10
```

### 3) Unique Python line

Python's `collections.deque` provides efficient insertion and removal at both ends. Using a list's `pop(0)` is slower because the remaining elements must shift.

```python
from collections import deque

q = deque([10, 20, 30])
q.append(40)     # Add to rear
q.popleft()      # Remove from front
```

Both `append()` and `popleft()` take **O(1)** time.

### 4) Why we use it / Main purpose

The main purpose is to process elements in the order they arrive.
Queues are used in task scheduling, request processing, and printer queues.
In DSA, queues are essential for **Breadth-First Search (BFS)** in trees and graphs.
