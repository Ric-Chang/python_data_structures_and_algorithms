# 查找

查找可以說是我們业务代碼里用得最多的操作，比如我們經常需要在一個列表里找到我們需要的一個元素，然後返回它的位置。
其实之前我們介绍的哈希表就是非常高效率的查找數據結構，很明显地它是用空間换時間。這一節介绍兩個基本的基于線性結構的查找。

# 線性查找
線性查找就是从头找到尾，直到符合條件了就返回。比如在一個 list 中找到一個等于 5 的元素并返回下标：

```py
number_list = [0, 1, 2, 3, 4, 5, 6, 7]


def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1


assert linear_search(5, number_list) == 5

```
是不是 so easy。當然我們需要來一點花样，比如传一個谓词进去，你要知道，在 python 里一切皆對象，所以我們可以把函数當成一個参数传给另一個函数。

```py
def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    return -1


assert linear_search_v2(lambda x: x == 5, number_list) == 5
```

效果是一样的，但是传入一個谓词函数进去更灵活一些，比如我們可以找到第一個大于或者小于 5 的，从而控制函数的行為。
還能玩出什么花样呢？前面我們刚学习了遞迴，能不能发挥自虐精神没事找事用遞迴來實現呢？

```py
def linear_search_recusive(array, value):
    if len(array) == 0:
        return -1
    index = len(array)-1
    if array[index] == value:
        return index
    return linear_search_recusive(array[0:index], value)


assert linear_search_recusive(number_list, 5) == 5
assert linear_search_recusive(number_list, 8) == -1
assert linear_search_recusive(number_list, 7) == 7
assert linear_search_recusive(number_list, 0) == 0
```
這裡的 assert 我多写了几個，包括正常情况、异常情况和邊界值等，因為遞迴比较容易出错。注意這裡的兩個遞迴出口。
當然业务代碼里如果碰到這種問題我們肯定是选上邊最直白的方式來實現，要不你的同事肯定想打你。

# 二分查找
上一小節說的線性查找針對的是无序序列，假如一個序列已經有序了呢，我們還需要从头找到尾嗎？當然不用，折半(二分)是一種經典思想。日常生活中還有哪些經典的二分思想呢？

- 猜数字游戏
- 一尺之棰,日取其半,万世不竭
- 有些民間股神，告诉一堆人某個股票會涨，告诉另一半人會跌。後來真涨了，慢慢又告诉信了他的一半人另一個股票會涨，另一半說會跌。就這样韭菜多了总有一些人信奉他為股神。。。

其实之前写過博客[《抱歉，我是開发，你居然让我写單測[影片]》](https://zhuanlan.zhihu.com/p/35352024)講過二分查找，當时主要是為了引入單元測试這個概念的，因為很多不正规的项目代碼很糙，更别說写單測了。這裡我就直接贴代碼啦

```py
def binary_search(sorted_array, val):
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array) - 1

    while beg <= end:
        mid = int((beg + end) / 2)  # beg + (end-beg)/2， 為了屏蔽 python 2/3 差异我用了强转
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1
    return -1


def test_binary_search():
    a = list(range(10))

    # 正常值
    assert binary_search(a, 1) == 1
    assert binary_search(a, -1) == -1

    # 异常值
    assert binary_search(None, 1) == -1

    # 邊界值
    assert binary_search(a, 0) == 0
```


# 思考题
- 给你個挑战，用遞迴來實現本章的二分查找。你要十分注意邊界條件，注意用單測測试呦，在你写代碼的时候，可能會碰到邊界問題或者无穷遞迴等。 如果你想不起來，可以看看本章的代碼示例
- 二分查找有一個变形，比如我們想在一個有序数组中插入一個值之後，数组仍保持有序，請你找出這個位置。(bisect 模块)


# 延伸閱讀
這裡没给鏈接，請善用 google 等搜索引擎和 Dash(mac) 等文档查询工具，在你学习代碼的過程中你會非常频繁地使用它们。
或者如果你有時間也可以跳转到這些模块的源碼，看看它们的實現方式。标准库都是些高手写的，肯定能学到一些姿势。

- 閱讀 python 文档關于二分的 bisect 模块。
- 閱讀 python 文档 itertools 相關模块和常見的几個函数 takewhile, dropwhile, from_iterable, count, tee 等用法
- [每個程序员都应该會點形式化证明](https://zhuanlan.zhihu.com/p/35364999?group_id=967109293607129088)


# Leetcode

[找旋转過的排序数组中最小的数 find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

[已排序的数组中找到第一和最後一個元素 find-first-and-last-position-of-element-in-sorted-array/](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/)
