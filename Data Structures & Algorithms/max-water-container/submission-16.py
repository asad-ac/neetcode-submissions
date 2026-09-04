class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # whichever side is lower

        # if maxArea variable set to negative infinity
        # left right pointers
        # calculate area the minimum and right - left

        maxArea = float("-inf")

        left = 0
        right = len(heights) - 1

        while left < right:

            area = min(heights[left], heights[right]) * (right - left)
            maxArea = max(area, maxArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea