# Definition for a binary tree node.
from typing import Optional

# 687
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_depth = Solution.maxDepth(self, root.left)
            right_depth = Solution.maxDepth(self, root.right)

            if root.left and root.left.val == root.val:
                left_depth += 1
            else:
                left_depth = 0

            if root.right and root.right.val == root.val:
                right_depth += 1
            else:
                right_depth = 0

            return max(left_depth, right_depth)

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            max = Solution.maxDepth(self, root)
            return max

Solution.maxDepth(
    None, TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
)
# Solution.maxDepth(
#     None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None)))))
# )
# Solution.maxDepth(
#     None, TreeNode(1, TreeNode(2, None, None), None)
# )
