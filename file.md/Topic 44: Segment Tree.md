# Topic 44: Segment Tree

## 1. What It Does

A **Segment Tree** is a tree-based data structure that helps answer questions about a specific range of an array efficiently.

For example:

* Find the sum of array elements from index 1 to 4.
* Find the minimum or maximum value in a range.
* Update an element and answer range queries again.

## 2. Diagram

Suppose we have this array:

```text
Index:  0   1   2   3
Array: [2,  4,  6,  8]
```

We want to find the **sum of all elements**.

A simplified Segment Tree for range sums looks like this:

```text
             [0–3: 20]
             /       \
       [0–1: 6]     [2–3: 14]
        /    \        /    \
   [0: 2]  [1: 4] [2: 6] [3: 8]
```

Each node stores the sum of the array range it represents.

For example:

* Range `[0–1]` → 2 + 4 = 6
* Range `[2–3]` → 6 + 8 = 14
* Range `[0–3]` → 2 + 4 + 6 + 8 = 20

If we ask for the sum of elements in range `[1–3]`, the answer is:

**4 + 6 + 8 = 18**

The Segment Tree can calculate this without adding every element individually.

## 3. Unique Point

Three important concepts:

* **Range Query:** Ask for information about a portion of an array, such as its sum, minimum or maximum.
* **Point Update:** Change one array element and update the relevant tree nodes.
* **Lazy Propagation:** An optimization used for certain range updates, allowing multiple changes to be processed efficiently without immediately updating every affected element.

For a typical Segment Tree:

* Building the tree: `O(n)`
* Range query: `O(log n)`
* Point update: `O(log n)`

Here, `n` is the number of array elements.

## 4. Main Purpose

The main purpose of a Segment Tree is to **answer repeated range queries efficiently, even when array elements change**.

Consider this array:

```text
[2, 4, 6, 8]
```

You ask for the sum of indices 1 to 3.

Answer: `4 + 6 + 8 = 18`

Now, suppose the value at index 2 changes from `6` to `10`.

Updated array:

```text
[2, 4, 10, 8]
```

You ask for the same range again.

New answer: `4 + 10 + 8 = 22`

The Segment Tree updates the relevant nodes, so future queries can be answered efficiently.

**Important:** If you only need a single range-sum query, a Segment Tree is usually unnecessary. It becomes useful when you need many queries and updates.

## 5. Real-World Apps

**1. Competitive Programming**

Problems involving repeated range-sum, minimum or maximum queries often use Segment Trees to avoid repeatedly scanning the array.

**2. Data Analytics**

Suppose a system frequently calculates totals for different ranges of recorded values. A Segment Tree can support these range queries while the underlying values change.

**3. Real-Time Monitoring**

A monitoring system may need to calculate the minimum, maximum or sum of measurements over different index ranges while new measurements or corrections update the stored data.
