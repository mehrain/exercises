class BSTNode:
    def exists(self, val):
        if self.val == val:
            return True
        elif self.val < val:
            if self.right:
                return self.right.exists(val)
            else:
                return False
        else:  # self.val > val
            if self.left:
                return self.left.exists(val)
            else:
                return False


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