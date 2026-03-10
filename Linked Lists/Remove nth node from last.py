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

    def remove_nth_node_from_last(self,n):
        print()
        if n!=0:
            l=r=self.head
            for _ in range(n):
                r=r.next
            
            if r is None:
                self.head=self.head.next
            else:
                while r.next:
                    l=l.next
                    r=r.next
                l.next=l.next.next
        
        self.traverse()

        
elements = [1,2,3,4,5]
obj = ll(elements)
n=2
obj.traverse()
obj.remove_nth_node_from_last(n)