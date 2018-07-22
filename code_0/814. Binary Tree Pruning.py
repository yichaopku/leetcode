# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recursive(self,root):
        if root==None:
            return None
        ll=self.recursive(root.left)
        rr=self.recursive(root.right)
        root.left,root.right=ll,rr
        if ll==None:
            if rr==None:
                if root.val==0:
                    return None
        return root

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.recursive(root)
