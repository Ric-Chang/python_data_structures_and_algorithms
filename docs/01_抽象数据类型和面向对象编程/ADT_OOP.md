# Python 一切皆對象

举個例子，在 python 中我們經常使用的 list

```py
l = list()    # 實例化一個 list 對象 l
l.append(1)    # 调用 l 的 append 方法
l.append(2)
l.remove(1)
print(len(l))    # 调用對象的 `__len__` 方法
```

在後面實現新的數據类型时，我們将使用 python 的 class 實現，它包含属性和方法。
属性一般是使用某種特定的數據类型，而方法一般是對属性的操作。
這裡你只需了解這么多就行了， 我們不會使用继承等特性。


# 什么是抽象數據类型 ADT

實际上 python 内置的 list 就可以看成一種抽象數據类型。

ADT: Abstract Data Type，抽象數據类型，我們在组合已有的數據結構來實現一種新的數據类型， ADT 定義了类型的數據和操作。

我們以抽象一個背包(Bag) 數據类型來說明，背包是一種容器类型，我們可以给它添加東西，也可以移除東西，并且我們想知道背包里
有多少東西。于是我們可以定義一個新的數據类型叫做 Bag.

```py
class Bag:
    """ 背包类型 """
    pass
```


# 實現一個 Bag ADT
影片中我們将使用 python 的 class 來實現一個新的容器类型叫做 Bag。


# 實現 ADT 我們应该注意什么？
- 如何选用恰當的數據結構作為存储？
- 选取的數據結構能否满足 ADT 的功能需求
- 實現效率如何？


# 小問題：
- 你了解 python 的魔術方法嗎？ 比如 `__len__` ，调用 len(l) 的时候發生了什么？
- 你了解單測嗎？我們以後将使用 pytest 运行單元測试，保证我們實現的數據結構和算法是正确的。你可以网上搜索下它的簡單用法

# 延伸閱讀：

[數據結構与算法--ADT](http://www.atjiang.com/data-structures-using-python-ADT/)

[http://www.nhu.edu.tw/~chun/CS-ch12-Abstract%20Data%20Types.pdf](http://www.nhu.edu.tw/~chun/CS-ch12-Abstract%20Data%20Types.pdf)
