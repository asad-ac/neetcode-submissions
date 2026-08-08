class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # two pointers
        
        # left 1 and left 2
        # we add alternatively
        # and at the end add whichever one is remaining

        left1, left2 = 0, 0

        merged = ""

        while left1 < len(word1) and left2 < len(word2):
            merged += word1[left1]
            merged += word2[left2]
            left1 += 1
            left2 += 1
        
        while left1 < len(word1):
            merged += word1[left1]
            left1 += 1

        while left2 < len(word2):
            merged += word2[left2]
            left2 += 1
        return merged

        # Time O(n + m) | Space O(1)

        
