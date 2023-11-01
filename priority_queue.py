class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.size = 0

    def __sizeof__(self):
        return self.size

    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def push(self, val):
        self.heap.append(val)
        ch = self.size
        self.size += 1

        while ch > 0:
            par = (ch - 1) // 2
            if self.heap[par] < self.heap[ch]:
                self.swap(par, ch)
            else:
                break
            ch = par

    def pop(self):
        self.swap(-1, 0)
        self.size -= 1
        par = 0
        while True:
            ch1 = par * 2 + 1
            ch2 = ch1 + 1
            if ch2 < self.size:
                if self.heap[ch1] > self.heap[ch2]:
                    if self.heap[par] < self.heap[ch1]:
                        self.swap(par, ch1)
                        par = ch1
                elif self.heap[par] < self.heap[ch2]:
                    self.swap(par, ch2)
                    par = ch2
                else:
                    break
            elif ch1 < self.size and self.heap[par] < self.heap[ch1]:
                self.swap(par, ch1)
                par = ch1
            else:
                break
        return self.heap.pop(-1)

    def top(self):
        return self.heap[0]


pr = PriorityQueue()
pr.push(4)
pr.push(2)
pr.push(3)
pr.push(5)
pr.push(6)

print(pr.pop(), pr.heap)

print(pr.pop(), pr.heap)