class BinarySearchNode:

    #find_min(), find_max(), sum(), preorder(),postorder()

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,child):
        if self.data == child: #no duplicates allowed in BST
            return
        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = BinarySearchNode(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = BinarySearchNode(child)

    def sum(self):
        sum =self.data

        if self.left:
            sum += self.left.sum()

        if self.right:
            sum += self.right.sum()

        if self.left == None and self.right== None:
            return sum
        
        return sum

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def preorder_traversal(self):
        elem =[]

         # visit base node
        elem.append(self.data)

        # visit left tree first
        if self.left:
            elem += self.left.preorder_traversal()

        # visit right tree
        if self.right:
            elem += self.right.preorder_traversal()

        return elem
    
    def postorder_traversal(self):
        elem =[]

        # visit left tree first
        if self.left:
            elem += self.left.postorder_traversal()

        # visit right tree
        if self.right:
            elem += self.right.postorder_traversal()

         # visit base node 3326.38
        elem.append(self.data)

        return elem

    def search(self,val):
        if val == self.data:
            return True
        
        if val <self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val> self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
def build_tree(elements):
    root = BinarySearchNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root
    
if __name__ == "__main__":
    nums= [10,20,5,3,15,25,9]
    nums_tree=build_tree(nums)
    print("minimum value is",nums_tree.find_min())
    print("maximum value is",nums_tree.find_max())

    print(nums_tree.preorder_traversal()) #[10, 5, 3, 9, 20, 15, 25]
    print(nums_tree.postorder_traversal()) #[3, 9, 5, 15, 25, 20, 10]

    print("sum of BST:", nums_tree.sum())
 
