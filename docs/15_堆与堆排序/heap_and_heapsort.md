# 堆(heap)
前面我們講了兩種使用分治和遞迴解决排序問題的归并排序和快速排序，中間又穿插了一把树和二叉树，
本章我們開始介绍另一種有用的數據結構堆(heap)， 以及借助堆來實現的堆排序，相比前兩種排序算法要稍难實現一些。
最後我們簡單提一下 python 标准库内置的 heapq 模块。


# 什么是堆？
堆是一種完全二叉树（請你回顾下上一章的概念），有最大堆和最小堆兩種。

- 最大堆: 對于每個非叶子節點 V，V 的值都比它的兩個孩子大，称為 最大堆特性(heap order property)
最大堆里的根总是存储最大值，最小的值存储在叶節點。
- 最小堆：和最大堆相反，每個非叶子節點 V，V 的兩個孩子的值都比它大。

![](./heap.png)

# 堆的操作
堆提供了很有限的几個操作：

- 插入新的值。插入比较麻烦的就是需要维持堆的特性。需要 sift-up 操作，具體會在影片和代碼里解释，文字描述起來比较麻烦。
- 获取并移除根節點的值。每次我們都可以获取最大值或者最小值。這個时候需要把底层最右邊的節點值替换到 root 節點之後
执行 sift-down 操作。

![](./siftup.png)
![](./siftdown.png)

# 堆的表示
上一章我們用一個節點类和二叉树类表示树，這裡其实用数组就能實現堆。

![](heap_array.png)

仔细觀察下，因為完全二叉树的特性，树不會有間隙。對于数组里的一個下标 i，我們可以得到它的父亲和孩子的節點對应的下标：

```
parent = int((i-1) / 2)    # 取整
left = 2 * i + 1
right = 2 * i + 2
```
超出下标表示没有對应的孩子節點。

# 實現一個最大堆
我們将在影片里详细描述和编写各個操作

```py
class MaxHeap(object):
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
            if self._elements[ndx] > self._elements[parent]:    # 如果插入的值大于 parent，一直交换
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
                self._elements[left] >= self._elements[right]):  # 原书這個地方没写实际上找的未必是largest
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


def test_maxheap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()
```

# 實現堆排序
上邊我們實現了最大堆，每次我們都能 extract 一個最大的元素了，于是一個倒序排序函数就能很容易写出來了：

```py
def heapsort_reverse(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    res = []
    for i in range(length):
        res.append(maxheap.extract())
    return res


def test_heapsort_reverse():
    import random
    l = list(range(10))
    random.shuffle(l)
    assert heapsort_reverse(l) == sorted(l, reverse=True)
```

# Python 里的 heapq 模块
python 其实自带了 heapq 模块，用來實現堆的相關操作，原理是类似的。請你閱讀相關文档并使用内置的 heapq 模块完成堆排序。
一般我們刷题或者写业务代碼的时候，使用這個内置的 heapq 模块就够用了，内置的實現了是最小堆。


# Top K 問題
面试题中有這样一类問題，让求出大量數據中的top k 個元素，比如一亿個数字中最大的100個数字。
對于這種問題有很多種解法，比如直接排序、mapreduce、trie 树、分治法等，當然如果内存够用直接排序是最簡單的。
如果内存不够用呢？ 這裡我們提一下使用固定大小的堆來解决這個問題的方式。

一開始的思路可能是，既然求最大的 k 個数，是不是应该维护一個包含 k 個元素的最大堆呢？
稍微嘗試下你會发现走不通。我們先用数组的前面 k 個元素建立最大堆，然後對剩下的元素进行比對，但是最大堆只能每次获取堆顶
最大的一個元素，如果我們取下一個大于堆顶的值和堆顶替换，你會发现堆底部的小数一直不會被换掉。如果下一個元素小于堆顶
就替换也不對，這样可能最大的元素就被我們丢掉了。

相反我們用最小堆呢？
先迭代前 k 個元素建立一個最小堆，之後的元素如果小于堆顶最小值，跳過，否则替换堆顶元素并重新调整堆。你會发现最小堆里
慢慢就被替换成了最大的那些值，并且最後堆顶是最大的 topk 個值中的最小值。
（比如1000個数找10個，最後堆里剩余的是 [990, 991, 992, 996, 994, 993, 997, 998, 999, 995]，第一個 990 最小)

按照這個思路很容易写出來代碼：

```py
import heapq


class TopK:
    """获取大量元素 topk 大個元素，固定内存
    思路：
    1. 先放入元素前 k 個建立一個最小堆
    2. 迭代剩余元素：
        如果當前元素小于堆顶元素，跳過该元素（肯定不是前 k 大）
        否则替换堆顶元素為當前元素，并重新调整堆
    """

    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:  # 當然你可以直接 if val > min_val操作，這裡我只是显示指出跳過這個元素
                pass
            else:
                heapq.heapreplace(self.minheap, val)  # 返回并且pop堆顶最小值，推入新的 val 值并调整堆
        else:
            heapq.heappush(self.minheap, val)  # 前面 k 個元素直接放入minheap

    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap


def test():
    import random
    i = list(range(1000))  # 這裡可以是一個可迭代元素，節省内存
    random.shuffle(i)
    _ = TopK(i, 10)
    print(_.get_topk())  # [990, 991, 992, 996, 994, 993, 997, 998, 999, 995]


if __name__ == '__main__':
    test()
```


# 练习题

- 這裡我用最大堆實現了一個 heapsort_reverse 函数，請你實現一個正序排序的函数。似乎不止一種方式
- 請你實現一個最小堆，你需要修改那些代碼呢？
- 我們實現的堆排序是 inplace 的嗎，如果不是，你能改成 inplace 的嗎？
- 堆排序的時間複雜度是多少？ siftup 和 siftdown 的時間複雜度是多少？（小提示：考虑树的高度，它决定了操作次数）
- 請你思考 Top K 問題的時間複雜度是多少？


# 延伸閱讀
- 《算法导论》第 6 章 Heapsort
- 《Data Structures and Algorithms in Python》 13.5 節 Heapsort
- 閱讀 Python heapq 模块的文档

# Leetcode

合并 k 個有序鏈表 https://leetcode.com/problems/merge-k-sorted-lists/description/
