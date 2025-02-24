from typing import Optional

from base_tree import TreeNode, to_binary_tree, to_list_from_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [(1, root)]
        dm = 1
        while q:
            d, curr = q.pop()
            if curr.right:
                q.append((d + 1, curr.right))
            if curr.left:
                q.append((d + 1, curr.left))
            if (curr.right or curr.left) and (d + 1) > dm:
                dm = d + 1

        return dm


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [3, 9, 20, None, None, 15, 7]
    out = 3
    s_out = s.maxDepth(to_binary_tree(input_))
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [1, None, 2]
    out = 2
    s_out = s.maxDepth(to_binary_tree(input_))
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3


if __name__ == "__main__":
    test_solution(Solution)
