class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subroot:
            return True
        
        if self.isSameTree(root, subroot):
            return True
        
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)


    def isSameTree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        # Case 1: both None
        if not root and not subroot:
            return True
        # Case 2: one None, one not None → mismatch
        if not root or not subroot:
            return False
        # Case 3: values mismatch
        if root.val != subroot.val:
            return False
        
        # Case 4: compare children
        return self.isSameTree(root.left, subroot.left) and self.isSameTree(root.right, subroot.right)
