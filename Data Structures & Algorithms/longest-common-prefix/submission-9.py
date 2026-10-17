class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = []
        min_len = len(min(strs, key=len))
        for count in range(min_len):
            char = strs[0][count]
            for i in range(1, len(strs)):
                if strs[i][count] != char:
                    return ''.join(common)
            common.append(char)
        return ''.join(common)
      
       
       

        