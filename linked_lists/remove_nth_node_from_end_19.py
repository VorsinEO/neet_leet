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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Основная идея  - попасть в позицию n с конца.
        Для этого отмеряем n сначала как fast pointer(right) и slow pointer (left)
        Движемся по списку, пока fast не упрется в конец. Вот мы и в нужной позиции (left).
        Теперь нам нужно у текущей ноды поменять next на значение через 1 ноду.

        temp это расширение списка head слева на одну нулевую ноду.
        Это нужно, чтобы left указавыл именно на n с конца ноду, иначе будет на n-1 с конца
        """
        temp = ListNode(0, head)
        left = temp
        right = head
        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        left.next = left.next.next

        return temp.next


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [1, 2, 3, 4, 5]
    n = 2
    out = [1, 2, 3, 5]
    s_out = s.removeNthFromEnd(list_to_LL(input_), n)
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [1]
    n = 1
    out = []
    s_out = s.removeNthFromEnd(list_to_LL(input_), n)
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = [1, 2]
    n = 1
    out = [1]
    s_out = s.removeNthFromEnd(list_to_LL(input_), n)
    s_out = LL_to_list(s_out)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
