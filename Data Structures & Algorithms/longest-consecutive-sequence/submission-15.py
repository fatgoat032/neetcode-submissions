class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(set(nums), key=int)
        longest = 0
        longest_list = []
        for i in range(1, len(sorted_nums)):
            if ((sorted_nums[i] - sorted_nums[i - 1]) == 1):
                longest += 1
            elif ((sorted_nums[i] - sorted_nums[i - 1]) != 1):
                longest_list.append(longest)
                longest = 0
        longest_list.append(longest)
        return max(longest_list) + 1
        


        