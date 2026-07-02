class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap variable
        # to store unique values
        # mapped to the amount
        # loop through dict and check if any value is > 1
        x = {}
        for n in nums:
            x[n] = x.get(n,0) + 1

        for value in x.values():
            if value > 1:
                return True
        return False