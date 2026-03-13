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

    def swap_pair_nodes(self):
        """
        3 pointer approach
        prev,curr,next
        """
        prev=None
        curr=self.head
        while curr and curr.next:
            n=curr.next
            curr.next=n.next
            n.next=curr
            if prev==None:
                self.head=n
            else:
                prev.next=n
            prev=curr
            curr=curr.next

        self.traverse()
        
elements = [1,2,3,4,5]
obj = ll(elements)
obj.traverse()
print()
obj.swap_pair_nodes()