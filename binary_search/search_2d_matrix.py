from typing import List

# O(logn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 1:
            res = self.bin_search(matrix[0], target)
            if res:
                return True
            else:
                return False

        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
        if not (l <= r):
            return False
        m = (l + r) // 2
        for row in [m]:
            res = self.bin_search(matrix[row], target)
            if res:
                return True

        return False

    def bin_search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True
        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 1:
            res = self.bin_search(matrix[0], target)
            if res:
                return True
            else:
                return False

        l, r = 0, len(matrix) - 1

        while l < r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][-1]:
                if target > matrix[m][0]:
                    res = self.bin_search(matrix[m], target)
                    if res:
                        return True
                    else:
                        return False
                r = m - 1
            else:
                return True

        for row in [m, m - 1, m + 1]:
            res = self.bin_search(matrix[row], target)
            if res:
                return True

        return False

    def bin_search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True
        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    out = True
    s_out = s.searchMatrix(input_, target)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    out = False
    s_out = s.searchMatrix(input_, target)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test 3
    input_ = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 10
    out = True
    s_out = s.searchMatrix(input_, target)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
