class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        n = len(nums) / 2
        for i in range(len(nums)):
            count = 0
            num = nums[i]
            for j in range(len(nums)):
                if nums[j] == num:
                    count += 1
            if count % 2 != 0:
                return False
        return True



        