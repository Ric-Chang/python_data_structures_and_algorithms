# -*- coding: utf-8 -*-

# 從數組和列表章复制的原始碼


class Array(object):

    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    """定義一個 hash 表 數組的槽
    注意，一個槽有三種狀態，看你能否想明白。相比鏈接法解決衝突，二次探查法删除一個 key 的操作稍微复杂。
    1.從未使用 HashMap.UNUSED。此槽没有被使用和衝突過，查找時只要找到 UNUSED 就不用再繼续探查了
    2.使用過但是 remove 了，此時是 HashMap.EMPTY，該探查點後面的元素扔可能是有key
    3.槽正在使用 Slot 節點
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):

    UNUSED = None  # 没被使用過
    EMPTY = Slot(None, None)  # 使用却被删除過

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)   # 保持 2*i 次方
        self.length = 0

    @property
    def _load_factor(self):
        # load_factor 超過 0.8 重新分配
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5 + 1) % _len
        return None

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index*5 + 1) % _len
        return index

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED)

    def __contains__(self, key):  # in operator
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)

        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key

#########################################
# 上邊是從 哈希表章 拷貝過來的原始碼，我們會直接繼承 HashTable 實現 dict
#########################################


class DictADT(HashTable):

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.get(key)

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)


test_dict_adt()
