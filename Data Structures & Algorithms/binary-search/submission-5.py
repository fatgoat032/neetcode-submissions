class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        while last >= first:
            m = (last + first) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                last = m - 1
            else:
                first = m + 1
        return -1
        