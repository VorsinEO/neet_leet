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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [[1, 4, 5], [1, 3, 4], [2, 6]]
    out = [1, 1, 2, 3, 4, 4, 5, 6]
    lists = [list_to_LL(k) for k in input_]
    s_out = s.mergeKLists(lists)
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = []
    out = []
    lists = [list_to_LL(k) for k in input_]
    s_out = s.mergeKLists(lists)
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = [[]]
    out = []
    lists = [list_to_LL(k) for k in input_]
    s_out = s.mergeKLists(lists)
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
