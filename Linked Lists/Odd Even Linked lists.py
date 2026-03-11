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

    def odd_even(self):
        odd=self.head
        if self.head:  # if ll is empty
            even_start=even=odd.next

            while even and even.next:
                odd.next=even.next
                odd = odd.next

                even.next=odd.next
                even = even.next
            
            odd.next=even_start
        # return self.head
        self.traverse()

        
elements = [1,2,3,4,5]
# elements = []
obj = ll(elements)
obj.traverse()
print()
obj.odd_even()