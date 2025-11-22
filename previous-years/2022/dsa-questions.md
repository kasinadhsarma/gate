# GATE 2022 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~9 questions  
> **Total Marks**: ~15 marks  
> **Difficulty**: Mixed

---

## Question 1: Binary Tree Properties (2 marks)

**Year**: 2022 | **Topic**: Trees | **Difficulty**: Easy

### Problem Statement
A binary tree has 15 nodes. What are the minimum and maximum possible heights?

### Solution
**Minimum height**: ⌊log₂(15)⌋ = **3** (complete binary tree)

**Maximum height**: 15 - 1 = **14** (skewed tree)

**Formulas**:
- Min height for n nodes: ⌊log₂(n)⌋
- Max height for n nodes: n - 1

---

## Question 2: Graph Connectivity (2 marks)

**Year**: 2022 | **Topic**: Graphs | **Difficulty**: Medium

### Problem Statement
A graph has 10 vertices. What is the minimum number of edges required to ensure the graph is connected?

### Solution
**Answer**: **9 edges**

**Explanation**:
- Connected graph needs spanning tree
- Spanning tree has exactly V-1 edges
- For 10 vertices: 10 - 1 = **9 edges**

**Example**: Chain of 10 vertices needs 9 edges

---

## Question 3: Merge Sort (1 mark)

**Year**: 2022 | **Topic**: Sorting | **Difficulty**: Easy

### Problem Statement
What is the number of comparisons made by Merge Sort in the worst case for n elements?

### Solution
**Answer**: **Θ(n log n)**

**Recurrence**: C(n) = 2C(n/2) + (n-1)

**Solution**: C(n) = n⌈log₂(n)⌉ - 2^⌈log₂(n)⌉ + 1 ≈ **n log n**

**Exact for powers of 2**: n log₂(n) - n + 1

---

## Question 4: Stack Applications (2 marks)

**Year**: 2022 | **Topic**: Stack | **Difficulty**: Medium

### Problem Statement
Which of the following can be implemented using a single stack?

**(A)** Queue  
**(B)** Priority Queue  
**(C)** Recursion  
**(D)** Expression evaluation

### Solution
**Answer**: (C) Recursion and (D) Expression evaluation

**Explanation**:
- **(C)**: Function call stack uses stack
- **(D)**: Infix/postfix evaluation uses stack
- **(A)**: Queue needs two stacks
- **(B)**: Priority queue needs heap, not stack

---

## Question 5: Hashing Performance (2 marks)

**Year**: 2022 | **Topic**: Hashing | **Difficulty**: Medium

### Problem Statement
In a hash table with separate chaining, if load factor α = 3, what is the average search time for unsuccessful search?

### Solution
**Answer**: **Θ(1 + α) = Θ(4)**

**Explanation**:
- Unsuccessful search checks entire chain
- Average chain length = α = 3
- Time = O(1) hash + O(α) traversal
- Total = **O(1 + 3) = O(4) = Θ(1)**

**For successful search**: Θ(1 + α/2)

---

## Question 6: Binary Search (1 mark)

**Year**: 2022 | **Topic**: Searching | **Difficulty**: Easy

### Problem Statement
Binary search requires the array to be:

### Solution
**Answer**: **Sorted**

**Why**:
- Binary search eliminates half the elements each step
- Only works if array is sorted
- Time: O(log n)

**Unsorted array**: Must use linear search O(n)

---

## Question 7: Tree Traversal (2 marks)

**Year**: 2022 | **Topic**: Trees | **Difficulty**: Medium

### Problem Statement
Given preorder: A, B, D, E, C, F and inorder: D, B, E, A, F, C. Find postorder.

### Solution
**Answer**: D, E, B, F, C, A

**Steps**:
1. Preorder first = root = A
2. In inorder, left of A: D,B,E | right of A: F,C
3. Recursively build tree
4. Postorder: Left → Right → Root

**Tree structure**:
```
      A
     / \
    B   C
   / \   /
  D   E F
```

**Postorder**: D, E, B, F, C, A

---

## Question 8: Dijkstra's Algorithm (2 marks)

**Year**: 2022 | **Topic**: Graphs | **Difficulty**: Medium

### Problem Statement
Dijkstra's algorithm fails for graphs with:

### Solution
**Answer**: **Negative edge weights**

**Why**:
- Dijkstra uses greedy approach
- Assumes once a vertex is processed, shortest path is found
- Negative weights can create shorter paths later

**Alternative**: Use **Bellman-Ford** for negative weights

---

## Question 9: Complexity Class (1 mark)

**Year**: 2022 | **Topic**: Complexity | **Difficulty**: Easy

### Problem Statement
Which is faster: O(n²) or O(n log n)?

### Solution
**Answer**: **O(n log n)** is faster

**Comparison** for large n:
- n = 1000: n log n ≈ 10,000 vs n² = 1,000,000
- n = 10,000: n log n ≈ 130,000 vs n² = 100,000,000

**Growth rates**: 1 < log n < n < n log n < n² < n³ < 2^n < n!

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Trees | 2 | 4 |
| Graphs | 2 | 4 |
| Sorting | 1 | 1 |
| Stack | 1 | 2 |
| Hashing | 1 | 2 |
| Searching | 1 | 1 |
| Complexity | 1 | 1 |
| **Total** | **9** | **15** |

---

## Key Takeaways

1. **Tree height**: Min = log n, Max = n-1
2. **Connected graph**: Needs V-1 edges minimum
3. **Merge sort**: Always Θ(n log n) comparisons
4. **Hashing**: Search time = O(1 + α)
5. **Dijkstra limitation**: No negative weights

## Practice Focus
- Tree construction from traversals
- Graph connectivity problems
- Sorting algorithm analysis
- Hash table performance
- Algorithm limitations
