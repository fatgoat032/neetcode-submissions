class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pointer = -1
        info = sorted(zip(position, speed), reverse=True)
        for position, speed in info:
            time = (target - position) / speed
            if stack and time <= stack[pointer]:
                continue
            else:
                stack.append(time)
                pointer += 1
        return len(stack)


        