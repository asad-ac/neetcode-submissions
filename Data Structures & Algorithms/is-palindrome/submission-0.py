class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for letter in s:
            if letter.isalnum():
                clean.append(letter.lower())
    
        clean = "".join(clean)
        reverse = clean[::-1]
        
        for i in range(len(clean)):
            if clean[i] != reverse[i]:
                return False
        return True
