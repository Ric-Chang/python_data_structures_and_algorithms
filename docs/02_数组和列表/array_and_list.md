# 線性結構
本節我們從最簡單和常用的線性結構開始，並結合 Python 语言本身内置的數據結構和其底层實現方式來講解。
雖然本质上數據結構的思想是语言無關的，但是了解 Python 的實現方式有助於你避免一些坑。

我們會在原始碼中注释出操作的時間複雜度。


# 數組 array

數組是最常用到的一種線性結構，其實 python 内置了一個 array 模塊，但是大部人甚至從來没用過它。
Python 的 array 是記憶體連續、存儲的都是同一數據類型的結構，而且只能存數值和字符。

我建議你課下看下 array 的文档：https://docs.python.org/2/library/array.html

你可能很少會使用到它(我推荐你用 numpy.array)，我將在影片裡簡單介绍下它的使用和工作方式，最常用的還是接下來要說的 list，
本章最後我們會用 list 來實現一個固定長度、並且支持所有 Python 數據類型的數組 Array.


# 列表 list
如果你學過 C++，list 其實和 C++ STL（標准模板库）中的 vector 很類似，它可能是你的 Python 學習中使用最頻繁的數據結構之一。
這裡我們不再去自己實現 list，因為這是個 Python 提供的非常基础的數據類型，我會在影片中講解它的工作方式和記憶體分配策略，
避免使用過程中碰到一些坑。當然如果你有毅力或者興趣的了解底层是如何實現的，可以看看 cpython 解释器的具體實現。


操作                                  | 平均時間複雜度 |
--------------------------------------|----------------|
list[index]                           | O(1)           |
list.append                           | O(1)           |
list.insert                           | O(n)           |
list.pop(index), default last element | O(1)           |
list.remove                           | O(n)           |

![](./list.png)

# 用 list 實現 Array ADT
講完了 list 讓我們來實現一個定長的數組 Array ADT，在其他一些语言中，内置的數組結構就是定長的。
這裡我們會使用 list 作為 Array 的一個成员（代理）。具體請参考影片講解和原始碼示例，後面我們會使用到這個 Array 類。


# 小問題
- 你知道線性結構的查找，删除，訪問一個元素的平均時間複雜度嗎？(後面我們會介绍這個概念，現在你可以簡單地理解為一個操作需要的平均步骤)
- list 記憶體重新分配的時候為什麼要有冗餘？不會浪费空間嗎？
- 當你頻繁的pop list 的第一個元素的時候，會發生什麼？如果需要頻繁在兩頭增添元素，你知道更高效的數據結構嗎？後面我們會講到


# 延伸閱讀

[Python list implementation](https://www.laurentluce.com/posts/python-list-implementation/)

[https://github.com/python/cpython/blob/master/Objects/listobject.c](https://github.com/python/cpython/blob/master/Objects/listobject.c)


# 勘誤
影片裡的 Array.clear 方法有誤。應該是 `for i in range(len(self._items))`，已經在後续所有使用到 Array 的原始碼裡修正
