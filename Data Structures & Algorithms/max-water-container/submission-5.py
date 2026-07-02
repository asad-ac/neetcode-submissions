class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        result = 0

        # how it knows when to stop
        while l < r:
            area = min(heights[l],heights[r]) * (r - l)
            result = max(result, area)

            # If the left wall is shorter,
            # it is limiting the amount of water
            if heights[l] < heights[r]:
                # Move left pointer to try to find a taller wall
                l += 1
            else:
                # Otherwise, the right wall is shorter or equal,
                # so move the right pointer inward
                r -= 1

        return result
                