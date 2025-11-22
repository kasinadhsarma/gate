# GATE 2018 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~9 questions  
> **Total Marks**: ~15 marks  
> **Difficulty**: Mixed

---

## Question 1: Queue with Linked List (2 marks)

**Year**: 2018 | **Topic**: Queue, Linked List | **Difficulty**: Medium

### Problem Statement
A queue is implemented using a non-circular singly linked list with head and tail pointers. Enqueue is done by inserting at head, dequeue by deleting from tail. What is the time complexity?

**Options**:
- (A) θ(1), θ(1)
- (B) θ(1), θ(n)
- (C) θ(n), θ(1)
- (D) θ(n), θ(n)

### Solution
**Answer**: (B) θ(1), θ(n)

**Explanation**:
- **Enqueue (insert at head)**: O(1)
  - Just update head pointer and new node's next
  
- **Dequeue (delete from tail)**: O(n)
  - Must traverse entire list to find second-to-last node
  - Update its next to NULL
  - Update tail pointer

**Better Implementation**: Enqueue at tail, dequeue from head = both O(1)

---

## Question 2: Binary Tree Height from Traversals (2 marks)

**Year**: 2018 | **Topic**: Trees | **Difficulty**: Medium

### Problem Statement
Given traversals:
- **Postorder**: 8, 9, 6, 7, 4, 5, 2, 3, 1
- **Inorder**: 8, 6, 9, 4, 7, 2, 5, 1, 3

Find the height of the tree.

### Solution
**Answer**: **4**

**Steps to construct tree**:
1. Last element in postorder = root = 1
2. In inorder, elements left of 1 = left subtree: 8,6,9,4,7,2,5
3. Elements right of 1 = right subtree: 3
4. Recursively build subtrees

**Resulting tree**:
```
        1
       / \
      2   3
     / \
    4   5
   / \
  6   7
 / \
8   9
```

**Longest path**: 1 → 2 → 4 → 6 → 8 (or 9) = **4 edges**

**Height = 4**

---

## Question 3: DFS and BFS Properties (2 marks)

**Year**: 2018 | **Topic**: Graphs | **Difficulty**: Hard

### Problem Statement
Let G be a simple undirected graph. Let T_D be a DFS tree and T_B be a BFS tree. Which statements are true?

**(I)** No edge of G is a cross edge with respect to T_D  
**(II)** For every edge (u,v), if u is at depth i and v at depth j in T_B, then |i-j| ≤ 1

**Options**:
- (A) I only
- (B) II only
- (C) Both I and II
- (D) Neither

### Solution
**Answer**: (B) II only

**Explanation**:

**(I) is FALSE**:
- In **undirected** graph DFS, we can have:
  - Tree edges
  - Back edges (to ancestors)
- No cross edges in undirected graph DFS
- **Wait, this makes (I) TRUE for undirected graphs!**

Actually, for **undirected graphs**:
- DFS has only tree and back edges
- No forward or cross edges
- So (I) is **TRUE**

**(II) is TRUE**:
- In BFS, nodes are visited level by level
- Any edge connects nodes at same level or adjacent levels
- Therefore |i-j| ≤ 1

**Correct Answer**: (C) Both I and II

---

## Question 4: Number of Min-Heaps (3 marks)

**Year**: 2018 | **Topic**: Heap | **Difficulty**: Hard

### Problem Statement
How many distinct min-heaps can be formed using values {1, 2, 3, 4, 5, 6, 7}?

### Solution
**Answer**: **80**

**Approach**:
1. Root must be 1 (minimum element)
2. Remaining 6 elements distributed in left and right subtrees
3. For 7 nodes: 3 in left subtree, 3 in right subtree

**Formula**:
```
H(n) = C(n-1, k) × H(k) × H(n-1-k)
```
Where k = size of left subtree

For n=7, k=3:
```
H(7) = C(6,3) × H(3) × H(3)
     = 20 × 2 × 2
     = 80
```

**Calculating H(3)**:
- Root = min
- 2 remaining elements: 1 left, 1 right
- H(3) = C(2,1) × H(1) × H(1) = 2 × 1 × 1 = 2

---

## Question 5: Sorting Algorithm Stability (1 mark)

**Year**: 2018 | **Topic**: Sorting | **Difficulty**: Easy

### Problem Statement
Which of the following sorting algorithms is stable?

**Options**:
- (A) Quicksort
- (B) Heapsort
- (C) Merge sort
- (D) Selection sort

### Solution
**Answer**: (C) Merge sort

**Stable Algorithms**:
- ✓ Merge Sort
- ✓ Insertion Sort
- ✓ Bubble Sort
- ✓ Counting Sort
- ✓ Radix Sort

**Unstable**:
- ✗ Quicksort
- ✗ Heapsort
- ✗ Selection Sort

**Stability**: Maintains relative order of equal elements

---

## Question 6: AVL Tree Rotations (2 marks)

**Year**: 2018 | **Topic**: AVL Trees | **Difficulty**: Medium

### Problem Statement
After inserting elements 10, 20, 30, 40, 50, 25 into an initially empty AVL tree (in that order), how many rotations are performed?

### Solution
**Answer**: **3 rotations**

**Step-by-step**:
1. Insert 10: No rotation
2. Insert 20: No rotation (10 root, 20 right child)
3. Insert 30: **Left rotation** at 10 (20 becomes root)
4. Insert 40: No rotation
5. Insert 50: **Left rotation** at 30, then **left rotation** at 20
6. Insert 25: No rotation

**Total**: 3 rotations

---

## Question 7: Graph Shortest Path (2 marks)

**Year**: 2018 | **Topic**: Graphs | **Difficulty**: Medium

### Problem Statement
In a weighted directed graph with negative edge weights, which algorithm correctly finds shortest paths from a single source?

**Options**:
- (A) Dijkstra's algorithm
- (B) Bellman-Ford algorithm
- (C) Floyd-Warshall algorithm
- (D) Both B and C

### Solution
**Answer**: (D) Both B and C

**Explanation**:
- **Dijkstra's**: Does NOT work with negative weights
- **Bellman-Ford**: Works with negative weights, detects negative cycles
- **Floyd-Warshall**: All-pairs shortest path, works with negative weights

**Time Complexity**:
- Bellman-Ford: O(VE)
- Floyd-Warshall: O(V³)

---

## Question 8: Hash Table Collision (1 mark)

**Year**: 2018 | **Topic**: Hashing | **Difficulty**: Easy

### Problem Statement
Using hash function h(k) = k mod 11, insert keys 23, 34, 45 using linear probing. What are the final positions?

### Solution
**Calculation**:
- h(23) = 23 mod 11 = 1 → **position 1**
- h(34) = 34 mod 11 = 1 (collision) → try 2 → **position 2**
- h(45) = 45 mod 11 = 1 (collision) → try 2 (occupied) → try 3 → **position 3**

**Final positions**: 1, 2, 3

**Linear Probing**: h(k, i) = (h(k) + i) mod m

---

## Question 9: Complexity of Nested Loops (1 mark)

**Year**: 2018 | **Topic**: Complexity | **Difficulty**: Easy

### Problem Statement
```c
for (i = 1; i <= n; i *= 2) {
    for (j = 1; j <= n; j++) {
        // O(1) operation
    }
}
```

What is the time complexity?

### Solution
**Answer**: **O(n log n)**

**Analysis**:
- Outer loop: i = 1, 2, 4, 8, ..., n (log n iterations)
- Inner loop: n iterations each time
- Total: log n × n = **O(n log n)**

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Graphs | 2 | 4 |
| Trees | 2 | 4 |
| Heap | 1 | 3 |
| Queue/Linked List | 1 | 2 |
| Sorting | 1 | 1 |
| Hashing | 1 | 1 |
| Complexity | 1 | 1 |
| **Total** | **9** | **16** |

---

## Key Takeaways

1. **Tree construction** from traversals is important
2. **Min-heap counting** uses combinatorics
3. **Graph properties** - DFS vs BFS edge types
4. **AVL rotations** - track carefully
5. **Negative weights** - use Bellman-Ford or Floyd-Warshall

## Practice Focus
- Construct trees from traversals
- Count structures (heaps, BSTs)
- Graph algorithm selection
- AVL tree operations
- Complexity analysis of nested loops
