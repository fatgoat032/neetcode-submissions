class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_last = len(numbers) - 1
        pointer_first = 0
        for i in range(len(numbers)):
            if (numbers[pointer_first] + numbers[pointer_last] < target):
                pointer_first += 1
            elif (numbers[pointer_first] + numbers[pointer_last] > target):
                pointer_last -= 1
            else:
                return [pointer_first + 1, pointer_last + 1]
        