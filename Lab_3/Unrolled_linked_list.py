SIZE = 6

class Element:
    def __init__(self):
        self.tab = [None for i in range(SIZE)]
        self.count = 0
        self.next = None
        
    def add(self, data, index):
        if index < 0 or (self.count == SIZE and index >= SIZE):
            raise IndexError("Index out of range")
        if self.count == SIZE:
            raise OverflowError("Node is full")
        if index >= self.count:
            self.tab[self.count] = data
        else:
            for i in range(self.count, index, -1):
                self.tab[i] = self.tab[i-1]
            self.tab[index] = data
        self.count += 1
        
    def remove(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        if index < self.count:
            for i in range(index, self.count - 1):
                self.tab[i] = self.tab[i+1]
            self.tab[self.count - 1] = None
            self.count -= 1
            
    def __str__(self):
        return str(self.tab)
            
            
class Unrolled_Linked_List:
    def __init__(self):
        self.head = None
        
    def get(self, index):
        if self.head is not None:
            current = self.head
            while index >= current.count:
                if current.next is not None:
                    index -= current.count
                    current = current.next
                else:
                    return None
            return current.tab[index]
        else:
            return None
        
    def insert(self, data, index):
        if index < 0:
            raise IndexError("Index out of range")
        if self.head is None:
            self.head = Element()
        current = self.head
        while index >= current.count:
            if current.next is None:
                break
            if current.count == index and current.count != SIZE:
                break
            index -= current.count
            current = current.next
        if current.count == SIZE:
            if current.next is not None:
                tail = current.next
                current.next = Element()
                current.next.next = tail
            else:
                current.next = Element()
            if index >= SIZE:
                current.next.add(data, index)
            else:
                for i in range(SIZE, SIZE - int(SIZE/2), -1):
                    current.next.add(current.tab[i-1], 0)
                    current.remove(i-1)
                current.add(data, index)
        else:
            current.add(data, index)

    def delete(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        if self.head is not None:
            current = self.head
            while index >= current.count:
                if current.next is None:
                    break
                index -= current.count
                current = current.next
            current.remove(index) #dokonczyc
            if current.count < SIZE/2 and current.next is not None:
                while current.count < SIZE/2 and current.next.count != 0:
                    current.add(current.next.tab[0], current.count)
                    current.next.remove(0)
                if current.next.count < SIZE/2:
                    for i in range(current.next.count):
                        current.add(current.next.tab[0], current.count)
                        current.next.remove(0)
                    if current.next.next is not None:
                        tail = current.next.next
                        current.next = None
                        current.next = tail
                    else:
                        current.next = None

    def __str__(self):
        current = self.head
        text = str(self.head)
        if current is not None:
            while current.next is not None:
                current = current.next
                text += '->' +str(current)
        return text

def main():
    list = Unrolled_Linked_List()
    for i in range(9):
        list.insert(i+1, i)
    print(list.get(4))
    list.insert(10, 1)
    list.insert(11, 8)
    print(list)
    list.delete(1)
    list.delete(2)
    print(list)

if __name__ == "__main__":
    main()