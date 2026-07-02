class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i in range(len(nums)):
            x[nums[i]] = x.get(nums[i], 0) + 1
        
        y = []
        for i in range(k):
            highestValue = -1
            bestKey = None
            for key, value in x.items():
                if value > highestValue:
                    highestValue = value
                    bestKey = key
            y.append(bestKey)
            x.pop(bestKey)
        return y