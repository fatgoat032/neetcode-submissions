class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "_" + "~" + "$" + string + "."
        return encoded

    def decode(self, s: str) -> List[str]:
        next_start = 0
        print(s)
        str_list = []
        for i in range(len(s)):
            if s[i] == "_" and s[i + 1] == "~" and s[i + 2] == "$":
                str_length = int(s[next_start : i])
                print(f"str length: {str_length}")
                str_list.append(s[i + 3 : i + 3 + str_length])
                next_start = i + 4 + str_length
                if next_start >= len(s):
                    break
                print(f"character at next_start: {s[next_start]}")
        return str_list
                
