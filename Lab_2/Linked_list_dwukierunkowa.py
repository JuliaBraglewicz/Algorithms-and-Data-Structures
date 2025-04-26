class List:
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None
        
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def destroy(self):
        node = self.head
        while node is not None:
            node.prev = None
            node = node.next
        self.head = None
        self.tail = None
        
    def add(self, data):
        new_head = List(data)
        if self.head is not None:
            new_head.next = self.head
            self.head.prev = new_head
        self.head = new_head
        if new_head.next is None:
            self.tail = self.head
        
    def append(self, data):
        new_node = List(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            last = self.tail
            last.next = new_node
            new_node.prev = last
            self.tail = new_node
        
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
    
    def remove_end(self):
        if self.head is not None:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                last = self.tail
                self.tail = last.prev
                self.tail.next = None
                last.prev = None
        
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
            
    def length(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count
            
    def get(self):
        if self.head is None:
            return None
        return self.head.data
        
    def get_last(self):
        if self.tail is None:
            return None
        return self.tail.data
        
    def __str__(self):
        text = ''
        if self.head is None:
            return text
        else:
            current = self.head
            while current.next is not None:
                text += '-> ' + str(current.data) + '\n'
                current = current.next
            return text + '-> ' + str(current.data)
            
    def str_back(self):
        text = ''
        if self.tail is None:
            return text
        else:
            current = self.tail
            while current.prev is not None:
                text += '-> ' + str(current.data) + '\n'
                current = current.prev
            return text + '-> ' + str(current.data)
        
def main():
    list = [('AGH', 'Kraków', 1919),('UJ', 'Kraków', 1364),('PW', 'Warszawa', 1915),('UW', 'Warszawa', 1915),('UP', 'Poznań', 1919),('PG', 'Gdańsk', 1945)]
    uczelnie = Linked_list()
    uczelnie.append(list[0])
    uczelnie.append(list[1])
    uczelnie.append(list[2])
    for i in range(3, len(list)):
        uczelnie.add(list[i])
    print(str(uczelnie) + '\n')
    print(uczelnie.str_back())
    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(str(uczelnie) + '\n')
    print(uczelnie.str_back())
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.append(list[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())
    
if __name__ == "__main__":
    main()