class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in dic.values():
            if num == 1:
                return -1
            elif num % 3 == 0:
                count += num / 3
            else:
                count += num // 3 + 1
        return int(count)
        


        