# Definition for a binary tree node.
from typing import Optional, List


# 105
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root_index = self.findMiddleIndex(nums)

        if root_index < 0:
            return

        root = TreeNode(nums[root_index])
        root.left = self.sortedArrayToBST(nums[:root_index])
        root.right = self.sortedArrayToBST(nums[root_index + 1:])

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_index = inorder.index(preorder.pop(0))

        if root_index < 0:
            return

        root = TreeNode(inorder[root_index])
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])

        return root

pre = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

Solution().buildTree(pre, inorder)

#
# Solution.maxDepth(
#     None, root
# )