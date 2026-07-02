class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for num in nums:
            x[num] = x.get(num,0) + 1
        
        for value in x.values():
            if value > 1:
                return True
        return False