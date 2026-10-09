# 9) Deque (Double-Ended Queue)

### 1) What it does

A deque is a data structure that allows you to **add and remove elements from both ends**.
You can insert or delete elements from the front and rear.
Unlike a normal queue, which typically adds at the rear and removes from the front, a deque supports both directions.
In Python, we use `collections.deque` to implement it.

### 2) Diagram

```text
       FRONT                  REAR
         ↓                     ↓
       [10] ⇄ [20] ⇄ [30] ⇄ [40]

Add:     appendleft() | append()
Remove:  popleft()    | pop()
```

### 3) Unique Python line

Python's `deque` supports efficient operations at both ends, but **indexing in the middle is O(n)**.

```python
from collections import deque

d = deque([10, 20, 30])
d.appendleft(5)
d.append(40)
d.popleft()
d.pop()
```

### 4) Why we use it / Main purpose

The main purpose is to manage data efficiently from both ends.
Adding and removing elements at either end takes **O(1)** time.
It is useful for sliding-window problems, palindrome checking, and implementing queues.
In DSA interviews, `deque` is especially useful when elements must be added or removed from both ends.
