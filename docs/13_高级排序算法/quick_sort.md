# 快速排序

快速排序名字可不是盖的，很多程序语言標准库實現的内置排序都有它的身影，我們就直奔主题吧。
和归并排序一样，快排也是一種分而治之(divide and conquer)的策略。归并排序把数組遞迴成只有單個元素的数組，之後再不断兩兩
合并，最後得到一個有序数組。這裡的遞迴基本條件就是只包含一個元素的数組，當数組只包含一個元素的时候，我們可以认為它本來就是有序的（當然空数組也不用排序）。

快排的工作過程其實比较簡單，三步走：

- 選择基准值 pivot 将数組分成兩個子数組：小于基准值的元素和大于基准值的元素。這個過程称之為 partition

- 對這兩個子数組进行快速排序。

- 合并結果

![](./quick_sort.png)

根據這個想法我們可以快速写出快排的代碼，简直就是在翻译上邊的描述：

```py
def quicksort(array):
    size = len(array)
    if not array or size < 2:  # NOTE: 遞迴出口，空数組或者只有一個元素的数組都是有序的
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx != i]
    return quicksort(less_part) + [pivot] + quicksort(great_part)

def test_quicksort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    assert quicksort(seq) == sorted(seq)
```
是不是很簡單，下次面试官让你手写快排你再写不出來就有點不太合适啦。 當然這個實現有兩個不好的地方:

- 第一是它需要额外的存儲空間，我們想實現 inplace 原地排序。
- 第二是它的 partition 操作每次都要兩次遍历整個数組，我們想改善一下。

這裡我們就來優化一下它，實現 inplace 排序并且改善下 partition 操作。新的代碼大概如下：

```py
def quicksort_inplace(array, beg, end):    # 注意這裡我們都用左闭右開區間，end 傳入 len(array)
    if beg < end:    # beg == end 的时候遞迴出口
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot+1, end)
```

能否實現只遍历一次数組就可以完成 partition 操作呢？實際上是可以的。我們设置首位俩個指針 left, right，兩個指針不断向中間收拢。如果遇到 left 位置的元素大于 pivot 并且 right 指向的元素小于 pivot，我們就交换這俩元素，當 left > right 的时候退出就行了，這样實現了一次遍历就完成了 partition。如果你感覺懵逼，纸上画画就立马明白了。我們來撸代碼實現：

![](./partition.png)

```py
def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1    # 開區間，最後一個元素位置是 end-1     [0, end-1] or [0: end)，括号表示開區間

    while True:
        # 從左邊找到比 pivot 大的
        while left <= right and array[left] < pivot:
            left += 1

        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right   # 新的 pivot 位置


def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0
    l = [4, 3, 2, 1]
    assert partition(l, 0, len(l))
```

大功告成，新的快排就實現好了。

# 時間複雜度
在比较理想的情况下，比如数組每次都被 pivot 均分，我們可以得到遞迴式：

T(n) = 2T(n/2) + n

上一節我們講過通過遞迴树得到它的時間複雜度是 O(nlog(n))。即便是很坏的情况，比如 pivot 每次都把数組按照 1:9 划分，依然是 O(nlog(n))，感興趣請閱讀算法导论相關章節。

![](quicksort_worst.png)


# 思考题
- 請你补充 quicksort_inplace 的單元測试
- 最坏的情况下快排的時間複雜度是多少？什麼时候會發生這種情况？
- 我們實現的快排是稳定的啵？
- 選择基准值如果選不好就可能导致複雜度升高，算导中提到了一種『median of 3』策略，就是說選择 pivot 的时候 從子数組中随機選三個元素，再取它的中位数，你能實現這個想法嗎？這裡我們的代碼很簡單地取了第一個元素作為 pivot
- 利用快排中的 partition 操作，我們還能實現另一個算法，nth_element，快速查找一個无序数組中的第 n 大元素，請你嘗試實現它并编写單測。其實這個函数是 C++ STL 中的一個函数。
- 你知道 Python 内置的 sorted 如何實現的嗎？請你 Google 相關資料了解下。很多内置的排序都使用了快排的改良版。


# 延伸閱讀
- 《算法导论》第 7 章
- [《面试必备 | 排序算法的Python實現》](https://zhuanlan.zhihu.com/p/36419582)

# 总結

面试經常问的就是常用排序算法的時間空間复杂，這裡列一個表格方便记忆：

| 排序算法   | 最差時間分析 | 平均時間複雜度 | 稳定度 | 空間複雜度     |
|------------|--------------|----------------|--------|----------------|
| 冒泡排序   | O(n^2)       | O(n^2)         | 稳定   | O(1)           |
| 選择排序   | O(n^2)       | O(n^2)         | 不稳定 | O(1)           |
| 插入排序   | O(n^2)       | O(n^2)         | 稳定   | O(1)           |
| 二叉树排序 | O(n^2)       | O(n\*log2n)    | 不一顶 | O(n)           |
| 快速排序   | O(n^2)       | O(n\*log2n)    | 不稳定 | O(log2n)\~O(n) |
| 堆排序     | O(n\*log2n)  | O(n\*log2n)    | 不稳定 | O(1)           |

[數據結構与算法-排序篇-Python描述](https://blog.csdn.net/mrlevo520/article/details/77829204<Paste>)

# Leetcode

无序数組寻找第 k 大的数字，不止一種方法。
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
