class Node:

    def __init__(self, position, direction, cost):
        self.pos = position
        self.dir = direction
        self.cost = cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __str__(self):
        return f'({self.pos}, {self.dir}, {self.cost})'


class Heap:

    def __init__(self):
        self.elem = list()

    @staticmethod
    def parent(x):
        return (x - 1) >> 1

    @staticmethod
    def left_child(x):
        return (x << 1) + 1

    @staticmethod
    def right_child(x):
        return (x << 1) + 2

    def swap(self, a, b):
        temp = self.elem[a]
        self.elem[a] = self.elem[b]
        self.elem[b] = temp

    def sift_down(self, idx):
        min_flag = False
        while self.left_child(idx) < len(self.elem) and not min_flag:
            lower = self.left_child(idx)
            if self.right_child(idx) < len(self.elem) \
                    and self.elem[self.right_child(idx)] < self.elem[self.left_child(idx)]:
                lower = self.right_child(idx)
            if self.elem[lower] < self.elem[idx]:
                self.swap(idx, lower)
                idx = lower
            else:
                min_flag = True

    def sift_up(self, idx):
        min_flag = False
        while idx > 0 and not min_flag:
            if self.elem[idx] < self.elem[self.parent(idx)]:
                self.swap(idx, self.parent(idx))
                idx = self.parent(idx)
            else:
                min_flag = True

    def insert(self, node):
        self.elem.append(node)
        self.sift_up(len(self.elem) - 1)

    def pop(self):
        ret = self.elem[0]
        temp = self.elem.pop()
        if self.elem:
            self.elem[0] = temp
        self.sift_down(0)
        return ret

