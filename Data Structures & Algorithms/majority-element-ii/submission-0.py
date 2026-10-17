class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        threshold = (len(nums) // 3)
        for num, count in freq.items():
            if count > threshold:
                res.append(num)
        return res

        