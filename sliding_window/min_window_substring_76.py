# from typing import List


class Solution:
    def check_curr_wind(self, curr_cnt, t_cnt, curr_wind):
        for k, v in t_cnt.items():
            if v > curr_cnt.get(k, 0):
                return ""
        return curr_wind

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l = 0
        r = len(t)
        t_cnt = {}
        for ch in t:
            t_cnt[ch] = 1 + t_cnt.get(ch, 0)
        curr_cnt = {}
        for ch in s[l:r]:
            curr_cnt[ch] = 1 + curr_cnt.get(ch, 0)

        answer = ""

        while (r <= len(s)) & (l <= len(s) - len(t)):
            curr_wind = s[l:r]
            if (answer != "") & (len(curr_wind) >= len(answer)):
                curr_cnt[s[l]] -= 1
                l += 1
            else:
                curr_answer = self.check_curr_wind(curr_cnt, t_cnt, curr_wind)
                if curr_answer != "":
                    curr_cnt[s[l]] -= 1
                    l += 1

                    if (answer == "") or (len(answer) > len(curr_answer)):
                        answer = curr_answer
                else:

                    r += 1
                    if (r - 1) < len(s):
                        curr_cnt[s[r - 1]] = 1 + curr_cnt.get(s[r - 1], 0)
        return answer


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

                while have == need:
                    # update our result
                    if (r - l + 1) < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                    # pop from left
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = "ADOBECODEBANC"
    input_2 = "ABC"
    out = "BANC"
    s_out = s.minWindow(input_, input_2)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = "a"
    input_2 = "a"
    out = "a"
    s_out = s.minWindow(input_, input_2)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = "a"
    input_2 = "aa"
    out = ""
    s_out = s.minWindow(input_, input_2)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
