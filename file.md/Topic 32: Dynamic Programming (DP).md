# Topic 32: Dynamic Programming (DP) 🧠

## 1. What It Does

* **Dynamic Programming (DP)** is a problem-solving technique that avoids solving the same smaller problem again and again.
* It breaks a big problem into smaller subproblems, solves them, and stores their answers for reuse.
* DP is especially useful when the same subproblems appear repeatedly.
* Its main goal is to **save time by reusing previously calculated results**.
* DP is commonly used in problems involving maximum profit, minimum cost, counting ways, and finding the best possible solution.

## 2. Diagram 📊

Imagine calculating the Fibonacci sequence, where each number is the sum of the previous two numbers.

Formula: `F(n) = F(n-1) + F(n-2)`

Without DP, the same calculations repeat many times.

**Without DP — repeated work:**

```text
                 F(5)
               /      \
            F(4)       F(3)
           /   \       /  \
        F(3)   F(2)  F(2) F(1)
        /  \
      F(2) F(1)

      F(3) and F(2) are calculated repeatedly!
```

**With DP — store and reuse results:**

```text
Calculate F(0) = 0
       ↓
Calculate F(1) = 1
       ↓
Calculate F(2) = 1  → Store
       ↓
Calculate F(3) = 2  → Store
       ↓
Calculate F(4) = 3  → Store
       ↓
Calculate F(5) = 5

Result: 5
```

**Main difference:** DP remembers previous answers instead of calculating them repeatedly.

## 3. Unique Point 💡

DP mainly works when a problem has two important properties:

* **Overlapping Subproblems:** The same smaller problems appear multiple times.
* **Optimal Substructure:** The best answer to a larger problem can be built using answers to its smaller subproblems.

DP has two common approaches:

* **Memoization (Top-Down):** Solve the problem recursively and store answers so they can be reused.
* **Tabulation (Bottom-Up):** Start with smaller problems and build up to the final answer, usually using a table.

DP does not automatically make every problem faster. The benefit depends on the problem's structure and how much repeated work can be avoided.

## 4. Main Purpose 🎯

**The main purpose of DP is to reduce repeated calculations and solve complex problems more efficiently.**

It is especially important for optimisation problems:

* **Maximum:** Find the maximum profit or score.
* **Minimum:** Find the minimum cost, distance, or number of steps.
* **Counting:** Count how many different ways a task can be completed.
* **Decision-making:** Determine whether a valid combination or solution exists.
* **Efficiency:** Replace repeated calculations with stored results.

For example, a problem that takes exponential time with a basic recursive approach may become polynomial-time with DP if it has a manageable number of distinct subproblems.

## 5. Real-World Apps 🌍

**1. Google Maps**

* Route-planning systems can use dynamic programming techniques to solve certain shortest-path and optimisation problems.
* These techniques help reuse results from smaller parts of a problem.

**2. Spell Checkers and Text Editors**

* Edit-distance algorithms use DP to calculate the minimum number of insertions, deletions, or substitutions needed to transform one word into another.
* This helps suggest corrections for misspelled words.

**3. Finance and Investment Systems**

* DP can help solve resource-allocation and investment problems under defined constraints.
* It compares possible decisions and reuses results from smaller subproblems to find an optimal solution.

---
