class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        longest = 0

        for num in nums:
            streak = 0
            current = num
            while current in nums:
                current += 1
                streak += 1
            longest = max(longest, streak)
        return longest