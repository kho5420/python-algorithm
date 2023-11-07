# Definition for a binary tree node.
from typing import Optional, List


# 1038
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

    def makeTree(self, nums: List[int]) -> Optional[TreeNode]:
        root_index = len(nums) // 2

        if not nums:
            return

        root = TreeNode(nums[root_index])
        root.left = self.makeTree(nums[:root_index])
        root.right = self.makeTree(nums[root_index + 1:])

        return root

    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_list = self.findVal(root, [])
        sum_list = [sum(x for x in node_list if x >= num) for num in node_list]
        node = self.makeTree(sum_list)
        return node


root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)

Solution().bstToGst(root)

#
# Solution.maxDepth(
#     None, root
# )