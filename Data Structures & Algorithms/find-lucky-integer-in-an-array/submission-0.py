class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        print(c)
        l = []
        for key, value in c.items():
            print(key)
            print(value)
            if key == value:
                l.append(value)
        
        if l:
            return max(l)
        else:
            return -1