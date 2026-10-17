class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicateHere = set()
        for i in range(len(nums)):
            if nums[i] in isDuplicateHere:
                return True
            isDuplicateHere.add(nums[i])
        return False