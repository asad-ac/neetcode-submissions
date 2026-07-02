class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # result variable that stores max length of set
        # start at each character index
        # make a set
        # if it is in the set, exit loop to go to next character
        # other wise add it to the set

        result = 0

        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            result = max(result, len(charSet))
        return result