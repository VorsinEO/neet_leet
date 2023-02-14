from typing import List


class Solution:
    def check_k(self, piles, h, k):
        res = 0
        for p in piles:
            res += p // k + (p % k > 0)

        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            test_m = self.check_k(piles, h, k=m)
            if test_m > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1

        return res


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [3, 6, 7, 11]
    h = 8
    out = 4
    s_out = s.minEatingSpeed(input_, h)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [30, 11, 23, 4, 20]
    h = 5
    out = 30
    s_out = s.minEatingSpeed(input_, h)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    s = my_sol_class()
    input_ = [30, 11, 23, 4, 20]
    h = 6
    out = 23
    s_out = s.minEatingSpeed(input_, h)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
