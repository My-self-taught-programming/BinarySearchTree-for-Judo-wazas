import judo_moves


class BinarySearchTree:
    def __init__(self, value, data, depth=1):
        self.data = data
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value, data):
        if (value < self.value):
            if (self.left is None):
                self.left = BinarySearchTree(value, data, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value, data)
        else:
            if (self.right is None):
                self.right = BinarySearchTree(value,data, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value, data)
            
    def get_node_by_value(self, value,):
        if (self.value == value):
            return self.data
        elif ((self.left is not None) and (value < self.value)):
            return self.left.get_node_by_value(value)
        elif ((self.right is not None) and (value >= self.value)):
            return self.right.get_node_by_value(value)
        else:
            return None
    
    def depth_first_traversal(self):
        if (self.left is not None):
            self.left.depth_first_traversal()
            print(f'Depth={self.depth}, Value={self.value}, Data={self.data}')
        if (self.right is not None):
            self.right.depth_first_traversal()
    
    def is_in_tree(self,value):
        if value == self.value:
            print(f"{value} is in BST")
            return True
        if value < self.value:
            if self.left == None:
                return False
            return self.left.is_in_tree(value)
        if self.right == None:
            return False
        return self.right.is_in_tree(value)
                
   






tree = BinarySearchTree(11, judo_moves.judo)

tree.insert(1, judo_moves.nage)
tree.insert(2, judo_moves.Nage_waza)
tree.insert(3, judo_moves.Tachi_waza)
tree.insert(4, judo_moves.Te_waza)
tree.insert(5, judo_moves.Koshi_waza)
tree.insert(6, judo_moves.Ashi_waza)
tree.insert(7, judo_moves.Sutemi_waza)
tree.insert(8, judo_moves.Ma_Sutemi_waza)
tree.insert(9, judo_moves.Yoko_Sutemi_waza)
tree.insert(10, judo_moves.katame)
tree.insert(12, judo_moves.katame_waza)
tree.insert(13, judo_moves.Osae_komi_waza)
tree.insert(14, judo_moves.Kesa_gatame_kei)
tree.insert(15, judo_moves.Shido_gatame_kei)
tree.insert(16, judo_moves.shime_waza)
tree.insert(17, judo_moves.Kansetsu_waza)
tree.insert(18, judo_moves.Ukemi)
tree.insert(19, judo_moves.back_ukemi)
tree.insert(20, judo_moves.forward_ukemi)
tree.insert(21, judo_moves.side_ukemi)


  
# print("Printing the inorder depth-first traversal:")
# tree.depth_first_traversal()