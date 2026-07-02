class Solution:
    def trap(self, height: List[int]) -> int:
        
        # two pointers each on opposite end, l and r
        # leftMax and rightMax variable to calculate each side
        # in the result variable add max of 
        # whichever pointer is greatest, the current index or the max of that side
        # return result variable

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        result = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        return result
