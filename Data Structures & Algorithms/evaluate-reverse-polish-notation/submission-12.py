import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [0 for i in range(len(tokens))]
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda a, b: int(a/b)}
        pointer = -1
        for token in tokens:
            if token not in ops:
                pointer += 1
                stack[pointer] = int(token)
            else:
                res = ops[token](stack[pointer - 1], stack[pointer])
                pointer -= 1
                stack[pointer] = res
        return stack[0]
                
                

