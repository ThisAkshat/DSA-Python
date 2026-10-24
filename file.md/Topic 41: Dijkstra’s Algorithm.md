# Topic 41: Dijkstra’s Algorithm

## 1. What It Does

* **Dijkstra’s Algorithm** finds the shortest path from one starting node to other nodes in a weighted graph.
* Each edge has a weight, such as distance, travel time, or cost.
* It repeatedly selects the unvisited node with the smallest known distance and updates its neighbours.
* It works with **non-negative edge weights**; it does not correctly handle negative-weight edges in general.

## 2. Diagram

Imagine finding the shortest route from A to D.

```text
          4
     A -------- B
      \         |
     1 \        | 1
        \       |
         C -----D
            2
```

Possible routes from A to D:

* `A → B → D` = `4 + 1 = 5`
* `A → C → D` = `1 + 2 = 3`

**Shortest path: A → C → D**

Total cost = **3**

Dijkstra compares possible distances and finds the cheapest route.

## 3. Unique Point

* Dijkstra commonly uses a **Min Heap / Priority Queue** to select the node with the smallest tentative distance efficiently.
* With an adjacency list and a binary heap, its typical time complexity is **`O((V + E) log V)`**.

## 4. Main Purpose

* **Shortest Routes:** Find the minimum-distance path.
* **Travel Planning:** Calculate routes using distance or travel time as weights.
* **Network Routing:** Find low-cost paths between computers or routers.
* **Cost Optimisation:** Find the cheapest path through a weighted network.

## 5. Real-World Apps

**1. Google Maps:** Shortest-path algorithms help calculate routes using road distances, travel times, and other costs.

**2. Network Routing:** Routing systems use shortest-path techniques to determine efficient paths through networks.

**3. Delivery Platforms:** Route-planning systems can use weighted graphs to find cost-effective routes between locations.

---
