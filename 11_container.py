class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':

        n = len(height)
        if n == 0:
            return 0
        lo, hi = 0, n-1
        maxA = 0
        while lo < hi:
            maxA = max(maxA, min(height[lo], height[hi])*(hi-lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1

        return maxA
