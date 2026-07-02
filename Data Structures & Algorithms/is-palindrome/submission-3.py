class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for letter in s:
            if letter.isalnum():
              clean += letter.lower()
        l = 0
        r = len(clean) - 1
        while l < r:
            if clean[l] != clean[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        

