class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def __repr__(self):
        return (f"{self.data}")

class MyList:
    def __init__(self):
        self.head=None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    def __getitem__(self, index):
        current_node = self.head
        new_index = index if index >=0 else len(self)+index
        for _ in range(index):
            current_node = current_node.next
        return current_node.data

    def __len__(self):
        current_node = self.head
        counter = 0 
        while current_node is not None:
            counter+=1
            current_node = current_node.next
        return counter

    def map(self, func):
        current_node = self.head
        while current_node is not None:
            current_node.data = func(current_node.data)
            current_node = current_node.next

def custom_method(x):
    return x.lower()

if __name__ == "__main__": #only called when specifically this file is called

    ml = MyList()
    ml.append("A")
    #print(ml.head)
    ml.append("B")
    ml.append("C")
    for element in ml:
        print(element)
    
    print(ml[0])
    print(ml[-1])
    #ml.map(lambda x : x.lower())
    ml.map(custom_method)
    for element in ml:
        print(element)
    