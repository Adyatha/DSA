class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_front(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_list_val(self,list_values):
        self.head=None
        for data in list_values:
            self.insert_at_end(data)

    def get_length(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head=self.head.next
            return
        
        c=0
        itr = self.head
        while itr:
            if c == index-1:
                itr.next= itr.next.next
                break
            itr = itr.next
            c+=1

    #insert at particular index
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_end(data)
            return 
        
        c=0
        itr = self.head
        while itr:
            if c == index-1:
                node = Node(data,itr.next)
                itr.next=node
                break

            itr = itr.next
            c+=1

    def print_list(self):
        if self.head is None:
            print("list is empty")
            return

        llist=""
        itr=self.head
        while itr:
            llist+=str(itr.data)+ " -->"
            itr=itr.next
        llist+="None"
        print(llist)

    def reverse_linked_list(self):
        prev,curr=None,self.head
        llist=""
        while curr:
            nxt = curr.next
            curr.next=prev
            prev=curr
            curr = nxt
        self.head= prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_front(5)
    ll.insert_at_front(89)
    ll.insert_at_end(88)
    # list_val= ["banana","mango","grapes","orange"]
    # ll.insert_list_val(list_val)
    # ll.print_list()
    # ll.remove_at(20)  #index not present in the list raises exception
    # ll.remove_at(2)
    ll.print_list()
    ll.reverse_linked_list()
    ll.print_list()
    # print("length of list is:", ll.get_length())
    # ll.insert_at(2,"figs")
    # ll.print_list()