class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = []
        firstNum = 0
        secondNum = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                firstNum = nums[i]
                secondNum = nums[j]
                if firstNum + secondNum == target:
                    x.append(i)
                    x.append(j)
        return x
