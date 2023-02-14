from typing import List

# O(n**2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []
        if len(temperatures) == 1:
            return [0]
        for i, t_0 in enumerate(temperatures):
            for j, t_1 in enumerate(temperatures[i:]):
                if t_1 > t_0:
                    res.append(j)
                    break
            if len(res) < i + 1:
                res.append(0)

        return res


# O(N*2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            if i == 0:
                stack.append((i, t))
            else:
                for inv_i in range(len(stack) - 1, -1, -1):
                    j, t_0 = stack[inv_i]
                    if t > t_0:
                        stack.pop()
                        res[j] = i - j
                    else:
                        break
                stack.append((i, t))

        return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [73, 74, 75, 71, 69, 72, 76, 73]
    out = [1, 1, 4, 2, 1, 1, 0, 0]
    s_out = s.dailyTemperatures(input_)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [30, 40, 50, 60]
    out = [1, 1, 1, 0]
    s_out = s.dailyTemperatures(input_)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = [30, 60, 90]
    out = [1, 1, 0]
    s_out = s.dailyTemperatures(input_)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
