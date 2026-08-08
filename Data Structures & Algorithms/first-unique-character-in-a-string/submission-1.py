class Solution:
    def firstUniqChar(self, s: str) -> int:
    
        mp = {}

        for letter in s:
            mp[letter] = mp.get(letter, 0) + 1

        for index, letter in enumerate(s): 
            if mp[letter] == 1:
                return index
        return -1