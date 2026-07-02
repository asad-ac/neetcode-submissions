class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # permutation is same letters in diff order
        # sort s1
        # want to loop through s2 and sort
        # if equal return true
        # otherwise return false

        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i : j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False
            