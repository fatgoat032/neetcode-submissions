class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        counts = {}
        for row in wall:
            position = 0
            for brick in row:
                position += brick
                if position != sum(row):
                    if position not in counts:
                        counts[position] = 1
                    else:
                        counts[position] += 1

        if not counts:
            return len(wall)
        max_ = max(counts.values())
        return len(wall) - max_
        

