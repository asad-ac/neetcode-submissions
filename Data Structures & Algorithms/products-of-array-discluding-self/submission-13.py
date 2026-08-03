class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            runningProduct = 1
            for j in range(len(nums)):
                if i != j:
                    runningProduct *= nums[j]
            output.append(runningProduct)
        return output
