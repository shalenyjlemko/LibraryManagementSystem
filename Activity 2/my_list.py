class ListLike:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def map(self, func):
        current = self.head
        while current:
            current.data = func(current.data)  # Apply the function to the node's data
            current = current.next
