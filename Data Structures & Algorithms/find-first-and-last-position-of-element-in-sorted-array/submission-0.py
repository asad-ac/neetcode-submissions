class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        output = [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                if output[0] == -1:
                    output[0] = i
                    output[1] = i
                else:
                    output[1] = i
        return output
        
        
        
        