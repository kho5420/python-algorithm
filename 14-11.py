# Definition for a binary tree node.
from typing import Optional, List


# 938
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        else:
            left_val = self.rangeSumBST(root.left, low, high)
            right_val = self.rangeSumBST(root.right, low, high)

            sum_val = root.val if low <= root.val <= high else 0
            return sum_val + left_val + right_val

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = None
root.right.right = TreeNode(18)

Solution().rangeSumBST(root, 7, 15)

#
# Solution.maxDepth(
#     None, root
# )