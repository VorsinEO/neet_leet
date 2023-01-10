# from typing import List

# O(n)
class SolutionMy:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        res = ""
        temp_sub = ""
        for i, c in enumerate(s):
            if c not in temp_sub:
                temp_sub += c
            else:
                if len(temp_sub) > len(res):
                    res = temp_sub
                start_pos = temp_sub.find(c) + 1
                temp_sub = temp_sub[start_pos:] + c
        return max(len(res), len(temp_sub))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = "abcabcbb"
    out = 3
    s_out = s.lengthOfLongestSubstring(input_)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = "aabaab!bb"
    out = 3
    s_out = s.lengthOfLongestSubstring(input_)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = "dvdf"
    out = 3
    s_out = s.lengthOfLongestSubstring(input_)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
