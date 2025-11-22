# GATE 2020 - Data Structures & Algorithms Questions

> **Total DSA Questions**: 10 questions  
> **Total Marks**: 16 marks  
> **Difficulty**: Mixed

---

## Question 1: AVL Tree Insertion (2 marks)

**Year**: 2020 | **Topic**: AVL Trees | **Difficulty**: Medium

### Problem Statement
What is the worst-case time complexity of inserting n elements into an empty AVL tree?

### Solution
**Answer**: **O(n log n)**

**Explanation**:
- Each insertion in AVL tree: O(log n)
- For n insertions: n × O(log n) = O(n log n)
- AVL maintains balance, so height = O(log n)

**Key Points**:
- AVL tree is self-balancing BST
- Balance factor ∈ {-1, 0, 1}
- Rotations maintain O(log n) height

---

## Question 2: BST Traversals (2 marks)

**Year**: 2020 | **Topic**: BST, Tree Traversal | **Difficulty**: Medium

### Problem Statement
Given preorder and postorder traversals of a BST, can we uniquely construct the tree?

### Solution
**Answer**: **Yes**

**Explanation**:
For **BST specifically**:
- Preorder: Root → Left → Right
- Postorder: Left → Right → Root
- BST property: Left < Root < Right

**Steps to construct**:
1. First element of preorder = root
2. Last element of postorder = root (verification)
3. Use BST property to partition elements
4. Recursively build left and right subtrees

**Note**: For general binary tree, need inorder + (preorder OR postorder)

---

## Question 3: Recurrence Relation (2 marks)

**Year**: 2020 | **Topic**: Complexity Analysis | **Difficulty**: Hard

### Problem Statement
Solve: T(n) = T(n/2) + T(n/4) + n

### Solution
**Using Recursion Tree Method**:

```
Level 0: n
Level 1: n/2 + n/4 = 3n/4
Level 2: 3n/8 + 3n/16 = 9n/16
...
```

Sum = n(1 + 3/4 + 9/16 + ...) = n × 4 = **O(n)**

**Answer**: **Θ(n)**

**Verification**: Work at each level decreases geometrically

---

## Question 4: Sorted Linked List Insertion (2 marks)

**Year**: 2020 | **Topic**: Linked List | **Difficulty**: Medium

### Problem Statement
What is the worst-case time complexity to insert n elements into an initially empty sorted linked list?

### Solution
**Answer**: **O(n²)**

**Explanation**:
- 1st insertion: O(1) - list empty
- 2nd insertion: O(1) - compare with 1 element
- 3rd insertion: O(2) - compare with 2 elements
- ...
- nth insertion: O(n-1)

Total: 1 + 2 + 3 + ... + (n-1) = **n(n-1)/2 = O(n²)**

---

## Question 5: Range Query in BST (2 marks)

**Year**: 2020 | **Topic**: BST | **Difficulty**: Medium

### Problem Statement
In a balanced BST with n nodes, what is the time complexity to report all elements in range [a, b]?

### Solution
**Answer**: **O(log n + k)** where k = number of elements in range

**Explanation**:
- Find lower bound 'a': O(log n)
- Traverse in-order from 'a' to 'b': O(k)
- Total: O(log n + k)

**Code Approach**:
```c
void rangeQuery(Node* root, int a, int b) {
    if (root == NULL) return;
    
    if (root->data > a)
        rangeQuery(root->left, a, b);
    
    if (root->data >= a && root->data <= b)
        printf("%d ", root->data);
    
    if (root->data < b)
        rangeQuery(root->right, a, b);
}
```

---

## Question 6: Maximum in Min-Heap (1 mark)

**Year**: 2020 | **Topic**: Heap | **Difficulty**: Easy

### Problem Statement
Where can the maximum element be located in a min-heap?

### Solution
**Answer**: **At any leaf node**

**Explanation**:
- Min-heap: Parent ≤ Children
- Maximum element has no children
- Must be a leaf node
- Could be any of the ⌈n/2⌉ leaf nodes

**Time to find max**: O(n/2) = **O(n)**

---

## Question 7: Minimum Spanning Tree Weight (3 marks)

**Year**: 2020 | **Topic**: Graphs, MST | **Difficulty**: Medium

### Problem Statement
Given a weighted graph, find the weight of the minimum spanning tree.

### Solution Approach
**Use Kruskal's or Prim's Algorithm**:

**Kruskal's Steps**:
1. Sort all edges by weight
2. Pick smallest edge that doesn't form cycle
3. Repeat until V-1 edges selected

**Prim's Steps**:
1. Start from any vertex
2. Add minimum weight edge connecting tree to non-tree vertex
3. Repeat until all vertices included

**Time Complexity**:
- Kruskal's: O(E log E)
- Prim's: O((V+E) log V) with min-heap

---

## Question 8: Hash Table with Chaining (2 marks)

**Year**: 2020 | **Topic**: Hashing | **Difficulty**: Medium

### Problem Statement
In a hash table with chaining, if load factor α = 2, what is the average search time?

### Solution
**Answer**: **Θ(1 + α) = Θ(3)**

**Explanation**:
- Load factor α = n/m (elements per slot)
- Average chain length = α
- Search time = O(1) hash + O(α) chain traversal
- For α = 2: **O(1 + 2) = O(3) = Θ(1)**

**Note**: With good hash function, still constant time!

---

## Question 9: Graph Connectivity (1 mark)

**Year**: 2020 | **Topic**: Graphs | **Difficulty**: Easy

### Problem Statement
Minimum number of edges required to make a graph with n vertices connected?

### Solution
**Answer**: **n - 1 edges**

**Explanation**:
- Connected graph: Path exists between any two vertices
- Minimum edges = Tree structure
- Tree with n vertices has exactly **n-1 edges**

**Example**:
- 4 vertices need minimum 3 edges
- Forms a tree (connected, acyclic)

---

## Question 10: Stack Operations (1 mark)

**Year**: 2020 | **Topic**: Stack | **Difficulty**: Easy

### Problem Statement
Given a sequence of push and pop operations, is the output sequence valid?

### Solution Approach
**Validation Rules**:
1. Can't pop from empty stack
2. Pop returns most recently pushed element (LIFO)
3. Number of pops ≤ number of pushes at any point

**Example**:
- Input: 1, 2, 3, 4
- Valid output: 1, 2, 3, 4 (push all, pop all)
- Valid output: 2, 1, 4, 3 (push 1,2, pop 2,1, push 3,4, pop 4,3)
- Invalid: 4, 3, 2, 1 then push 1 (can't pop 4 first)

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Trees (BST/AVL) | 3 | 6 |
| Graphs | 2 | 4 |
| Linked List | 1 | 2 |
| Heap | 1 | 1 |
| Hashing | 1 | 2 |
| Complexity | 1 | 2 |
| Stack | 1 | 1 |
| **Total** | **10** | **18** |

---

## Key Takeaways

1. **AVL trees** and **balanced BST** operations
2. **MST algorithms** (Kruskal's/Prim's)
3. **Recurrence relations** solving
4. **Range queries** in BST
5. **Load factor** in hashing

## Practice Focus
- AVL tree rotations and insertions
- BST construction from traversals
- Solve complex recurrences
- MST algorithms implementation
- Hash table analysis
