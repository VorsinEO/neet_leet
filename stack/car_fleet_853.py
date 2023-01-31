from typing import List

# O(n*2)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]:  # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


def test_solution(my_sol_class):
    s = my_sol_class()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    out = 3
    s_out = s.carFleet(target, position, speed)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    target = 10
    position = [3]
    speed = [3]
    out = 1
    s_out = s.carFleet(target, position, speed)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]
    out = 1
    s_out = s.carFleet(target, position, speed)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
