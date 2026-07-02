class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        while nums:
            smallest = nums[0]
            for num in nums:
                if num < smallest:
                    smallest = num
            res.append(smallest)
            nums.remove(smallest)
        return res
