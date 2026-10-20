# Topic 31: Greedy Algorithms 🧠

## 1. What It Does

* A **Greedy Algorithm** solves a problem by choosing what looks like the best option at the current step.
* It makes a decision and moves forward without reconsidering previous decisions.
* Its goal is to reach a good or optimal solution through a series of local choices.
* Example: If you want to reach a destination, you might choose the road that gets you closest to your destination at each step.
* **Important:** A greedy choice does not always produce the best overall answer. It works optimally only when the problem has the right properties.

## 2. Diagram

Imagine you want to select activities that do not overlap.

```text
Activity A: [1────3]
Activity B:   [2────5]
Activity C:       [4────6]
Activity D:             [6────8]

Greedy choice:
Select A → Select C → Select D

Selected activities: A, C, D
Total activities: 3
```

**How it works:**

* Select Activity A because it finishes earliest.
* Activity B overlaps with A, so skip it.
* Select Activity C because it starts after A finishes.
* Select Activity D because it starts when C finishes.
* We select three non-overlapping activities.

This is an example of the **Activity Selection Problem**, where choosing the activity that finishes earliest leads to the maximum number of compatible activities.

## 3. Unique Point 💡

* Greedy algorithms make **local optimal choices** at each step.
* A local best choice means the best option according to the current decision rule.
* A global optimal solution means the best answer for the entire problem.
* Greedy works when the local choices can lead to a globally optimal solution.
* Unlike backtracking, greedy algorithms generally do not undo their choices or explore every possibility.
* Their time complexity depends on the problem. Some require sorting first, which usually takes `O(n log n)` time.

## 4. Main Purpose

Greedy algorithms help solve optimisation problems efficiently.

They are useful for:

* **Minimisation:** Finding a solution with the smallest cost.
* **Maximisation:** Finding the greatest possible profit or number of activities.
* **Scheduling:** Selecting compatible activities or jobs.
* **Resource allocation:** Distributing limited resources efficiently.
* **Reducing complexity:** Avoiding the need to examine every possible combination when a greedy strategy is valid.

## 5. Real-World Apps 🌍

**1. Google Maps**

* Route-planning algorithms may use greedy strategies as part of finding promising routes.
* However, shortest-path algorithms such as Dijkstra's algorithm are needed when the goal is to guarantee the shortest path under its assumptions.

**2. Network Routing**

* Network systems can use greedy-style decisions to select promising paths or links based on costs and other metrics.
* The exact algorithm depends on the network and its requirements.

**3. Data Compression**

* Huffman coding uses a greedy strategy to build an efficient prefix code.
* It repeatedly combines the two symbols or groups with the lowest frequencies to reduce the overall encoded length.

---
