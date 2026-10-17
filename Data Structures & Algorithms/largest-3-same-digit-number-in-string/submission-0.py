class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = [digit for digit, group in groupby(num) if len(list(group)) >= 3]
        if not result:
            return ""
        return max(result) * 3