class Element:
    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet
    
    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"
    
class Priority_Queue:
    def __init__(self):
        self.tab = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.tab[0]

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            high_elem = self.tab[0]
            self.tab[0], self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]
            self.size -= 1
            self._fix(0)
            return high_elem

    def _fix(self, index):
        left = self._left(index)
        right = self._right(index)
        new_index = index
        if right < self.size and self.tab[right] > self.tab[new_index]:
            new_index = right
        if left < self.size and self.tab[left] > self.tab[new_index]:
            new_index = left
        if new_index != index:
            self.tab[index], self.tab[new_index] = self.tab[new_index], self.tab[index]
            self._fix(new_index)

    def enqueue(self, element):
        if self.size == len(self.tab):
            self.tab.append(element)
        else:
            self.tab[self.size] = element
        index = self.size
        self.size += 1
        while index > 0 and self.tab[index] > self.tab[self._parent(index)]:
            self.tab[index], self.tab[self._parent(index)] = self.tab[self._parent(index)], self.tab[index]
            index = self._parent(index)

    def _left(self, index):
        return 2 * index + 1
    
    def _right(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
        
    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end = ' ')
        print( '}')
        
    def print_tree(self, idx, lvl):
        if idx < self.size:           
            self.print_tree(self._right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self._left(idx), lvl+1)
        
def main():
    queue = Priority_Queue()
    prio = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    data = ["G", "R", "Y", "M", "O", "T", "Y", "L", "A"]
    for i in range(9):
        queue.enqueue(Element(data[i], prio[i]))
    queue.print_tree(0, 0)
    queue.print_tab()
    deleted = queue.dequeue()
    print(queue.peek())
    queue.print_tab()
    print(deleted)
    while not queue.is_empty():
        print(queue.dequeue())
    queue.print_tab()

if __name__ == "__main__":
    main()