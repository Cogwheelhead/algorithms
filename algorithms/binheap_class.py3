from copy import copy


class Heap:
    def __init__(self, xs):
        self._heap = copy(xs)
        self.size = len(xs)
        self._heapify()

    def _parent(self, i):
        return (i-1) // 2

    def _children(self, i):
        return [c for c in (2*i + 1, 2*i + 2) if c < self.size]

    def _swap_values(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _siftup(self, i):
        if i and self._heap[i] < self._heap[self._parent(i)]:
            self._swap_values(i, self._parent(i))
            self._siftup(self._parent(i))

    def _siftdown(self, i):
        m_idx = min([i] + self._children(i), key=lambda c: self._heap[c])
        if m_idx != i:
            self._swap_values(i, m_idx)
            self._siftdown(m_idx)

    def _heapify(self):
        for i in reversed(range(self.size)):
            self._siftdown(i)

    def get_min(self):
        return self._heap[0]

    def push(self, x):
        self._heap.append(x)
        self._siftup(self.size)
        self.size += 1

    def pop(self):
        self._swap_values(0, -1)
        self.size -= 1
        self._siftdown(0)
        return self._heap.pop()

    def remove(self, i):
        self._heap[i] = float('-inf')
        self._siftup(i)
        self.pop()

    def set_priority(self, i, p):
        old = self._heap[i]
        self._heap[i] = p
        if p < old:
            self._siftup(i)
        elif p > old:
            self._siftdown(i)
