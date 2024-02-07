# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # store traversed nodes
        nums = []

        def dfs(node):
            # each time you can visit an existing node
            if node:
                dfs(node.left)
                nums.append(node.val)
                dfs(node.right)

        dfs(root)
        return nums
