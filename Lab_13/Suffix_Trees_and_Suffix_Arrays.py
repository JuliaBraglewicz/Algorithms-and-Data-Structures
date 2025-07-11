#not finished yet

class SuffixNode:
    def __init__(self, key = None, is_root = False):
        self.key = key
        self.is_leaf = False
        self.is_root = is_root
        if self.is_root:
            self.children = []
            self.chars = []
        else:
            self.left = None
            self.right = None

class SuffixTree:
    def __init__(self):
        self.root = SuffixNode(is_root = True)

    def build(self, text):
        for i in range(len(text)):
            self.insert(text[i:])

    def insert(self, text):
        current = self.root
        for char in text:
            if current is self.root and (char not in current.chars or len(current.chars) == 0):
                current.children.append(SuffixNode(char))
                current.chars.append(char)
                current = current.children[-1]
            elif current.left is not None and current.left.key != char:
                current.right = SuffixNode(char)
            elif current.left is None:
                current.left = SuffixNode(char)
        current.is_leaf = True

    # def compress(self, node):
    #     if len(node.next) == 1: # dokonczyc


    # def print_tree(self):
    #     print("==============")
    #     for i in range(len(self.root.children)):
    #         self.__print_tree(self.root.children[i], 0)
    #     print("==============")

    # def __print_tree(self, node, lvl):
    #     if node!=None:
    #         self.__print_tree(node.right, lvl+5)

    #         print()
    #         print(lvl*" ", node.key)
     
    #         self.__print_tree(node.left, lvl+5)


def main():
    T = "banana\0"
    print(len(T[:]))

    tree = SuffixTree()
    tree.build(T)
    print(len(tree.root.children))

if __name__ == "__main__":
    main()