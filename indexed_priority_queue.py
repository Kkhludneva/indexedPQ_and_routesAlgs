class IndexPriorityQueue:

    def __init__(self, order=True):
        self.heap = []
        self.val = {}
        self.pos_in_heap = {}
        if order:
            self.sift_up = self.sift_up_max
            self.sift_down = self.sift_down_max
        else:
            self.sift_up = self.sift_up_min
            self.sift_down = self.sift_down_min

    def __str__(self):
        heap = '['
        for key in self.heap:
            heap += str(key) + ':' + str(self.val[key]) + ', '
        return 'val '+str(self.val)+'\nheap '+heap[:-2] + ']' + '\npos_in_heap ' + str(self.pos_in_heap)+'\n'

    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]
        self.pos_in_heap[self.heap[i1]], self.pos_in_heap[self.heap[i2]] = self.pos_in_heap[self.heap[i2]], self.pos_in_heap[self.heap[i1]]

    def sift_up_max(self, ch):
        while ch > 0:
            par = (ch - 1) // 2
            # из кучи берём индексы
            ch_key = self.heap[ch]
            par_key = self.heap[par]
            # по индексам берём значение
            ch_val = self.val[ch_key]
            par_val = self.val[par_key]
            if par_val < ch_val:
                self.swap(ch, par)
            else:
                break
            ch = par

    def sift_up_min(self, ch):
        while ch > 0:
            par = (ch - 1) // 2
            # из кучи берём индексы
            ch_key = self.heap[ch]
            par_key = self.heap[par]
            # по индексам берём значение
            ch_val = self.val[ch_key]
            par_val = self.val[par_key]
            if par_val > ch_val:
                self.swap(ch, par)
            else:
                break
            ch = par

    def sift_down_min(self, par):
        ch1 = par * 2 + 1
        ch2 = ch1 + 1
        while ch1 < len(self.heap):
            ch1_val = self.val[self.heap[ch1]]
            par_val = self.val[self.heap[par]]

            if ch2 >= len(self.heap):
                if par_val > ch1_val:
                    self.swap(par, ch1)
                break
            else:
                ch2_val = self.val[self.heap[ch2]]

                min_ch_val = min(ch1_val, ch2_val)
                if ch1_val == min_ch_val:
                    min_ch = ch1
                else:
                    min_ch = ch2

                if par_val > min_ch_val:
                    self.swap(par, min_ch)
                    par = min_ch
                else:
                    break
            ch1 = par * 2 + 1
            ch2 = ch1 + 1

    def sift_down_max(self, par):
        ch1 = par * 2 + 1
        ch2 = ch1 + 1
        while ch1 < len(self.heap):
            ch1_val = self.val[self.heap[ch1]]
            par_val = self.val[self.heap[par]]

            if ch2 >= len(self.heap):
                if par_val < ch1_val:
                    self.swap(par, ch1)
                break
            else:
                ch2_val = self.val[self.heap[ch2]]

                max_ch_val = max(ch1_val, ch2_val)
                if ch1_val == max_ch_val:
                    max_ch = ch1
                else:
                    max_ch = ch2

                if par_val < max_ch_val:
                    self.swap(par, max_ch)
                    par = max_ch
                else:
                    break
            ch1 = par * 2 + 1
            ch2 = ch1 + 1

    def empty(self):
        return len(self.heap) == 0

    def push(self, key, val):
        self.val[key] = val
        self.heap.append(key)
        self.pos_in_heap[key] = len(self.heap) - 1

        ch = len(self.heap) - 1
        self.sift_up(ch)

    def pop(self, key=None):
        popped_pos = 0 if key is None else self.pos_in_heap[key]
        self.swap(-1, popped_pos)
        popped_key = self.heap.pop(-1)
        self.pos_in_heap.pop(popped_key)
        popped_value = self.val.pop(popped_key)
        par = 0
        self.sift_down(par)
        return [popped_key, popped_value]

    def get_val(self, key):
        if key not in self.val:
            return None
        return self.val[key]

    def changeAtKey(self, key, value):
        if key not in self.val:
            return
        else:
            self.val[key] = value
            pos = self.pos_in_heap[key]
            self.sift_up(pos)
            self.sift_down(pos)

    def top(self):
        return [self.heap[0], self.val[self.heap[0]]]

#
# ipr = IndexPriorityQueue(True)
# ipr.push(0, 15)
# ipr.push(1, 9)
# ipr.push(2, 10)
# ipr.push(3, 8)
# ipr.push(4, 6)
# ipr.push(5, 13)
#
# print(ipr)
# ipr.push(6, 14)
# print(ipr)
