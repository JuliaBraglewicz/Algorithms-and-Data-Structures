class Node():
    def __init__(self, max_children):
        self.keys = []
        self.children = [None for _ in range(max_children)]
        self.size = 0
        self.max_children = max_children

    def add(self, key, new_node = None):
        if new_node is not None:
            if self.size < self.max_children - 1:
                self.add(key)
                i = 0
                while self.keys[i] < key:
                    i += 1
                i += 1
                self.children.insert(i, new_node)
                del self.children[-1]
                return None
            elif self.size == self.max_children - 1:
                new_node_2 = Node(self.max_children)
                middle = self.keys[self.size //2]
                new_node_2.keys = self.keys[self.size // 2 + 1:]
                new_node_2.size = len(new_node_2.keys)
                new_node_2.children[0:self.max_children // 2] = self.children[self.max_children // 2:]
                self.children[self.max_children // 2:] = [None] * (self.max_children // 2)
                self.keys = self.keys[:self.size // 2]
                self.size = len(self.keys)
                if key > middle:
                    new_node_2.add(key)
                    i = 0
                    while new_node_2.keys[i] < key:
                        i += 1
                    i += 1
                    new_node_2.children.insert(i, new_node)
                    del new_node_2.children[-1]
                else:
                    self.add(key)
                    i = 0
                    while self.keys[i] < key:
                        i += 1
                    i += 1
                    self.children.insert(i, new_node)
                    del self.children[-1]
                return middle, new_node_2
        else:
            if self.size != len(self.children) - 1:
                i = 0
                while i < self.size and key >= self.keys[i]:
                    i += 1
                self.keys.insert(i, key)
                self.size += 1
                return None
            else:
                new_node = Node(self.max_children)
                middle = self.keys[self.size // 2]
                new_node.keys = self.keys[self.size // 2 + 1:]
                new_node.size = len(new_node.keys)
                self.keys = self.keys[:self.size // 2]
                self.size = len(self.keys)
                if key > middle:
                    new_node.add(key)
                else:
                    self.add(key)
                return middle, new_node

class B_Tree():
    def __init__(self, max_children):
        self.root = None
        self.max_children = max_children

    def insert(self, key):
        if self.root is None:
            self.root = Node(self.max_children)
            self.root.add(key)
        else:
            self.root = self._insert(key, self.root)

    def _insert(self, key, node):
        i = 0
        while i < node.size - 1 and node.keys[i] <= key:
            i += 1
        if node.children[0] is not None:
            if key > node.keys[i]:
                result = self._insert(key, node.children[i + 1])
            else:
                result = self._insert(key, node.children[i])
            if isinstance(result, tuple):
                result = node.add(result[0], result[1])
                if node == self.root and result is not None:
                    new_root = Node(self.max_children)
                    new_root.add(result[0])
                    new_root.children[0] = node
                    new_root.children[1] = result[1]
                    node = new_root
                elif result is not None:
                    return result
            return node
        else:
            result = node.add(key)
            if result is not None and node == self.root:
                new_root = Node(self.max_children)
                new_root.add(result[0])
                new_root.children[0] = node
                new_root.children[1] = result[1]
                node = new_root
            elif result is not None:
                return result
            return node

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(node.size + 1): 	                	
                self._print_tree(node.children[i], lvl + 1)
                if i < node.size:
                    print(lvl*'  ', node.keys[i])	

def main():
    tree = B_Tree(4)
    for key in [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]:
        tree.insert(key)
    tree.print_tree()

    tree_2 = B_Tree(4)
    for i in range(20):
        tree_2.insert(i)
    tree_2.print_tree()

    for i in range(20, 200):
        tree_2.insert(i)
    tree_2.print_tree()

    tree_3 = B_Tree(6)
    for i in range(200):
        tree_3.insert(i)
    tree_3.print_tree()

if __name__ == "__main__":
    main()