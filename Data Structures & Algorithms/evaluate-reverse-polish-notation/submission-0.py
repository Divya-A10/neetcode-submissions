class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)   # truncate toward 0
        }

        for i in tokens:

            if i in operations:

                b = stack.pop()
                a = stack.pop()

                result = operations[i](a, b)

                stack.append(result)

            else:
                stack.append(int(i))

        return stack[-1]
        