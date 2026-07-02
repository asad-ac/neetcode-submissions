class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}

        for num in nums:
            x[num] = x.get(num, 0) + 1

        for key, value in x.items():
            if value > 1:
                return True
        return False