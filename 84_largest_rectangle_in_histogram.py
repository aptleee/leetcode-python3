class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        # width plus the smallest height
        # brute force
        maxArea = 0
        for i in range(len(heights)):
            minh = heights[i]
            for j in range(i, len(heights)):
                minh = min(minh, heights[j])
                maxArea = max(maxArea, minh * (j-i+1))

        return maxArea


class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        #  base case
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        #  divide and conquer
        shortest = float("inf")
        idx = 0
        #  divide
        for i, x in enumerate(heights):
            if x < shortest:
                shortest = x
                idx = i

        return max(max(shortest*len(heights), self.largestRectangleArea(heights[:idx])), self.largestRectangleArea(heights[idx+1:]))


class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        heights.append(0)
        stack = [-1]
        ret = 0
        for i in range(len(heights)):

            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] # i is the right boundary and stack[-1] is the left boundary
                ret = max(ret, h*w)
            stack.append(i)
        heights.pop()
        return ret

