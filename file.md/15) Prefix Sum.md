# 15) Prefix Sum

### 1) What it does

Prefix Sum stores the running sum of array elements.
Each position contains the sum of all elements from the beginning up to that position.
Once calculated, it helps us find the sum of any continuous range quickly.
Instead of adding the elements again and again, we use subtraction to get the answer.

### 2) Diagram

```text
Original Array:
[2, 4, 3, 5, 1]

Prefix Sum:
[2, 6, 9, 14, 15]
 ↓  ↓  ↓   ↓   ↓
 2  2+4  6+3  9+5  14+1

Find sum from index 1 to 3:

Original: [2, 4, 3, 5, 1]
              └─────┘
              4+3+5 = 12

Prefix Sum: 14 - 2 = 12
             ↑   ↑
          prefix[3] prefix[0]
```

### 3) Unique Python line

Python can build a prefix sum using a running total and `append()`:

```python
prefix = [0]

for num in arr:
    prefix.append(prefix[-1] + num)
```

**Useful fact:** Starting with `[0]` makes range-sum calculations simpler because the prefix before index `0` is zero.

### 4) Why we use it / Main purpose

The main purpose is to answer **multiple range-sum queries quickly**.
Building the prefix sum takes **O(n)** time.
Each range-sum query then takes **O(1)** time.
It is useful in array problems involving range sums, cumulative totals, and subarray calculations.
