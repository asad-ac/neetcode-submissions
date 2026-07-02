class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i in range(len(nums)):
            if nums[i] not in x:
                x[nums[i]] = 1
            elif nums[i] in x:
                x[nums[i]] += 1
        
        y = []
        for i in range(k):
            highestValue = -1
            bestKey = None
            for key, value in x.items():
                if value > highestValue:
                    highestValue = value
                    bestKey = key
            y.append(bestKey)
            del x[bestKey]
        return y