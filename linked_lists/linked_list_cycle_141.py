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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# dont know how emulate cycle in LL
def test_solution(my_sol_class):
    print("dont know how emulate cycle in LL - please debug in LeetCode -_- ")


if __name__ == "__main__":
    test_solution(Solution)
