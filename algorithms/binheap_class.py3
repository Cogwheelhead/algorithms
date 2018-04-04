class Heap:
    def __init__(self, lst):
        self._heap = lst
        self._traceback = []
        self._heapify()
        
    @property
    def size(self):
        return len(self._heap)

    def _parent(self, i):
        return (i-1) // 2

    def _children(self, i):
        return [c for c in (2*i + 1, 2*i + 2) if c < self.size]
    
    def _swap(self, i, j):
        self._traceback.append((i, j))
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
    
    def _siftup(self, i):
        while i > 0 and self._heap[i] < self._heap[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)
        
    def _siftdown(self, i):
        min_child = min(self._children(i), key=lambda c: self._heap[c]) if self._children(i) else None
        if min_child and min_child != i:
            self._swap(i, min_child)
            self._siftdown(min_child)

    def _heapify(self):
        for i in reversed(range(self.size)):
            self._siftdown(i)

    @property
    def n_swaps(self):
        return len(self._traceback)
    
    def pop(self):
        result = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._siftdown(0)
        return result
            
    def push(self, elem):
        self._heap.append(elem)
        self._siftup(self.size-1)
        
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