import random
import time

class Element:
    def __init__(self, priorytet, dane):
        self.__dane = dane
        self.__priorytet = priorytet

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet
    
    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"
    
class Heap:
    def __init__(self, tab = None):
        if tab is None:
            self.tab = []
            self.size = 0
        else:
            self.tab = tab
            self.size = len(tab)
            for i in range(self.size // 2 - 1, -1, -1):
                self._fix(i)

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

def insertion(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key

def shell(tab):
    h = 1
    while h * 3 + 1 < len(tab) / 3:
        h = h * 3 + 1
    while h > 0:
        for i in range(h, len(tab)):
            current = tab[i]
            j = i
            while j >= h and tab[j - h] > current:
                tab[j] = tab[j - h]
                j -= h
            tab[j] = current
        h //= 3


# def shell(tab): #alternatywna wersja ze swapowaniem (wolniejsza w tym przypadku)
#     h = 1
#     while h * 3 + 1 < len(tab) / 3:
#         h = h * 3 + 1
#     while h > 0:
#         for i in range(h, len(tab)):
#             j = i
#             while j >= h and tab[j - h] > tab[j]:
#                 tab[j], tab[j - h] = tab[j - h], tab[j]
#                 j -= h
#         h //= 3

def main():
    lst = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    tab_1 = [Element(key, value) for key, value in lst]
    tab_2 = tab_1.copy()
    
    insertion(tab_1)
    print(tab_1)
    print("STABILNE")
        
    shell(tab_2)
    print(tab_2)
    print("STABILNE")

    tab_3 = [int(random.random() * 100) for i in range(10000)]
    tab_4 = tab_3.copy()
    tab_5 = tab_3.copy()

    t_start = time.perf_counter()
    insertion(tab_3)
    t_stop = time.perf_counter()
    print("Czas obliczeń insertion sort:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    shell(tab_4)
    t_stop = time.perf_counter()
    print("Czas obliczeń shell sort:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    heap = Heap(tab_5)
    for _ in range(10000):
        heap.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń heap sort:", "{:.7f}".format(t_stop - t_start))

if __name__ == "__main__":
    main()