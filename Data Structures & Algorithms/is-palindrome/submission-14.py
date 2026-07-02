class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        
        for letter in s:
            if letter.isalnum():
                clean += letter.lower()

        cleanReverse = ""

        for i in range(len(clean) - 1, - 1, -1):
            cleanReverse += clean[i]
        
        for i in range(len(clean) - 1, -1, -1):
            if clean[i] != cleanReverse[i]:
                return False
        return True
        