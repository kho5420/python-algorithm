# Definition for a binary tree node.
from typing import Optional, List


# 108
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMiddleIndex(self, list):
        length = len(list)

        if length % 2 == 1:
            middle_index = length // 2
        else:
            middle_index = length // 2 - 1

        return middle_index

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root_index = self.findMiddleIndex(nums)

        if root_index < 0:
            return

        root = TreeNode(nums[root_index])
        root.left = self.sortedArrayToBST(nums[:root_index])
        root.right = self.sortedArrayToBST(nums[root_index + 1:])

        return root

lst = [-10, -3, 0, 5, 9]
Solution().sortedArrayToBST(lst)

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)
#
# Solution.maxDepth(
#     None, root
# )