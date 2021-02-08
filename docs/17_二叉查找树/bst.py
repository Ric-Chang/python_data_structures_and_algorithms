# -*- coding: utf-8 -*-


class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


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

    def _bst_search(self, subtree, key):
        if subtree is None:   # 没找到
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def __contains__(self, key):
        """實現 in 操作符"""
        return self._bst_search(self.root, key) is not None

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value

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
            else:  # 俩孩子，尋找後繼節點替換，並删除其右子樹的後繼節點，同時更新其右子樹
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(subtree.right, successor_node.key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)


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


def test_bst_tree():
    bst = BST.build_from(NODE_LIST)
    for node_dict in NODE_LIST:
        key = node_dict['key']
        assert bst.get(key) == key
    assert bst.size == len(NODE_LIST)
    assert bst.get(-1) is None    # 單例的 None 我們用 is 來比较

    assert bst.bst_min() == 1

    bst.add(0, 0)
    assert bst.bst_min() == 0

    bst.remove(12)
    assert bst.get(12) is None

    bst.remove(1)
    assert bst.get(1) is None

    bst.remove(29)
    assert bst.get(29) is None
