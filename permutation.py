class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        ret = []

        def P(depth, t):
            if depth == len(nums):
                e = t.copy()
                ret.append(e)
                return

            for i in range(len(nums)):
                if nums[i] not in t:
                    t.append(nums[i])
                    P(depth + 1, t)
                    t.pop()

        P(0, [])
        return ret