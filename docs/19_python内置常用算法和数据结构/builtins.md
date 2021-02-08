# Python 常用内置算法和數據結構
相信到這裡大家對常用的數據結構和算法及其實現都比较熟悉了。
之前在每章的數據結構和算法中涉及到的章節我都會提到對應的 python 内置模塊，一般如果内置的可以满足需求，我們優先使用内置模塊，
因為在性能和容错性方面内置模塊要好於我們自己實現（比如有些是 c 實現的）。本章我們不會再對每個模塊的原理詳細說明，仅列舉出一些常見模塊供大家参考，
如果有需要最好的學習方式就是参考 Python 的官方文件。很多高級的數據結構我們也可以通過 google 搜索現成的庫拿來直接用。

- 常用内置數據類型：list, tuple, dict, set, frozenset
- collections
- heapq
- bisect

下邊我列了一個常用的表格，如果有遗漏可以在 issue 中提出。確保你了解這些數據結構和算法的使用以及時間、空間複雜度。

|  數據結構/算法 | 语言内置                        | 内置庫                                                        |
|----------------|---------------------------------|---------------------------------------------------------------|
| 線性結構       | list(列表)/tuple(元祖)          | array(數組，不常用)/collections.namedtuple                    |
| 鏈式結構       |                                 | collections.deque(双端陣列)                                   |
| 字典結構       | dict(字典)                      | collections.Counter(計數器)/OrderedDict(有序字典)/defaultdict |
| 集合結構       | set(集合)/frozenset(不可變集合) |                                                               |
| 排序算法       | sorted                          |                                                               |
| 二分算法       |                                 | bisect模塊                                                    |
| 堆算法         |                                 | heapq模塊                                                     |
| 缓存算法       |                                 | functools.lru_cache(Least Recent Used, python3)               |
