class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        def R(A):
            i, j = 0, len(A)-1
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

        n = len(nums)
        if n == 0 or n == 1:
            return

        i = n-2

        while i >= 0:
            if nums[i] > nums[i+1]:
                break
            i -= 1

        if i < 0:
            R(nums)
            return

        j = n-1

        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = nums[i+1:][::-1]