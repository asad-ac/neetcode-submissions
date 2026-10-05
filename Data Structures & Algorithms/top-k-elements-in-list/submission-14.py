class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        output = []

        for number, freq in freqMap.items():
            output.append([freq, number])

        output.sort(reverse = True)

        frequent = []

        for freq, number in output:
            frequent.append(number)
            if len(frequent) == k:
                break
        return frequent
                   