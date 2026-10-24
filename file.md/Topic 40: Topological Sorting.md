# Topic 40: Topological Sorting

## 1. What It Does

* **Topological Sorting** arranges nodes in an order that respects their dependencies.
* It works only on a **Directed Acyclic Graph (DAG)** — a directed graph with no cycles.
* If task B depends on task A, then A must appear before B in the sorted order.
* Two common methods are **Kahn’s Algorithm (BFS-based)** and **DFS-based Topological Sorting**.

## 2. Diagram

Imagine these tasks for building a website:

```text
       Learn HTML
           |
           v
       Learn CSS
           |
           v
     Build Website
           |
           v
       Deploy Site
```

**Possible topological order:**

```text
Learn HTML
     ↓
Learn CSS
     ↓
Build Website
     ↓
Deploy Site
```

HTML must come before CSS in this example, and the website must be built before deployment.

If multiple tasks have no dependencies between them, they may appear in different valid orders.

## 3. Unique Point

* **Kahn’s Algorithm:** Starts with nodes having an indegree of `0` (no incoming edges).
* **DFS Method:** Adds nodes to the result after exploring their dependent nodes, then reverses the result.
* Both methods typically take **`O(V + E)`** time.
* If a directed graph contains a cycle, a valid topological ordering does not exist.

## 4. Main Purpose

Topological sorting helps organise tasks that depend on one another.

* **Task Scheduling:** Decide which task must happen first.
* **Build Systems:** Compile dependencies before the programs that need them.
* **Course Planning:** Complete prerequisite subjects before advanced subjects.
* **Dependency Management:** Install required packages before dependent packages.

## 5. Real-World Apps

**1. GitHub Actions:** Workflow jobs can define dependencies so prerequisite jobs finish before dependent jobs run.

**2. Build Tools:** Systems such as Maven organise project dependencies so required components are available during builds.

**3. University Course Systems:** Courses can be arranged according to prerequisites, ensuring students complete required subjects first.

---
