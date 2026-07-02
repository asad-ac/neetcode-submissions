class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0
        for i in range(len(heights)):
            for j in range(1 + i, len(heights)):
                result = max(result, min(heights[i], heights[j]) * (j-i))
        return result

                



        