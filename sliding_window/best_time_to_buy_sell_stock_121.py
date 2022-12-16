from typing import List

#O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        res = 0
        curr_prof = 0
        while r<len(prices):
            curr_prof = prices[r] - prices[l]
            if prices[r]<prices[l]:
                l=r
   
            res = max(res, curr_prof)
            r+=1
                
        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        lp = 0
        rp =1
        while rp< len(prices):
            curr_ = prices[rp]-prices[lp]
            if curr_ > max_prof:
                max_prof = curr_
            if prices[rp]<prices[lp]:
                lp=rp
            rp+=1
        return max_prof

def test_solution(my_sol_class):
    s =my_sol_class()
    input_ = [7,1,5,3,6,4]
    out = 5
    s_out = s.maxProfit(input_)
    if s_out==out:
        print('test1 success')
    else:
        print('test1 fail')
        print(s_out)
    ## test_2
    input_ = [7,6,4,3,1]
    out = 0
    s_out = s.maxProfit(input_)
    if s_out==out:
        print('test2 success')
    else:
        print('test2 fail')
        print(s_out)
    ## test_3
    input_ = [2,1,2,1,0,1,2]
    out = 2
    s_out = s.maxProfit(input_)
    if s_out==out:
        print('test3 success')
    else:
        print('test3 fail')
        print(s_out)    
if __name__=="__main__":
    test_solution(Solution)