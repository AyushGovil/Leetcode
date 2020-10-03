class Solution:

    def isValidBST(self, root):
      
        def bst(root):
            
            if root==None:
                return -float('Inf'),float('Inf')
            max1,min1=bst(root.left)
     
            if max1==None or min1==None:
                return None,None
            if root.val<=max1:
                return None,None
            max2,min2=bst(root.right)
            if max2==None or min2==None:
                return None,None
            if root.val>=min2:
                return None,None
            return max(max1,max2,root.val),min(min1,min2,root.val)
        if bst(root)==(None,None):
            return False
        return True
        
