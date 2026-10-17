class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for i in range(len(logs)):
            if "./" == logs[i][:2]:
                print(f"./ {i}")
                continue
            elif "../" == logs[i][:3]:
                print(f"../ {i}")
                if depth <= 0:
                    continue
                else:
                    depth -= 1
            elif "/" in logs[i]:
                print(f"/ {i}")
                depth += 1
        return depth
        