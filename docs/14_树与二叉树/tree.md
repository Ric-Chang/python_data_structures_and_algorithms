# 树和二叉树
前面我們講了兩種使用分治和遞迴解決排序問題的归並排序和快速排序，堆排序先就此打住，因為涉及到树的概念，所以我們先來講講树。
講完了树之後後面我們開始介绍一種有用的數據結構堆(heap)， 以及借助堆來實現的堆排序，相比前兩種排序算法要稍难理解和實現一些。

# 树
這裡先簡單講講树的概念。树結構是一種包括節點(nodes)和邊(edges)的拥有层级關系的一種結構， 它的形式和家谱树非常類似:

![](./family_tree.png)

如果你了解 linux 文件結構（tree 命令），它的結構也是一棵树。我們快速看下树涉及到的一些概念：

![](./tree.png)

- 根節點(root): 树的最上层的節點，任何非空的树都有一個節點
- 路径(path): 從起始節點到终止節點經历過的邊
- 父亲(parent)：除了根節點，每個節點的上一层邊连接的節點就是它的父亲(節點)
- 孩子(children): 每個節點由邊指向的下一层節點
- 兄弟(siblings): 同一個父亲並且處在同一层的節點
- 子树(subtree): 每個節點包含它所有的後代組成的子树
- 叶子節點(leaf node): 没有孩子的節點成為叶子節點


# 二叉树

了解完树的結構以後，我們來看树結構裡一種簡單但是却比较常用的树-二叉树。
二叉树是一種簡單的树，它的每個節點最多只能包含兩個孩子，以下都是一些合法的二叉树:

![](./binary_tree.png)
![](./binary_tree_level.png)

通過上邊這幅图再來看幾個二叉树相關的概念:

- 節點深度(depth): 節點對应的 level 數字
- 树的高度(height): 二叉树的高度就是 level 數 + 1，因為 level 從 0開始計算的
- 树的宽度(width): 二叉树的宽度指的是包含最多節點的层级的節點數
- 树的 size：二叉树的節點总個數。

一棵 size 為 n 的二叉树高度最多可以是 n，最小的高度是 $ \lfloor lgn \rfloor + 1 $，這裡 log 以 2 為底簡寫為
lgn，和算法導論保持一致。這個結果你只需要用高中的累加公式就可以得到。

# 一些特殊的二叉树
在了解了二叉树的術语和概念之後，我們來看看一些特殊的二叉树，後续章節我們會用到：

### 满二叉树(full binary tree)
如果每個内部節點（非叶節點）都包含兩個孩子，就成為满二叉树。下邊是一些例子，它可以有多種形状：

![](./full_binary_tree.png)

### 完美二叉树(perfect binary tree)
當所有的叶子節點都在同一层就是完美二叉树，毫無間隙填充了 h 层。

![](./perfect_binary_tree.png)

### 完全二叉树(complete binary tree)
當一個高度為 h 的完美二叉树减少到 h-1，並且最底层的槽被毫無間隙地從左到右填充，我們就叫它完全二叉树。
下图就是完全二叉树的例子：

![](./complete_binary_tree.png)

# 二叉树的表示
說了那麼多，那麼怎麼表示一棵二叉树呢？其實你發現會和鏈表有一些相似之處，一個節點，然後節點需要保存孩子的指針，我以构造下邊這個二叉树為例子：
我們先定義一個類表示節點：

![](preorder.png)

```py
class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
```

當然和鏈表類似，root 節點是我們的入口，於是乎定義一個 二叉树：

```py
class BinTree(object):
    def __init__(self, root=None):
        self.root = root
```

怎麼构造上图中的二叉树呢，似乎其他課本没找到啥例子(有些例子是寫了一堆嵌套節點來定義，很难搞清楚层次關系)，我自己定義了一種方法，首先我們輸入節點信息，仔细看下邊原始碼，叶子節點的 left 和 right 都是 None，並且只有一個根節點 A:

```py
node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]
```

然後我們给 BinTreeNode 定義一個 build_from 方法，當然你也可以定義一種自己的构造方法：

```py
class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """通過節點信息构造二叉树
        第一次遍历我們构造 node 節點
        第二次遍历我們给 root 和 孩子赋值
        最後我們用 root 初始化這個類並返回一個對象

        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)
btree = BinTree.build_from(node_list)
```

大功告成，這樣我們就构造了一棵二叉树對象。下邊我們看看它的一些常用操作。

# 二叉树的遍历
不知道你有没有發現，二叉树其實是一種遞迴結構，因為單独拿出來一個 subtree 子树出來，其實它還是一棵树。那遍历它就很方便啦，我們可以直接用遞迴的方式來遍历它。但是當處理顺序不同的時候，树又分為三種遍历方式:

- 先(根)序遍历: 先處理根，之後是左子树，然後是右子树
- 中(根)序遍历: 先處理左子树，之後是根，最後是右子树
- 後(根)序遍历: 先處理左子树，之後是右子树，最後是根

我們來看下實現，其實算是比较直白的遞迴函數:

```py
class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """通過節點信息构造二叉树
        第一次遍历我們构造 node 節點
        第二次遍历我們给 root 和 孩子赋值

        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    def preorder_trav(self, subtree):
        """ 先(根)序遍历

        :param subtree:
        """
        if subtree is not None:
            print(subtree.data)    # 遞迴函數裡先處理根
            self.preorder_trav(subtree.left)   # 遞迴處理左子树
            self.preorder_trav(subtree.right)    # 遞迴處理右子树


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]
btree = BinTree.build_from(node_list)
btree.preorder_trav(btree.root)    # 輸出 A, B, D, E, H, C, F, G, I, J
```
怎麼樣是不是挺簡單的，比较直白的遞迴函數。如果你不明白，影片裡我們會画個图來說明。

# 二叉树层序遍历

除了遞迴的方式遍历之外，我們還可以使用层序遍历的方式。层序遍历比较直白，就是從根節點開始按照一层一层的方式遍历節點。
我們可以從根節點開始，之後把所有當前层的孩子都按照從左到右的顺序放到一個列表裡，下一次遍历所有這些孩子就可以了。

```py
    def layer_trav(self, subtree):
        cur_nodes = [subtree]  # current layer nodes
        next_nodes = []
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                print(node.data)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_nodes = next_nodes  # 繼续遍历下一层
            next_nodes = []
```

還有一種方式就是使用一個陣列，之前我們知道陣列是一個先進先出結構，如果我們按照一层一层的顺序從左往右把節點放到一個陣列裡，
也可以實現层序遍历：

```py
    def layer_trav_use_queue(self, subtree):
        q = Queue()
        q.append(subtree)
        while not q.empty():
            cur_node = q.pop()
            print(cur_node.data)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)


from collections import deque
class Queue(object):  # 借助内置的 deque 我們可以迅速實現一個 Queue
    def __init__(self):
        self._items = deque()

    def append(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.popleft()

    def empty(self):
        return len(self._items) == 0
```


# 反轉二叉树
之所以單拎出來說這個是因為 mac 下著名的 brew 工具作者据說是因為面試 google 白板编程没寫出來反轉二叉树跪了。然後人家就去了苹果 😂。其實吧和遍历操作相比也没啥太大區别，遞迴交換就是了：

```py
    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)
```


# 練習题
- 請你完成二叉树的中序遍历和後序遍历以及單元測試
- 树的遍历我們用了 print，請你嘗試換成一個 callback，這樣就能自定義處理树節點的方式了。
- 請问树的遍历操作時間複雜度是多少？假设它的 size 是 n
- 你能用非遞迴的方式來實現树的遍历嗎？我們知道計算機内部使用了 stack，如果我們自己模擬如何實現？請你嘗試完成
- 只根據二叉树的中序遍历和後序遍历能否確定一棵二叉树？你可以舉一個反例嗎？


# 延伸閱讀
- 《Data Structures and Algorithms in Python》 13 章 Binary Trees
-  [https://www.geeksforgeeks.org/iterative-preorder-traversal/](https://www.geeksforgeeks.org/iterative-preorder-traversal/)


# Leetcode 練習

- [leetcode binary-tree-preorder-traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
二叉树的先序遍历

- [leetcode binary-tree-inorder-traversal/](https://leetcode.com/problems/binary-tree-inorder-traversal/)
二叉树的中序遍历

- [leetcode binary-tree-postorder-traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
二叉树的後序遍历

- [leetcode binary-tree-right-side-view](https://leetcode.com/problems/binary-tree-right-side-view/description/)
使用树的层序遍历我們能實現一個树的左右视图，比如從一個二叉树的左邊能看到哪些節點。 請你嘗試做這個練習题

- [leetcode construct-binary-tree-from-preorder-and-postorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/submissions/)
根據二叉树的 前序和後序遍历，返回一颗完整的二叉树。
