class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':

        sum1, j, res = 0, 0, float("inf")
        for i in range(len(nums)):
            sum1 += nums[i]
            print(sum1)
            while sum1 >= s:
                res = min(res, i - j + 1)
                sum1 -= nums[j]
                j += 1
        if j == 0:
            return 0
        return res



