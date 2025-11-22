# GATE 2021 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~8 questions  
> **Total Marks**: ~14 marks  
> **Difficulty**: Mixed

---

## Question 1: Binary Min-Heap (2 marks)

**Year**: 2021 Set 2 | **Topic**: Heap | **Difficulty**: Medium

### Problem Statement
In a binary min-heap containing n elements, what is the time complexity to find the maximum element?

### Solution
**Answer**: **Θ(n)**

**Explanation**:
- In min-heap, maximum element is at a leaf node
- Number of leaves ≈ n/2
- Must check all leaves to find maximum
- **Time**: Θ(n/2) = Θ(n)

**Alternative**: If heap is stored in array, check elements from index ⌈n/2⌉ to n

---

## Question 2: Reversing Singly Linked List (2 marks)

**Year**: 2021 | **Topic**: Linked List | **Difficulty**: Easy

### Problem Statement
What is the time and space complexity to reverse a singly linked list?

### Solution
**Answer**: Time = O(n), Space = O(1)

**Iterative Approach**:
```c
Node* reverse(Node* head) {
    Node *prev = NULL, *curr = head, *next;
    
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
```

**Recursive**: O(n) space due to call stack

---

## Question 3: Graph Traversal (2 marks)

**Year**: 2021 | **Topic**: Graphs | **Difficulty**: Medium

### Problem Statement
In a directed acyclic graph (DAG), which traversal gives a topological ordering?

### Solution
**Answer**: **DFS with finishing time ordering**

**Algorithm**:
1. Perform DFS on all vertices
2. When vertex finishes, push to stack
3. Pop stack for topological order

**Alternative**: Kahn's algorithm (BFS-based)

**Time**: O(V + E)

---

## Question 4: AVL Tree Height (1 mark)

**Year**: 2021 | **Topic**: AVL Trees | **Difficulty**: Easy

### Problem Statement
What is the maximum height of an AVL tree with n nodes?

### Solution
**Answer**: **1.44 log₂(n+2)**

**Formula**: h ≤ 1.44 log₂(n+2) - 0.328

**Practical**: Height ≈ log₂(n)

**Comparison**:
- BST worst: n-1 (skewed)
- AVL: ~1.44 log n
- Red-Black: ~2 log n

---

## Question 5: Quick Sort Partition (2 marks)

**Year**: 2021 | **Topic**: Sorting | **Difficulty**: Medium

### Problem Statement
In Quicksort, if we always choose the median as pivot, what is the time complexity?

### Solution
**Answer**: **O(n log n)** always

**Explanation**:
- Median divides array into equal halves
- Recurrence: T(n) = 2T(n/2) + O(n)
- Solution: O(n log n)

**Finding median**: O(n) using median-of-medians

**Total**: Still O(n log n)

---

## Question 6: Hash Table (1 mark)

**Year**: 2021 | **Topic**: Hashing | **Difficulty**: Easy

### Problem Statement
With double hashing, what is the probe sequence?

### Solution
**Formula**: h(k, i) = (h₁(k) + i × h₂(k)) mod m

Where:
- h₁(k) = primary hash function
- h₂(k) = secondary hash function
- i = probe number (0, 1, 2, ...)

**Requirement**: h₂(k) and m must be relatively prime

---

## Question 7: Binary Search Tree (2 marks)

**Year**: 2021 | **Topic**: BST | **Difficulty**: Medium

### Problem Statement
How many structurally different BSTs with n nodes have the same inorder traversal?

### Solution
**Answer**: **Only 1**

**Explanation**:
- Inorder of BST gives sorted sequence
- Given inorder (sorted), only one BST structure possible
- Each element's position is determined

**Different question**: How many BSTs with keys 1..n? = Catalan number

---

## Question 8: Dynamic Programming (2 marks)

**Year**: 2021 | **Topic**: DP | **Difficulty**: Medium

### Problem Statement
For 0/1 Knapsack with n items and capacity W, what is the space complexity of the DP solution?

### Solution
**Answer**: **O(W)** with space optimization

**Standard DP**: O(n × W)
```c
int dp[n+1][W+1];
```

**Optimized**: O(W)
```c
int dp[W+1];
// Process items one by one
for (int i = 0; i < n; i++) {
    for (int w = W; w >= weight[i]; w--) {
        dp[w] = max(dp[w], dp[w-weight[i]] + value[i]);
    }
}
```

**Key**: Traverse weights in reverse order

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Heap | 1 | 2 |
| Linked List | 1 | 2 |
| Graphs | 1 | 2 |
| AVL Trees | 1 | 1 |
| Sorting | 1 | 2 |
| Hashing | 1 | 1 |
| BST | 1 | 2 |
| Dynamic Programming | 1 | 2 |
| **Total** | **8** | **14** |

---

## Key Takeaways

1. **Min-heap max**: Check all leaves = O(n)
2. **Linked list reversal**: O(1) space iteratively
3. **Topological sort**: DFS-based approach
4. **AVL height**: ~1.44 log n
5. **Knapsack optimization**: O(W) space possible

## Practice Focus
- Heap operations and properties
- Linked list manipulation
- Topological sorting
- AVL tree properties
- Space-optimized DP
