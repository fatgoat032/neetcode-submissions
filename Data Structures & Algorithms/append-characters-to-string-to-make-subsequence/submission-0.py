class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        k = len(s)
        j = 0
        for i in range(k):
            if s[i] == t[j]:
                j += 1
            if j == len(t):
                return len(t) - j
        return len(t) - j
        