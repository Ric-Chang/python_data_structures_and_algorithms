# Python 一切皆對象

舉個例子，在 python 中我們經常使用的 list

```py
l = list()    # 實例化一個 list 對象 l
l.append(1)    # 調用 l 的 append 方法
l.append(2)
l.remove(1)
print(len(l))    # 調用對象的 `__len__` 方法
```

在後面實現新的數據類型時，我們將使用 python 的 class 實現，它包含屬性和方法。
屬性一般是使用某種特定的數據類型，而方法一般是對屬性的操作。
這裡你只需了解這麼多就行了， 我們不會使用繼承等特性。


# 什麼是抽象數據類型 ADT

實際上 python 内置的 list 就可以看成一種抽象數據類型。

ADT: Abstract Data Type，抽象數據類型，我們在組合已有的數據結構來實現一種新的數據類型， ADT 定義了類型的數據和操作。

我們以抽象一個背包(Bag) 數據類型來說明，背包是一種容器類型，我們可以给它添加東西，也可以移除東西，並且我們想知道背包裡
有多少東西。於是我們可以定義一個新的數據類型叫做 Bag.

```py
class Bag:
    """ 背包類型 """
    pass
```


# 實現一個 Bag ADT
影片中我們將使用 python 的 class 來實現一個新的容器類型叫做 Bag。


# 實現 ADT 我們應該注意什麼？
- 如何選用恰當的數據結構作為存儲？
- 選取的數據結構能否满足 ADT 的功能需求
- 實現效率如何？


# 小問題：
- 你了解 python 的魔術方法嗎？ 比如 `__len__` ，調用 len(l) 的時候發生了什麼？
- 你了解單測嗎？我們以後將使用 pytest 運行單元測試，保證我們實現的數據結構和算法是正確的。你可以網上搜索下它的簡單用法

# 延伸閱讀：

[數據結構與算法--ADT](http://www.atjiang.com/data-structures-using-python-ADT/)

[http://www.nhu.edu.tw/~chun/CS-ch12-Abstract%20Data%20Types.pdf](http://www.nhu.edu.tw/~chun/CS-ch12-Abstract%20Data%20Types.pdf)
