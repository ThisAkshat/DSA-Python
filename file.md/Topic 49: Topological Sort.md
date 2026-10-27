# Topic 49: Topological Sort

## 1. What It Does

1. Topological Sort arranges tasks in an order where **every task comes after its required tasks**.
2. It works on a **Directed Acyclic Graph (DAG)**, meaning a directed graph without cycles.
3. It uses two common methods: **Kahn’s Algorithm (BFS)** and **DFS**.
4. Time Complexity: `O(V + E)`, where `V` = vertices and `E` = edges.

## 2. Diagram

Imagine you must complete these tasks:

* A = Learn Basics
* B = Learn Arrays
* C = Learn Graphs
* D = Solve Graph Problems

**Rules:** A must finish before B and C. Both B and C must finish before D.

```text
          A
       /     \
      v       v
      B       C
       \     /
        v   v
          D
```

### Step 1: Find tasks with no requirements

```text
A → B
A → C
B → D
C → D

Indegree:
A = 0
B = 1
C = 1
D = 2

Queue: [A]
```

### Step 2: Complete A

```text
Remove A from queue.

B's indegree: 1 → 0
C's indegree: 1 → 0

Queue: [B, C]
Answer: [A]
```

### Step 3: Complete B

```text
Remove B from queue.

D's indegree: 2 → 1

Queue: [C]
Answer: [A, B]
```

### Step 4: Complete C

```text
Remove C from queue.

D's indegree: 1 → 0

Queue: [D]
Answer: [A, B, C]
```

### Step 5: Complete D

```text
Remove D from queue.

Queue: []
Answer: [A, B, C, D]
```

**Final order:**

```text
Learn Basics
      ↓
Learn Arrays / Learn Graphs
      ↓
Solve Graph Problems
```

Notice that B and C can change places because neither depends on the other.

## 3. Unique Point

1. Topological Sort is possible only when the directed graph has no cycles.
2. A graph can have multiple valid topological orders.
3. Kahn’s Algorithm uses indegree, while DFS uses the order in which nodes finish processing.
4. If Kahn’s Algorithm processes fewer than `V` vertices, the graph contains a cycle.

## 4. Main Purpose

1. **Main job:** Arrange dependent tasks in a valid execution order.
2. **Why it was created:** Some tasks cannot start until their required tasks are completed.
3. **Why it helps:** It avoids performing a task before its prerequisites are ready.
4. **Difference from normal sorting:** Normal sorting orders values, while Topological Sort orders tasks according to dependencies.

## 5. Real-World Apps

1. **Course planning:** Complete prerequisite subjects before advanced subjects.
2. **Build systems:** Compile required files before compiling the files that depend on them.
3. **Task scheduling:** Complete dependent tasks in the correct order.
4. **Package installation:** Install required packages before installing packages that depend on them.
