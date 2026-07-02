class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Move left pointer to the next alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
            # Move right pointer to the previous alphanumeric character
            while l < r and not s[r].isalnum():
                r -= 1

            # Compare ignoring case. If mismatch, not a palindrome.
            if s[l].lower() != s[r].lower():
                return False

            # Move towards the center
            l += 1
            r -= 1

        # All compared pairs (if any) matched
        return True
            