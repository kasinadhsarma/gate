# Graphs

## 📌 Topic Overview

Graphs are a **VERY HIGH** priority topic for GATE. Graph algorithms appear frequently and are often combined with other topics.

## 🎯 Key Concepts

### Graph Representations
- **Adjacency Matrix**: O(V²) space, O(1) edge lookup
- **Adjacency List**: O(V+E) space, O(degree) edge lookup
- **Edge List**: O(E) space

### Graph Types
- Directed vs Undirected
- Weighted vs Unweighted
- Cyclic vs Acyclic (DAG)
- Connected vs Disconnected
- Sparse vs Dense

## 💡 Essential Algorithms

### 1. Graph Traversal
- **BFS (Breadth-First Search)**
  - Time: O(V+E), Space: O(V)
  - Uses: Shortest path (unweighted), level-order traversal
  
- **DFS (Depth-First Search)**
  - Time: O(V+E), Space: O(V)
  - Uses: Cycle detection, topological sort, connected components

### 2. Shortest Path Algorithms

| Algorithm | Type | Time | Use Case |
|-----------|------|------|----------|
| BFS | Unweighted | O(V+E) | Unweighted graphs |
| Dijkstra | Weighted (non-negative) | O((V+E) log V) | Single source |
| Bellman-Ford | Weighted (any) | O(VE) | Negative edges |
| Floyd-Warshall | All pairs | O(V³) | All pairs shortest path |

### 3. Minimum Spanning Tree (MST)

- **Prim's Algorithm**
  - Time: O((V+E) log V) with min-heap
  - Greedy approach, works on connected graphs
  
- **Kruskal's Algorithm**
  - Time: O(E log E) or O(E log V)
  - Uses Union-Find, works on disconnected graphs

### 4. Advanced Algorithms
- **Topological Sort**: O(V+E) - for DAGs
- **Strongly Connected Components**: O(V+E) - Kosaraju's/Tarjan's
- **Articulation Points & Bridges**: O(V+E)
- **Cycle Detection**: O(V+E)

## 🔥 GATE Must-Know Problems

### Critical (Must Master)
- [ ] BFS and DFS implementation
- [ ] Dijkstra's Algorithm
- [ ] Bellman-Ford Algorithm
- [ ] Floyd-Warshall Algorithm
- [ ] Prim's MST
- [ ] Kruskal's MST
- [ ] Topological Sort
- [ ] Cycle Detection (directed & undirected)
- [ ] Strongly Connected Components

### Important
- [ ] Shortest path in DAG
- [ ] Bipartite Graph Check
- [ ] Graph Coloring
- [ ] Hamiltonian Path/Cycle
- [ ] Eulerian Path/Cycle
- [ ] Articulation Points
- [ ] Bridges in Graph

## 📊 Complexity Comparison

```
Graph with V vertices, E edges:

Adjacency Matrix:
- Space: O(V²)
- Add edge: O(1)
- Check edge: O(1)
- Get all neighbors: O(V)

Adjacency List:
- Space: O(V+E)
- Add edge: O(1)
- Check edge: O(degree)
- Get all neighbors: O(degree)
```

## 💡 Problem-Solving Patterns

### When to use BFS?
- Shortest path in unweighted graph
- Level-order traversal
- Finding all nodes at distance k

### When to use DFS?
- Cycle detection
- Topological sorting
- Finding connected components
- Path finding (any path, not shortest)

### When to use Dijkstra?
- Shortest path with non-negative weights
- Single source to all destinations

### When to use Bellman-Ford?
- Negative edge weights present
- Detect negative cycles

## 📝 Practice Strategy

### Week 1: Fundamentals
- Graph representations
- BFS and DFS
- Connected components

### Week 2: Shortest Paths
- Dijkstra's algorithm
- Bellman-Ford
- Floyd-Warshall

### Week 3: MST & Advanced
- Prim's and Kruskal's
- Topological Sort
- Strongly Connected Components

### Week 4: GATE Questions
- Previous year problems
- Mixed concept questions
- Complexity analysis

## 🎯 GATE Question Patterns

1. **Algorithm Output**: Given graph, find output of algorithm
2. **Complexity**: Analyze time/space complexity
3. **Correctness**: Which algorithm works for given scenario?
4. **Comparison**: Compare different algorithms
5. **Code Analysis**: Trace through algorithm code

## 📚 Important Theorems

- **Handshaking Lemma**: Sum of degrees = 2 × edges
- **Euler's Theorem**: Eulerian path/cycle conditions
- **Planar Graph**: V - E + F = 2 (Euler's formula)
- **Tree Properties**: V = E + 1 for connected tree

## 🎓 Resources

- CLRS Chapter 22-25 (Graph Algorithms)
- GeeksforGeeks Graph section
- GATE Overflow graph questions
- Visualgo.net for algorithm visualization

---

**Difficulty Distribution**: Easy: 25% | Medium: 50% | Hard: 25%  
**Expected Questions in GATE**: 2-4 questions (4-8 marks)
