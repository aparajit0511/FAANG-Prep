class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token != "+" or token != "*" or token != "-" or token != "/":
                stack.append(token)
                continue

            if token == "+" or token == "-" or token == "*" or token == "/":
                item1 = stack.pop()
                item2 = stack.pop()

                if token == "+":
                    value = int(item2) + int(item1)
                elif token == "-":
                    value = int(item2) - int(item1)
                elif token == "*":
                    value = int(item2) * int(item1)
                elif token == "/":
                    value = int(item2) / int(item1)

                stack.append(value)

        return stack[-1]