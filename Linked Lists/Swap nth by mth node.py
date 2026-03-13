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

    # def swap_n_m_nodes_1(self,n_len,m_len):
    #     """
    #     """
    #     prev_n=prev_m=None
    #     n=m=self.head

    #     if n_len==m_len:
    #         # edge case
    #         return self.traverse()

    #     prev_n=None
    #     if n_len==1:
    #         prev_n=self.head

    #     if m_len-n_len==1:
    #         # when n & m are adjacent
    #         curr=self.head
    #         for _ in range(n_len):
    #             prev_n=curr
    #             curr=curr.next
    #         n=curr.next
    #         curr.next=n.next
    #         n.next=curr
    #         prev_n.next=n

    #     else:
    #         # iterate to nth and mth nodes
    #         # move to nth node
    #         for _ in range(n_len-1):
    #             prev_n = n
    #             n = n.next

    #         # move to mth node
    #         for _ in range(m_len-1):
    #             prev_m = m
    #             m = m.next

    #         # swap
    #         after_n=n.next
    #         after_m=m.next

    #         prev_n.next=m
    #         m.next=after_n

    #         prev_m.next=n
    #         n.next=after_m

    #     self.traverse()
        
    def swap_n_m_nodes(self,n_len,m_len):
        if n_len==m_len:
            print("No change needed as n==m")
            return self.traverse()
        
        # always taking m >= n
        if n_len>m_len:
            n_len,m_len=m_len,n_len

        prev_n=prev_m=None
        n=m=self.head

        for _ in range(n_len-1):
            prev_n=n
            n=n.next
        
        for _ in range(m_len-1):
            prev_m=m
            m=m.next

        if prev_n:
            prev_n.next=m
        else:
            self.head=m
        
        if prev_m:
            print(prev_m.data,n.data)
            print(prev_m.next.data,n.next.data)
            prev_m.next=n
            
        
        n.next,m.next=m.next,n.next

        self.traverse()
        
elements = [1,2,3,4,5,6]
n=1
m=2
obj = ll(elements)
obj.traverse()
print()
obj.swap_n_m_nodes(n,m)