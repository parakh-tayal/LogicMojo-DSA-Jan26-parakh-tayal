"""
Floyd's Algorithm - Fast/Slow Pointers - Hare/Tortoise Pointers
- Use to detect loop/cycle

Slow - 1 step
Fast - 2 steps

if loop exists - return True
else False
"""

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
        flag_next=None
        for i in range(len(elements)):
            new_node = node(elements[i])
            if self.head is None:
                self.head=new_node
            else:
                prev_node.next=new_node
                if i==1:
                    flag_next=new_node
            prev_node=new_node
            if i==len(elements)-1:
                self.tail=new_node
                new_node.next=flag_next

    def traverse(self):
        curr_node = self.head
        count=0
        while count<=5:
            print(curr_node.data,end='-')
            curr_node=curr_node.next
            count+=1
    
    def floyd_algo(self):
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

elements = [1,2,3,4,5]
obj = ll(elements)
obj.traverse()
print(obj.floyd_algo())