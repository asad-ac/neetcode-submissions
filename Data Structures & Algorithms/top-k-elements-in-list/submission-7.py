class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {} #val to frequency
        for i in range(len(nums)):
            x[nums[i]] = x.get(nums[i], 0) + 1
            
        y = []
        for i in range(k):
            highestValue = -1
            highestKey = None
            for key, value in x.items():
                if value > highestValue:
                    highestValue = value
                    highestKey = key
            y.append(highestKey)
            x.pop(highestKey)
        return y
            