class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x = {}

        for num in arr:
            x[num] = x.get(num, 0) + 1

        ans = -1
        
        for num, count in x.items():
            if num == count:
                ans = max(ans, num)
        return ans