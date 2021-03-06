# 鏈式結構

上一節講到了支持随機訪問的線性結構，這次我們開始講鏈式結構, 影片裡我會說下這兩種結構的區别，然後講解最常見的單鏈表和双鏈表。
之前在专栏文章[那些年，我們一起跪過的算法题[影片]](https://zhuanlan.zhihu.com/p/35175401)裡實現過一個 lru_cache，
使用到的就是循環双端鏈表，如果感覺這篇文章有點难理解，我們這裡將會循序渐進地來實現。
後面講到哈希表的衝突解決方式的時候，我們會再次提到鏈表。

上一節我們分析了 list 的各種操作是如何實現的，如果你還有印象的話，list
在頭部進行插入是個相當耗時的操作（需要把後面的元素一個一個挪個位置）。假如你需要頻繁在數組兩頭增删，list 就不太合适。
今天我們介绍的鏈式結構將摆脱這個缺陷，當然了鏈式結構本身也有缺陷，比如你不能像數組一樣随機根據下標訪問，你想查找一個元素只能老老實實從頭遍历。
所以嘛，學習和了解數據結構的原理和實現你才能准確地選择到底什麼時候該用什麼數據結構，而不是瞎選导致原始碼性能很差。


# 單鏈表
和線性結構不同，鏈式結構記憶體不連續的，而是一個個串起來的，這個時候就需要每個鏈接表的節點保存一個指向下一個節點的指針。
這裡可不要混淆了列表和鏈表（它們的中文發音類似，但是列表 list 底层其實還是線性結構，鏈表才是真的通過指針關联的鏈式結構）。
看到指針你也不用怕，這裡我們用的 python，你只需要一個簡單赋值操作就能實現，不用担心 c 语言裡复杂的指針。

先來定義一個鏈接表的節點，刚才說到有一個指針保存下一個節點的位置，我們叫它 next， 當然還需要一個 value 屬性保存值

```py
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```
然後就是我們的單鏈表 LinkedList ADT:

```py
class LinkedList(object):
    """ 鏈接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """
```
實現我們會在影片中用画图來模擬並且手動原始碼實現，原始碼裡我們會標识每個步骤的時間複雜度。這裡請高度集中精力，
雖然鏈表的思想很簡單，但是想要正確寫對鏈表的操作原始碼可不容易，稍不留神就可能丢失一些步骤。
這裡我們還是會用簡單的單測來驗證原始碼是否按照預期工作。

來看下時間複雜度：

鏈表操作                      | 平均時間複雜度 |
------------------------------|----------------|
linked_list.append(value)     | O(1)           |
linked_list.appendleft(value) | O(1)           |
linked_list.find(value)       | O(n)           |
linked_list.remove(value)     | O(n)           |


# 双鏈表
上邊我們親自實現了一個單鏈表，但是能看到很明显的問題，單鏈表雖然 append 是 O(1)，但是它的 find 和 remove 都是 O(n)的，
因為删除你也需要先查找，而單鏈表查找只有一個方式就是從頭找到尾，中間找到才退出。
這裡我之前提到過如果要實現一個 lru 缓存（訪問時間最久的踢出），我們需要在一個鏈表裡能高效的删除元素，
並把它追加到訪問表的最後一個位置，這個時候單鏈表就满足不了了，
因為缓存在 dict 裡查找的時間是 O(1)，你更新訪問順序就 O(n)了，缓存就没了優势。

這裡就要使用到双鏈表了，相比單鏈表來說，每個節點既保存了指向下一個節點的指針，同時還保存了上一個節點的指針。

```py
class Node(object):
    # 如果節點很多，我們可以用 __slots__ 來節省記憶體，把屬性保存在一個 tuple 而不是 dict 裡
    # 感興趣可以自行搜索  python  __slots__
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next
```

對， 就多了 prev，有啥優势嘛？

- 看似我們反過來遍历双鏈表了。反過來從哪裡開始呢？我們只要讓 root 的 prev 指向 tail 節點，不就串起來了嗎？
- 直接删除節點，當然如果给的是一個值，我們還是需要查找這個值在哪個節點？ - 但是如果给了一個節點，我們把它拿掉，直接讓它的前後節點互相指過去不就行了？哇欧，删除就是 O(1) 了，兩步操作就行啦

好，废話不多說，我們在影片裡介绍怎麼實現一個双鏈表 ADT。你可以直接在本項目的 `docs/03_鏈表/double_link_list.py` 找到原始碼。
最後讓我們看下它的時間複雜度:(這裡 CircularDoubleLinkedList 取大寫字母缩寫為 cdll)

循環双端鏈表操作                       | 平均時間複雜度 |
---------------------------------------|----------------|
cdll.append(value)                     | O(1)           |
cdll.appendleft(value)                 | O(1)           |
cdll.remove(node)，注意這裡参數是 node | O(1)           |
cdll.headnode()                        | O(1)           |
cdll.tailnode()                        | O(1)           |


# 小問題：
- 這裡單鏈表我没有實現 insert 方法，你能自己嘗試實現嗎？  insert(value, new_value)，我想在某個值之前插入一個值。你同樣需要先查找，所以這個步骤也不够高效。
- 你能嘗試自己實現個 lru cache 嗎？需要使用到我們這裡提到的循環双端鏈表
- 借助内置的 collections.OrderedDict，它有兩個方法 popitem 和 move_to_end，我們可以迅速實現一個 LRU cache。請你嘗試用 OrderedDict 來實現。
- python 内置庫的哪些數據結構使用到了本章講的鏈式結構？


# 相關閱讀

[那些年，我們一起跪過的算法题- Lru cache[影片]](https://zhuanlan.zhihu.com/p/35175401)

# 勘誤：

影片中 LinkedList.remove 方法講解有遗漏， linked_list.py 文件已經修正，請讀者注意。具體請参考 [fix linked_list & add gitigonre](https://github.com/PegasusWang/python_data_structures_and_algorithms/pull/3)。影片最後增加了一段勘誤說明。

# Leetcode

反轉鏈表 [reverse-linked-list](https://leetcode.com/problems/reverse-linked-list/)

這裡有一道關於 LRU 的練習题你可以嘗試下。
[LRU Cache](https://leetcode.com/problems/lru-cache/description/)

合並兩個有序鏈表 [merge-two-sorted-lists](/https://leetcode.com/problems/merge-two-sorted-lists/submissions/)
