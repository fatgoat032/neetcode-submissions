class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        alr_added = []
        for i in range(len(strs)):
            x_list = []
            if i in alr_added:
                continue
            else:
                x_list.append(strs[i])       
            for j in range(len(strs)):
                equal = True
                if i == j:
                    continue
                x = {}
                for character in strs[i]:
                    x[character] = x.get(character, 0) + 1
                if len(strs[i]) == len(strs[j]):
                    for char in strs[j]:
                        if char in strs[i]:
                           x[char] -= 1
                        else:
                           equal = False
                           break
                        if x[char] < 0:
                           equal = False
                           break
                    if equal == True:
                        x_list.append(strs[j])
                        alr_added.append(j)
            groups.append(x_list)
        return groups
                        
                    

        