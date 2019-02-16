class Solution:
    def findShortestSubArray(self, nums: 'List[int]') -> 'int':
        left, right, count = {}, {}, {}

        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i

            right[x] = i
            count[x] = count.get(x, 0) + 1

        max_degree = max(count.values())

        ret = len(nums)  #  start from the length of nums

        for x in count:
            if count[x] == max_degree:
                ret = min(ret, right[x] - left[x] + 1)

        return ret




