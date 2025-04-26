class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        if node is None:
            return None
        elif node.key == key:
            return node.value
        elif key > node.key:
            return self._search(key, node.right)
        else:
            return self._search(key, node.left)
        
    def _balance(self, node, node_balance):
        if node_balance == 2:
            left = node.left.left.height if node.left.left is not None else 0
            right = node.left.right.height if node.left.right is not None else 0
            child_balance = left - right
            if child_balance >= 0:
                node = self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                node = self._right_rotate(node)
        if node_balance == -2:
            left = node.right.left.height if node.right.left is not None else 0
            right = node.right.right.height if node.right.right is not None else 0
            child_balance = left - right
            if child_balance <= 0:
                node = self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                node = self._left_rotate(node)
        return node
        
    def insert(self, key, data):
        self.root = self._insert(key, data, self.root)

    def _insert(self, key, data, node):
        if node is None:
            return Node(key, data)
        elif node.key == key:
            node.value = data
            return node
        elif key > node.key:
            node.right = self._insert(key, data, node.right)
            if node.right.height >= node.height:
                node.height = node.right.height + 1
            left_branch = node.left.height if node.left is not None else 0
            right_branch = node.right.height if node.right is not None else 0
            node_balance = left_branch - right_branch
            if node_balance == -2 or node_balance == 2:
                node = self._balance(node, node_balance)
            return node
        else:
            node.left = self._insert(key, data, node.left)
            if node.left.height >= node.height:
                node.height = node.left.height + 1
            left_branch = node.left.height if node.left is not None else 0
            right_branch = node.right.height if node.right is not None else 0
            node_balance = left_branch - right_branch
            if node_balance == -2 or node_balance == 2:
                node = self._balance(node, node_balance)
            return node
    
    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return None
        elif key == node.key:
            if node.right is None and node.left is None:
                return None
            elif node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                current = node.right
                while current.left is not None:
                    current = current.left
                node.key = current.key
                node.value = current.value
                node.right = self._delete(current.key, node.right)
                left_branch = node.left.height if node.left is not None else 0
                right_branch = node.right.height if node.right is not None else 0
                node.height = 1 + max(right_branch, left_branch)
                node_balance = left_branch - right_branch
                if node_balance == -2 or node_balance == 2:
                    node = self._balance(node, node_balance)
                return node
        elif key > node.key:
            node.right = self._delete(key, node.right)
            left_branch = node.left.height if node.left is not None else 0
            right_branch = node.right.height if node.right is not None else 0
            node.height = 1 + max(right_branch, left_branch)
            node_balance = left_branch - right_branch
            if node_balance == -2 or node_balance == 2:
                node = self._balance(node, node_balance)
            return node
        else:
            node.left = self._delete(key, node.left)
            left_branch = node.left.height if node.left is not None else 0
            right_branch = node.right.height if node.right is not None else 0
            node.height = 1 + max(right_branch, left_branch)
            node_balance = left_branch - right_branch
            if node_balance == -2 or node_balance == 2:
                node = self._balance(node, node_balance)
            return node

    def print(self):
        self._print(self.root)
        print()

    def _print(self, node):
        if node is not None:
            self._print(node.left)
            print(f"{node.key}:{node.value}", end=',')
            self._print(node.right)

    def height(self):
        return self._height(self.root)
    
    def _height(self, node):
        if node is None:
            return 0
        else:
            l = 1
            r = 1
            if node.left is not None:
                l += self._height(node.left)
            if node.right is not None:
                r += self._height(node.right)
            return max(l, r)
            
    def _left_rotate(self, node):
        new_node = node.right
        moved = new_node.left
        new_node.left = node
        node.right = moved
        new_node.height = self._height(new_node)
        node.height = self._height(node)
        return new_node
        
    def _right_rotate(self, node):
        new_node = node.left
        moved = new_node.right
        new_node.right = node
        node.left = moved
        new_node.height = self._height(new_node)
        node.height = self._height(node)
        return new_node
        
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)

def main():
    tree = AVL()
    elements = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
    for k, v in elements.items():
        tree.insert(k, v)
    tree.print_tree()
    tree.print()
    print(tree.search(10))
    tree.delete(50)
    tree.delete(52)
    tree.delete(11)
    tree.delete(57)
    tree.delete(1)
    tree.delete(12)
    tree.insert(3, "AA")
    tree.insert(4, "BB")
    tree.delete(7)
    tree.delete(8)
    tree.print_tree()
    tree.print()

if __name__ == "__main__":
    main()