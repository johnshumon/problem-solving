"""Binary tree Postorder traversal module"""

# problem statement: https://leetcode.com/problems/binary-tree-inorder-traversal
# difficulty: easy

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:

        """Returns in-order traversal list of a given BST.
        > Traverse order: left -> root -> right
        """
        elements = []

        if root is None:
            return None

        if root.left:
            elements += self.inorder_traversal(root.left)

        elements.append(root.val)

        if root.right:
            elements += self.inorder_traversal(root.right)

        return elements
