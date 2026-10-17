class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        thestr = ""
        for char in s:
            if char in thestr:
                thestr = thestr[thestr.index(char) + 1: ] 
            thestr += char
            longest = max(longest, len(thestr))
        return longest
            
        