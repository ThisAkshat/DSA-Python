# 10) Hashing / Hash Table

### 1) What it does

A hash table stores data as **key-value pairs** or uses keys to locate values quickly.
It uses a hash function to convert a key into a hash value that helps determine where the data is stored.
When you search for a key, hashing helps you find its value without checking every element.
Collisions can happen when different keys map to the same location, so the hash table must handle them.

### 2) Diagram

```text
       KEY
        |
        v
  Hash Function
        |
        v
   Hash Value
        |
        v
  Hash Table
  ┌─────┬─────────┐
  │  0  │   --    │
  │  1  │  Apple  │
  │  2  │   --    │
  │  3  │  Mango  │
  │  4  │   --    │
  └─────┴─────────┘
```

### 3) Unique Python line

Python's `dict` and `set` use hashing. A useful detail is that **a dictionary key must be hashable**; for example, a tuple of hashable values can be a key, but a list cannot.

```python
data = {(1, 2): "hello"}  # Valid
# data[[1, 2]] = "hello"  # TypeError
```

### 4) Why we use it / Main purpose

The main purpose is **fast searching, insertion, and deletion**.
These operations take **O(1) average time**, though worst-case performance can be O(n).
Hashing is useful for counting frequencies, removing duplicates, and checking whether an element exists.
It is the foundation of Python's `dict` and `set`, which appear frequently in DSA interview problems.
