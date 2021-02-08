# 優先級陣列
你可能比较奇怪，陣列不是早就講了嘛。這裡之所以放到這裡講優先級陣列，是因為雖然名字有陣列，
但其實是使用堆來實現的。上一章講完了堆，這一章我們就趁熱打鐵來實現一個優先級陣列。


# 實現優先級陣列
優先級陣列(Priority Queue) 顧名思義，就是入隊的時候可以给一個優先級，通常是個數字或者時間戳等，
當出隊的時候我們希望按照给定的優先級出隊，我們按照 TDD(測試驅動開發) 的方式先來寫測試原始碼：

```py
def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')    # priority, value
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    assert res == ['purple', 'orange', 'black', 'white']
```

上邊就是期望的行為，寫完測試原始碼後我們來撰寫優先級陣列的原始碼，按照出隊的時候最大優先級先出的順序：


```py
class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        # 注意這裡把這個 tuple push 進去，python 比较 tuple 從第一個開始比较
        # 這樣就很巧妙地實現了按照優先級排序
        entry = (priority, value)    # 入隊的時候會根據 priority 維持堆的特性
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0
```


# 練習题
- 請你實現按照小優先級先出隊的順序的優先級陣列
