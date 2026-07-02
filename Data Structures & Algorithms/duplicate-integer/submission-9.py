class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for n in nums:
            x[n] = x.get(n,0) + 1

        for value in x.values():
            if value > 1:
                return True
        return False