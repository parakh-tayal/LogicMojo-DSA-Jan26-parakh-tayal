class node:
    def __init__(self,data=None):
        self.next=None
        self.data=data

class queue:

    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is not None:
            curr=self.head
            self.head=curr.next
            if self.head is None:
                self.tail = None
            return curr.data

        else:
            print("Queue is empty")
            return None
    
    def traverse(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next

        
obj = queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.traverse()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.traverse()







