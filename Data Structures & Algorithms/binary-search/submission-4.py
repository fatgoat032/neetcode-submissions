class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)
        m = 0
        while last >= first:
            m = (last + first) // 2
            print(m)
            if m >= len(nums):
                return - 1
                
            if nums[m] == target:
                return m
            elif nums[m] > target:
                last = m - 1
            else:
                first = m + 1
        return -1
        