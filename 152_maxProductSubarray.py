class Solution:
    def maxProduct(self, nums: 'List[int]') -> 'int':

        Max, Min, ret = nums[0], nums[0], nums[0]
        #  dp find the Max and Min of the former one
        #  go through the list, every time there is a negative number, swap Mx an Mn
        #  Mx = max(nums[i], Mx*nums[i])
        #  Mn = min(nums[i], Mn*nums[i])
        #  ret = max(r, Mx)

        for i in range(1, len(nums)):  # start from the second one
            if nums[i] < 0:
                Max, Min= Min, Max
            Max = max(nums[i], nums[i] * Max)
            Min = min(nums[i], nums[i] * Min)

            ret = max(ret, Max)
        return ret

