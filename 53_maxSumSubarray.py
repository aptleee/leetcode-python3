class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        sum1, Mx = nums[0], nums[0]
        for i in range(1, len(nums)):
            if sum1 <= 0:
                sum1 = nums[i]
            else:
                sum1 = sum1 + nums[i]
            Mx = max(Mx, sum1)

        return Mx