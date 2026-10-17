class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arra = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if i != j:
                    if int(boxes[j]) == 1:
                        count += abs(i - j)
            arra.append(count)
        return arra
        