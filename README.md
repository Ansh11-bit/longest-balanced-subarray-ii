# Longest Subarray with Equal Count of Odd and Even Numbers

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Time](https://img.shields.io/badge/Time-O(n%20log%20n)-brightgreen)
![Space](https://img.shields.io/badge/Space-O(n)-blue)
![Approach](https://img.shields.io/badge/Approach-Segment%20Tree%20%2B%20Lazy%20Propagation-orange)

Efficient solution using a **segment tree with lazy propagation** to find the longest subarray where the **number of odd elements equals the number of even elements**.

## Problem It Solves

Return the length of the **longest subarray** in which:

- count of odd numbers == count of even numbers

(or equivalently: prefix balance returns to zero after transformations)

**Important note**  
This is **not** the problem of equal number of **distinct** odd and even values.  
This version only cares about **parity count**, not distinct values.

## Examples

```text
Input:  [1,2,3,4,5]
Output: 4
Explanation: [2,3,4,5] → 2 odds (3,5), 2 evens (2,4)

Input:  [3,2,2,5,4]
Output: 4   (e.g. [2,2,5,4] or [3,2,2,5])
        (whole array has 2 odds + 3 evens → not balanced)

Input:  [2,4,6,1,3,5]
Output: 6
Explanation: whole array → 3 odds, 3 evens
