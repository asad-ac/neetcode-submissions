from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
        magMap = Counter(magazine)
        ransomMap = Counter(ransomNote)

        for letter, frequency in ransomMap.items():
            if letter not in magMap:
                return False
            elif frequency > magMap[letter]:
                return False
        return True
