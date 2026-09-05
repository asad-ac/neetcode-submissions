class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        noDuplicates = set(nums)

        for num in noDuplicates:
            if num - 1 not in noDuplicates:
                streak, current = 0, num
                while current in noDuplicates:
                    streak += 1
                    current += 1
                longest = max(longest, streak)
        return longest