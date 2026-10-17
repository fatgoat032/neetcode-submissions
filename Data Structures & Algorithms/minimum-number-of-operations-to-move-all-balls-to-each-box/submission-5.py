class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        x = len(boxes)
        balls = 0
        count = 0
        ans = [0 for i in range(x)]
        for i in range(x):
            ans[i] += count
            balls += int(boxes[i])
            count += balls
        balls = 0
        count = 0
        for i in range(x - 1, -1, -1):
            ans[i] += count
            balls += int(boxes[i])
            count += balls
        return ans

            