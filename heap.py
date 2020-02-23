
class Node:

    def __init__(self, pos, dist):
        self.pos = pos
        self.dist = dist

class Heap:

    def __init__(self):

        self.elem = list()

    def parent(self, x):
        return (x - 1) >> 1

    def left_child(self, x):
        return (x << 1) + 1

    def right_child(self, x):
        return  (x << 1) + 2

    def swap(self, a, b):
        temp = self.elem[a]
        self.elem[a] = self.elem[b]
        self.elem[b] = temp

    def sift_down(self, id):

        min_flag = False
        while self.left_child(id) < len(self.elem) and not min_flag:

            lower = self.left_child(id)
            if self.right_child(id) < len(self.elem) \
                and self.elem[self.right_child(id)] < self.elem[self.left_child(id)]:
                lower = self.right_child(id)

            if self.elem[lower] < self.elem[id]:
                self.swap(id, lower)
            else:
                min_flag = True

    def sift_up(self, id):

        min_flag = False
        while id > 0 and not min_flag:
            if self.elem[self.parent(id)] > self.elem[id]:
                self.swap(id, self.parent(id))
            else:
                min_flag = True

    def insert(self, node):
        self.elem.append(node)
        self.sift_up(len(self.elem) - 1)

    def pop(self):

        ret = self.elem[0]

        self.elem[0] = self.elem.pop()
        self.sift_down(0)

        return ret
