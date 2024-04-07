class BSTNode:
    def get_min(self):
        if self.left is None:
            return self.val
        else:
            return self.left.get_min()

    def get_max(self):
        if self.right is None:
            return self.val
        else:
            return self.right.get_max()


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
