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
