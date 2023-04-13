from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))


def LL_to_list(ll):
    l = []
    while ll is not None:
        l.append(ll.val)
        ll = ll.next
    return l


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res_ll = ListNode(0)
        res_tail = res_ll

        while list1 or list2:
            if list1:
                if list2:
                    if list1.val <= list2.val:
                        res_tail.next = ListNode(list1.val)
                        res_tail = res_tail.next
                        list1 = list1.next
                    else:
                        res_tail.next = ListNode(list2.val)
                        res_tail = res_tail.next
                        list2 = list2.next

                else:
                    res_tail.next = ListNode(list1.val)
                    res_tail = res_tail.next
                    list1 = list1.next
            elif list2:
                res_tail.next = ListNode(list2.val)
                res_tail = res_tail.next

                list2 = list2.next
        return res_ll.next


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [1, 2, 4]
    input_2 = [1, 3, 4]
    out = [1, 1, 2, 3, 4, 4]
    s_out = s.mergeTwoLists(list_to_LL(input_), list_to_LL(input_2))
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = []
    input_2 = []
    out = []
    s_out = s.mergeTwoLists(list_to_LL(input_), list_to_LL(input_2))
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = []
    input_2 = [0]
    out = [0]
    s_out = s.mergeTwoLists(list_to_LL(input_), list_to_LL(input_2))
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
