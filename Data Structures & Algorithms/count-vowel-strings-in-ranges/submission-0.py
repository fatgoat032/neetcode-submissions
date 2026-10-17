class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        valid = [0 for i in range(len(words))]
        ans = []
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels:
                valid[i] += 1
        for query in queries:
            count = 0
            count = sum(1 for x in valid[query[0]: query[1] + 1] if x == 1)
            ans.append(count)
        return ans

        