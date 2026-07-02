class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j: # skipping numbers based on values nums[i] != nums[j] rather than index
                    product = product * nums[j]
            x.append(product)
        return x
                