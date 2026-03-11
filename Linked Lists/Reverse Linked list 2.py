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

    def reverse(self,new_head,r):
        """
        3 pointer approach
        prevm,curr,next
        """
        prev=None
        curr = new_head

        for _ in range(r):
            n = curr.next
            curr.next=prev
            prev=curr
            curr=n
        # starting_node.next=prev
        # self.traverse()
        return prev,curr

    def reverse_2(self,l,r):
        curr=self.head
        starting_node=None

        # Iterate till Left
        for _ in range(l-1):
            starting_node=curr
            curr=curr.next
        
        #2 reverse till right
        rth_node,ending_node = self.reverse(curr,r-l+1)

        #3 point starting_node to rth node
        if starting_node:   # to handle edge case of beginning when l=1
            starting_node.next = rth_node
        else:
            self.head = rth_node

        #4  point new_end_node to ending_node
        curr.next=ending_node

        self.traverse()
        
elements = [1,2,3,4,5,6,7]
l=1
r=6
elements = [3,5]
l=1
r=2
obj = ll(elements)
obj.traverse()
print()
obj.reverse_2(l,r)