class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        x = []
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            #frequency count dictionary
            # number to amount

        for i in range(k):
            bestKey = -1
            bestValue = -1
            for key, value in dic.items():
                if value > bestValue:
                    bestValue = value
                    bestKey = key
            x.append(bestKey)
            dic.pop(bestKey)
        return x



