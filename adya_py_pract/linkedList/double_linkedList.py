class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next= None

class DoubleLinkedList:
    def __init__(self):
         self.head=None

    def insert_at_front(self,data):
        node=Node(data)
        if self.head is not None:
            node.next=self.head
            self.head.prev=node
        self.head=node

    def insert_at_end(self,data):
        node=Node(data)

        if self.head is None:
            self.head = node
            return

        itr=self.head
        while itr.next:
            itr = itr.next
        itr.next=node
        node.prev=itr

    def get_length(self):
        itr=self.head
        c=0
        while itr:
            c+=1
            itr=itr.next

        return c
 
    def remove_at_index(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid Index")
        
        c=0
        itr= self.head
        while itr:
            if c == index-1:
                node = itr.next.next
                itr.next=node
                node.prev=itr
                break
            itr=itr.next
            c+=1


    def print_ddl(self):
        if self.head is None:
            print("Doublely Linked List is empty")
            return
        
        itr= self.head
        dll=""
        while itr:
            dll+=str(itr.data) + " <---> "
            itr = itr.next
        print(dll)
    
if __name__=="__main__":
    doublLL=DoubleLinkedList()
    doublLL.insert_at_front(10)
    doublLL.insert_at_front(20)
    doublLL.insert_at_end(30)
    doublLL.print_ddl()
    doublLL.remove_at_index(1)
    doublLL.print_ddl()