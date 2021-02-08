# -*- coding: utf-8 -*-


import random


def bubble_sort(seq):  # O(n^2), n(n-1)/2 = 1/2(n^2 + n)
    n = len(seq)
    for i in range(n-1):
        print(seq)    # 我打印出來讓你看清楚每一輪最高、次高、次次高...的小朋友會冒泡到右邊
        for j in range(n-1-i):  # 這裡之所以 n-1 還需要 减去 i 是因為每一輪冒泡最大的元素都會冒泡到最後，無需再比较
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
        print(seq)


def test_bubble_sort():
    seq = list(range(10))  # 注意 python3 返回替代器，所以我都用 list 强轉了，python2 range 返回的就是 list
    random.shuffle(seq)   # shuffle inplace 操作，打乱數組
    sorted_seq = sorted(seq)  # 注意呦，内置的 sorted 就不是 inplace 的，它返回一個新的數組，不影響傳入的参數
    bubble_sort(seq)
    assert seq == sorted_seq


def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i    # 我們假设當前下標的元素是最小的
        for j in range(i+1, n):    # 從 i 的後面開始找到最小的元素，得到它的下標
            if seq[j] < seq[min_idx]:
                min_idx = j    # 一個 j 循環下來之後就找到了最小的元素它的下標
        if min_idx != i:    # swap
            seq[i], seq[min_idx] = seq[min_idx], seq[i]


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    select_sort(seq)
    assert seq == sorted_seq


def insertion_sort(seq):
    """ 每次挑選下一個元素插入已經排序的數組中,初始時已排序數組只有一個元素"""
    n = len(seq)
    print(seq)
    for i in range(1, n):
        value = seq[i]    # 保存當前位置的值，因為轉移的過程中它的位置可能被覆盖
        # 找到這個值的合适位置，使得前邊的數組有序 [0,i] 有序
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]  # 如果前邊的元素比它大，就讓它一直前移
            pos -= 1
        seq[pos] = value    # 找到了合适的位置赋值就好
        print(seq)
