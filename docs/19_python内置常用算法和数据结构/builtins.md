# Python 常用内置算法和數據結構
相信到這裡大家對常用的數據結構和算法及其實現都比较熟悉了。
之前在每章的數據結構和算法中涉及到的章節我都會提到對应的 python 内置模块，一般如果内置的可以满足需求，我們優先使用内置模块，
因為在性能和容错性方面内置模块要好于我們自己實現（比如有些是 c 實現的）。本章我們不會再對每個模块的原理详细說明，仅列举出一些常見模块供大家参考，
如果有需要最好的学习方式就是参考 Python 的官方文档。很多高级的數據結構我們也可以通過 google 搜索现成的库拿來直接用。

- 常用内置數據类型：list, tuple, dict, set, frozenset
- collections
- heapq
- bisect

下邊我列了一個常用的表格，如果有遗漏可以在 issue 中提出。确保你了解這些數據結構和算法的使用以及時間、空間複雜度。

|  數據結構/算法 | 语言内置                        | 内置库                                                        |
|----------------|---------------------------------|---------------------------------------------------------------|
| 線性結構       | list(列表)/tuple(元祖)          | array(数组，不常用)/collections.namedtuple                    |
| 鏈式結構       |                                 | collections.deque(双端队列)                                   |
| 字典結構       | dict(字典)                      | collections.Counter(计数器)/OrderedDict(有序字典)/defaultdict |
| 集合結構       | set(集合)/frozenset(不可变集合) |                                                               |
| 排序算法       | sorted                          |                                                               |
| 二分算法       |                                 | bisect模块                                                    |
| 堆算法         |                                 | heapq模块                                                     |
| 缓存算法       |                                 | functools.lru_cache(Least Recent Used, python3)               |
