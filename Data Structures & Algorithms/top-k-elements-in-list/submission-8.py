class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        x = {}
        for num in nums:
            x[num] = x.get(num, 0) + 1

        y = []
        for i in range(k):
            bestKey = None
            bestValue = -1
            for key, value in x.items():
                if value > bestValue:
                    bestValue = value
                    bestKey = key
            x.pop(bestKey)
            y.append(bestKey)
        return y