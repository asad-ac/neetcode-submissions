class Solution:
    def characterReplacement(self, s: str, k: int):
        answer = 0
        chars = set(s) # xy

        for target in chars:
            count = left = 0
            for right in range(len(s)):
                if s[right] == target:
                    count += 1
                while (right - left + 1) - count > k:
                    if s[left] == target:
                        count -= 1
                    left += 1
                answer = max(answer, right - left + 1)
        return answer