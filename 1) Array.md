# 1) Array

### 1) What it does

An array stores multiple values in a single structure.
Each value has an **index**, usually starting from `0`.
You can directly access an element using its index.
Example: `arr[2]` gives the third element.
Arrays are useful when you need to store and process a collection of similar data.

### 2) Diagram

```text
Array:  [10] [20] [30] [40] [50]
Index:    0    1    2    3    4

          ↓
       arr[2] = 30
```

### 3) Unique Python line

In Python, `list` is the closest built-in structure to an array, but internally it stores **references to objects**, not the actual values directly.

```python
arr = [10, 20, 30]
```

So Python lists can even contain different data types:

```python
arr = [10, "hello", 3.14]
```

### 4) Why we use it / Main purpose

The main purpose is **fast access to data by index**.
Accessing `arr[i]` is generally **O(1)**.
It is commonly used for storing numbers, strings, results, and collections of data.
Arrays also form the base for many other DSA techniques such as **two pointers, sliding window, prefix sum, sorting, and binary search**.
