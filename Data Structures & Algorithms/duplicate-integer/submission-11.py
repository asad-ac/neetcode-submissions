class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freqDict = {}

        if not nums:
            return False

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
        
        for amount in freqDict.values():
            if amount > 1:
                return True
        return False
        