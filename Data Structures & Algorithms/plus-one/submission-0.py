class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1 -> 1
        # 2 -> 1
        # 3 -> 1
        # 4 -> 1

        output = []

        # 959

        for i in range(len(digits) - 1, - 1, - 1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits

            

        