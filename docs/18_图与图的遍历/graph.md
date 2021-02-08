# 图
之前們講過很多數據結構了，包括線性結構、鏈式結構、树結構等，這些結構基本就能应付我們的業務開發了。
這一章來看下图結構，图的使用也比较广泛，比如人物關系、路径選择等等，相比前面的一些數據結構和算法要相對复杂一些。
不過也不用担心，除非是特定的後端業務，一般图結構的使用比较少。這一章我們簡單地介绍下图結構，以及图的搜索算法。

# 什麼是图？
我們先來考虑日常生活中的一個問題，我們在出行的時候一般會考虑使用地图软件搜下從一個地點到另外一個地點的路線。
這裡把地點抽象成一個圈，路径抽象成線，於是乎就有了下面的图，其實還是非常好理解的。

![](./graph_road.png)

簡單地說就是有節點(node)和邊(edge)組成的一種數據結構，相邻的節點称之為邻居。 注意图分為有向图和無向图，
比如有些路是單行道，有些是双行道，有向图我們用箭頭指向，無向图就是一條直線连接。

# 图的表示
那我們怎麼把一個图抽象成原始碼來表示呢？因為最终我們還是需要原始碼來實現的。通常有兩種表示方法，邻接表法和邻接矩陣表示。

![](./graph_rep.png)

- 邻接表法：對於每個图中的點，將它的邻居放到一個鏈表裡
- 邻接矩陣：對於 n 個點，构造一個 n * n 的矩陣，如果有從點 i 到點 j 的邊，就將矩陣的位置 matrix[i][j] 置為 1.

不過我們可以看到，用矩陣存儲图是非常耗费空間的，大部分情况下矩陣是稀疏的，所以我們後面選择使用邻接表。

# 图的遍历
遍历图最常用的有兩種方式，就是你常聽到的 BFS 和 DFS.

- BFS: Breadth First Search，广度優先搜索
- DFS: Depdth First Search，深度優先搜索

### BFS
BFS 類似於树的层序遍历，從第一個節點開始，先訪問离 A 最近的點，接着訪問次近的點。我們先來构造一個图：

```py
graph = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}
```
如何『由近及远』地訪問節點呢？我們先訪問起點 A 的邻居，然後邻居訪問完再訪問邻居的邻居不就行了？
就是這個思想，不過我們需要一個陣列辅助，陣列之前說過是一種先進先出結構，我們只需要把起點的邻居先入隊，
當邻居訪問完了再去訪問邻居的邻居就可以了，對於已經訪問過的節點，我們用一個 set 记录它就好了。原始碼如下：

```py
# -*- coding: utf-8 -*-

from collections import deque


GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def bfs(graph, start):
    search_queue = Queue()
    search_queue.push(start)
    searched = set()
    while search_queue:   # 陣列不為空就繼续
        cur_node = search_queue.pop()
        if cur_node not in searched:
            yield cur_node
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.push(node)

print('bfs:')
bfs(GRAPH, 'A')
"""
bfs:
A
B
F
C
I
G
E
D
H
"""
```

![](./bfs.png)

### DFS
深度優先搜索(DFS)是每遇到一個節點，如果没有被訪問過，就直接去訪問它的邻居節點，不断加深。原始碼其實很簡單：

```
DFS_SEARCHED = set()


def dfs(graph, start):
    if start not in DFS_SEARCHED:
        print(start)
        DFS_SEARCHED.add(start)
    for node in graph[start]:
        if node not in DFS_SEARCHED:
            dfs(graph, node)


print('dfs:')
dfs(GRAPH, 'A')  # A B C I D G F E H

```


# 思考题
- DFS 中我們使用到了遞迴，請你用堆疊來改写這個函數？（原始碼裡有答案，我建議你先嘗試自己實現）

# 延伸閱讀
图的算法還有很多，這裡就不一一列舉了，感興趣的讀者可以繼续閱讀一下材料。

- [數據結構之图](https://www.zybuluo.com/guoxs/note/249812)
- 《算法图解》第六章
