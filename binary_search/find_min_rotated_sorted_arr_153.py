from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while l <= r:
            m = (l + r) // 2
            # print(l, r, m)
            if nums[m] < nums[r]:
                if nums[m] < nums[m - 1]:
                    return nums[m]
                r = m - 1
            else:
                l = m + 1
        # print(l, r, m)
        return nums[m]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = float("inf")

        while start < end:
            mid = (start + end) // 2
            curr_min = min(curr_min, nums[mid])

            # right has the min
            if nums[mid] > nums[end]:
                start = mid + 1

            # left has the  min
            else:
                end = mid - 1

        return min(curr_min, nums[start])


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [3, 4, 5, 1, 2]
    out = 1
    s_out = s.findMin(
        input_,
    )
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [4, 5, 6, 7, 0, 1, 2]
    out = 0
    s_out = s.findMin(
        input_,
    )
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = [11, 13, 15, 17]
    out = 11
    s_out = s.findMin(
        input_,
    )
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
