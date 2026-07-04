from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        freqMap = Counter(arr)

        count = 1

        for char, frequency in freqMap.items():
            if frequency == 1:
                if count == k:
                    return char
                count += 1
        return ""

        

        
        