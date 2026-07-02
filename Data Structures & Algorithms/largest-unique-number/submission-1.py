class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        freqMap = {}

        nums.sort()

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        largest = -1

        # sort

        # two pointers

        for number, count in freqMap.items():
            if count == 1:
                largest = number
        return largest
        