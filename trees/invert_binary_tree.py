from typing import Optional

from base_tree import TreeNode, to_binary_tree, to_list_from_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def test_solution(my_sol_class):
    s = my_sol_class()
    input_ = [4, 2, 7, 1, 3, 6, 9]
    out = [4, 7, 2, 9, 6, 3, 1]
    s_out = s.invertTree(to_binary_tree(input_))
    s_out = to_list_from_tree(s_out)
    if s_out == out:
        print("test1 success")
    else:
        print("test1 fail")
        print(s_out)
    ## test_2
    input_ = [2, 1, 3]
    out = [2, 3, 1]
    s_out = s.invertTree(to_binary_tree(input_))
    s_out = to_list_from_tree(s_out)
    if s_out == out:
        print("test2 success")
    else:
        print("test2 fail")
        print(s_out)
    ## test_3
    input_ = []
    out = []
    s_out = s.invertTree(to_binary_tree(input_))
    s_out = to_list_from_tree(s_out)
    if s_out == out:
        print("test3 success")
    else:
        print("test3 fail")
        print(s_out)


if __name__ == "__main__":
    test_solution(Solution)
