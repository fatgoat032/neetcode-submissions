class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for i, num in enumerate(nums):
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        counts = sorted(counts.items(), key=lambda item: item[1], reverse=False)
        counts = counts[-k:]
        counts = [count[0] for count in counts ]
        return counts
            


        