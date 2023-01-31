from typing import List

# O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l)) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [-1, 0, 3, 5, 9, 12]
    target = 9
    out = 4
    s_out = s.search(input_, target)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [-1, 0, 3, 5, 9, 12]
    target = 2
    out = -1
    s_out = s.search(input_, target)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    s = my_sol_class()
    input_ = [2, 5]
    target = 2
    out = 0
    s_out = s.search(input_, target)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
