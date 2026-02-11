# Longest Balanced Subarray II

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![Contributors](https://img.shields.io/badge/contributors-5-orange)  

## Overview
This repository implements an algorithm for finding the longest balanced subarray within a given array. A balanced subarray is defined as a contiguous subarray whose number of 1s equals the number of 0s.  

## Algorithm Explanation
The algorithm employed in this solution uses a hash map to store the cumulative sums of elements encountered as we iterate through the array. The key idea is to convert the 0s to -1s so that we can treat the problem as finding the maximum length subarray with a cumulative sum of 0.  

### Steps:
1. **Initialize Variables**: Begin by defining a hash map to keep track of the cumulative sum indices and a variable to track the maximum length of the balanced subarray.  
2. **Iterate Through the Array**: As you loop through the array, update the cumulative sum.  
   - If the current element is 0, decrement the sum by 1 (treating 0 as -1);
   - If it is 1, increment the sum by 1.
3. **Check for Maximum Length**: If the cumulative sum has been seen before, calculate the length of the subarray from the index stored in the hash map to the current index. If this length is greater than the previously recorded maximum length, update it.  
4. **Store the Sum**: If the cumulative sum hasn’t been seen before, store its index in the hash map.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of elements in the array. We traverse the array once, performing constant-time operations.
- **Space Complexity**: O(n), where n is the maximum size of the hash map that stores the cumulative sums and their corresponding indices.

## Best Practices
- Always validate the input to handle edge cases such as empty arrays or arrays with all identical elements.
- Use meaningful variable names that convey purpose to improve code readability.
- Consider edge cases where elements may be repeated or when balancing isn’t possible.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.