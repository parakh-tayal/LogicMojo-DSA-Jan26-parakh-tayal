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
    def __init__(self,a,b,intersection_index):
        self.head=None
        self.tail=None
        self.head2 = self.create_intersecting_lists(a,b,intersection_index)

    def create_intersecting_lists(self, list1, list2, intersect_index):

        # build first list
        prev = None
        intersect_node = None

        for i in range(len(list1)):
            new_node = node(list1[i])

            if self.head is None:
                self.head = new_node
            else:
                prev.next = new_node

            prev = new_node

            if i == intersect_index:
                intersect_node = new_node

        self.tail = prev


        # build second list
        head2 = None
        prev2 = None

        for i in range(len(list2)):
            new_node = node(list2[i])

            if head2 is None:
                head2 = new_node
            else:
                prev2.next = new_node

            prev2 = new_node

        # attach second list to intersection node
        prev2.next = intersect_node

        return head2

    def traverse(self, head):
        curr_node = head
        while curr_node:
            print(curr_node.data, end='-')
            curr_node = curr_node.next
        print()

    def approach_1(self,head,head2):
        
        # count of ll1
        node = head
        len_ll1=0
        while node:
            len_ll1+=1
            node=node.next

        # count of ll1
        node = head2
        len_ll2=0
        while node:
            len_ll2+=1
            node=node.next

        if len_ll2>len_ll1:
            diff=len_ll2-len_ll1
            bigger=head2
            smaller=head
        else:
            diff=len_ll1-len_ll2
            bigger=head
            smaller=head2

        # giving a head start to bigger ll
        count=0
        while count<diff:
            count+=1
            bigger=bigger.next

        # now starting together pointers on both LL and checking if node1==node2

        # if no intersection is there - it will throw error - thats why we use "while bigger and smaller"
        while bigger and smaller and bigger!=smaller:
            bigger=bigger.next
            smaller=smaller.next
        return bigger.data
    
    def approach_2(self,head,head2): 
        """
        Classic Two pointer approach

        traverse both pointers simultaneously till end 
        when pointers reach to end/null/none
        reverse the pointers of both lls

        so that their distance level out 
        like node1=head1 becomes node1=head2
             node2=head2 becomes node2=head1
        """
        node1 = head
        node2 = head2

        while node1!=node2:
            node1=node1.next if node1 else head2
            node2=node2.next if node2 else head
        return node1.data


a=[1,2,3,4,5]
b=[9,8]
intersection_index = 2

obj = ll(a,b,intersection_index)

obj.traverse(obj.head)    # list A
obj.traverse(obj.head2)   # list B

print(obj.approach_1(obj.head,obj.head2))
print(obj.approach_2(obj.head,obj.head2))