# Dynamic Programming

## 📌 Topic Overview

Dynamic Programming (DP) is one of the **MOST IMPORTANT** topics for GATE with **VERY HIGH** weightage. Mastering DP is crucial for a good score.

## 🎯 Key Concepts

### Core Principles
- **Optimal Substructure**: Solution can be constructed from optimal solutions of subproblems
- **Overlapping Subproblems**: Same subproblems are solved multiple times
- **Memoization**: Top-down approach with caching
- **Tabulation**: Bottom-up approach with table filling

### Problem Types
1. **Linear DP**: Fibonacci, Climbing Stairs, House Robber
2. **2D DP**: Longest Common Subsequence, Edit Distance, Matrix Chain Multiplication
3. **Knapsack Problems**: 0/1 Knapsack, Unbounded Knapsack, Subset Sum
4. **String DP**: LCS, LIS, Edit Distance, Palindrome Partitioning
5. **Tree DP**: Diameter, Maximum Path Sum
6. **State Machine DP**: Stock Buy/Sell problems

## 💡 DP Patterns

### 1. Fibonacci Pattern
```
dp[i] = dp[i-1] + dp[i-2]
```
Examples: Climbing Stairs, Fibonacci

### 2. 0/1 Knapsack Pattern
```
dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w-weight[i]])
```
Examples: Subset Sum, Partition Equal Subset Sum

### 3. Unbounded Knapsack Pattern
```
dp[i][w] = max(dp[i-1][w], value[i] + dp[i][w-weight[i]])
```
Examples: Coin Change, Rod Cutting

### 4. LCS Pattern
```
dp[i][j] = dp[i-1][j-1] + 1  (if match)
         = max(dp[i-1][j], dp[i][j-1])  (if no match)
```
Examples: LCS, Edit Distance, Shortest Common Supersequence

## 📊 Complexity Analysis

| Problem Type | Time | Space |
|--------------|------|-------|
| 1D DP | O(n) | O(n) or O(1) |
| 2D DP | O(n²) | O(n²) or O(n) |
| Matrix Chain | O(n³) | O(n²) |
| Knapsack | O(n×W) | O(n×W) or O(W) |

## 🔥 GATE Must-Know Problems

### Classic Problems (100% Must Practice)
- [ ] Longest Common Subsequence (LCS)
- [ ] Longest Increasing Subsequence (LIS)
- [ ] 0/1 Knapsack
- [ ] Matrix Chain Multiplication
- [ ] Edit Distance
- [ ] Coin Change
- [ ] Rod Cutting
- [ ] Subset Sum
- [ ] Partition Problem
- [ ] Egg Dropping

### Important Problems
- [ ] Longest Palindromic Subsequence
- [ ] Palindrome Partitioning
- [ ] Word Break
- [ ] Climbing Stairs
- [ ] House Robber
- [ ] Maximum Subarray Sum (Kadane's)
- [ ] Minimum Path Sum
- [ ] Unique Paths

## 📝 Practice Strategy

### Week 1: Foundation
- Understand memoization vs tabulation
- Solve Fibonacci, Climbing Stairs
- Practice 1D DP problems

### Week 2: Knapsack Family
- 0/1 Knapsack and variations
- Subset Sum, Partition
- Unbounded Knapsack, Coin Change

### Week 3: String DP
- LCS and variations
- LIS and variations
- Edit Distance

### Week 4: Advanced DP
- Matrix Chain Multiplication
- Tree DP
- Previous year GATE questions

## 🎓 Problem-Solving Approach

1. **Identify DP**: Check for optimal substructure and overlapping subproblems
2. **Define State**: What does dp[i] or dp[i][j] represent?
3. **Find Recurrence**: How to compute dp[i] from previous states?
4. **Base Cases**: What are the initial values?
5. **Order of Computation**: Bottom-up or top-down?
6. **Space Optimization**: Can we reduce space from 2D to 1D?

## 💡 Common Mistakes to Avoid

- Not identifying the state correctly
- Missing base cases
- Wrong order of iteration in tabulation
- Not considering space optimization
- Forgetting to handle edge cases

## 🎯 GATE Previous Year Patterns

- **Complexity Analysis**: Given DP code, find time/space complexity
- **Recurrence Relations**: Convert recurrence to DP solution
- **Problem Identification**: Identify if DP is applicable
- **Code Analysis**: Find output of given DP code
- **Optimization**: Choose optimal approach among alternatives

## 📚 Resources

- CLRS Chapter 15 (Dynamic Programming)
- GeeksforGeeks DP section
- GATE Overflow DP tagged questions
- Aditya Verma DP playlist (YouTube)

---

**Difficulty Distribution**: Easy: 20% | Medium: 50% | Hard: 30%  
**Expected Questions in GATE**: 2-3 questions (4-6 marks)
