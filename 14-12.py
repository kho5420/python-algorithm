# Definition for a binary tree node.
from typing import Optional, List


# 783
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findVal(self, root: Optional[TreeNode], lst: list):
        if root is None:
            return None
        else:
            self.findVal(root.left, lst)
            self.findVal(root.right, lst)

            lst.append(root.val)
            return lst

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        val_list = self.findVal(root, [])

        min_list = []
        for i in range(len(val_list)):
            for j in range(i + 1, len(val_list)):
                diff = abs(val_list[i] - val_list[j])
                min_list.append(diff)

        return min(min_list)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = None
root.right.right = None

Solution().minDiffInBST(root)

#
# Solution.maxDepth(
#     None, root
# )