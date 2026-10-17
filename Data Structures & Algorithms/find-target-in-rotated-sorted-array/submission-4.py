class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        while last >= first:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[first]:
                if nums[first] <= target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if nums[last] >= target > nums[mid]:
                    first = mid + 1
                else:
                    last = mid - 1
        return -1
        