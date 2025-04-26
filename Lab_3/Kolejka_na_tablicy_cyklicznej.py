class Queue:
    def __init__(self, size = 5):
        self.size = size
        self.tab = [None for i in range(self.size)]
        self.read = 0
        self.write = 0
        
    def is_empty(self):
        if self.read == self.write and self.tab[self.read] is None:
            return True
        else:
            return False
            
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read]
            
    def dequeue(self):
        if self.is_empty():
            return None
        val = self.tab[self.read]
        self.tab[self.read] = None
        if self.read == self.size - 1:
            self.read = 0
            return val
        else:
            self.read += 1
            return val
            
    def enqueue(self, data):
        if (self.write + 1) % self.size == self.read:
            tab = [None for i in range(self.size)]
            self.tab = self.tab[:self.write+1] + tab + self.tab[self.read:]
            self.read += self.size
            self.size *= 2
        self.tab[self.write] = data
        if self.write == self.size - 1:
            self.write = 0
        else:
            self.write += 1
            
    def __str__(self):
        text = '['
        if not self.is_empty():
            if self.read <= self.write:
                for i in range(self.read, self.write):
                    text += str(self.tab[i])
                    if i != self.write - 1:
                        text += ', '
            else:
                for j in range(self.read, self.size):
                    text += str(self.tab[j])
                    if self.write != 0:
                        text += ', '
                    elif j != self.size - 1:
                        text += ', '
                for k in range(self.write):
                    text += str(self.tab[k])
                    if k != self.write - 1:
                        text += ', '
        return text + ']'
        
    def status(self):
        return self.tab
        
def main():
    queue = Queue()
    for i in range(1, 5):
        queue.enqueue(i)
    print(queue.dequeue())
    print(queue.peek())
    print(queue)
    for i in range(5, 9):
        queue.enqueue(i)
    print(queue.status())
    while not queue.is_empty():
        print(queue.dequeue())
    print(queue)
    
if __name__ == "__main__":
    main()