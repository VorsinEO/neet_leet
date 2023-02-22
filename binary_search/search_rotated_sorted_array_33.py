from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    out = 4
    s_out = s.search(input_, target)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    out = -1
    s_out = s.search(input_, target)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    out = 4
    s_out = s.search(input_, target)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
