class LinkedList:
    def __init__(self):
        self.head = None
        

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
            


    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        # Simple for now, will get updated
        self.head = node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
