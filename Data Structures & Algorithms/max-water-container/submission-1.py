class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0
        while right > left:
            length = min(heights[left], heights[right])
            width = abs(right - left)
            if length * width > best:
                best = length * width
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return best


        