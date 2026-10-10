# 11) HashSet

### 1) What it does

A HashSet is a data structure that stores **unique elements only**.
If you try to add the same element again, it won't store a duplicate.
It uses hashing to check whether an element already exists.
Unlike a list, a HashSet does not guarantee a particular element order.
In Python, the built-in `set` provides similar functionality.

### 2) Diagram

```text
Input:  [10, 20, 10, 30, 20, 40]
                  |
                  ▼
             HashSet / set
                  |
                  ▼
          ┌────────────────┐
          │ 10  20  30  40 │
          └────────────────┘
            Unique values
```

### 3) Unique Python line

Python's `set` can compare membership efficiently using `in`, which takes **O(1) average time**.

```python
numbers = {10, 20, 30, 40}

print(20 in numbers)  # True
print(50 in numbers)  # False
```

**Important:** An empty set is created using `set()`, not `{}`, because `{}` creates an empty dictionary.

### 4) Why we use it / Main purpose

The main purpose is to **remove duplicates and check membership quickly**.
Adding, removing, and searching typically take O(1) average time.
It is useful for finding common elements between collections and checking whether a value has appeared before.
In DSA interviews, sets are commonly used to solve duplicate-detection and uniqueness problems.
