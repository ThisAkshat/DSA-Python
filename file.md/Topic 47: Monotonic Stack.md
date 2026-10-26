# Topic 47: Monotonic Stack

## 1. What It Does

1. A stack that maintains elements in **increasing or decreasing order**.
2. Removes elements that break the required order.
3. Helps solve problems like Next Greater Element.
4. Commonly processes arrays in `O(n)` time.

## 2. Diagram

**Example:** Find the next greater element for each number.

```text
Array:  [2, 1, 4]

Step 1: Read 2
Stack:  [2]

Step 2: Read 1
Stack:  [2, 1]

Step 3: Read 4
        4 > 1 → Answer for 1 is 4
        4 > 2 → Answer for 2 is 4

Stack:  [4]

Final Answer:
Number: [2, 1, 4]
Next:   [4, 4, -1]
```

`-1` means no greater element exists to the right.

## 3. Unique Point

1. Each element is pushed onto the stack once and removed at most once.
2. Even with a loop inside a loop, the overall time can be `O(n)`.
3. An increasing monotonic stack and a decreasing monotonic stack solve different types of problems.
4. Elements removed from the stack are not necessarily useless; they have served their purpose for the current problem.

## 4. Main Purpose

1. **Problem:** Finding the next greater or smaller element by checking every element can take `O(n²)` time.
2. **Solution:** Keep only the elements needed to maintain the stack's order.
3. When a new element breaks that order, pop the affected elements and process their answers.
4. This reduces many array problems to `O(n)` time.

## 5. Real-World Apps

1. **Stock Analysis:** Find the next day when a stock price exceeds today's price.
2. **Weather Apps:** Find how many days until a warmer temperature.
3. **Data Analysis:** Find the next greater value in a sequence of measurements.
4. **Histogram Problems:** Find the largest rectangular area in a histogram efficiently.

---
