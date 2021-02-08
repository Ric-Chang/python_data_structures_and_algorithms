# 哈希表
不知道你有没有好奇過為什麼 Python 裡的 dict 和 set 查找速度這麼快呢，用了什麼黑魔法嗎？
經常聽别人說哈希表(也叫做散列表)，究竟什麼是哈希表呢？這一章我們來介绍哈希表，後续章節我們會看到 Python 中的字典和集合是如何實現的。

# 哈希表的工作過程
前面我們已經講到了數組和鏈表，數組能通過下標 O(1) 訪問，但是删除一個中間元素却要移動其他元素，時間 O(n)。
循環双端鏈表倒是可以在知道一個節點的情况下迅速删除它，但是吧查找又成了 O(n)。

难道就没有一種方法可以快速定位和删除元素嗎？似乎想要快速找到一個元素除了知道下標之外别無他法，於是乎聪明的計算機科學家又想到了一種方法。
能不能给每個元素一種『逻辑下標』，然後直接找到它呢，哈希表就是這種實現。它通過一個哈希函數來計算一個元素應該放在數組哪個位置，當然對於一個
特定的元素，哈希函數每次計算的下標必须要一樣才可以，而且范围不能超過给定的數組長度。

我們還是以书中的例子說明，假如我們有一個數組 T，包含 M=13 個元素，我們可以定義一個簡單的哈希函數 h

```
h(key) = key % M
```

這裡取模運算使得 h(key) 的結果不會超過數組的長度下標。我們來分别插入以下元素：

765, 431, 96, 142, 579, 226, 903, 388

先來計算下它們应用哈希函數後的結果:

```
M = 13
h(765) = 765 % M = 11
h(431) = 431 % M = 2
h(96) = 96 % M = 5
h(142) = 142 % M = 12
h(579) = 579 % M = 7
h(226) = 226 % M = 5
h(903) = 903 % M = 6
h(388) = 388 % M = 11
```
下邊我画個图演示整個插入過程(纯手工绘制，原谅我字寫得不太優雅):

![](./insert_hash.png)


# 哈希衝突 (collision)
這裡到插入 226 這個元素的時候，不幸地發現 h(226) = h(96) = 5，不同的 key 通過我們的哈希函數計算後得到的下標一樣，
這種情况成為哈希衝突。怎麼办呢？聪明的計算機科學家又想到了办法，其實一種直觀的想法是如果衝突了我能不能讓數組中
對应的槽变成一個鏈式結構呢？這就是其中一種解決方法，叫做 **鏈接法(chaining)**。如果我們用鏈接法來處理衝突，後面的插入是這樣的：

![](./insert_hash_chaining.png)

這樣就用鏈表解決了衝突問題，但是如果哈希函數選不好的話，可能就导致衝突太多一個鏈变得太長，這樣查找就不再是 O(1) 的了。
還有一種叫做開放尋址法(open  addressing)，它的基本思想是當一個槽被占用的時候，採用一種方式來尋找下一個可用的槽。
（這裡槽指的是數組中的一個位置），根據找下一個槽的方式不同，分為：

- 線性探查(linear probing): 當一個槽被占用，找下一個可用的槽。  $ h(k, i) = (h^\prime(k) + i)  \% m, i = 0,1,...,m-1 $
- 二次探查(quadratic probing): 當一個槽被占用，以二次方作為偏移量。 $ h(k, i) = (h^\prime(k) + c_1 + c_2i^2) \% m , i=0,1,...,m-1 $
- 双重散列(double hashing): 重新計算 hash 結果。 $ h(k,i) = (h_1(k) + ih_2(k)) \% m $

我們選一個簡單的二次探查函數 $ h(k, i) = (home + i^2) \% m $，它的意思是如果
遇到了衝突，我們就在原始計算的位置不断加上 i 的平方。我寫了段原始碼來模擬整個計算下標的過程：

```py
inserted_index_set = set()
M = 13

def h(key, M=13):
    return key % M

to_insert = [765, 431, 96, 142, 579, 226, 903, 388]
for number in to_insert:
    index = h(number)
    first_index = index
    i = 1
    while index in inserted_index_set:   # 如果計算發現已經占用，繼续計算得到下一個可用槽的位置
        print('\th({number}) = {number} % M = {index} collision'.format(number=number, index=index))
        index = (first_index +  i*i) % M   # 根據二次方探查的公式重新計算下一個需要插入的位置
        i += 1
    else:
        print('h({number}) = {number} % M = {index}'.format(number=number, index=index))
        inserted_index_set.add(index)
```
這段原始碼輸出的結果如下：

```
h(765) = 765 % M = 11
h(431) = 431 % M = 2
h(96) = 96 % M = 5
h(142) = 142 % M = 12
h(579) = 579 % M = 7
	h(226) = 226 % M = 5 collision
h(226) = 226 % M = 6
	h(903) = 903 % M = 6 collision
	h(903) = 903 % M = 7 collision
h(903) = 903 % M = 10
	h(388) = 388 % M = 11 collision
	h(388) = 388 % M = 12 collision
	h(388) = 388 % M = 2 collision
	h(388) = 388 % M = 7 collision
h(388) = 388 % M = 1
```

遇到衝突之後會重新計算，每個待插入元素最终的下標就是：

![](quadratic_hash.png)

![](quadratic_result.png)


# Cpython 如何解決哈希衝突
如果你對 cpython 解释器的實現感興趣，可以参考下這個文件 [dictobject.c](https://github.com/python/cpython/blob/master/Objects/dictobject.c#L165)。
不同 cpython 版本實現的探查方式是不同的，後面我們自己實現 HashTable ADT 的時候會模仿這個探查方式來解決衝突。


```
The first half of collision resolution is to visit table indices via this
recurrence:

    j = ((5*j) + 1) mod 2**i

For any initial j in range(2**i), repeating that 2**i times generates each
int in range(2**i) exactly once (see any text on random-number generation for
proof).  By itself, this doesn't help much:  like linear probing (setting
j += 1, or j -= 1, on each loop trip), it scans the table entries in a fixed
order.  This would be bad, except that's not the only thing we do, and it's
actually *good* in the common cases where hash keys are consecutive.  In an
example that's really too small to make this entirely clear, for a table of
size 2**3 the order of indices is:

    0 -> 1 -> 6 -> 7 -> 4 -> 5 -> 2 -> 3 -> 0 [and here it's repeating]
```

# 哈希函數
到這裡你應該明白哈希表插入的工作原理了，不過有個重要的問題之前没提到，就是 hash 函數怎麼選？
當然是散列得到的衝突越來越小就好啦，也就是說每個 key 都能尽量被等可能地散列到 m 個槽中的任何一個，並且與其他 key 被散列到哪個槽位無關。
如果你感興趣，可以閱讀後面提到的一些参考資料。影片裡我們使用二次探查函數，它相比線性探查得到的結果衝突會更少。


# 装载因子(load factor)
如果繼续往我們的哈希表裡塞東西會發生什麼？空間不够用。這裡我們定義一個負载因子的概念(load factor)，其實很簡單，就是已經使用的槽數比哈希表大小。
比如我們上邊的例子插入了 8 個元素，哈希表总大小是 13， 它的 load factor 就是 $ 8/13 \approx 0.62 $。當我們繼续往哈希表插入數據的時候，很快就不够用了。
通常當負载因子開始超過 0.8 的時候，就要新開辟空間並且重新進行散列了。


# 重哈希(Rehashing)
當負载因子超過 0.8 的時候，需要進行 rehashing 操作了。步骤就是重新開辟一塊新的空間，開多大呢？感興趣的話可以看下 cpython 的 dictobject.c 文件然後搜索
GROWTH_RATE 這個關键字，你會發現不同版本的 cpython 使用了不同的策略。python3.3 的策略是扩大為已經使用的槽數目的兩倍。開辟了新空間以後，會把原來哈希表裡
不為空槽的數據重新插入到新的哈希表裡，插入方式和之前一樣。這就是 rehashing 操作。

# HashTable ADT
實践是檢驗真理的唯一標准，這裡我們來實現一個簡化版的哈希表 ADT，主要是為了讓你更好地了解它的工作原理，有了它，後面實現起 dict 和 set 來就小菜一碟了。
這裡我們使用到了定長數組，還记得我們在數組和列表章節裡實現的 Array 吧，這裡要用上了。

解決衝突我們使用二次探查法，模擬 cpython 二次探查函數的實現。我們來實現三個哈希表最常用的基本操作，這實際上也是使用字典的時候最常用的操作。

- add(key, value)
- get(key, default)
- remove(key)

```py
class Slot(object):
    """定義一個 hash 表 數組的槽
    注意，一個槽有三種狀態，看你能否想明白
    1.從未使用 HashMap.UNUSED。此槽没有被使用和衝突過，查找時只要找到 UNUSED 就不用再繼续探查了
    2.使用過但是 remove 了，此時是 HashMap.EMPTY，該探查點後面的元素扔可能是有key
    3.槽正在使用 Slot 節點
    """
    def __init__(self, key, value):
        self.key, self.value = key, value

class HashTable(object):
    pass
```

具體的實現和原始碼编寫在影片裡講解。這個原始碼可不太好實現，稍不留神就會有错，我們還是通過编寫單元測試驗證原始碼的正確性。

# 思考题
- 請你分析下哈希表插入和删除元素的平均時間複雜度是多少？我們都實現原始碼了，相信這個問題你可以回答上來
- Slot 在二次探查法裡為什麼不能直接删除？為什麼我們要给它定義幾個狀態？

# 延伸閱讀
- 《Data Structures and Algorithms in Python》11 章 Hash Tables
- 《算法導論》第三版 11 章散列表，了解幾種哈希衝突的解決方式，以及為什麼我們選择二次探查而不是線性探查法？
- 介绍 c 解释器如何實現的 python dict對象：[Python dictionary implementation](http://www.laurentluce.com/posts/python-dictionary-implementation/)
