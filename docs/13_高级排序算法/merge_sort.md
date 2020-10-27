# 分治法 (Divide and Conquer)

很多有用的算法結構上是遞迴的，為了解决一個特定問題，算法一次或者多次遞迴调用其自身以解决若干子問題。
這些算法典型地遵循分治法的思想：将原問題分解為几個规模较小但是类似于原問題的子問題，遞迴求解這些子問題，
然後再合并這些問題的解來建立原問題的解。

分治法在每层遞迴时有三個步骤：

- **分解**原問題為若干子問題，這些子問題是原問題的规模最小的实例
- **解决**這些子問題，遞迴地求解這些子問題。當子問題的规模足够小，就可以直接求解
- **合并**這些子問題的解成原問題的解


# 归并排序
现在我們就來看下归并排序是是如何利用分治法解决問題的。

- **分解**：将待排序的 n 個元素分成各包含 n/2 個元素的子序列
- **解决**：使用归并排序遞迴排序兩個子序列
- **合并**：合并兩個已經排序的子序列以产生已排序的答案

考虑我們排序這個数组：[10,23,51,18,4,31,13,5] ，我們遞迴地将数组进行分解

![](./merge_sort_split.png)

當数组被完全分隔成只有單個元素的数组时，我們需要把它们合并回去，每次兩兩合并成一個有序的序列。

![](./merge_sort_merge.png)

用遞迴代碼來描述這個問題：

```py
def merge_sort(seq):
    if len(seq) <= 1:   # 只有一個元素是遞迴出口
        return seq
    else:
        mid = int(len(seq)/2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])

        # 合并兩個有序的数组
        new_seq = merge_sorted_list(left_half, right_half)
        return new_seq
```

注意我們這裡有一個函数没實現，就是如何合并兩個有序数组 merge_sorted_list。其实你在纸上画一画，
合并兩個有序数组并不难實現。

![](./merge_sorted_array.png)

![](./merge_sorted_array_2.png)


```py
def merge_sorted_list(sorted_a, sorted_b):
    """ 合并兩個有序序列，返回一個新的有序序列

    :param sorted_a:
    :param sorted_b:
    """
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1

    # 最後别忘记把多余的都放到有序数组里
    if a < length_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])

    return new_sorted_seq
```

這样就實現了归并排序，并且你會发现它返回一個新的数组而不是修改原有数组。


# 時間複雜度
我們來簡單看下它归并排序的時間複雜度，假设排序 n 個数字時間複雜度是 T(n)，這裡為了方便假设 n 是 2 的幂

\begin{align}
T(n)= \begin{cases} c, & \text {if $n$ = 1} \\ 2T(n/2)+cn, & \text{if $n$ > 1} \end{cases}
\end{align}

![](./merge_sort_recursion_tree.png)

总的代價是 $cnlg(n)+cn$ ，忽略常数项可以认為是  O(nlg(n))。如果這個图看不懂，我們自己求解下也不难，首先我們简化一下，
把常数系数當成 1，得到以下遞迴式：

\begin{align}
T(n)= \begin{cases} 1, & \text {if $n$ = 1} \\ 2T(n/2)+n, & \text{if $n$ > 1} \end{cases}
\end{align}

![](./tn.png)


# 思考题
- 請你完成归并排序的單元測试
- 這裡實現的归并排序是 inplace 的嗎？
- 归并排序是稳定的嗎？稳定指的是排序前後相同大小的数字依然保持相對顺序。

# 延伸閱讀
- 《算法导论》第 2 章和第 4 章，你需要了解下『主定理』，以及如何求解形如 $T(n)=aT(n/b) + f(n)$ 的遞迴式複雜度
-  了解算法导论上遞迴式的三種求解方法：代入法，遞迴树法，主方法
