class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount = {}
        tCount = {}
        for i in range(len(s)):
            if s[i] not in sCount:
                sCount[s[i]] = 0
            elif s[i] in sCount:
                sCount[s[i]] += 1
    
            if t[i] not in tCount:
                tCount[t[i]] = 0
            elif t[i] in tCount:
                tCount[t[i]] += 1
        return sCount == tCount