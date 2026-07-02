class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)):
            x.append(nums[i])

        for i in range(len(nums)):
            x.append(nums[i])

        return x
        
