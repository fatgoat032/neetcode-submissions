class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        count_table = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if int(boxes[j]) == 1:
                    count += abs(int(j) - int(i))
            count_table.append(count)

        return count_table


        