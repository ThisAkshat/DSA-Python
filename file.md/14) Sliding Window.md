# 14) Sliding Window

### 1) What it does

Sliding Window is a technique used to solve problems involving **continuous parts of an array or string**.
We maintain a window that covers a group of elements.
Instead of calculating everything again, we move the window and update the result.
The window can have a fixed size or a variable size.

### 2) Diagram

Example: Find the maximum sum of 3 consecutive elements.

```text
Array: [2, 1, 5, 1, 3, 2]

Window 1:
        [2, 1, 5] 1, 3, 2
         Sum = 8

Window 2:
         2, [1, 5, 1] 3, 2
             Sum = 7

Window 3:
         2, 1, [5, 1, 3] 2
                Sum = 9

Window 4:
         2, 1, 5, [1, 3, 2]
                    Sum = 6

Maximum sum = 9
```

### 3) Unique Python line

In a fixed-size sliding window, you can update the sum by **subtracting the element leaving the window and adding the new element entering it**.

```python
window_sum += arr[right] - arr[right - k]
```

This avoids recalculating the sum of every element in the window.

### 4) Why we use it / Main purpose

The main purpose is to process continuous subarrays or substrings efficiently.
It is useful for finding maximum sums, minimum lengths, and patterns in strings.
A sliding window can often reduce an **O(n × k)** solution to **O(n)**.
It is commonly used in interview problems involving consecutive elements or characters.
