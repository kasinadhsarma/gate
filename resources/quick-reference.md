# GATE DSA - Quick Reference Sheet

## 📊 Time Complexity Cheat Sheet

### Common Complexities (Best to Worst)
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

### Data Structure Operations

| Data Structure | Access | Search | Insert | Delete |
|----------------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| Hash Table | - | O(1) | O(1) | O(1) |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | - | O(n) | O(log n) | O(log n) |

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |

### Searching Algorithms

| Algorithm | Time | Space | Requirement |
|-----------|------|-------|-------------|
| Linear Search | O(n) | O(1) | None |
| Binary Search | O(log n) | O(1) | Sorted array |
| Jump Search | O(√n) | O(1) | Sorted array |
| Interpolation Search | O(log log n) | O(1) | Sorted + uniform |

---

## 🌳 Tree Formulas

### Binary Tree Properties
```
Maximum nodes at level L = 2^L
Maximum nodes in tree of height H = 2^(H+1) - 1
Minimum height for N nodes = log₂(N+1) - 1

For N nodes:
- Minimum height = log₂(N+1) - 1
- Maximum height = N - 1
```

### Binary Search Tree
```
Inorder traversal → Sorted order
Height of balanced BST = O(log n)
Height of skewed BST = O(n)
```

### Complete Binary Tree
```
If N nodes, height = floor(log₂N)
Parent of node i = floor((i-1)/2)
Left child of node i = 2i + 1
Right child of node i = 2i + 2
```

### AVL Tree
```
Balance Factor = height(left) - height(right)
Balance Factor ∈ {-1, 0, 1}
Height ≤ 1.44 log₂(N+2)
```

---

## 📈 Graph Formulas

### Graph Properties
```
Handshaking Lemma: Σ degree(v) = 2 × |E|

For undirected graph:
- Maximum edges = n(n-1)/2
- Minimum edges for connected = n-1

For directed graph:
- Maximum edges = n(n-1)

Tree properties:
- |V| = |E| + 1 (for connected tree)
```

### Graph Traversal
```
BFS: O(V + E) time, O(V) space
DFS: O(V + E) time, O(V) space
```

### Shortest Path
```
Dijkstra: O((V+E) log V) with min-heap
Bellman-Ford: O(VE)
Floyd-Warshall: O(V³)
```

### Minimum Spanning Tree
```
Prim's: O((V+E) log V)
Kruskal's: O(E log E)
```

---

## 🔢 Important Formulas

### Recurrence Relations

**Master Theorem**: T(n) = aT(n/b) + f(n)
```
Case 1: f(n) = O(n^(log_b(a) - ε))  →  T(n) = Θ(n^log_b(a))
Case 2: f(n) = Θ(n^log_b(a))        →  T(n) = Θ(n^log_b(a) × log n)
Case 3: f(n) = Ω(n^(log_b(a) + ε))  →  T(n) = Θ(f(n))
```

**Common Recurrences**:
```
T(n) = T(n-1) + O(1)           →  O(n)
T(n) = T(n-1) + O(n)           →  O(n²)
T(n) = 2T(n/2) + O(1)          →  O(n)
T(n) = 2T(n/2) + O(n)          →  O(n log n)  [Merge Sort]
T(n) = T(n/2) + O(1)           →  O(log n)    [Binary Search]
T(n) = T(n/2) + O(n)           →  O(n)
```

### Summation Formulas
```
Σ(i=1 to n) i = n(n+1)/2
Σ(i=1 to n) i² = n(n+1)(2n+1)/6
Σ(i=1 to n) i³ = [n(n+1)/2]²
Σ(i=0 to n) 2^i = 2^(n+1) - 1
Σ(i=1 to n) 1/i ≈ ln(n)  [Harmonic series]
```

### Logarithm Rules
```
log(ab) = log(a) + log(b)
log(a/b) = log(a) - log(b)
log(a^b) = b × log(a)
log_b(a) = log(a) / log(b)
```

---

## 💡 Algorithm Paradigms

### Divide and Conquer
```
1. Divide problem into subproblems
2. Conquer subproblems recursively
3. Combine solutions

Examples: Merge Sort, Quick Sort, Binary Search
```

### Greedy
```
1. Make locally optimal choice
2. Hope for global optimum

Examples: Dijkstra, Prim's, Kruskal's, Huffman Coding
```

### Dynamic Programming
```
1. Identify optimal substructure
2. Find overlapping subproblems
3. Memoize or tabulate

Examples: LCS, LIS, Knapsack, Matrix Chain
```

### Backtracking
```
1. Build solution incrementally
2. Abandon when constraints violated
3. Backtrack and try alternatives

Examples: N-Queens, Sudoku, Graph Coloring
```

---

## 🎯 Problem-Solving Patterns

### Two Pointers
- Pair sum in sorted array
- Remove duplicates
- Container with most water

### Sliding Window
- Maximum sum subarray of size k
- Longest substring without repeating chars
- Minimum window substring

### Fast & Slow Pointers
- Cycle detection in linked list
- Find middle of linked list
- Happy number problem

### Binary Search Variations
- Search in rotated sorted array
- Find peak element
- Square root using binary search

---

## 📝 Common Tricks

### Bit Manipulation
```
Check if power of 2: n & (n-1) == 0
Count set bits: __builtin_popcount(n)
Get ith bit: (n >> i) & 1
Set ith bit: n | (1 << i)
Clear ith bit: n & ~(1 << i)
Toggle ith bit: n ^ (1 << i)
```

### Array Tricks
```
Kadane's Algorithm: Max subarray sum
Dutch National Flag: 3-way partitioning
Moore's Voting: Majority element
```

### String Tricks
```
KMP: Pattern matching in O(n+m)
Rabin-Karp: Rolling hash for pattern matching
Manacher's: Longest palindromic substring
```

---

**Print this sheet and keep it handy during practice!**
