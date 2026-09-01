class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        # loop through array
        # if its a "+" we add previous two numbers on stack
        # if its a "C" we pop from the stack
        # if its a "D" we multiply the last number in the stack by itself and add it to the stack
        # we return the last number

        for character in operations:
            if character == "+":
                total = stack[-1] + stack[-2]
                stack.append(total)
            elif character == "C":
                stack.pop()
            elif character == "D":
                 double = stack[-1] * 2
                 stack.append(double)
            else:
                stack.append(int(character))
        return sum(stack)


        