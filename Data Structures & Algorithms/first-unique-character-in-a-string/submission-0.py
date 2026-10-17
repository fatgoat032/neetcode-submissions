class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for key, value in dic.items():
            if value == 1:
                return s.find(key)
        return -1

            