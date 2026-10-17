class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        m = s[::-1]
        print(f"m: {m}")
        print(f"s: {s}")
        if m == s:
            return True
        return False
