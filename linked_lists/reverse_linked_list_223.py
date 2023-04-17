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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.val is None:
            return head
        result = ListNode(0)
        result_tail = result
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            # print(temp)
            curr = curr.next
        while temp:
            result_tail.next = ListNode(temp.pop())
            result_tail = result_tail.next
        return result.next


# two(three) pointers solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # print(prev)
            # print(curr)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            # print(curr)
        return prev


# recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [1, 2, 3, 4, 5]
    out = [5, 4, 3, 2, 1]
    s_out = s.reverseList(list_to_LL(input_))
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [1, 2]
    out = [2, 1]
    s_out = s.reverseList(list_to_LL(input_))
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = []
    out = []
    s_out = s.reverseList(list_to_LL(input_))
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
