# Arrays & Strings - Notes

## Key Concepts Summary

### 1. Kadane's Algorithm (Maximum Subarray Sum)
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
**Time**: O(n) | **Space**: O(1)

---

### 2. Two Pointer Technique

**Pattern**: Used for sorted arrays or when we need to find pairs

```c
// Example: Find pair with given sum in sorted array
bool findPair(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return true;
        else if (sum < target) left++;
        else right--;
    }
    return false;
}
```
**Time**: O(n) | **Space**: O(1)

---

### 3. Sliding Window

**Pattern**: For subarray/substring problems with fixed or variable size

```c
// Example: Maximum sum of k consecutive elements
int maxSumK(int arr[], int n, int k) {
    int window_sum = 0, max_sum = 0;
    
    // First window
    for (int i = 0; i < k; i++)
        window_sum += arr[i];
    max_sum = window_sum;
    
    // Slide window
    for (int i = k; i < n; i++) {
        window_sum = window_sum - arr[i-k] + arr[i];
        max_sum = max(max_sum, window_sum);
    }
    return max_sum;
}
```
**Time**: O(n) | **Space**: O(1)

---

### 4. Prefix Sum

**Pattern**: For range sum queries

```c
// Preprocessing
void buildPrefixSum(int arr[], int prefix[], int n) {
    prefix[0] = arr[0];
    for (int i = 1; i < n; i++)
        prefix[i] = prefix[i-1] + arr[i];
}

// Query: sum from index l to r
int rangeSum(int prefix[], int l, int r) {
    if (l == 0) return prefix[r];
    return prefix[r] - prefix[l-1];
}
```
**Preprocessing**: O(n) | **Query**: O(1)

---

### 5. Dutch National Flag (3-Way Partitioning)

**Pattern**: Sort array with 3 distinct values

```c
void dutchFlag(int arr[], int n) {
    int low = 0, mid = 0, high = n - 1;
    
    while (mid <= high) {
        if (arr[mid] == 0) {
            swap(&arr[low], &arr[mid]);
            low++; mid++;
        }
        else if (arr[mid] == 1) {
            mid++;
        }
        else { // arr[mid] == 2
            swap(&arr[mid], &arr[high]);
            high--;
        }
    }
}
```
**Time**: O(n) | **Space**: O(1)

---

## Important String Algorithms

### 1. KMP Pattern Matching

```c
void computeLPS(char* pattern, int M, int* lps) {
    int len = 0;
    lps[0] = 0;
    int i = 1;
    
    while (i < M) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}

void KMP(char* text, char* pattern) {
    int N = strlen(text);
    int M = strlen(pattern);
    int lps[M];
    
    computeLPS(pattern, M, lps);
    
    int i = 0, j = 0;
    while (i < N) {
        if (pattern[j] == text[i]) {
            i++; j++;
        }
        
        if (j == M) {
            printf("Pattern found at index %d\n", i - j);
            j = lps[j - 1];
        }
        else if (i < N && pattern[j] != text[i]) {
            if (j != 0)
                j = lps[j - 1];
            else
                i++;
        }
    }
}
```
**Time**: O(n + m) | **Space**: O(m)

---

## Common Problems & Patterns

### Problem Type → Technique Mapping

| Problem Type | Best Technique | Time |
|--------------|----------------|------|
| Pair sum in sorted array | Two Pointers | O(n) |
| Subarray sum = k | Prefix Sum + Hash | O(n) |
| Max sum subarray | Kadane's | O(n) |
| Max sum k elements | Sliding Window | O(n) |
| Sort 0,1,2 | Dutch Flag | O(n) |
| Pattern matching | KMP | O(n+m) |
| Anagrams | Hashing/Sorting | O(n) |
| Palindrome | Two Pointers | O(n) |

---

## Important Formulas

- **Sum of array**: Σ arr[i]
- **Prefix sum at i**: prefix[i] = prefix[i-1] + arr[i]
- **Range sum [l,r]**: prefix[r] - prefix[l-1]
- **Subarray count**: n(n+1)/2

---

## Practice Checklist

- [ ] Two pointer problems (5 problems)
- [ ] Sliding window problems (5 problems)
- [ ] Kadane's algorithm variations
- [ ] KMP pattern matching
- [ ] Dutch national flag
- [ ] Prefix sum problems
- [ ] GATE previous year questions

---

**Last Updated**: Nov 22, 2024
