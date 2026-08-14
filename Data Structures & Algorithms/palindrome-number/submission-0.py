class Solution:
    def isPalindrome(self, x: int) -> bool:

        # turn into string
        
        stringX = str(x)

        left = 0
        right = len(stringX) - 1

        while left <= right:
            if stringX[left] != stringX[right]:
                return False
            left += 1
            right -= 1
        return True
        