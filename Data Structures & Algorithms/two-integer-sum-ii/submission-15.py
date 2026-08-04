class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

       # sorted in increasing order

       # brute force = Time O(n)^2 | Space O(1)

       # more optimal = Time  O(n) | Space (1)

       left = 0
       right = len(numbers) - 1
       
       while left < right:
        middle = numbers[left] + numbers[right]

        if middle == target:
            return [left + 1, right + 1]
        
        elif middle > target:
            right -= 1
        
        elif middle < target:
            left += 1


