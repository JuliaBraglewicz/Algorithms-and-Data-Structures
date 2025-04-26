class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

class BST:
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
        
    def insert(self, key, data):
        self.root = self._insert(key, data, self.root)
    
    def _insert(self, key, data, node):
        if node is None:
            return Node(key, data)
        elif node.key == key:
            node.value = data
        elif key > node.key:
            node.right = self._insert(key, data, node.right)
        else:
            node.left = self._insert(key, data, node.left)
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
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            node.left = self._delete(key, node.left)
        return node

    def print(self):
        self._print(self.root)
        print()

    def _print(self, node):
        if node is not None:
            self._print(node.left)
            print(f"{node.key} {node.value}", end=',')
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
    tree = BST()
    elements = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for k, v in elements.items():
        tree.insert(k, v)
    tree.print_tree()
    tree.print()
    print(tree.search(24))
    tree.insert(20, "AA")
    tree.insert(6, "M")
    tree.delete(62)
    tree.insert(59, "N")
    tree.insert(100, "P")
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, "R")
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print()
    tree.print_tree()

if __name__ == "__main__":
    main()