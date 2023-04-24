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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two half list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            first, second = tmp1, tmp2

        return head


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [1, 2, 3, 4]
    out = [1, 4, 2, 3]
    s_out = s.reorderList(list_to_LL(input_))
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [1, 2, 3, 4, 5]
    out = [1, 5, 2, 4, 3]
    s_out = s.reorderList(list_to_LL(input_))
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3


if __name__ == "__main__":
    test_solution(Solution)
