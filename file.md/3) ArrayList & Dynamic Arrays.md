# 3) ArrayList / Dynamic Arrays

### 1) What it does

A dynamic array is an array that can **grow or shrink when needed**.
Unlike a normal array, you don't need to decide its final size beforehand.
When it becomes full, it creates a larger storage area and moves the elements there.
In Java, `ArrayList` is the common implementation of a dynamic array.
In Python, `list` works like a dynamic array.

### 2) Diagram

```text
Initially:
[10] [20] [30]
 ↑
capacity = 3

Add 40 → not enough space

New storage:
[10] [20] [30] [40] [ ] [ ]

              ↑
        capacity increased
```

### 3) Unique Python line

Python's `list` automatically manages its internal capacity, so this works without manually resizing:

```python
arr = []
arr.append(10)
arr.append(20)
arr.append(30)
```

`append()` is **O(1) amortized**, even though some individual appends can take `O(n)` when resizing happens.

### 4) Why we use it / Main purpose

The main purpose is to store data when the **number of elements can change**.
It gives fast index-based access like a normal array.
Adding an element at the end is usually very fast.
It is useful when you don't know the required size in advance.
