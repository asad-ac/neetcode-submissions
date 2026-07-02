class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        while nums:
            smallest = nums[0]
            for n in nums:
                if n < smallest:
                    smallest = n
            res.append(smallest)
            nums.remove(smallest)

        return res
