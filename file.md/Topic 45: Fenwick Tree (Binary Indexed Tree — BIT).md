# Topic 45: Fenwick Tree (Binary Indexed Tree — BIT)

## 1. What It Does

A **Fenwick Tree** is a data structure that calculates prefix sums and updates array values efficiently.

For example, it can quickly calculate the sum of elements from index `0` to index `4` without adding every element individually.

## 2. Diagram

Suppose we have this array:

```text
Index:  1   2   3   4   5
Array: [2,  4,  6,  8, 10]
```

The Fenwick Tree stores partial sums in a special arrangement.

For this example, its internal values are:

```text
Index:  1   2   3   4   5
BIT:   [2,  6,  6, 20, 10]
```

Each position stores the sum of a particular range.

```text
BIT[1] = 2
BIT[2] = 2 + 4 = 6
BIT[3] = 6
BIT[4] = 2 + 4 + 6 + 8 = 20
BIT[5] = 10
```

**Example: Find the prefix sum up to index 4.**

```text
Array: [2, 4, 6, 8, 10]

Prefix sum = 2 + 4 + 6 + 8 + 10
           = 30
```

The Fenwick Tree calculates this by combining selected stored sums rather than visiting every array element.

*Note: Fenwick Tree implementations commonly use 1-based indexing, as shown here.*

## 3. Unique Point

Three important operations:

* **Update:** Add a value to an element and update the relevant tree positions.
* **Prefix Sum:** Calculate the sum from the beginning of the array to a specified index.
* **Range Sum:** Calculate the sum between two indices by subtracting two prefix sums.

For example:

`Range Sum(2, 4) = Prefix Sum(4) − Prefix Sum(1)`

Using our array:

`30 − 2 = 28`

The time complexity is:

* Build: `O(n log n)` using repeated updates; an optimized build can achieve `O(n)`.
* Update: `O(log n)`
* Prefix sum: `O(log n)`

## 4. Main Purpose

The main purpose of a Fenwick Tree is to **perform frequent prefix-sum queries and array updates quickly, using less memory and simpler implementation than a typical Segment Tree**.

Suppose an array contains thousands of values, and you repeatedly need to:

1. Update an element.
2. Calculate the sum up to a particular index.
3. Calculate the sum of a specific range.

A Fenwick Tree handles these operations efficiently.

**Important limitation:** A standard Fenwick Tree is particularly suited to prefix sums and related operations. A Segment Tree is more flexible for different range queries, such as range minimum and maximum.

## 5. Real-World Apps

**1. Financial Data Analysis**

Calculate cumulative totals and sums across ranges of transaction records while correcting or updating individual values.

**2. Competitive Programming**

Solve problems involving prefix sums, range sums, and frequent point updates efficiently.

**3. Real-Time Statistics**

Maintain cumulative counts, such as the number of events recorded up to a particular position, while new events update the stored values.

---
