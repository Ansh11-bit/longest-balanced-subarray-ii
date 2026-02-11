# Longest Balanced Subarray II

LeetCode Problem: [Longest Balanced Subarray II](https://leetcode.com/problems/longest-balanced-subarray-ii/?envType=daily-question&envId=2026-02-11)

## Problem Description

Find the longest contiguous subarray where for every even number at position `i`, there exists an odd number at position `i+1`, and vice versa (alternating even-odd pattern).

## Solution Approach

This solution uses an **advanced segment tree with lazy propagation** to efficiently handle range updates and queries.

### Key Features

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Optimization Techniques:**
  - Segment tree with lazy propagation for efficient range updates
  - Array module for cache efficiency and memory compactness
  - Bitwise operations for parity checking (odd/even detection)
  - Local variable binding for speed optimization

### Algorithm Overview

1. **Parity Tracking:** Track odd numbers as +1 and even numbers as -1
2. **Range Updates:** Use segment tree to update ranges efficiently
3. **Balance Calculation:** Maintain running balance and search for longest valid subarray
4. **Binary Search:** Find the leftmost position where the balance satisfies constraints

### Data Structures Used

- **Lazy Array:** Tracks pending updates
- **Min/Max Trees:** Maintain minimum and maximum values in ranges
- **Lookup Table:** Maps values to their positions

## How to Use

```python
from solution import Solution

# Example 1
nums = [1, 2, 3, 4]
solution = Solution()
result = solution.longestBalanced(nums)
print(result)  # Output: 4

# Example 2
nums = [1, 1, 1, 2, 2, 2]
solution = Solution()
result = solution.longestBalanced(nums)
print(result)  # Output: 0
```

## Complexity Analysis

- **Time:** O(n log n) - n iterations with log n operations per iteration
- **Space:** O(n) - segment tree and auxiliary data structures

## Optimization Details

- Uses Python's `array` module for signed integers ('i') instead of lists
- Bitwise operations for parity detection: `num & 1`
- Local variable binding for frequently called methods (_apply, _pull, _push)
- Efficient lazy propagation to avoid redundant computations

---

**Author:** Ansh11-bit  
**Date:** 2026-02-11