class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap
        # subtract target - num: 
        # index -> num
        # 0 to 3

        seen = {}

        for index in range(len(nums)):
            value = target - nums[index]
            if value in seen:
                return [seen[value], index]
            seen[nums[index]] = index
        return []


        # 3 to 0
        # 
            
        