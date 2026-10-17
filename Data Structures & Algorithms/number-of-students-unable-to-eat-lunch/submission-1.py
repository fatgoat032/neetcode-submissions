class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = students[:]
        stack_index = 0
        rotations = 0

        while queue and rotations < len(queue):
            if queue[0] == sandwiches[stack_index]:
                stack_index += 1
                rotations = 0
                queue.pop(0)
            else:
                rotations += 1
                queue.append(queue.pop(0))
        return len(queue)