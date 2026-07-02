class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for num in nums:
            if num not in x:
                x[num] = 1
            elif num in x:
                x[num] += 1
        
        for value in x.values():
            if value > 1:
                return True
        return False