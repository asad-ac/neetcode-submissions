class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]

                if self.contains(substring, t):
                    if res == "" or len(substring) < len(res):
                        res = substring

        return res

    def contains(self, substring, t):
        for c in t:
            if substring.count(c) < t.count(c):
                return False
        return True
        

