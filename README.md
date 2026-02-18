# Longest Balanced Subarray (Distinct Parity)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Time](https://img.shields.io/badge/Time-O(n%20log%20n)-brightgreen)
![Space](https://img.shields.io/badge/Space-O(n)-blue)

Find the **longest subarray** in which the number of **distinct even numbers** equals the number of **distinct odd numbers**.

## Problem

Given an integer array `nums`, return the length of the longest subarray where  
**the count of unique even values == the count of unique odd values**.

**Note**: Repeated numbers do **not** increase the distinct count.

## Examples

```text
Example 1:
Input: nums = [2,5,4,3]
Output: 4
Explanation: [2,5,4,3] → evens: {2,4}, odds: {5,3} → 2 == 2

Example 2:
Input: nums = [3,2,2,5,4]
Output: 5
Explanation: whole array → evens: {2,4}, odds: {3,5} → 2 == 2

Example 3:
Input: nums = [1,2,3,2]
Output: 3
Explanation: [2,3,2] → evens: {2}, odds: {3} → 1 == 1
           [1,2,3]   → evens: {2}, odds: {1,3} → 1 != 2
