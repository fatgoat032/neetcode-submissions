class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        letters = []
        used = set()
        for char in order:
            if char in count:
                letters.append(char * count[char])
                used.add(char)
        for char in count:
            if char not in used:
                letters.append(char * count[char])
                used.add(char)
        return ''.join(letters)
        
        

        
        
        
            
            
            

        