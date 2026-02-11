from typing import List
import sys
from array import array

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        """
        Segment tree with lazy propagation for range updates.
        Optimized for Python with array module and local variable binding.
        Time: O(n log n), Space: O(n)
        """
        n = len(nums) + 1
        
        # Compute base as next power of 2
        base = 1
        while base < n:
            base <<= 1
        
        # Use arrays for cache efficiency and memory compactness
        # 'i' = signed int, much faster than list of objects
        lazy = array('i', [0]) * (base * 2)
        min_tree = array('i', [0]) * (base * 2)
        max_tree = array('i', [0]) * (base * 2)
        
        # Local binding for speed
        _apply = self._apply
        _pull = self._pull
        _push = self._push
        
        result = 0
        lookup = {}
        curr = 0
        
        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            d = 1 if num & 1 else -1  # Bitwise parity check
            
            if num in lookup:
                L = lookup[num]
                # Range update [L, n-1] by -d
                self._range_update(L, n - 1, -d, base, lazy, min_tree, max_tree, _apply, _pull)
                curr -= d
            
            curr += d
            lookup[num] = i
            
            # Range update [i, n-1] by +d
            self._range_update(i, n - 1, d, base, lazy, min_tree, max_tree, _apply, _pull)
            
            # Binary search for leftmost index where curr is in [min, max]
            l = i - self._binary_search(curr, base, lazy, min_tree, max_tree, _apply)
            if l > result:
                result = l
        
        return result
    
    def _apply(self, x, val, base, lazy, min_tree, max_tree):
        """Apply lazy value to node x."""
        min_tree[x] += val
        max_tree[x] += val
        if x < base:
            lazy[x] += val
    
    def _pull(self, x, base, lazy, min_tree, max_tree):
        """Pull updates up from leaf x to root."""
        while x > 1:
            x >>= 1
            left = x << 1
            right = left | 1
            min_tree[x] = min_tree[left] if min_tree[left] < min_tree[right] else min_tree[right]
            max_tree[x] = max_tree[left] if max_tree[left] > max_tree[right] else max_tree[right]
            if lazy[x]:
                min_tree[x] += lazy[x]
                max_tree[x] += lazy[x]
    
    def _push(self, x, base, lazy, min_tree, max_tree, _apply):
        """Push lazy values down from root to leaf x."""
        # Compute highest bit
        h = x.bit_length() - 1
        while h > 0:
            y = x >> h
            if lazy[y]:
                _apply(y << 1, lazy[y], base, lazy, min_tree, max_tree)
                _apply((y << 1) | 1, lazy[y], base, lazy, min_tree, max_tree)
                lazy[y] = 0
            h -= 1
    
    def _range_update(self, L, R, val, base, lazy, min_tree, max_tree, _apply, _pull):
        """Range update [L, R] by val using lazy propagation."""
        L += base
        R += base
        L0, R0 = L, R
        
        while L <= R:
            if L & 1:
                _apply(L, val, base, lazy, min_tree, max_tree)
                L += 1
            if not (R & 1):
                _apply(R, val, base, lazy, min_tree, max_tree)
                R -= 1
            L >>= 1
            R >>= 1
        
        _pull(L0, base, lazy, min_tree, max_tree)
        _pull(R0, base, lazy, min_tree, max_tree)
    
    def _binary_search(self, x, base, lazy, min_tree, max_tree, _apply):
        """Find leftmost index where x is in [min, max]."""
        i = 1
        while i < base:
            if lazy[i]:
                _apply(i << 1, lazy[i], base, lazy, min_tree, max_tree)
                _apply((i << 1) | 1, lazy[i], base, lazy, min_tree, max_tree)
                lazy[i] = 0
            i <<= 1
            # Check if x is NOT in left child's range
            if not (min_tree[i] <= x <= max_tree[i]):
                i |= 1
        return i - base
