# 線性結構
本節我們从最簡單和常用的線性結構開始，并結合 Python 语言本身内置的數據結構和其底层實現方式來講解。
雖然本质上數據結構的思想是语言无關的，但是了解 Python 的實現方式有助于你避免一些坑。

我們會在代碼中注释出操作的時間複雜度。


# 数组 array

数组是最常用到的一種線性結構，其實 python 内置了一個 array 模块，但是大部人甚至从來没用過它。
Python 的 array 是内存连续、存储的都是同一數據类型的結構，而且只能存数值和字符。

我建議你课下看下 array 的文档：https://docs.python.org/2/library/array.html

你可能很少會使用到它(我推荐你用 numpy.array)，我将在影片里簡單介绍下它的使用和工作方式，最常用的還是接下來要說的 list，
本章最後我們會用 list 來實現一個固定长度、并且支持所有 Python 數據类型的数组 Array.


# 列表 list
如果你学過 C++，list 其實和 C++ STL（标准模板库）中的 vector 很类似，它可能是你的 Python 学习中使用最频繁的數據結構之一。
這裡我們不再去自己實現 list，因為這是個 Python 提供的非常基础的數據类型，我會在影片中講解它的工作方式和内存分配策略，
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
講完了 list 让我們來實現一個定长的数组 Array ADT，在其他一些语言中，内置的数组結構就是定长的。
這裡我們會使用 list 作為 Array 的一個成员（代理）。具體請参考影片講解和代碼示例，後面我們會使用到這個 Array 类。


# 小問題
- 你知道線性結構的查找，删除，訪問一個元素的平均時間複雜度嗎？(後面我們會介绍這個概念，现在你可以簡單地理解為一個操作需要的平均步骤)
- list 内存重新分配的时候為什么要有冗余？不會浪费空間嗎？
- 當你频繁的pop list 的第一個元素的时候，會發生什么？如果需要频繁在兩头增添元素，你知道更高效的數據結構嗎？後面我們會講到


# 延伸閱讀

[Python list implementation](https://www.laurentluce.com/posts/python-list-implementation/)

[https://github.com/python/cpython/blob/master/Objects/listobject.c](https://github.com/python/cpython/blob/master/Objects/listobject.c)


# 勘誤
影片里的 Array.clear 方法有誤。应该是 `for i in range(len(self._items))`，已經在後续所有使用到 Array 的代碼里修正
