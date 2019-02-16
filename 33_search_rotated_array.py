class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        lo, hi = 0, len(nums)
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[hi]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                lo += 1
        return -1