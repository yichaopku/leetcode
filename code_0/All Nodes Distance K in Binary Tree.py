# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recursive(self,root,dis):
        if root==None:
            return
        if dis!=None:
            if dis+1==self.K:
                self.rs.append(root.val)
            elif dis+1<self.K:
                self.recursive(root.left,dis+1)
                self.recursive(root.right,dis+1)
        else:
            if root.val==self.target:
                self.recursive(root.left,0)
                self.recursive(root.right,0)
                return 0
            ll=self.recursive(root.left,None)
            if ll!=None:
                if ll+1==self.K:
                    self.rs.append(root.val)
                elif ll+1<self.K:
                    self.recursive(root.right,ll+1)
                    return ll+1
            else:
                rr=self.recursive(root.right,None)
                if rr!=None:
                    if rr+1==self.K:
                        self.rs.append(root.val)
                    elif rr+1<self.K:
                        self.recursive(root.left,rr+1)
                        return rr+1


    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if K==0:
            return [target.val]
        self.rs=[]
        self.target=target.val
        self.K=K
        self.recursive(root,None)
        return self.rs
