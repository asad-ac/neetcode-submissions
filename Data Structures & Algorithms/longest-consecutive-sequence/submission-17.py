class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # sort

        # 2 3 4 5 10 20

        # 0 1 1 2 3 4 5 6

        if not nums:
            return 0
        
        nums.sort()
        
        longest = 1
        current_longest = 1
        left = 0
        
        for r in range(1, len(nums)):
            if nums[r] == nums[left]:
                left += 1
                continue
            if nums[r] == nums[left] + 1:
                current_longest += 1
                left += 1
            else:
                current_longest = 1
                left = r
            longest = max(longest, current_longest)
        return longest





