"""
python3 only
LRU cache
"""
from collections import OrderedDict
from functools import wraps


def fib(n):
    if n <= 1:  # 0 or 1
        return n
    return f(n - 1) + f(n - 2)  # 由於涉及到重复計算，這個遞迴函數在 n 大了以後會非常慢。 O(2^n)


"""
下邊就來寫一個缓存装饰器來優化它。傳统方法是用個數組记录之前計算過的值，但是這種方式不够 Pythonic
"""


def cache(func):
    """先引入一個簡單的装饰器缓存，其實原理很簡單，就是内部用一個字典缓存已經計算過的結果"""
    store = {}

    @wraps(func)
    def _(n):   # 這裡函數没啥意義就随便用下划線命名了
        if n in store:
            return store[n]
        else:
            res = func(n)
            store[n] = res
            return res
    return _


@cache
def f(n):
    if n <= 1:  # 0 or 1
        return n
    return f(n - 1) + f(n - 2)


"""
問題來了，假如空間有限怎麼办，我們不可能一直向缓存塞東西，當缓存达到一定個數之後，我們需要一種策略踢出一些元素，
用來给新的元素腾出空間。
一般缓存失效策略有
- LRU(Least-Recently-Used): 替換掉最近請求最少的對象，實際中使用最广。cpu缓存淘汰和虚拟記憶體效果好，web應用欠佳
- LFU(Least-Frequently-Used): 缓存污染問題(一個先前流行的缓存對象會在缓存中驻留很長時間)
- First in First out(FIFO)
- Random Cache: 随機選一個删除

LRU 是常用的一個，比如 redis 就實現了這個策略，這裡我們來模擬實現一個。
要想實現一個 LRU，我們需要一種方式能够记录訪問的順序，並且每次訪問之後我們要把最新使用到的元素放到最後（表示最新訪問）。
當容量满了以後，我們踢出最早訪問的元素。假如用一個鏈表來表示的話：

[1] -> [2] -> [3]

假设最後面是最後訪問的，當訪問到一個元素以後，我們把它放到最後。當容量满了，我們踢出第一個元素就行了。
一開始的想法可能是用一個鏈表來记录訪問順序，但是單鏈表有個問題就是如果訪問了中間一個元素，我們需要拿掉它並且放到鏈表尾部。
而單鏈表無法在O(1)的時間内删除一個節點（必须要先搜索到它），但是双端鏈表可以，因為一個節點记录了它的前後節點，
只需要把要删除的節點的前後節點鏈接起來就行了。
還有個問題是如何把删除後的節點放到鏈表尾部，如果是循環双端鏈表就可以啦，我們有個 root 節點鏈接了首位節點，
只需要讓 root 的前一個指向這個被删除節點，然後讓之前的最後一個節點也指向它就行了。

使用了循環双端鏈表之後，我們的操作就都是 O(1) 的了。這也就是使用一個 dict 和一個 循環双端鏈表 實現LRU 的思路。
不過一般我們使用内置的 OrderedDict(原理和這個類似)就好了，要實現一個循環双端鏈表是一個不簡單的事情。

"""


class LRUCache:
    def __init__(self, capacity=128):
        self.capacity = capacity
        # 借助 OrderedDict 我們可以快速實現一個 LRUCache，OrderedDict 内部其實也是使用循環双端鏈表實現的
        # OrderedDict 有兩個重要的函數用來實現 LRU，一個是 move_to_end，一個是 popitem，請自己看文件
        self.od = OrderedDict()

    def get(self, key, default=None):
        val = self.od.get(key, default)  # 如果没有返回 default，保持 dict 语義
        self.od.move_to_end(key)   # 每次訪問就把key 放到最後表示最新訪問
        return val

    def add_or_update(self, key, value):
        if key in self.od:  # update
            self.od[key] = value
            self.od.move_to_end(key)
        else:  # insert
            self.od[key] = value
            if len(self.od) > self.capacity:  # full
                self.od.popitem(last=False)

    def __call__(self, func):
        """
        一個簡單的 LRU 實現。有一些問題需要思考下：

        - 這裡為了簡化默认参數只有一個數字 n，假如可以傳入多個参數，如何確定缓存的key 呢？
        - 這裡實現没有考虑線程安全的問題，要如何才能實現線程安全的 LRU 呢？當然如果不是多線程环境下使用是不需要考虑的
        - 假如這裡没有用内置的 dict，你能使用 redis 來實現這個 LRU 嗎，如果使用了 redis，我們可以存儲更多數據到服务器。而使用字典實際上是缓存了Python進程裡(localCache)。
        - 這裡只是實現了 lru 策略，你能同時實現一個超時 timeout 参數嗎？比如像是memcache 實現的 lazy expiration 策略
        - LRU有個缺點就是，對於周期性的數據訪問會导致命中率迅速下降，有一種優化是 LRU-K，訪問了次數达到 k 次才會將數據放入缓存
        """
        def _(n):
            if n in self.od:
                return self.get(n)
            else:
                val = func(n)
                self.add_or_update(n, val)
                return val
        return _


@LRUCache(10)
def f_use_lru(n):
    if n <= 1:  # 0 or 1
        return n
    return f(n - 1) + f(n - 2)


def test():
    import time
    beg = time.time()
    for i in range(34):
        print(f(i))
    print(time.time() - beg)
    beg = time.time()
    for i in range(34):
        print(f_use_lru(i))
    print(time.time() - beg)


# TODO 要怎麼给 lru 寫單測？

if __name__ == '__main__':
    test()
