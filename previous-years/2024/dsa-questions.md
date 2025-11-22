# GATE 2024 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~9 questions  
> **Total Marks**: ~16 marks  
> **Difficulty**: Mixed

---

## Question 1: Binary Tree Traversal (2 marks)

**Year**: 2024 | **Topic**: Trees | **Difficulty**: Medium

### Problem Statement
Given a binary tree, if preorder and postorder traversals are the same, what can we conclude?

### Solution
**Answer**: **Tree has only one node**

**Explanation**:
- Preorder: Root → Left → Right
- Postorder: Left → Right → Root
- For them to be same, tree must have only root

**Example**: Preorder = Postorder = [5] ✓

---

## Question 2: Hash Table with Open Addressing (2 marks)

**Year**: 2024 | **Topic**: Hashing | **Difficulty**: Medium

### Problem Statement
Using quadratic probing with h(k) = k mod 13, insert keys 18, 31, 44. What are the positions?

### Solution
**Quadratic probing**: h(k, i) = (h(k) + i²) mod m

**Insertions**:
- h(18) = 18 mod 13 = 5 → **position 5**
- h(31) = 31 mod 13 = 5 (collision)
  - Try (5 + 1²) mod 13 = 6 → **position 6**
- h(44) = 44 mod 13 = 5 (collision)
  - Try (5 + 1²) mod 13 = 6 (occupied)
  - Try (5 + 2²) mod 13 = 9 → **position 9**

**Final positions**: 5, 6, 9

---

## Question 3: Recursion Time Complexity (2 marks)

**Year**: 2024 | **Topic**: Complexity Analysis | **Difficulty**: Medium

### Problem Statement
```c
int mystery(int n) {
    if (n <= 1) return 1;
    return mystery(n-1) + mystery(n-1);
}
```

What is the time complexity?

### Solution
**Answer**: **O(2^n)**

**Recurrence**: T(n) = 2T(n-1) + O(1)

**Expansion**:
- T(n) = 2T(n-1)
- T(n) = 2²T(n-2)
- T(n) = 2³T(n-3)
- T(n) = 2^n T(0)
- **T(n) = O(2^n)**

**Note**: This is inefficient; can be optimized to O(n) with memoization

---

## Question 4: Graph Minimum Cut (2 marks)

**Year**: 2024 | **Topic**: Graphs | **Difficulty**: Hard

### Problem Statement
In a flow network, what is the relationship between max-flow and min-cut?

### Solution
**Answer**: **Max-flow = Min-cut** (Max-flow Min-cut Theorem)

**Explanation**:
- Maximum flow from source to sink
- Equals minimum capacity of cut separating source and sink
- Fundamental theorem in network flow

**Applications**:
- Network optimization
- Image segmentation
- Bipartite matching

---

## Question 5: AVL Tree Deletion (2 marks)

**Year**: 2024 | **Topic**: AVL Trees | **Difficulty**: Medium

### Problem Statement
After deleting a node from an AVL tree, how many rotations might be needed to rebalance?

### Solution
**Answer**: **O(log n)** rotations in worst case

**Explanation**:
- Deletion can cause imbalance up the path to root
- Height of AVL tree = O(log n)
- May need one rotation at each level
- **Worst case**: O(log n) rotations

**Insertion**: At most 2 rotations (one double rotation)

---

## Question 6: Sorting Stability (1 mark)

**Year**: 2024 | **Topic**: Sorting | **Difficulty**: Easy

### Problem Statement
Which sorting algorithm is NOT stable?

**Options**: (A) Merge Sort (B) Quick Sort (C) Insertion Sort (D) Bubble Sort

### Solution
**Answer**: (B) Quick Sort

**Stable algorithms**:
- Merge Sort ✓
- Insertion Sort ✓
- Bubble Sort ✓
- Counting Sort ✓

**Unstable**:
- Quick Sort ✗
- Heap Sort ✗
- Selection Sort ✗

---

## Question 7: Linked List Operations (1 mark)

**Year**: 2024 | **Topic**: Linked List | **Difficulty**: Easy

### Problem Statement
In a doubly linked list, what is the time complexity to delete a node given a pointer to it?

### Solution
**Answer**: **O(1)**

**Code**:
```c
void deleteNode(Node* node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
    free(node);
}
```

**Comparison**:
- Singly linked list: O(1) (but can't delete last node)
- Doubly linked list: O(1) (can delete any node)

---

## Question 8: Dynamic Programming - LCS (2 marks)

**Year**: 2024 | **Topic**: DP | **Difficulty**: Medium

### Problem Statement
For strings of length m and n, what is the space complexity of LCS with space optimization?

### Solution
**Answer**: **O(min(m, n))**

**Standard DP**: O(m × n)

**Optimized**:
```c
// Use only two rows
int dp[2][n+1];
for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
        if (X[i-1] == Y[j-1])
            dp[i%2][j] = dp[(i-1)%2][j-1] + 1;
        else
            dp[i%2][j] = max(dp[(i-1)%2][j], dp[i%2][j-1]);
    }
}
```

**Space**: O(2 × n) = **O(n)** if m > n

---

## Question 9: Heap Construction (2 marks)

**Year**: 2024 | **Topic**: Heap | **Difficulty**: Medium

### Problem Statement
What is the time complexity to build a heap from an unsorted array of n elements?

### Solution
**Answer**: **O(n)**

**Explanation**:
- Naive approach (insert n times): O(n log n)
- **Heapify approach**: O(n)

**Why O(n)**:
- Start from last non-leaf node
- Heapify down
- Most nodes are near bottom (do less work)
- Total work = O(n)

**Proof**: Σ(h=0 to log n) (n/2^(h+1)) × h = O(n)

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Trees | 2 | 4 |
| Hashing | 1 | 2 |
| Complexity | 1 | 2 |
| Graphs | 1 | 2 |
| AVL Trees | 1 | 2 |
| Sorting | 1 | 1 |
| Linked List | 1 | 1 |
| Dynamic Programming | 1 | 2 |
| Heap | 1 | 2 |
| **Total** | **9** | **16** |

---

## Key Takeaways

1. **Preorder = Postorder** → Single node tree
2. **Quadratic probing** → h(k, i) = (h(k) + i²) mod m
3. **Recursion complexity** → Analyze recurrence
4. **Max-flow = Min-cut** → Fundamental theorem
5. **Heap building** → O(n) with heapify

## Practice Focus
- Tree traversal properties
- Hashing collision resolution
- Recursion complexity analysis
- Network flow algorithms
- Space-optimized DP
