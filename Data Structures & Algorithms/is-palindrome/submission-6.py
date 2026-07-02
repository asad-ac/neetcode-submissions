class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lower case
        # isalnum (either a letter or number)
        # loop through and add to clean variable
        # compare clean variable to itself backwards
        clean = ""
        for letter in s:
            if letter.isalnum():
                clean += letter.lower()
        return clean == clean[::-1]