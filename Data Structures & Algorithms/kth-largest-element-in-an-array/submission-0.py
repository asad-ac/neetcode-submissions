class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        i = 1

        # 1 2 3 4 5

        nums.sort()
        nums.reverse()

        # 5 4 3 2 1

        for num in nums:
            if i == k:
                return num
            i += 1
        