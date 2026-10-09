# 7) Stack

### 1) What it does

A stack is a data structure that follows **LIFO (Last In, First Out)**.
The last element you add is the first element you remove.
You add elements using `push` and remove them using `pop`.
You can access the top element without removing it.
Think of a stack of plates: you put a plate on top and take the top plate first.

### 2) Diagram

```text
        TOP
         ↓
      ┌──────┐
      │  30  │ ← Last added, first removed
      ├──────┤
      │  20  │
      ├──────┤
      │  10  │ ← First added
      └──────┘

       POP → 30
```

### 3) Unique Python line

Python lists can work as stacks using `append()` and `pop()`. Both operations at the end are **O(1) amortized**.

```python
stack = [10, 20, 30]
stack.append(40)  # Push 40
stack.pop()       # Removes 40
```

### 4) Why we use it / Main purpose

The main purpose is to manage data in **Last In, First Out order**.
It is used in undo/redo operations, browser navigation, and function calls.
In DSA, stacks are important for checking balanced parentheses, reversing data, and solving next-greater-element problems.
