from typing import List

# O(n2)
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i, l in enumerate(height):
            if i < len(height) - 1:
                for j in range(i + 1, len(height)):
                    r = height[j]
                    w = j - i
                    h = min(l, r)
                    max_area = max(w * h, max_area)
            else:

                return max_area


# O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while r > l:
            w = r - l
            h = min(height[l], height[r])
            max_area = max(w * h, max_area)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return max_area


def test_solution(my_sol_class):
    s = my_sol_class()
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    out = 49
    s_out = s.maxArea(nums)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
        nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ## test_2
    nums = [1, 1]
    out = 1
    s_out = s.maxArea(nums)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
