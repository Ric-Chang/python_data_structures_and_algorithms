# 字典 dict

上一章我們介绍了哈希表，其實 python 内置的 dict 就是用哈希表實現的，所以這一章實現 dict 就非常簡單了。
當然 cpython 使用的是 c 语言實現的，远比我們写的复杂得多 (cpython/Objects/dictobject.c)。
上一章我們用 python 自己写的一個 Array 來代表定長數組，然後用它實現的 HashTable，它支持三個最基本的方法

- add(key ,value): 有 key 则更新，否则插入
- get(key, default=None): 或者 key 的值，不存在返回默认值 None
- remove(key): 删除一個 key，這裡其實不是真删除，而是標记為 Empty

字典最常使用的场景就是 k,v 存儲，經常用作缓存，它的 key 值是唯一的。
内置库 collections.OrderedDict 還保持了 key 的添加顺序，其實用我們之前實現的鏈表也能自己實現一個 OrderedDict。

# 實現 dict ADT

其實上邊 HashTable 實現的三個基本方法就是我們使用字典最常用的三個基本方法， 這裡我們繼承一下這個類，
然後實現更多 dict 支持的方法，items(), keys(), values()。不過需要注意的是，在 python2 和 python3 裡這些方法
的返回是不同的，python3 裡一大改進就是不再返回浪费記憶體的 列表，而是返回迭代器，你要获得列表必须用 list() 轉換成列表。 這裡我們實現 python3 的方式返回迭代器。


```py
class DictADT(HashTable):
    pass
```

影片裡我們將演示如何實現這些方法，並且写單測驗證正確性。

# Hashable
作為 dict 的 key 必须是可哈希的，也就是說不能是 list 等可变對象。不信你在 ipython 裡運行如下原始碼：

```py
d = dict()
d[[1]] = 1
# TypeError: unhashable type: 'list'
```

我引用 python 文档裡的說法，大家可以自己理解下：

```
An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal (except with themselves), and their hash value is derived from their id().
```


# 思考题：
- 你能在哈希表的基础上實現 dict 的其他操作嗎？
- 對於 python 來說，哪些内置數據類型是可哈希的呢？list, dict, tuple, set 等類型哪些可以作為字典的 key 呢?
- 你了解可变對象和不可变對象的區别嗎？
- 你了解 python 的 hash 函數嗎？你了解 python 的`__hash__`  和 `__eq__` 魔術方法嗎？它們何時被調用

# 延伸閱讀
閱讀 python 文档關於 dict 的相關内容
