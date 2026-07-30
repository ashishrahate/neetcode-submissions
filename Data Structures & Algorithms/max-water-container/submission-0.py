class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_capacity = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            capacity = width * height
            max_capacity = max(max_capacity, capacity)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_capacity