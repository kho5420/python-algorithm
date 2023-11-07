# Definition for a binary tree node.
from typing import Optional

# 297
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            root.left = Solution.invertTree(self, root.right)
            root.right = Solution.invertTree(self, root.left)
            return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

Solution.maxDepth(
    None, root
)
# Solution.maxDepth(
#     None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None)))))
# )
# Solution.maxDepth(
#     None, TreeNode(1, TreeNode(2, None, None), None)
# )
