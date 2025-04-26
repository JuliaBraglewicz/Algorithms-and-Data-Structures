from typing import TypeVar

Deleted = TypeVar("Deleted")

class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        
    def __str__(self):
        return str(self.key) + ':' + str(self.data)

class Hash_table:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2
        
    def hash_function(self, key):
        if isinstance(key, str):
            key = sum(ord(char) for char in key)
        return key % self.size
        
    def conflict(self, key, attempt):
        return (self.hash_function(key) + self.c1 * attempt + self.c2 * attempt**2) % self.size
        
    def search(self, key):
        index = self.hash_function(key)
        if self.tab[index] is None:
            return None
        elif self.tab[index] is not Deleted and self.tab[index].key == key:
            return self.tab[index].data
        else:
            for i in range(1, self.size):
                index = self.conflict(key, i)
                if self.tab[index] is Deleted:
                    continue
                elif self.tab[index] is None:
                    return None
                elif self.tab[index].key == key:
                    return self.tab[index].data
        return None
        
    def insert(self, key, data):
        current = None
        index = self.hash_function(key)
        if self.tab[index] is None:
            self.tab[index] = Element(key, data)
            return
        if self.tab[index] is Deleted:
            current = index
        if self.tab[index] is not Deleted and self.tab[index].key == key:
            self.tab[index] = Element(key, data)
            return
        for i in range(1, self.size):
            index = self.conflict(key, i)
            if self.tab[index] is None:
                self.tab[index] = Element(key, data)
                return
            if self.tab[index] is Deleted and current is None:
                if current is None:
                    current = index
                continue
            if self.tab[index] is not None and self.tab[index] is not Deleted and self.tab[index].key == key:
                self.tab[index] = Element(key, data)
                return
        if current is not None:
            self.tab[current] = Element(key, data)
        else:
            print("Brak miejsca")
            
    def remove(self, key):
        index = self.hash_function(key)
        if self.tab[index] is not None and self.tab[index] is not Deleted and self.tab[index].key == key:
            self.tab[index] = Deleted
            return
        if self.tab[index] is None:
            print("Brak danej")
            return
        for i in range(1, self.size):
            index = self.conflict(key, i)
            if self.tab[index] is not None and self.tab[index] is not Deleted and self.tab[index].key == key:
                self.tab[index] = Deleted
                return
            if self.tab[index] is None:
                print("Brak danej")
                return
        print("Brak danej")
            
    def __str__(self):
        text = '{'
        for i in range(self.size):
            if i != self.size - 1:
                if self.tab[i] is Deleted:
                    text += "None, "
                else:
                    text += str(self.tab[i]) + ', '
            else:
                if self.tab[i] is Deleted:
                    text += "None"
                else:
                    text += str(self.tab[i])
        return text + '}'
        
def main():
    def first_test(size, c1 = 1, c2 = 0):
        tab = Hash_table(size, c1, c2)
        let = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        for i in range(1, 16):
            if i == 6:
                tab.insert(18, "F")
            elif i == 7:
                tab.insert(31, "G")
            else:
                tab.insert(i, let[i - 1])
        print(tab)
        print(tab.search(5))
        print(tab.search(14))
        tab.insert(5, "Z")
        print(tab.search(5))
        tab.remove(5)
        print(tab)
        print(tab.search(31))
        tab.insert("test", "W")
        print(tab)
        
    def second_test(size, c1 =1, c2 = 0):
        tab = Hash_table(size, c1, c2)
        let = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        for i in range(1, 16):
            tab.insert(i*13, let[i - 1])
        print(tab)

    first_test(13)
    second_test(13)
    second_test(13, 0, 1)
    first_test(13, 0, 1)

if __name__ == "__main__":
    main()