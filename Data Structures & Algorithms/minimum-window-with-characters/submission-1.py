class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]

                if self.contains(sub, t):
                    if res == "" or len(sub) < len(res):
                        res = sub

        return res

    def contains(self, sub, t):
        for c in t:
            if sub.count(c) < t.count(c):
                return False
        return True
        

