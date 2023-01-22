from typing import List

# O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)

        return res


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = 3
    out = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    s_out = s.generateParenthesis(input_)
    s_out = [i for i in out if i in s_out]
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = 1
    out = ["()"]
    s_out = s.generateParenthesis(input_)
    s_out = [i for i in out if i in s_out]
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
