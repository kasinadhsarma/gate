# GATE 2023 - Data Structures & Algorithms Questions

> **Total DSA Questions**: 8 questions  
> **Total Marks**: 17 marks  
> **Difficulty**: Mixed (Easy: 2, Medium: 4, Hard: 2)

---

## Question 1: Array - Maximum Subarray Sum (2 marks)

**Year**: 2023 | **Topic**: Arrays, Kadane's Algorithm | **Difficulty**: Medium

### Problem Statement
Given an array of integers, find the contiguous subarray which has the largest sum.

```
Input: arr[] = {-2, -3, 4, -1, -2, 1, 5, -3}
Output: 7
Explanation: Subarray {4, -1, -2, 1, 5} has maximum sum = 7
```

### Solution Approach
Use Kadane's Algorithm:
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

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

**Key Concept**: Dynamic Programming - maintain maximum sum ending at current position

---

## Question 2: Binary Search Tree - Inorder Successor (2 marks)

**Year**: 2023 | **Topic**: Trees, BST | **Difficulty**: Medium

### Problem Statement
Find the inorder successor of a given node in a Binary Search Tree.

### Solution Approach
1. If node has right subtree: successor is leftmost node in right subtree
2. If no right subtree: successor is the nearest ancestor for which node is in left subtree

```c
TreeNode* findSuccessor(TreeNode* root, TreeNode* node) {
    // Case 1: Node has right subtree
    if (node->right != NULL) {
        TreeNode* temp = node->right;
        while (temp->left != NULL)
            temp = temp->left;
        return temp;
    }
    
    // Case 2: No right subtree
    TreeNode* successor = NULL;
    while (root != NULL) {
        if (node->data < root->data) {
            successor = root;
            root = root->left;
        } else if (node->data > root->data) {
            root = root->right;
        } else {
            break;
        }
    }
    return successor;
}
```

**Time Complexity**: O(h) where h is height  
**Space Complexity**: O(1)

---

## Question 3: Graph - Dijkstra's Algorithm (3 marks)

**Year**: 2023 | **Topic**: Graphs, Shortest Path | **Difficulty**: Hard

### Problem Statement
Given a weighted graph, find the shortest path from source to all other vertices using Dijkstra's algorithm. What is the time complexity with min-heap?

### Answer
**Time Complexity**: O((V + E) log V)

**Explanation**:
- Each vertex is extracted from min-heap once: O(V log V)
- Each edge is relaxed once: O(E log V)
- Total: O((V + E) log V)

**Key Points**:
- Works only for non-negative edge weights
- Greedy approach
- Uses priority queue (min-heap)

---

## Question 4: Dynamic Programming - LCS Length (2 marks)

**Year**: 2023 | **Topic**: DP, Strings | **Difficulty**: Medium

### Problem Statement
Find the length of Longest Common Subsequence of two strings.

```
X = "AGGTAB"
Y = "GXTXAYB"
Output: 4
Explanation: LCS is "GTAB"
```

### Solution
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

**Time Complexity**: O(m × n)  
**Space Complexity**: O(m × n) or O(min(m,n)) with optimization

---

## Question 5: Stack - Expression Evaluation (2 marks)

**Year**: 2023 | **Topic**: Stack | **Difficulty**: Easy

### Problem Statement
What is the postfix expression for: `A + B * C - D / E`?

### Answer
**Postfix**: `A B C * + D E / -`

**Conversion Steps**:
1. A + (B * C) - (D / E)
2. A (B C *) + (D E /) -
3. A B C * + D E / -

**Operator Precedence**: `* / > + -`

---

## Question 6: Hashing - Collision Resolution (2 marks)

**Year**: 2023 | **Topic**: Hashing | **Difficulty**: Easy

### Problem Statement
In a hash table of size 10, using hash function h(k) = k mod 10, insert keys: 12, 22, 32 using:
a) Linear Probing
b) Quadratic Probing

### Answer

**Linear Probing**:
- 12 → index 2
- 22 → index 2 (collision) → 3
- 32 → index 2 (collision) → 3 (collision) → 4

**Quadratic Probing** (h(k, i) = (h(k) + i²) mod 10):
- 12 → index 2
- 22 → index 2 (collision) → (2 + 1²) mod 10 = 3
- 32 → index 2 (collision) → (2 + 1²) mod 10 = 3 (collision) → (2 + 2²) mod 10 = 6

---

## Question 7: Complexity Analysis (2 marks)

**Year**: 2023 | **Topic**: Time Complexity | **Difficulty**: Medium

### Problem Statement
What is the time complexity of the following code?

```c
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j = j * 2) {
        printf("%d %d\n", i, j);
    }
}
```

### Answer
**Time Complexity**: O(n log n)

**Explanation**:
- Outer loop runs n times: O(n)
- Inner loop runs log n times (j doubles each time): O(log n)
- Total: O(n × log n) = O(n log n)

---

## Question 8: Graph - Minimum Spanning Tree (2 marks)

**Year**: 2023 | **Topic**: Graphs, MST | **Difficulty**: Hard

### Problem Statement
For a connected weighted graph with V vertices and E edges, what is the time complexity of Kruskal's algorithm?

### Answer
**Time Complexity**: O(E log E) or O(E log V)

**Explanation**:
1. Sort all edges: O(E log E)
2. Process each edge with Union-Find: O(E × α(V)) ≈ O(E)
3. Since E ≤ V², log E ≤ 2 log V, so O(E log E) = O(E log V)

**Key Points**:
- Uses Union-Find data structure
- Greedy approach
- Works on disconnected graphs too

---

## Summary Statistics

| Topic | Questions | Marks |
|-------|-----------|-------|
| Arrays | 1 | 2 |
| Trees | 1 | 2 |
| Graphs | 2 | 5 |
| DP | 1 | 2 |
| Stack | 1 | 2 |
| Hashing | 1 | 2 |
| Complexity | 1 | 2 |
| **Total** | **8** | **17** |

---

**Practice Tips**:
1. Focus on complexity analysis - appears in every GATE
2. Master graph algorithms (highest weightage)
3. Practice DP problems regularly
4. Understand data structure operations thoroughly
