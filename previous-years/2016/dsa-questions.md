# GATE 2016 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~9 questions  
> **Total Marks**: ~14 marks  
> **Difficulty**: Mixed

---

## Question 1: Queue and Stack Operations (2 marks)

**Year**: 2016 Set 1 | **Topic**: Queue, Stack | **Difficulty**: Medium

### Problem Statement
A queue is implemented using two stacks S1 and S2. The operations are defined as follows:

```c
enqueue(x):
    push x to S1

dequeue():
    if S2 is empty:
        while S1 is not empty:
            pop from S1 and push to S2
    pop from S2
```

What is the maximum number of iterations of the while loop in a sequence of n enqueue and dequeue operations?

### Solution
**Answer**: **n**

**Explanation**:
- Each element is moved from S1 to S2 at most once
- In worst case, all n elements are in S1 when dequeue is called
- The while loop runs n times to move all elements
- Subsequent dequeues don't need the loop until S2 is empty

**Amortized Time**: O(1) per operation

---

## Question 2: Sorting Algorithms Complexity (2 marks)

**Year**: 2016 | **Topic**: Sorting | **Difficulty**: Easy

### Problem Statement
What are the worst-case running times of Insertion Sort, Merge Sort, and Quicksort?

### Solution

| Algorithm | Worst Case | Best Case | Average Case |
|-----------|------------|-----------|--------------|
| **Insertion Sort** | O(n²) | O(n) | O(n²) |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) |
| **Quicksort** | O(n²) | O(n log n) | O(n log n) |

**Key Points**:
- Merge Sort is always O(n log n)
- Quicksort worst case: when pivot is always min/max
- Insertion Sort best case: already sorted array

---

## Question 3: Minimum Spanning Tree (2 marks)

**Year**: 2016 | **Topic**: Graphs, MST | **Difficulty**: Medium

### Problem Statement
In a weighted undirected graph, which of the following properties must hold for a Minimum Spanning Tree?

**Options**:
- (A) The MST contains the edge with minimum weight
- (B) The MST may not contain the edge with minimum weight
- (C) All edges in MST have the same weight
- (D) MST is unique

### Solution
**Answer**: (A) The MST contains the edge with minimum weight

**Explanation**:
- The edge with minimum weight will always be in some MST
- **Proof**: If not included, adding it creates a cycle. Removing any other edge from the cycle gives a lighter spanning tree (contradiction)
- MST may not be unique (if multiple edges have same weight)

**Cut Property**: Minimum weight edge crossing any cut is in some MST

---

## Question 4: Graph Adjacency List (2 marks)

**Year**: 2016 Set 2 | **Topic**: Graphs | **Difficulty**: Medium

### Problem Statement
In an undirected graph represented using adjacency lists, if we maintain "twin pointers" (each edge (u,v) has two entries: one in u's list pointing to v, and one in v's list pointing to u), what is the advantage?

### Solution
**Answer**: **O(1) edge deletion**

**Explanation**:
- With twin pointers, each adjacency list node points to its twin
- To delete edge (u,v):
  1. Find the entry in u's list (may take O(degree(u)))
  2. Use twin pointer to find entry in v's list in O(1)
  3. Delete both in O(1)

**Without twin pointers**: Need to search both lists = O(degree(u) + degree(v))

---

## Question 5: Heap Operations (2 marks)

**Year**: 2016 | **Topic**: Heap | **Difficulty**: Easy

### Problem Statement
In a max-heap with n elements, what is the time complexity to find the kth largest element?

### Solution
**Answer**: **O(k log k)** using modified heap approach

**Naive Approach**: O(k log n)
- Extract max k times
- Each extraction: O(log n)

**Optimized Approach**: O(k log k)
- Use auxiliary max-heap
- Start with root of original heap
- Extract max from auxiliary heap
- Add children of extracted element
- Repeat k times

---

## Question 6: Binary Search Tree (1 mark)

**Year**: 2016 | **Topic**: BST | **Difficulty**: Easy

### Problem Statement
How many distinct BSTs can be formed with keys 1, 2, 3?

### Solution
**Answer**: **5 BSTs**

**Formula**: Catalan number C(n) = (2n)! / ((n+1)! × n!)

For n=3: C(3) = 6!/(4! × 3!) = 720/(24 × 6) = **5**

**The 5 BSTs**:
```
  1        1        2        3      3
   \        \      / \      /      /
    2        3    1   3    1      2
     \      /              \     /
      3    2                2   1
```

---

## Question 7: Time Complexity Analysis (2 marks)

**Year**: 2016 | **Topic**: Complexity | **Difficulty**: Medium

### Problem Statement
What is the time complexity of the following code?

```c
int count = 0;
for (int i = n; i > 0; i /= 2) {
    for (int j = 0; j < i; j++) {
        count++;
    }
}
```

### Solution
**Analysis**:
- Outer loop: i = n, n/2, n/4, ..., 1 (log n iterations)
- Inner loop iterations: n + n/2 + n/4 + ... + 1

Sum = n(1 + 1/2 + 1/4 + ...) = n × 2 = **2n**

**Answer**: **O(n)**

---

## Question 8: Linked List Operations (1 mark)

**Year**: 2016 | **Topic**: Linked List | **Difficulty**: Easy

### Problem Statement
In a singly linked list, what is the time complexity to delete a node given only a pointer to that node (not the head)?

### Solution
**Answer**: **O(1)** (with caveat)

**Approach**:
```c
void deleteNode(Node* node) {
    if (node->next == NULL) return; // Can't delete last node
    
    // Copy next node's data
    node->data = node->next->data;
    
    // Delete next node
    Node* temp = node->next;
    node->next = temp->next;
    free(temp);
}
```

**Limitation**: Cannot delete last node this way

---

## Question 9: Hashing with Chaining (1 mark)

**Year**: 2016 | **Topic**: Hashing | **Difficulty**: Easy

### Problem Statement
In a hash table with m slots and n elements using chaining, what is the expected length of the longest chain?

### Solution
**Answer**: **Θ(log n / log log n)** with high probability

**Average chain length**: α = n/m

**For uniform hashing**:
- Expected max chain length ≈ log n / log log n
- This assumes simple uniform hashing

**Practical**: Usually α is kept < 1 for good performance

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Graphs | 2 | 4 |
| Sorting | 1 | 2 |
| Heap | 1 | 2 |
| Queue/Stack | 1 | 2 |
| BST | 1 | 1 |
| Complexity | 1 | 2 |
| Linked List | 1 | 1 |
| Hashing | 1 | 1 |
| **Total** | **9** | **15** |

---

## Key Takeaways

1. **Queue using two stacks** - Important pattern
2. **MST properties** - Cut property and minimum edge
3. **Sorting complexities** - Know all cases
4. **Graph representations** - Adjacency list optimizations
5. **Catalan numbers** - For counting BSTs

## Practice Focus
- Implement queue using stacks
- MST algorithms and properties
- Sorting algorithm analysis
- Graph representation trade-offs
- BST counting problems
