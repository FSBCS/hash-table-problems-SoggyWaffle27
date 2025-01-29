class PriorityQueue():
    def __init__(self):
        self.queue = [100, 10, 5, 6 , 4, 3, 1, 2, 1]
    def parent(self, n):
        return n // 2
    def children(self, n):
        return n * 2, n * 2 + 1 
    def insert(self, n):
        self.queue.append(n)
        self.swap(len(self.queue)-1)
    def swap(self, n):
        parent = self.parent(n)
        print(self.queue[parent], self.queue[n])
        if self.queue[parent] < self.queue[n]:
            self.queue[parent], self.queue[n] = self.queue[n], self.queue[parent]
            self.swap(parent)
        return
    def display(self):
        print(self.queue)
PQ = PriorityQueue()
PQ.insert(45)
print([100, 10, 5, 6 , 4, 3, 1, 2, 1])
PQ.display()
