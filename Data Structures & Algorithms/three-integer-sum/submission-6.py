class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        mylist = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = i + 1
            last = len(nums) - 1
            while last > first:
                target = -nums[i]
                if nums[first] + nums[last] > target:
                    last -= 1
                elif nums[first] + nums[last] < target:
                    first += 1
                else:
                    mylist.append([nums[i], nums[first], nums[last]])
                    last -= 1
                    first += 1
        return mylist
                
                
                
        