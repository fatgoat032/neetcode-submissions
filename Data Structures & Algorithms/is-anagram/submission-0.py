class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        FoundAlr = set()
        if len(s) != len(t):
            return False
        counts = {} #hashmap
        for character in s:
            counts[character] = counts.get(character, 0) + 1 #+1 as initially character won't be in counts
            print(character, "count:", counts.get(character))
        for char in t:
            if char not in counts:
                return False
            counts[char] -= 1
            if counts[char] < 0:
                print("this is the mole:", char)
                return False
        return True
        