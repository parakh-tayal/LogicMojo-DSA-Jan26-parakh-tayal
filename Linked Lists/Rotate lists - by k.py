class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class ll:
    def __init__(self,elements):
        self.head=None
        self.tail=None
        self.link_list(elements)

    def link_list(self,elements):
        for i in range(len(elements)):
            new_node = node(elements[i])
            if self.head is None:
                self.head=new_node
            else:
                prev_node.next=new_node
            prev_node=new_node
            if i==len(elements)-1:
                self.tail=new_node

    def traverse(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end='-')
            curr_node=curr_node.next

    def rotate_list(self,k):
        """
        2 pointer + 3 pointer approach(prev,curr,last)
        """
        # if k is greater than length of Linked list
        node=self.head
        node_length=0
        while node:
            node=node.next
            node_length+=1
        if k>node_length:
            k=k%node_length

        if k%node_length!=0:            
            prev=curr=last=self.head
            for _ in range(k-1):
                last=last.next
            while last.next:
                prev=curr
                curr=curr.next
                last=last.next
            prev.next=None
            last.next=self.head
            self.head=curr

        self.traverse()
        
elements = [1,2,3,4,5]
k=6
obj = ll(elements)
obj.traverse()
print()
obj.rotate_list(k)