class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for letter in s:
            if letter.isalnum():
                clean += letter.lower()
        return clean == clean[::-1]