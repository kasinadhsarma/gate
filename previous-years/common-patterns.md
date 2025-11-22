# GATE Common & Recurring Questions (2015-2025)

> **Consolidated collection of frequently asked question patterns across all years**

This file contains question patterns that appear repeatedly in GATE exams. Mastering these will give you a strong foundation.

---

## 🔥 Most Common Question Patterns

### 1. Heap Operations (Appears: 2015, 2020, 2023)

#### Pattern: Insert Element into Max/Min Heap

**Generic Question**: Given a heap, insert a new element and show the resulting heap.

**Example (GATE 2015)**:
Max heap: `40, 30, 20, 10, 15, 16, 17, 8, 4`  
Insert: 35

**Solution Approach**:
1. Add element at the end
2. Compare with parent
3. Swap if heap property violated
4. Repeat until heap property restored

**Code Template**:
```c
void insertMaxHeap(int heap[], int *n, int value) {
    (*n)++;
    int i = *n - 1;
    heap[i] = value;
    
    // Heapify up
    while (i > 0 && heap[(i-1)/2] < heap[i]) {
        swap(&heap[i], &heap[(i-1)/2]);
        i = (i - 1) / 2;
    }
}
```

**Time Complexity**: O(log n)

---

#### Pattern: Find Maximum in Min-Heap (GATE 2020)

**Question**: Where is the maximum element in a min-heap?

**Answer**: At any leaf node (⌈n/2⌉ to n)

**Time to find**: O(n/2) = O(n)

---

#### Pattern: Build Heap from Array (GATE 2015)

**Question**: Minimum swaps to convert array to max-heap?

**Solution**: Use heapify from bottom-up  
**Time Complexity**: O(n)

---

### 2. BST Operations (Appears: 2015, 2017, 2020, 2023)

#### Pattern: Worst-Case Complexity (GATE 2015)

**Question**: Worst-case time complexity of insertion/deletion in BST?

**Answer**: **Θ(n)** for both (when tree is skewed)

**Key Point**: Balanced BST (AVL) → O(log n)

---

#### Pattern: Inorder Successor (GATE 2023)

**Question**: Find inorder successor of a node in BST.

**Solution**:
```c
TreeNode* findSuccessor(TreeNode* root, TreeNode* node) {
    // Case 1: Node has right subtree
    if (node->right != NULL) {
        TreeNode* temp = node->right;
        while (temp->left != NULL)
            temp = temp->left;
        return temp;
    }
    
    // Case 2: Find nearest ancestor
    TreeNode* successor = NULL;
    while (root != NULL) {
        if (node->data < root->data) {
            successor = root;
            root = root->left;
        } else if (node->data > root->data) {
            root = root->right;
        } else break;
    }
    return successor;
}
```

**Time**: O(h) where h is height

---

#### Pattern: Construct BST from Traversals (GATE 2020)

**Question**: Can we uniquely construct BST from preorder and postorder?

**Answer**: **Yes** (BST property helps partition)

**For general binary tree**: Need inorder + (preorder OR postorder)

---

#### Pattern: Range Query in BST (GATE 2020)

**Question**: Report all elements in range [a, b] in balanced BST.

**Time Complexity**: **O(log n + k)** where k = output size

```c
void rangeQuery(Node* root, int a, int b) {
    if (root == NULL) return;
    if (root->data > a) rangeQuery(root->left, a, b);
    if (root->data >= a && root->data <= b)
        printf("%d ", root->data);
    if (root->data < b) rangeQuery(root->right, a, b);
}
```

---

### 3. AVL Tree Operations (Appears: 2020, 2024)

#### Pattern: Insertion Time Complexity

**Question**: Worst-case time to insert n elements into empty AVL tree?

**Answer**: **O(n log n)**
- Each insertion: O(log n)
- n insertions: n × O(log n)

**Key Properties**:
- Balance factor ∈ {-1, 0, 1}
- Height = O(log n)
- Rotations maintain balance

---

### 4. Tree Properties (Appears: 2015, 2017, 2020)

#### Pattern: Maximum/Minimum Nodes at Height H

**Question**: Max and min nodes in binary tree of height H?

**Formulas**:
- **Maximum**: 2^(H+1) - 1
- **Minimum**: H + 1

**Example**: Height 5
- Max: 2^6 - 1 = 63 nodes
- Min: 6 nodes (skewed)

---

#### Pattern: Leaves vs Internal Nodes (GATE 2015)

**Question**: Tree has L leaves, how many nodes with 2 children?

**Formula**: **L = I₂ + 1**

Where I₂ = nodes with 2 children

**Example**: 20 leaves → 19 nodes with 2 children

---

### 5. Graph Algorithms (Appears: Every Year)

#### Pattern: BFS Traversal (GATE 2017)

**Question**: Valid BFS traversal order?

**Properties**:
- Level-by-level traversal
- All nodes at distance k before k+1
- Uses queue (FIFO)

**Time**: O(V + E)  
**Space**: O(V)

---

#### Pattern: DFS Edge Types (GATE 2017)

**Question**: Which edges exist in DFS of undirected graph?

**Answer**: **Tree edges** and **Back edges** only

**For directed graph**: All 4 types (tree, back, forward, cross)

---

#### Pattern: Minimum Spanning Tree (GATE 2020, 2023)

**Question**: Find MST weight or algorithm complexity.

**Algorithms**:
- **Kruskal's**: O(E log E)
  - Sort edges, use Union-Find
  
- **Prim's**: O((V+E) log V)
  - Start from vertex, grow tree

**MST Properties**:
- Exactly V-1 edges
- Connects all vertices
- Minimum total weight

---

#### Pattern: Dijkstra's Algorithm (GATE 2023)

**Question**: Time complexity with min-heap?

**Answer**: **O((V + E) log V)**

**Key Points**:
- Works only for non-negative weights
- Greedy approach
- Single source shortest path

---

#### Pattern: Graph Connectivity (GATE 2020)

**Question**: Minimum edges for n-vertex connected graph?

**Answer**: **n - 1 edges** (forms a tree)

---

### 6. Complexity Analysis (Appears: Every Year)

#### Pattern: Recurrence Relations

**Common Recurrences**:

1. **T(n) = 2T(√n) + 1** (GATE 2017)
   - Solution: **Θ(log n)**

2. **T(n) = T(n/2) + T(n/4) + n** (GATE 2020)
   - Solution: **Θ(n)**

3. **T(n) = 2T(n/2) + n** (Merge Sort)
   - Solution: **Θ(n log n)**

4. **T(n) = T(n-1) + n**
   - Solution: **Θ(n²)**

**Master Theorem**: T(n) = aT(n/b) + f(n)
```
Compare f(n) with n^(log_b(a)):
Case 1: f(n) smaller → Θ(n^log_b(a))
Case 2: f(n) equal → Θ(n^log_b(a) × log n)
Case 3: f(n) larger → Θ(f(n))
```

---

#### Pattern: Nested Loop Analysis (GATE 2017, 2023)

**Question**: Time complexity of nested loops?

**Example**:
```c
for (i = 1; i <= n; i++) {
    for (j = 1; j <= i; j++) {
        // O(1) operation
    }
}
```

**Analysis**: Σ(i=1 to n) i = n(n+1)/2 = **O(n²)**

---

### 7. Hashing (Appears: 2015, 2020, 2023)

#### Pattern: Load Factor (GATE 2015, 2020)

**Question**: Calculate load factor α.

**Formula**: α = n / m
- n = number of elements
- m = number of slots

**Example**: 2000 elements, 25 slots → α = 80

**Search Time with Chaining**: O(1 + α)

---

#### Pattern: Collision Resolution (GATE 2023)

**Question**: Insert keys using linear/quadratic probing.

**Linear Probing**: h(k, i) = (h(k) + i) mod m

**Quadratic Probing**: h(k, i) = (h(k) + i²) mod m

**Example**: h(k) = k mod 10, insert 12, 22, 32
- 12 → index 2
- 22 → index 2 (collision) → 3
- 32 → index 2 (collision) → 3 (collision) → 4

---

### 8. Dynamic Programming (Appears: 2020, 2023)

#### Pattern: Longest Common Subsequence (GATE 2023)

**Question**: Find LCS length of two strings.

**Recurrence**:
```
dp[i][j] = dp[i-1][j-1] + 1           if X[i] == Y[j]
         = max(dp[i-1][j], dp[i][j-1]) if X[i] != Y[j]
```

**Code**:
```c
int lcs(char* X, char* Y, int m, int n) {
    int dp[m+1][n+1];
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (X[i-1] == Y[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
    return dp[m][n];
}
```

**Time**: O(m × n)  
**Space**: O(m × n) or O(min(m,n)) optimized

---

### 9. Sorting Algorithms (Appears: 2015, 2017)

#### Pattern: Merge Sort Time Scaling (GATE 2015)

**Question**: If merge sort takes 30 sec for n=64, time for n=512?

**Solution**:
- T(n) = n log n
- T(64) = 64 × 6 = 384 units
- T(512) = 512 × 9 = 4608 units
- Ratio = 4608/384 = 12
- Time = 30 × 12 = 360 seconds

---

#### Pattern: Stable Sorting (GATE 2017)

**Question**: Which algorithms are stable?

**Stable**:
- ✓ Merge Sort
- ✓ Insertion Sort
- ✓ Bubble Sort
- ✓ Counting Sort

**Unstable**:
- ✗ Quick Sort
- ✗ Heap Sort
- ✗ Selection Sort

---

### 10. Arrays & Strings (Appears: 2023)

#### Pattern: Kadane's Algorithm (GATE 2023)

**Question**: Maximum subarray sum.

**Algorithm**:
```c
int maxSubarraySum(int arr[], int n) {
    int max_so_far = arr[0];
    int max_ending_here = arr[0];
    
    for (int i = 1; i < n; i++) {
        max_ending_here = max(arr[i], max_ending_here + arr[i]);
        max_so_far = max(max_so_far, max_ending_here);
    }
    return max_so_far;
}
```

**Time**: O(n)  
**Space**: O(1)

---

#### Pattern: Finding Neither Max nor Min (GATE 2015)

**Question**: Comparisons to find element neither max nor min?

**Answer**: **Θ(1)** - Pick any 3 elements, middle one is answer!

---

### 11. Linked Lists (Appears: 2017, 2020)

#### Pattern: Sorted Insertion (GATE 2020)

**Question**: Insert n elements into sorted linked list?

**Time**: **O(n²)**
- 1st: O(1), 2nd: O(1), 3rd: O(2), ..., nth: O(n-1)
- Total: 1+2+3+...+(n-1) = n(n-1)/2

---

#### Pattern: Circular Queue with Linked List (GATE 2017)

**Question**: Pointers needed for O(1) insert/delete?

**Answer**: **Tail pointer only**
- tail->next = head
- Insert/delete both O(1)

---

### 12. Stacks & Queues (Appears: 2020, 2023)

#### Pattern: Expression Evaluation (GATE 2023)

**Question**: Convert infix to postfix.

**Example**: `A + B * C - D / E`

**Steps**:
1. Respect precedence: `* /` > `+ -`
2. Postfix: `A B C * + D E / -`

---

#### Pattern: Valid Stack Sequence (GATE 2020)

**Question**: Is output sequence valid?

**Rules**:
- Can't pop from empty stack
- LIFO order
- Pops ≤ pushes at any point

---

## 📊 Quick Statistics

| Pattern | Frequency | Importance |
|---------|-----------|------------|
| Tree Properties | Very High | ⭐⭐⭐⭐⭐ |
| Graph Algorithms | Very High | ⭐⭐⭐⭐⭐ |
| Complexity Analysis | Every Year | ⭐⭐⭐⭐⭐ |
| BST Operations | High | ⭐⭐⭐⭐ |
| Heap Operations | High | ⭐⭐⭐⭐ |
| Hashing | Medium | ⭐⭐⭐ |
| Dynamic Programming | Medium | ⭐⭐⭐⭐ |
| Sorting | Medium | ⭐⭐⭐ |

---

## 🎯 Practice Strategy

### Week 1-2: Master These Patterns
1. Tree formulas and properties
2. Heap operations
3. BST basic operations
4. Simple recurrences

### Week 3-4: Intermediate Patterns
5. Graph traversals (BFS/DFS)
6. Hashing and load factor
7. Sorting algorithms
8. Linked list operations

### Week 5-6: Advanced Patterns
9. MST algorithms
10. Complex recurrences
11. Dynamic programming
12. AVL trees

### Week 7+: Mixed Practice
- Solve questions combining multiple patterns
- Time yourself
- Focus on accuracy

---

## 💡 Key Formulas to Memorize

```
Trees:
- Max nodes at height H = 2^(H+1) - 1
- Min nodes at height H = H + 1
- Leaves = Internal(2 children) + 1

Graphs:
- MST edges = V - 1
- Min edges for connectivity = V - 1

Complexity:
- Σ(i=1 to n) i = n(n+1)/2
- Σ(i=1 to n) i² = n(n+1)(2n+1)/6

Hashing:
- Load factor α = n / m
- Search time = O(1 + α)

Sorting:
- Merge Sort: O(n log n) always
- Quick Sort: O(n²) worst, O(n log n) average
```

---

**Total Patterns**: 12 major patterns  
**Coverage**: ~80% of GATE DSA questions  
**Practice Time**: 6-8 weeks recommended

**Master these patterns and you'll be well-prepared for GATE! 🚀**
