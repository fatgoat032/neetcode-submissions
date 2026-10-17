class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] != target):
                    continue
                else:
                    if i != j: 
                        indices_list.append(i)
                        indices_list.append(j)
                        return indices_list
        