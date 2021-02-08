# -*- coding: utf-8 -*-


def quicksort(array):
    size = len(array)
    if not array or size < 2:  # NOTE: 遞迴出口，空數組或者只有一個元素的數組都是有序的
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
    assert quicksort(seq) == sorted(seq)    # 用内置的sorted 『對拍』


def quicksort_inplace(array, beg, end):    # 注意這裡我們都用左闭右開區間
    if beg < end:    # beg == end 的時候遞迴出口
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot + 1, end)


def partition(array, beg, end):
    """對给定數組执行 partition 操作，返回新的 pivot 位置"""
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
    assert partition(l, 0, len(l)) == 3
    l = [1]
    assert partition(l, 0, len(l)) == 0
    l = [2,1]
    assert partition(l, 0, len(l)) == 1


def test_quicksort_inplace():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    quicksort_inplace(seq, 0, len(seq))
    assert seq == sorted_seq


def nth_element(array, beg, end, nth):
    """查找一個數組第 n 大元素"""
    if beg < end:
        pivot_idx = partition(array, beg, end)
        if pivot_idx == nth - 1:    # 數組小標從 0 開始
            return array[pivot_idx]
        elif pivot_idx > nth - 1:
            return nth_element(array, beg, pivot_idx, nth)
        else:
            return nth_element(array, pivot_idx + 1, end, nth)


def test_nth_element():
    l1 = [3, 5, 4, 2, 1]
    assert nth_element(l1, 0, len(l1), 3) == 3
    assert nth_element(l1, 0, len(l1), 2) == 2

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in l:
        assert nth_element(l, 0, len(l), i) == i
    for i in reversed(l):
        assert nth_element(l, 0, len(l), i) == i

    array = [3, 2, 1, 5, 6, 4]
    assert nth_element(array, 0, len(array), 2) == 2

    array = [2,1]
    assert nth_element(array, 0, len(array), 1) == 1
    assert nth_element(array, 0, len(array), 2) == 2

    array = [3,3,3,3,3,3,3,3,3]
    assert nth_element(array, 0, len(array), 1) == 3


if __name__ == '__main__':
    test_nth_element()
