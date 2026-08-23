# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(curr, list1):
            if not curr:
                return
            list1.append(curr.val)
            dfs(curr.left, list1)
            dfs(curr.right, list1)

        list1 = []
        dfs(root, list1)

        list1.sort()
        return list1[k - 1]

        