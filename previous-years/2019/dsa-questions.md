# GATE 2019 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~9 questions  
> **Total Marks**: ~16 marks  
> **Difficulty**: Mixed

---

## Question 1: B+ Tree Properties (2 marks)

**Year**: 2019 | **Topic**: B+ Trees | **Difficulty**: Medium

### Problem Statement
Which statement is NOT correct about B+ tree data structure?

**Options**:
- (A) Key values in each node are kept in sorted order
- (B) Each leaf node has a pointer to the next leaf node
- (C) B+ tree is a height-balanced tree
- (D) Non-leaf nodes have pointers to data records

### Solution
**Answer**: (D) Non-leaf nodes have pointers to data records

**Explanation**:
- **(A) TRUE**: Keys are sorted in each node
- **(B) TRUE**: Leaf nodes form a linked list
- **(C) TRUE**: All leaves at same level (balanced)
- **(D) FALSE**: Only **leaf nodes** have data pointers, internal nodes only have keys and child pointers

**B+ Tree Properties**:
- All data in leaves
- Internal nodes for navigation only
- Efficient range queries

---

## Question 2: Stack with findMin() (2 marks)

**Year**: 2019 | **Topic**: Stack | **Difficulty**: Medium

### Problem Statement
Enhance a stack to support `findMin()` in O(1) time without increasing PUSH/POP complexity. Which approach works?

**Options**:
- (A) Keep pointer to min with each record
- (B) Keep single pointer to minimum
- (C) Keep sorted auxiliary array
- (D) Keep min-heap

### Solution
**Answer**: (A) Keep pointer to min with each record

**Explanation**:
- **Approach A**: Each node stores pointer to current minimum
  - PUSH: O(1) - compare with previous min
  - POP: O(1) - just pop
  - findMin: O(1) - check top's min pointer

**Implementation**:
```c
struct StackNode {
    int data;
    int min;  // Minimum so far
    struct StackNode* next;
};

void push(int x) {
    StackNode* node = new StackNode();
    node->data = x;
    node->min = (stack empty) ? x : min(x, top->min);
    node->next = top;
    top = node;
}

int findMin() {
    return top->min;
}
```

**Why others fail**:
- (B): Need to recalculate on POP
- (C): Maintaining sorted array is O(n)
- (D): Heap operations are O(log n)

---

## Question 3: Cache Memory (2 marks)

**Year**: 2019 | **Topic**: Computer Organization (relevant to DSA) | **Difficulty**: Hard

### Problem Statement
Fully associative cache: 16 KB size, 16-byte blocks, 32-bit address. How many bits for Tag and Index?

### Solution
**Answer**: Tag = 28 bits, Index = 0 bits

**Calculation**:
- Cache size = 16 KB = 2^14 bytes
- Block size = 16 bytes = 2^4 bytes
- Number of blocks = 2^14 / 2^4 = 2^10 = 1024

**Address breakdown**:
- Total bits = 32
- Block offset = log₂(16) = 4 bits
- **Fully associative** = no index (any block can go anywhere)
- Tag = 32 - 4 - 0 = **28 bits**
- Index = **0 bits**

---

## Question 4: Graph Coloring (2 marks)

**Year**: 2019 | **Topic**: Graphs | **Difficulty**: Medium

### Problem Statement
What is the chromatic number of a complete graph K_n?

### Solution
**Answer**: **n**

**Explanation**:
- Complete graph K_n: Every vertex connected to every other
- No two vertices can have same color
- Need n different colors

**Examples**:
- K_3 (triangle): 3 colors
- K_4: 4 colors
- K_5: 5 colors

**Chromatic number**: Minimum colors needed for proper vertex coloring

---

## Question 5: Binary Search Tree Deletion (2 marks)

**Year**: 2019 | **Topic**: BST | **Difficulty**: Medium

### Problem Statement
In a BST, after deleting a node with two children, which node replaces it?

**Options**:
- (A) Inorder predecessor
- (B) Inorder successor
- (C) Either A or B
- (D) Neither

### Solution
**Answer**: (C) Either inorder predecessor or successor

**Explanation**:
Both maintain BST property:

**Inorder Successor**:
- Smallest node in right subtree
- Leftmost node of right child

**Inorder Predecessor**:
- Largest node in left subtree
- Rightmost node of left child

**Code (using successor)**:
```c
Node* deleteNode(Node* root, int key) {
    if (root == NULL) return NULL;
    
    if (key < root->data)
        root->left = deleteNode(root->left, key);
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
    else {
        // Node with two children
        if (root->left && root->right) {
            Node* successor = findMin(root->right);
            root->data = successor->data;
            root->right = deleteNode(root->right, successor->data);
        }
        // ... handle other cases
    }
    return root;
}
```

---

## Question 6: Sorting Algorithm Selection (1 mark)

**Year**: 2019 | **Topic**: Sorting | **Difficulty**: Easy

### Problem Statement
Which sorting algorithm is best for nearly sorted array?

### Solution
**Answer**: **Insertion Sort**

**Explanation**:
- **Best case**: O(n) when array is already sorted
- Works well with nearly sorted data
- Adaptive algorithm

**Comparison**:
| Algorithm | Nearly Sorted |
|-----------|---------------|
| Insertion Sort | O(n) |
| Bubble Sort | O(n) |
| Quick Sort | O(n log n) |
| Merge Sort | O(n log n) |

---

## Question 7: Linked List Cycle Detection (2 marks)

**Year**: 2019 | **Topic**: Linked List | **Difficulty**: Medium

### Problem Statement
Floyd's cycle detection algorithm uses two pointers (slow and fast). If there's a cycle, where do they meet?

### Solution
**Answer**: **Somewhere inside the cycle** (not necessarily at the start)

**Algorithm**:
```c
bool hasCycle(Node* head) {
    Node *slow = head, *fast = head;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        
        if (slow == fast)
            return true;  // Cycle detected
    }
    return false;
}
```

**To find cycle start**:
1. After meeting, reset one pointer to head
2. Move both one step at a time
3. They meet at cycle start

**Time**: O(n), **Space**: O(1)

---

## Question 8: Heap Sort (1 mark)

**Year**: 2019 | **Topic**: Sorting, Heap | **Difficulty**: Easy

### Problem Statement
What is the space complexity of Heap Sort?

### Solution
**Answer**: **O(1)** (in-place sorting)

**Explanation**:
- Heap Sort sorts in-place
- No extra array needed
- Only constant extra space for variables

**Time Complexity**: O(n log n) in all cases

**Comparison**:
- Merge Sort: O(n) space
- Quick Sort: O(log n) space (recursion stack)
- Heap Sort: O(1) space ✓

---

## Question 9: Dynamic Programming - Matrix Chain (2 marks)

**Year**: 2019 | **Topic**: Dynamic Programming | **Difficulty**: Medium

### Problem Statement
For matrix chain multiplication with n matrices, what is the time complexity of the DP solution?

### Solution
**Answer**: **O(n³)**

**Explanation**:
- **States**: dp[i][j] = min cost to multiply matrices i to j
- **Number of states**: O(n²)
- **Transitions**: Try all k between i and j = O(n)
- **Total**: O(n²) × O(n) = **O(n³)**

**Recurrence**:
```
dp[i][j] = min(dp[i][k] + dp[k+1][j] + cost(i,k,j))
           for all k from i to j-1
```

**Space**: O(n²)

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Trees (B+, BST) | 2 | 4 |
| Stack | 1 | 2 |
| Graphs | 1 | 2 |
| Sorting | 2 | 2 |
| Linked List | 1 | 2 |
| Dynamic Programming | 1 | 2 |
| Cache/Memory | 1 | 2 |
| **Total** | **9** | **16** |

---

## Key Takeaways

1. **B+ Trees** - Only leaves have data
2. **Stack enhancement** - Augment with extra info
3. **Fully associative cache** - No index field
4. **BST deletion** - Two valid approaches
5. **Floyd's algorithm** - Cycle detection in O(1) space

## Practice Focus
- B+ tree operations and properties
- Stack/queue enhancements
- Graph coloring problems
- BST deletion cases
- Floyd's cycle detection
- Matrix chain DP
