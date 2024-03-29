# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Solution 1: recursive depth first search Time: O(n) Space (n)
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
    
        # Solution2: iterative breadth first search
        level =0
        q = deque([root])
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
        # Solution 3： Iterative Depth First Search - Stack
        stack = [[root,1]]
        result = 1
        while stack:
            node, depth=stack.pop()

            if node:
                res = max(res,depth)
                stack.append([node.left, depth+1])
                stack.append([node.right,depth+1])
        return res