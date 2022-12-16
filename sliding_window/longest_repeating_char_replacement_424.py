#from typing import List

#O(26n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        countChar = {}
        maxf = 0
        for r in range(len(s)):
            countChar[s[r]] = 1+ countChar.get(s[r],0)
            maxf = max(maxf, countChar[s[r]])
            while (r-l+1) - maxf > k:
                countChar[s[l]]-=1
                l+=1
            res = max(res, r-l +1)
        return res

def test_solution(my_sol_class):
    s =my_sol_class()
    input_ = "ABAB"
    k = 2
    out = 4
    s_out = s.characterReplacement(input_, k)
    if s_out==out:
        print('test1 success')
    else:
        print('test1 fail')
        print(s_out)
    ## test_2
    input_ = "AABABBA"
    k = 1
    out = 4
    s_out = s.characterReplacement(input_, k)
    if s_out==out:
        print('test2 success')
    else:
        print('test2 fail')
        print(s_out)
    
if __name__=="__main__":
    test_solution(Solution)