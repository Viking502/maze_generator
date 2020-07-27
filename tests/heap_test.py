import unittest
import heap


class TestHeap(unittest.TestCase):

    def test_insert(self):
        cont = heap.Heap()
        for i in reversed(range(10)):
            temp = heap.Node(i, (0, 0), i)
            cont.insert(temp)
            self.assertEqual(temp, cont.elem[0])

    def test_sort(self):

        cont = heap.Heap()
        tab = [heap.Node(i, (0, 0), i) for i in reversed(range(10))]
        for i in tab:
            cont.insert(i)
        for e in sorted(tab):
            self.assertEqual(e, cont.pop())


if __name__ == '__main__':
    unittest.main()
