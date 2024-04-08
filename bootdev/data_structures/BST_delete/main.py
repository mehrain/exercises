class BSTNode:
    def delete(self, val):
        
        if self.val is None:
            return None
        
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self 
        
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        
        if val == self.val: 
            if not self.right:
                return self.left
            if not self.left:
                return self.right
            if self.left and self.right:
                self.val = self.right.find_min()
                self.right = self.right.delete(self.val)
            return self
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.val
            
        
            


    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
