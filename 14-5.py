# Definition for a binary tree node.
from typing import Optional

# 617
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            new_node = TreeNode(root1.val + root2.val)
            new_node.left = Solution.mergeTrees(self, root1.left, root2.left)
            new_node.right = Solution.mergeTrees(self, root1.right, root2.right)
            return new_node
        else:
            return root1 if root1 else root2


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

Solution.mergeTrees(
    None, root, root2
)
# Solution.maxDepth(
#     None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None)))))
# )
# Solution.maxDepth(
#     None, TreeNode(1, TreeNode(2, None, None), None)
# )
