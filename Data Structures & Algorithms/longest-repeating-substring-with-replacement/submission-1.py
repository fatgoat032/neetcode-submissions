class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        left = 0
        length = len(s)
        counts = {}
        for i in range(length):
            counts[s[i]] = counts.get(s[i], 0) + 1
            while ((i - left + 1) - max(counts.values())) > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, i - left + 1)
        return best
            


        