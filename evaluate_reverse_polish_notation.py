#  Evaluate the value of an arithmetic expression in Reverse Polibh Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    def evalRPN(self, tokens):
        num_stack = []

        for token in tokens:
            try:
                num = int(token)
                num_stack.append(num)
            except:
                num1 = num_stack.pop()
                num2 = num_stack.pop()

                if token == "+":
                    num_stack.append(num2 + num1)
                elif token == "-":
                    num_stack.append(num2 - num1)
                elif token == "*":
                    num_stack.append(num2 * num1)
                elif token == "/":
                    num_stack.append(int(float(num2) / num1))
        return num_stack.pop()


tokens = ["4","13","5","/","+"]
print Solution().evalRPN(tokens)
