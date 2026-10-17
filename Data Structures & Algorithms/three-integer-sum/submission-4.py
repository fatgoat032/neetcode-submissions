class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        L = []
        nums.sort() 
        for i in range(len(nums) - 2):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while k > j:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    L.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        for i, l in enumerate(L):
            l.sort()
        tupled_l = [tuple(x) for x in L]
        L = list(set(tupled_l))
        return L
  


               


        
        
        