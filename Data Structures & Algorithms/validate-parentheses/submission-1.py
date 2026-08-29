class Solution:
    def isValid(self, s: str) -> bool:

        mp = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        stack = []

        for letter in s:
            if letter in "[({":
                stack.append(letter)
            elif letter not in "[({":
                
                if len(stack) == 0:
                    return False
                
                if mp[letter] != stack[-1]:
                    return False
                
                stack.pop()

        return len(stack) == 0

        