# -*- coding:utf-8 -*-

# 第二章拷贝的 Array 原始碼


class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

#####################################################
# heap 實現
#####################################################


class MaxHeap(object):
    """
    Heaps:
    完全二叉树，最大堆的非叶子節點的值都比孩子大，最小堆的非叶子結點的值都比孩子小
    Heap包含兩個屬性，order property 和 shape property(a complete binary tree)，在插入
    一個新節點的時候，始终要保持這兩個屬性
    插入操作：保持堆屬性和完全二叉树屬性, sift-up 操作维持堆屬性
    extract操作：只获取根節點數據，並把树最底层最右節點copy到根節點後，sift-down操作维持堆屬性

    用數組實現heap，從根節點開始，從上往下從左到右给每個節點编号，则根據完全二叉树的
    性质，给定一個節點i， 其父亲和孩子節點的编号分别是:
        parent = (i-1) // 2
        left = 2 * i + 1
        rgiht = 2 * i + 2
    使用數組實現堆一方面效率更高，節省树節點的記憶體占用，一方面還可以避免复杂的指針操作，减少
    調試难度。

    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)  # 维持堆的特性

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[ndx] > self._elements[parent]:    # 如果插入的值大於 parent，一直交換
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)    # 遞迴

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]    # 保存 root 值
        self._count -= 1
        self._elements[0] = self._elements[self._count]    # 最右下的節點放到root後siftDown
        self._siftdown(0)    # 维持堆特性
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # determine which node contains the larger value
        largest = ndx
        if (left < self._count and     # 有左孩子
                self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):  # 原书這個地方没寫實際上找的未必是largest
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        entry = (priority, value)    # 注意這裡把這個 tuple push進去，python 比较 tuple 從第一個開始比较
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    assert res == ['purple', 'orange', 'black', 'white']
