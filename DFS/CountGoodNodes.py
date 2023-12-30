# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''1448. Count Good Nodes in Binary Tree'''
'''Use DFS (Depth First Search) to traverse the tree, and constantly keep track of the current path maximum.'''
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            nonlocal num_good_nodes
            if max_so_far <= node.val:
                num_good_nodes += 1
                max_so_far = node.val
            if node.right:
                dfs(node.right, max_so_far)
            if node.left:
                dfs(node.left, max_so_far)

        num_good_nodes = 0
        dfs(root, float("-inf"))
        return num_good_nodes