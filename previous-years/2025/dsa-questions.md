# GATE 2025 - Data Structures & Algorithms Questions

> **Total DSA Questions**: ~8 questions  
> **Total Marks**: ~18 marks  
> **Difficulty**: Mixed

---

## Question 1: Binary Tree Properties (2 marks)

**Year**: 2025 | **Topic**: Trees | **Difficulty**: Medium

### Problem Statement
A complete binary tree has 31 nodes. What is its height?

### Solution
**Answer**: **4**

**Formula**: For complete binary tree with n nodes:
- Height h = ⌊log₂(n)⌋
- For n = 31: h = ⌊log₂(31)⌋ = ⌊4.95⌋ = **4**

**Verification**: 
- Max nodes at height 4 = 2^5 - 1 = 31 ✓

---

## Question 2: Hashing with Chaining (3 marks)

**Year**: 2025 | **Topic**: Hashing | **Difficulty**: Hard

### Problem Statement
Hash table with m = 10 slots, n = 100 elements using chaining. What is the expected length of the longest chain?

### Solution
**Answer**: **Θ(log n / log log n)** with high probability

**Load factor**: α = n/m = 100/10 = 10

**Expected max chain length**:
- With uniform hashing: Θ(log n / log log n)
- For n = 100: ≈ log(100) / log(log(100)) ≈ 6.64 / 1.53 ≈ **4-5**

**Average chain length**: α = 10

---

## Question 3: Time Complexity Analysis (2 marks)

**Year**: 2025 | **Topic**: Complexity | **Difficulty**: Medium

### Problem Statement
```c
for (int i = 1; i <= n; i++) {
    for (int j = i; j <= n; j += i) {
        count++;
    }
}
```

What is the time complexity?

### Solution
**Answer**: **O(n log n)**

**Analysis**:
- For i=1: n iterations
- For i=2: n/2 iterations
- For i=3: n/3 iterations
- ...
- For i=n: 1 iteration

Total = n(1 + 1/2 + 1/3 + ... + 1/n) = n × H(n) ≈ **n log n**

(H(n) is harmonic series ≈ log n)

---

## Question 4: Graph Shortest Path (3 marks)

**Year**: 2025 | **Topic**: Graphs | **Difficulty**: Hard

### Problem Statement
In a graph with negative edge weights but no negative cycles, which algorithm finds shortest paths correctly?

**Options**: (A) Dijkstra (B) Bellman-Ford (C) Floyd-Warshall (D) B and C

### Solution
**Answer**: (D) Both Bellman-Ford and Floyd-Warshall

**Explanation**:
- **Dijkstra**: ✗ Fails with negative weights
- **Bellman-Ford**: ✓ Works, detects negative cycles
- **Floyd-Warshall**: ✓ Works for all pairs

**Time Complexity**:
- Bellman-Ford: O(VE)
- Floyd-Warshall: O(V³)

---

## Question 5: Recursion and Memoization (2 marks)

**Year**: 2025 | **Topic**: DP, Recursion | **Difficulty**: Medium

### Problem Statement
Fibonacci with memoization has what time and space complexity?

### Solution
**Answer**: Time = O(n), Space = O(n)

**Without memoization**: O(2^n)

**With memoization**:
```c
int fib(int n, int memo[]) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n];
}
```

- Each subproblem solved once: O(n) time
- Store n values: O(n) space

---

## Question 6: Sorting Lower Bound (2 marks)

**Year**: 2025 | **Topic**: Sorting | **Difficulty**: Medium

### Problem Statement
What is the lower bound for comparison-based sorting?

### Solution
**Answer**: **Ω(n log n)**

**Proof** (Decision tree):
- n! possible permutations
- Decision tree has n! leaves
- Height h ≥ log₂(n!)
- log₂(n!) = Θ(n log n) (Stirling's approximation)

**Algorithms achieving this**:
- Merge Sort
- Heap Sort
- Optimal Quick Sort

---

## Question 7: Stack with getMin() (2 marks)

**Year**: 2025 | **Topic**: Stack | **Difficulty**: Medium

### Problem Statement
Design a stack supporting push, pop, and getMin() all in O(1) time.

### Solution
**Approach**: Use auxiliary stack

```c
struct MinStack {
    stack<int> mainStack;
    stack<int> minStack;
    
    void push(int x) {
        mainStack.push(x);
        if (minStack.empty() || x <= minStack.top())
            minStack.push(x);
    }
    
    void pop() {
        if (mainStack.top() == minStack.top())
            minStack.pop();
        mainStack.pop();
    }
    
    int getMin() {
        return minStack.top();
    }
};
```

**All operations**: O(1)  
**Space**: O(n) worst case

---

## Question 8: Binary Search Variations (2 marks)

**Year**: 2025 | **Topic**: Searching | **Difficulty**: Medium

### Problem Statement
In a rotated sorted array, what is the time complexity to find an element?

### Solution
**Answer**: **O(log n)**

**Algorithm**:
1. Find rotation point using binary search: O(log n)
2. Determine which half to search
3. Binary search in that half: O(log n)

**Example**: [4,5,6,7,0,1,2], find 0
- Rotation point at index 4
- Search in right half

**Total**: O(log n)

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Trees | 1 | 2 |
| Hashing | 1 | 3 |
| Complexity | 1 | 2 |
| Graphs | 1 | 3 |
| DP/Recursion | 1 | 2 |
| Sorting | 1 | 2 |
| Stack | 1 | 2 |
| Searching | 1 | 2 |
| **Total** | **8** | **18** |

---

## Key Takeaways

1. **Complete binary tree** height = ⌊log₂(n)⌋
2. **Harmonic series** ≈ log n (important for complexity)
3. **Negative weights** → Use Bellman-Ford or Floyd-Warshall
4. **Memoization** reduces exponential to linear
5. **Sorting lower bound** = Ω(n log n) for comparisons

## Practice Focus
- Tree height calculations
- Harmonic series in complexity
- Graph algorithms with negative weights
- Memoization techniques
- Stack enhancements
- Binary search variations
