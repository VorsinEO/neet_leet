from typing import List

# O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opers = ["+", "-", "*", "/"]

        digits = []
        for t in tokens:
            if t not in opers:
                digits.append(t)
            else:
                x2 = digits.pop()
                x1 = digits.pop()
                digits.append(self._math_oper(int(x1), int(x2), t))
        return int(digits[-1])

    def _math_oper(self, x1, x2, oper):
        if oper == "+":
            return x1 + x2
        elif oper == "-":
            return x1 - x2
        elif oper == "*":
            return x1 * x2
        else:
            return int(x1 / x2)


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = ["2", "1", "+", "3", "*"]
    out = 9
    s_out = s.evalRPN(input_)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = ["4", "13", "5", "/", "+"]
    out = 6
    s_out = s.evalRPN(input_)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    out = 22
    s_out = s.evalRPN(input_)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
