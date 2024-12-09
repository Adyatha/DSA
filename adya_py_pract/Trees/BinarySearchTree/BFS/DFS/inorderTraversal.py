class BinarySearchNode:
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

    def inorder_traversal(self):
        elem =[]

        # visit left tree first
        if self.left:
            elem += self.left.inorder_traversal()

        # visit base node
        elem.append(self.data)

        # visit right tree
        if self.right:
            elem += self.right.inorder_traversal()

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
    print(nums_tree.inorder_traversal())
    print(nums_tree)
    print(nums_tree.search(20)) #[3, 5, 9, 10, 15, 20, 25]
    print(nums_tree.search(21))
