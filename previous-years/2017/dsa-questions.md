# GATE 2017 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~9 questions  
> **Total Marks**: ~14 marks  
> **Difficulty**: Mixed

---

## Question 1: BFS Traversal Order (2 marks)

**Year**: 2017 | **Topic**: Graphs, BFS | **Difficulty**: Medium

### Problem Statement
Given a graph, which of the following is a possible BFS traversal order starting from a given vertex?

### Solution Approach
**BFS Properties**:
- Visit all neighbors at distance k before visiting nodes at distance k+1
- Uses queue (FIFO)
- Level-order traversal

**Steps to verify**:
1. Check if nodes are visited level by level
2. Ensure no node at level L+1 appears before all nodes at level L
3. Within same level, any order is valid

**Time Complexity**: O(V + E)  
**Space Complexity**: O(V) for queue

---

## Question 2: Recurrence Relation (2 marks)

**Year**: 2017 | **Topic**: Complexity Analysis | **Difficulty**: Hard

### Problem Statement
Solve the recurrence: T(n) = 2T(√n) + 1

### Solution
**Method**: Substitution

Let n = 2^m, then √n = 2^(m/2)

T(2^m) = 2T(2^(m/2)) + 1

Let S(m) = T(2^m):
- S(m) = 2S(m/2) + 1

Using Master Theorem:
- a = 2, b = 2, f(m) = 1
- log_b(a) = log₂(2) = 1
- f(m) = O(m^0) < O(m^1)
- **Case 1**: S(m) = Θ(m)

Therefore: T(n) = Θ(log n)

**Answer**: **Θ(log n)**

---

## Question 3: Time Complexity of C Function (2 marks)

**Year**: 2017 | **Topic**: Complexity Analysis | **Difficulty**: Medium

### Problem Statement
What is the time complexity of the following function?

```c
void function(int n) {
    int i, j;
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= i; j++) {
            printf("*");
        }
    }
}
```

### Solution
**Analysis**:
- Outer loop: i from 1 to n (n iterations)
- Inner loop: j from 1 to i (i iterations)

Total operations:
```
Σ(i=1 to n) i = 1 + 2 + 3 + ... + n
            = n(n+1)/2
            = O(n²)
```

**Answer**: **Θ(n²)**

---

## Question 4: Algorithm Time Complexity Matching (2 marks)

**Year**: 2017 | **Topic**: Algorithms | **Difficulty**: Easy

### Problem Statement
Match algorithms with their time complexities:

| Algorithm | Time Complexity |
|-----------|----------------|
| 1. Tower of Hanoi | A. O(log n) |
| 2. Binary Search | B. O(n log n) |
| 3. Heap Sort | C. O(2^n) |
| 4. Matrix Addition | D. O(n²) |

### Solution
**Correct Matching**:
- **Tower of Hanoi**: O(2^n) - C
  - Recurrence: T(n) = 2T(n-1) + 1
  
- **Binary Search**: O(log n) - A
  - Divide array in half each time
  
- **Heap Sort**: O(n log n) - B
  - Build heap O(n) + n deletions O(log n each)
  
- **Matrix Addition**: O(n²) - D
  - Add each element once

**Answer**: 1-C, 2-A, 3-B, 4-D

---

## Question 5: Circular Queue with Linked List (2 marks)

**Year**: 2017 | **Topic**: Queue, Linked List | **Difficulty**: Medium

### Problem Statement
For O(1) insertion and deletion in a circular queue using singly linked list, what pointers should be maintained?

**Options**:
- (A) Head pointer only
- (B) Tail pointer only
- (C) Both head and tail
- (D) Neither needed

### Solution
**Answer**: (B) Tail pointer only

**Explanation**:
In circular singly linked list:
- Tail->next points to head
- **Insert at front**: Insert after tail, O(1)
- **Delete from front**: Delete tail->next, O(1)
- Only tail pointer needed!

```c
// Insert
new_node->next = tail->next;
tail->next = new_node;

// Delete
temp = tail->next;
tail->next = temp->next;
free(temp);
```

---

## Question 6: Huffman Coding (3 marks)

**Year**: 2017 | **Topic**: Greedy, Trees | **Difficulty**: Medium

### Problem Statement
Given character frequencies, construct Huffman tree and find encoding.

**Characters**: A(5), B(9), C(12), D(13), E(16), F(45)

### Solution
**Steps**:
1. Create leaf nodes for each character
2. Build tree bottom-up:
   - Combine two smallest: A(5) + B(9) = 14
   - Next: AB(14) + C(12) = 26
   - Next: D(13) + E(16) = 29
   - Next: ABC(26) + DE(29) = 55
   - Final: ABCDE(55) + F(45) = 100

**Encoding** (example):
- F: 0
- D: 100
- E: 101
- C: 110
- A: 1110
- B: 1111

**Average code length** = Σ(frequency × code_length) / total_frequency

---

## Question 7: BST Preorder Traversal (2 marks)

**Year**: 2017 | **Topic**: BST, Tree Traversal | **Difficulty**: Easy

### Problem Statement
Given a BST with specific structure, what is the preorder traversal?

### Solution Approach
**Preorder**: Root → Left → Right

**BST Property**: Left < Root < Right

**Steps**:
1. Visit root
2. Recursively traverse left subtree
3. Recursively traverse right subtree

**Example**:
```
      50
     /  \
   30    70
  /  \   /  \
20  40 60  80
```

Preorder: **50, 30, 20, 40, 70, 60, 80**

---

## Question 8: Graph DFS Properties (1 mark)

**Year**: 2017 | **Topic**: Graphs, DFS | **Difficulty**: Easy

### Problem Statement
In DFS traversal of an undirected graph, which edges can exist?

**Options**:
- (A) Tree edges only
- (B) Tree and back edges
- (C) Tree, back, and cross edges
- (D) All types of edges

### Solution
**Answer**: (B) Tree and back edges

**Explanation**:
In **undirected** graph DFS:
- **Tree edges**: Part of DFS tree
- **Back edges**: Connect to ancestor
- **No forward edges**: Would be back edges from other direction
- **No cross edges**: Would create cycle

In **directed** graph: All 4 types possible

---

## Question 9: Sorting Algorithm Stability (1 mark)

**Year**: 2017 | **Topic**: Sorting | **Difficulty**: Easy

### Problem Statement
Which sorting algorithms are stable?

**Options**:
- (A) Quick Sort
- (B) Heap Sort
- (C) Merge Sort
- (D) Selection Sort

### Solution
**Answer**: (C) Merge Sort

**Stable Sorting Algorithms**:
- ✓ Bubble Sort
- ✓ Insertion Sort
- ✓ **Merge Sort**
- ✓ Counting Sort
- ✓ Radix Sort

**Unstable**:
- ✗ Quick Sort
- ✗ Heap Sort
- ✗ Selection Sort

**Stability**: Maintains relative order of equal elements

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Graphs | 2 | 3 |
| Complexity Analysis | 3 | 6 |
| Trees | 2 | 3 |
| Queue | 1 | 2 |
| Sorting | 1 | 1 |
| **Total** | **9** | **15** |

---

## Key Takeaways

1. **Recurrence relations** are critical
2. **Graph algorithms** (BFS/DFS) well-tested
3. **Complexity analysis** of code snippets
4. **Huffman coding** appeared (greedy algorithm)

## Practice Focus
- Master recurrence solving techniques
- Practice BFS/DFS traversals
- Analyze code complexity
- Understand Huffman encoding
