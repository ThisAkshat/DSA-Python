# Topic 47: Knapsack Patterns

## 1. What It Does

1. Selects items to get the best result within a limited capacity.
2. Each item has a weight and a value.
3. Dynamic Programming (DP) helps compare different combinations.
4. Common patterns: 0/1 Knapsack, Unbounded Knapsack, and Subset Sum.

## 2. Diagram

**Bag capacity = 5 kg**

```text
Items: A(1kg, ₹10)
       B(2kg, ₹15)
       C(3kg, ₹40)

Choose B + C
      ↓
Weight = 2 + 3 = 5 kg
Value  = 15 + 40 = ₹55
      ↓
Maximum Value = ₹55
```

## 3. Unique Point

1. **0/1 Knapsack:** Each item can be selected once.
2. **Unbounded Knapsack:** An item can be selected multiple times.
3. **Subset Sum:** Checks whether a target sum is possible.
4. Greedy selection does not always give the optimal answer.

## 4. Main Purpose

1. Find the best combination within limited resources.
2. Avoid checking every combination repeatedly.
3. DP stores previous results to reduce repeated work.
4. 0/1 Knapsack typically takes `O(n × W)` time, where `n` is the number of items and `W` is capacity.

## 5. Real-World Apps

1. **Cargo loading:** Select valuable goods within a weight limit.
2. **Budget planning:** Choose projects within a fixed budget.
3. **Cloud computing:** Allocate limited computing resources.
4. **Investment planning:** Select suitable combinations within a budget.
