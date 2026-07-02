class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        x = 0
        numbers = set(nums)

        for num in nums:
            streak = 0
            current = num
            while current in numbers:
                streak += 1
                current += 1
            x = max(x,streak)
        return x