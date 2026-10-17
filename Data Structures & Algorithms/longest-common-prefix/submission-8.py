class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = []
        if "" in strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs) - 1):
            if strs[i][0] != strs[i + 1][0]:
                print("failed")
                return ""
        longest.append(strs[0][0])
        let = 1
        while let != len(min(strs, key=len)):
            for j in range(1, len(strs)):
                letter = strs[0][let]
                if strs[j][let] != letter:
                    print("failed")
                    print(f"{strs[j][let]} and {letter}")
                    return "".join(longest)
            longest.append(letter)    
            let += 1
        return "".join(longest)
