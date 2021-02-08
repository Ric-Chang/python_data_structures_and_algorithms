# 二叉查找樹(BST)

二叉樹的一種應用就是來實現堆，今天我們再看看用二叉查找樹(Binary Search Tree, BST)。
前面有章節說到了查找操作，包括線性查找、二分查找、哈希查找等，線性查找效率比较低，二分又要求必须是有序的序列，
為了維持有序插入的代價比较高、哈希查找效率很高但是浪费空間。能不能有一種插入和查找都比较快的數據結構呢？二叉查找樹就是這樣一種結構，可以高效地插入和查询節點。

# BST 定義

二叉查找樹是這樣一種二叉樹結構，它的每個節點包含一個 key 和它附带的數據，對於每個内部節點 V：

- 所有 key 小於 V 的都被存儲在 V 的左子樹
- 所有 key 大於 V 的都存儲在 V 的右子樹

![](./bst.png)

注意這個限制條件，可别和堆搞混了。說白了就是對於每個内部節點，左子樹的 key 都比它小，右子樹都比它大。
如果中序遍历(二叉樹遍历講過了)這颗二叉樹，你會發現輸出的順序正好是有序的。
我們先來定義一下 BST 的節點結構：

```py
class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right
```

# 构造一個 BST
我們還像之前构造二叉樹一樣，按照上图构造一個 BST 用來演示：

```py
class BST(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}
        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTNode(key, value=key)   # 這裡值暂時用 和 key一樣的

        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            if node_dict['is_root']:
                root = node
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            cls.size += 1
        return cls(root)


NODE_LIST = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False},
]
bst = BST.build_from(NODE_LIST)
```


# BST 操作

## 查找
如何查找一個指定的節點呢，根據定義我們知道每個内部節點左子樹的 key 都比它小，右子樹的 key 都比它大，所以
對於带查找的節點 search_key，從根節點開始，如果 search_key 大於當前 key，就去右子樹查找，否则去左子樹查找。 一直到當前節點是 None 了說明没找到對應 key。

![](./bst_search.png)

好，撸原始碼：

```py
    def _bst_search(self, subtree, key):
        if subtree is None:   # 没找到
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value
```


## 獲取最大和最小 key 的節點

其實還按照其定義，最小值就一直向着左子樹找，最大值一直向右子樹找，遞迴查找就行。

```py
    def _bst_min_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:   # 找到左子樹的頭
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.value if node else None
```

## 插入
插入節點的時候我們需要一直保持 BST 的性质，每次插入一個節點，我們都通過遞迴比较把它放到正確的位置。
你會發現新節點总是被作為叶子結點插入。（請你思考這是為什麼）

![](./bst_insert.png)

```py
    def _bst_insert(self, subtree, key, value):
        """ 插入並且返回根節點

        :param subtree:
        :param key:
        :param value:
        """
        if subtree is None:   # 插入的節點一定是根節點，包括 root 為空的情况
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node is not None:   # 更新已經存在的 key
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True
```

## 删除節點
删除操作相比上邊的操作要麻烦很多，首先需要定位一個節點，删除節點後，我們需要始终保持 BST 的性质。
删除一個節點涉及到三種情况：

- 節點是叶節點
- 節點有一個孩子
- 節點有兩個孩子

我們分别來看看三種情况下如何删除一個節點：

#### 删除叶節點
這是最簡單的一種情况，只需要把它的父親指向它的指針设置為 None 就好。

![](./bst_remove_leaf.png)

#### 删除只有一個孩子的節點
删除有一個孩子的節點時，我們拿掉需要删除的節點，之後把它的父親指向它的孩子就行，因為根據 BST
左子樹都小於節點，右子樹都大於節點的特性，删除它之後這個條件依旧满足。

![](./bst_remove_node_with_one_child.png)

#### 删除有兩個孩子的内部節點
假如我們想删除 12 這個節點改怎麼做呢？你的第一反應可能是按照下图的方式：

![](./remove_interior_replace.png)

但是這種方式可能會影響樹的高度，降低查找的效率。這裡我們用另一種非常巧妙的方式。
還记得上邊提到的嗎，如果你中序遍历 BST 並且輸出每個節點的 key，你會發現就是一個有序的數組。
`[1 4 12 23 29 37 41 60 71 84 90 100]`。這裡我們定義兩個概念，逻辑前任(predecessor)和後繼(successor)，請看下图:

![](./predecessor_successor.png)

12 在中序遍历中的逻辑前任和後繼分别是 4 和 23 節點。於是我們還有一種方法來删除 12 這個節點：

- 找到待删除節點 N(12) 的後繼節點 S(23)
- 复制節點 S 到節點 N
- 從 N 的右子樹中删除節點 S，並更新其删除後繼節點後的右子樹

說白了就是找到後繼並且替換，這裡之所以能保證這種方法是正確的，你會發現替換後依旧是保持了 BST 的性质。
有個問題是如何找到後繼節點呢？待删除節點的右子樹的最小的節點不就是後繼嘛，上邊我們已經實現了找到最小 key 的方法了。


![](./find_successor.png)

我們開始撰寫原始碼實現，和之前的操作類似，我們還是通過辅助函數的形式來實現，這個遞迴函數會比较复杂，請你仔細理解:

```py
    def _bst_remove(self, subtree, key):
        """删除節點並返回根節點"""
        if subtree is None:
            return None
        elif key < subtree.key:
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self._bst_remove(subtree.right, key)
            return subtree
        else:  # 找到了需要删除的節點
            if subtree.left is None and subtree.right is None:    # 叶節點，返回 None 把其父親指向它的指針置為 None
                return None
            elif subtree.left is None or subtree.right is None:  # 只有一個孩子
                if subtree.left is not None:
                    return subtree.left   # 返回它的孩子並讓它的父親指過去
                else:
                    return subtree.right
            else:  # 俩孩子，尋找後繼節點替換，並從待删節點的右子樹中删除後繼節點
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(subtree.right, successor_node.key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)
```

完整原始碼你可以在本章的 bst.py  找到。
另外推荐一個可以在線演示過程的網址大家可以手動执行下看看效果： https://www.cs.usfca.edu/~galles/visualization/BST.html

# 時間複雜度分析

上邊介绍的操作時間複雜度和二叉樹的形状有關。平均來說時間複雜度是和樹的高度成正比的，樹的高度 h 是 log(n)，
但是最坏情况下以上操作的時間複雜度都是 O(n)。為了改善 BST 有很多變種，感興趣請参考延伸閱讀中的内容。

![](./bst_worstcase.png)


# 練習题：
- 請你實現查找 BST 最大值的函數


# 延伸閱讀
- 《Data Structures and Algorithms in Python》14 章，樹的概念和算法還有很多，我們這裡介绍最基本的帮你打個基础
- 了解红黑樹。普通二叉查找樹有個很大的問題就是难以保證樹的平衡，极端情况下某些節點可能會非常深，导致查找複雜度大幅退化。而平衡二叉樹就是為了解決這個問題。請搜索對應資料了解下。
- 了解 mysql 索引使用的 B-Tree 結構(多路平衡查找樹)，這個是後端面試資料庫的常考點。想想為什麼？當元素非常多的時候，二叉樹的深度會很深，导致多次磁盘查找。[從B樹、B+樹、B*樹谈到R 樹](https://blog.csdn.net/v_JULY_v/article/details/6530142)


# Leetcode

驗證是否是合法二叉搜索樹 [validate-binary-search-tree](https://leetcode.com/problems/validate-binary-search-tree/
