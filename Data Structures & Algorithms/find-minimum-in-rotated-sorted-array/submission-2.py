class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0
        last = len(nums) - 1
        if first == last:
            return nums[0]
        while last > first:
            mid = (first + last) // 2
            if nums[mid] > nums[-1]:
                first = mid + 1
            elif nums[mid] < nums[-1]:
                last = mid 
        return nums[last]
        
            