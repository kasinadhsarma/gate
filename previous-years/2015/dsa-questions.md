# GATE 2015 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~10 questions  
> **Total Marks**: ~15 marks  
> **Difficulty**: Mixed

---

## Question 1: Data Structure for Best Asymptotic Complexity (2 marks)

**Year**: 2015 Set 1 | **Topic**: Data Structures Comparison | **Difficulty**: Medium

### Problem Statement
Which data structure is most suited to achieve the best total asymptotic complexity considering all operations: Find, Insert, Delete, and Decrease Key?

**Options**:
- (A) Unsorted array
- (B) Min-heap
- (C) Sorted array
- (D) Sorted doubly linked list

### Solution
**Answer**: (A) Unsorted array

**Explanation**:
- **Unsorted Array**:
  - Find: O(n)
  - Insert: O(1) - add at end
  - Delete: O(1) - swap with last element and remove
  - Decrease Key: O(1) - if pointer given
  
- **Min-Heap**:
  - Find: O(n) - need to search
  - Insert: O(log n)
  - Delete: O(log n)
  - Decrease Key: O(log n)

- **Sorted Array**:
  - Find: O(log n) - binary search
  - Insert: O(n) - need to shift elements
  - Delete: O(n) - need to shift elements
  - Decrease Key: O(n)

For best **total** complexity with all operations, unsorted array wins.

---

## Question 2: Max Heap Insertion (2 marks)

**Year**: 2015 Set 1 | **Topic**: Heap | **Difficulty**: Easy

### Problem Statement
Consider a max heap represented by array: `40, 30, 20, 10, 15, 16, 17, 8, 4`

After inserting 35, what is the new heap?

### Solution
**Answer**: `40, 35, 20, 10, 30, 16, 17, 8, 4, 15`

**Step-by-step**:
1. Insert 35 at end: `40, 30, 20, 10, 15, 16, 17, 8, 4, 35`
2. Compare with parent (index 4, value 15): 35 > 15, swap
3. New array: `40, 30, 20, 10, 35, 16, 17, 8, 4, 15`
4. Compare with parent (index 1, value 30): 35 > 30, swap
5. Final: `40, 35, 20, 10, 30, 16, 17, 8, 4, 15`

**Time Complexity**: O(log n)

---

## Question 3: Binary Tree Height (2 marks)

**Year**: 2015 Set 1 | **Topic**: Trees | **Difficulty**: Easy

### Problem Statement
The height of a tree is the length of the longest root-to-leaf path. What are the maximum and minimum number of nodes in a binary tree of height 5?

### Solution
**Maximum nodes**: 2^(h+1) - 1 = 2^6 - 1 = **63 nodes**

**Minimum nodes**: h + 1 = 5 + 1 = **6 nodes** (skewed tree)

**Formulas**:
- Max nodes at level L = 2^L
- Max nodes in tree of height H = 2^(H+1) - 1
- Min nodes in tree of height H = H + 1

---

## Question 4: BST Operations Complexity (1 mark)

**Year**: 2015 Set 1 | **Topic**: BST | **Difficulty**: Easy

### Problem Statement
What are the worst-case complexities of insertion and deletion in a Binary Search Tree?

**Options**:
- (A) Θ(log n) for both
- (B) Θ(n) for both
- (C) Θ(n) for insertion, Θ(log n) for deletion
- (D) Θ(log n) for insertion, Θ(n) for deletion

### Solution
**Answer**: (B) Θ(n) for both

**Explanation**:
In the worst case, BST becomes skewed (like a linked list).
- Insertion: Need to traverse to leaf = O(n)
- Deletion: Need to find node + rearrange = O(n)

For **balanced** BST (like AVL): Both are O(log n)

---

## Question 5: Hash Table Load Factor (1 mark)

**Year**: 2015 Set 3 | **Topic**: Hashing | **Difficulty**: Easy

### Problem Statement
A hash table T has 25 slots and stores 2000 elements. What is the load factor α?

### Solution
**Answer**: α = 2000 / 25 = **80**

**Load Factor Formula**: α = n / m
- n = number of elements
- m = number of slots

**Note**: Load factor > 1 indicates chaining is used (multiple elements per slot).

---

## Question 6: Building Max-Heap (2 marks)

**Year**: 2015 Set 3 | **Topic**: Heap | **Difficulty**: Medium

### Problem Statement
Given array: `〈89, 19, 50, 17, 12, 15, 2, 5, 7, 11, 6, 9, 100〉`

What is the minimum number of interchanges needed to convert it into a max-heap?

### Solution
**Answer**: **4 interchanges**

**Process** (Build heap using heapify):
1. Start from last non-leaf node: index = ⌊n/2⌋ - 1 = 5
2. Heapify from index 5 to 0
3. Count swaps during heapification

**Time Complexity**: O(n) for building heap

---

## Question 7: Merge Sort Scaling (2 marks)

**Year**: 2015 Set 3 | **Topic**: Sorting, Complexity | **Difficulty**: Medium

### Problem Statement
Merge sort takes 30 seconds for input size 64 in worst case. What is the maximum input size that can be solved in 6 minutes (360 seconds)?

### Solution
**Answer**: **512**

**Calculation**:
- Merge sort: T(n) = O(n log n)
- T(64) = 64 × log₂(64) = 64 × 6 = 384 units = 30 sec
- 1 unit = 30/384 sec
- For 360 sec: 360 × 384/30 = 4608 units
- n × log₂(n) = 4608
- Trying n = 512: 512 × 9 = 4608 ✓

---

## Question 8: Binary Tree with 20 Leaves (1 mark)

**Year**: 2015 Set 2 | **Topic**: Trees | **Difficulty**: Easy

### Problem Statement
A binary tree T has 20 leaves. How many nodes in T have exactly two children?

### Solution
**Answer**: **19 nodes**

**Formula**: For binary tree,
- L = number of leaves
- I₂ = number of nodes with 2 children
- **L = I₂ + 1**

Therefore: I₂ = L - 1 = 20 - 1 = **19**

---

## Question 9: Complete Binary Tree to Heap (2 marks)

**Year**: 2015 Set 2 | **Topic**: Heap | **Difficulty**: Medium

### Problem Statement
Consider a complete binary tree where left and right subtrees of root are max-heaps. What is the lower bound for operations to convert the tree to a heap?

**Options**:
- (A) Ω(log n)
- (B) Ω(n)
- (C) Ω(n log n)
- (D) Ω(n²)

### Solution
**Answer**: (A) Ω(log n)

**Explanation**:
- Only root might violate heap property
- Need to heapify down from root
- Height of tree = log n
- Heapify operation = O(log n)

---

## Question 10: Finding Neither Max nor Min (1 mark)

**Year**: 2015 Set 2 | **Topic**: Arrays, Searching | **Difficulty**: Easy

### Problem Statement
An unordered list has n distinct elements. How many comparisons to find an element that is neither maximum nor minimum?

**Options**:
- (A) Θ(n log n)
- (B) Θ(n)
- (C) Θ(log n)
- (D) Θ(1)

### Solution
**Answer**: (D) Θ(1)

**Explanation**:
- Pick any 3 elements
- Compare them (2 comparisons)
- The middle one is neither max nor min
- **Constant time!**

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Heap | 3 | 6 |
| Trees | 3 | 4 |
| BST | 1 | 1 |
| Hashing | 1 | 1 |
| Sorting | 1 | 2 |
| Arrays | 1 | 1 |
| **Total** | **10** | **15** |

---

## Key Takeaways

1. **Heap operations** were heavily tested
2. **Tree properties** and formulas are important
3. **Complexity analysis** appears frequently
4. **Practical problem-solving** over theory

## Practice Focus
- Build and manipulate heaps
- Tree traversals and properties
- Time complexity analysis
- Data structure comparisons
