# 13) Two Pointers

### 1) What it does

Two Pointers is a technique that uses two variables to track positions in a data structure, usually an array or string.
Each pointer represents an index.
They can move towards each other or in the same direction.
Instead of repeatedly checking every possible pair, we use these pointers to solve problems more efficiently.

### 2) Diagram

Example: Find whether two numbers add up to `10` in a sorted array.

```text
Array:  [1, 2, 3, 4, 6]
        ↑           ↑
      Left        Right

      1 + 6 = 7
      Sum < 10 → Move Left

Array:  [1, 2, 3, 4, 6]
           ↑        ↑
         Left     Right

      2 + 6 = 8
      Sum < 10 → Move Left

Array:  [1, 2, 3, 4, 6]
              ↑     ↑
            Left  Right

      3 + 6 = 9
      Sum < 10 → Move Left

Array:  [1, 2, 3, 4, 6]
                 ↑  ↑
               Left Right

      4 + 6 = 10 ✓
```

### 3) Unique Python line

In Python, two pointers are usually just **two integer variables storing indices**. They don't require any special library.

```python
left, right = 0, len(arr) - 1
```

This initializes one pointer at the beginning and the other at the end.

### 4) Why we use it / Main purpose

The main purpose is to solve array and string problems efficiently.
It is commonly used for finding pairs, reversing arrays, checking palindromes, and removing duplicates from sorted arrays.
For example, finding a pair with a target sum can take **O(n)** time using two pointers on a sorted array, instead of checking every pair in **O(n²)** time.
