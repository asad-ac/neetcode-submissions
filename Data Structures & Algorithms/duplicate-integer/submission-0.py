class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for i in range(len(nums)):
            if nums[i] not in x:
                x[nums[i]] = 1
            elif nums[i] in x:
                x[nums[i]] += 1

        for key, value in x.items():
            if value > 1:
                return True
        return False
            


        