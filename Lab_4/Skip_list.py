import random

class Element:
    def __init__(self, key, data, level):
        self.key = key
        self.data = data
        self.level = level
        self.tab = [None for _ in range(level)]

class Skip_list:
    def __init__(self, maxlevel):
        self.maxlevel = maxlevel
        self.head = Element(None, None, maxlevel)

    def randomLevel(self, p = 0.5):
        lvl = 1   
        while random.random() < p and lvl < self.maxlevel:
                lvl = lvl + 1
        return lvl
        
    def search(self, key):
        current = self.head
        for i in range(self.maxlevel-1, -1, -1):
            while current.tab[i] is not None and current.tab[i].key < key:
                current = current.tab[i]
        current = current.tab[0]
        if current is None or current.key != key:
            return None
        return current.data
        
    def insert(self, key, data):
        prev = [None for _ in range(self.maxlevel)]
        current = self.head
        for i in range(self.maxlevel-1, -1, -1):
            while current.tab[i] is not None and current.tab[i].key < key:
                current = current.tab[i]
            prev[i] = current
        if current.tab[0] is not None and current.tab[0].key == key:
            current.tab[0].data = data
        else:
            elem = Element(key, data, self.randomLevel())
            for i in range(elem.level):
                elem.tab[i] = prev[i].tab[i]
                prev[i].tab[i] = elem

    def remove(self, key):
        prev = [None for _ in range(self.maxlevel)]
        current = self.head
        for i in range(self.maxlevel-1, -1, -1):
            while current.tab[i] is not None and current.tab[i].key < key:
                current = current.tab[i]
            prev[i] = current
        current = current.tab[0]
        if current is not None and current.key == key:
            for i in range(current.level):
                if prev[i].tab[i] != current:
                    break
                prev[i].tab[i] = current.tab[i]

    def __str__(self):
        text = '['
        current = self.head.tab[0]
        while current is not None:
            text += str(current.key) + ':' + str(current.data)
            if current.tab[0] is not None:
                text += ", "
            current = current.tab[0]
        return text + "]"
    
    def displayList_(self):
        node = self.head.tab[0]  # pierwszy element na poziomie 0
        keys = [ ]                        # lista kluczy na tym poziomie
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.maxlevel - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()
    
def main():
    random.seed(42)
    list = Skip_list(5)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(15):
        list.insert(i + 1, letters[i])
    list.displayList_()
    print(list.search(2))
    list.insert(2, "Z")
    print(list.search(2))
    for i in range(5, 8):
        list.remove(i)
    print(list)
    list.insert(6, "W")
    print(list)

    list_back = Skip_list(5)
    for i in range(15, 0, -1):
        list_back.insert(i, letters[15 - i])
    list_back.displayList_()
    print(list_back.search(2))
    list_back.insert(2, "Z")
    print(list_back.search(2))
    for i in range(5, 8):
        list_back.remove(i)
    print(list_back)
    list_back.insert(6, "W")
    print(list_back)
    
if __name__ == "__main__":
    main()
        