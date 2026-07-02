class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0

        for num in nums:
            streak = 0
            current = num
            while current in nums:
                streak += 1
                current += 1
            longest = max(longest, streak)
        return longest
        