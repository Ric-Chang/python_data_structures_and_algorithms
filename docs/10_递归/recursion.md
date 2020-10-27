# 遞迴

>    Recursion is a process for solving problems by subdividing a larger
>    problem into smaller cases of the problem itself and then solving
>    the smaller, more trivial parts.

遞迴是计算機科學里出现非常多的一個概念，有时候用遞迴解决問題看起來非常簡單優雅。
之前講過的數據結構中我們并没有使用遞迴，因為遞迴涉及到调用栈，可能會让初學者搞晕。這一章我們開始介绍遞迴，
後面講到树和一些排序算法的时候我們還會碰到它。我非常推荐你先看看《算法图解》第三章 遞迴，
舉的例子比较浅显易懂。


# 什麼是遞迴？
遞迴用一種通俗的话來說就是自己调用自己，但是需要分解它的参数，让它解决一個更小一點的問題，當問題小到一定规模的时候，需要一個遞迴出口返回。
這裡舉一個和其他很多老套的教科书一样喜欢舉的例子，階乘函数，我覺得用來它演示再直觀不過。它的定義是這样的：

![](./fact.png)

我們很容易根據它的定義写出這样一個遞迴函数，因為它本身就是遞迴定義的。

```py
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
```
看吧，几乎完全是按照定義來写的。我們來看下遞迴函数的几個特點:

- 遞迴必须包含一個基本的出口(base case)，否则就會无限遞迴，最终导致栈溢出。比如這裡就是 n == 0 返回 1
- 遞迴必须包含一個可以分解的問題(recursive case)。 要想求得 fact(n)，就需要用 n * fact(n-1)
- 遞迴必须必须要向着遞迴出口靠近(toward the base case)。 這裡每次遞迴调用都會 n-1，向着遞迴出口 n == 0 靠近


# 调用栈
看了上一個例子你可能覺得遞迴好簡單，先别着急，我們再舉個簡單的例子，上邊我們并没有講遞迴如何工作的。
假如让你输出從 1 到 10 這十個数字，如果你是個正常人的话，我想你的第一反应都是這麼写：

```py
def print_num(n):
    for i in range(1, n + 1):    # 注意很多编程语言使用的都是 從 0 開始的左闭右開區間, python 也不例外
        print(i)


if __name__ == '__main__':
    print_num(10)
```

我們嘗試写一個遞迴版本，不就是自己调用自己嘛：

```py
def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n-1)
        print(n)
```

你猜下它的输出？然後我們调换下 print 顺序，你再猜下它的输出

```py
def print_num_recursive_revserve(n):
    if n > 0:
        print(n)
        print_num_recursive_revserve(n-1)
```
你能明白是為什麼嗎？我建議你運行下這几個小例子，它們很簡單但是却能說明問題。
计算機内部使用调用栈來實現遞迴，這裡的栈一方面指的是内存中的栈區，一方面栈又是之前講到的後进先出這種數據結構。
每當进入遞迴函数的时候，系统都會為當前函数開辟内存保存當前变量值等信息，每個调用栈之間的數據互不影响，新调用的函数
入栈的时候會放在栈顶。影片里我們會画图來演示這個過程。

遞迴只用大脑不用紙筆模擬的话很容易晕，因為明明是同一個变量名字，但是在不同的调用栈里它是不同的值，所以我建議
你最好手動画画這個過程。

![](./print_rec.png)

# 用栈模擬遞迴
刚才說到了调用栈，我們就用栈來模擬一把。之前栈這一章我們講了如何自己實現栈，不過這裡為了不拷贝太多代碼，我們直接用 collections.deque 就可以
快速實現一個簡單的栈。

```py
from collections import deque


class Stack(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_use_stack(n):
    s = Stack()
    while n > 0:    # 不断将参数入栈
        s.push(n)
        n -= 1

    while not s.is_empty():    # 参数弹出
        print(s.pop())
```
這裡結果也是输出 1 到 10，只不過我們是手動模擬了入栈和出栈的過程，帮助你理解计算機是如何實現遞迴的，是不是挺簡單！现在你能明白為什麼上邊 print_num_recursive print_num_recursive_revserve 兩個函数输出的區别了嗎？


# 尾遞迴
上邊的代碼示例(麻雀雖小五脏俱全)中實際上包含了兩種形式的遞迴，一種是普通的遞迴，還有一種叫做尾遞迴：

```py
def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n-1)
        print(n)


def print_num_recursive_revserve(n):
    if n > 0:
        print(n)
        print_num_recursive_revserve(n-1)    # 尾遞迴
```

概念上它很簡單，就是遞迴调用放在了函数的最後。有什麼用呢？
普通的遞迴, 每一级遞迴都产生了新的局部变量, 必须创建新的调用栈, 随着遞迴深度的增加, 创建的栈越來越多, 造成爆栈。雖然尾遞迴调用也會创建新的栈,
但是我們可以優化使得尾遞迴的每一级调用共用一個栈!, 如此便可解决爆栈和遞迴深度限制的問題!
不幸的是 python 默认不支持尾遞迴優化（見延伸閱讀），不過一般尾遞迴我們可以用一個迭代來優化它。


# 汉诺塔問題

有三根杆子A，B，C。A杆上有N個(N>1)穿孔圆盘，盘的尺寸由下到上依次变小。要求按下列规则将所有圆盘移至C杆：
但是有兩個條件：

- 每次只能移動一個圆盘；
- 大盘不能叠在小盘上面。

> 最早發明這個問題的人是法国数學家爱德华·卢卡斯。
> 傳說越南河内某間寺院有三根银棒，上串64個金盘。寺院里的僧侣依照一個古老的预言，以上述规则移動這些盘子；预言說當這些盘子移動完毕，世界就會灭亡。
> 這個傳說叫做梵天寺之塔問題（Tower of Brahma puzzle）。但不知道是卢卡斯自创的這個傳說，還是他受他人启發。



![五個盘子的汉诺塔問題](./hanoi_tower.png)

理解這個問題需要我們一些思维上的转换，因為我們正常的思维可能都是從上邊最小的盘子開始移動，但是這裡我們從移動最底下的盘子開始思考。
假设我們已經知道了如何移動上邊的四個盘子到 B(pole2)，现在把最大的盘子從 A -> C 就很簡單了。當把最大的盘子移動到
C 之後，只需要把 B 上的 4 個盘子從 B -> C 就行。（這裡的 pole1, 2, 3 分别就是 A, B, C 杆）

![](./hanoi_four_disks.png)

問題是仍要想办法如何移動上邊的 4 個盘子，我們可以同样的方式來移動上邊的 4 個盘子，這就是一種遞迴的解法。
给定 n 個盘子和三個杆分别是 源杆(Source), 目標杆(Destination)，和中介杆(Intermediate)，我們可以定義如下遞迴操作：

- 把上邊的 n-1 個盘子從 S 移動到 I，借助 D 杆
- 把最底下的盘子從 S 移動到 D
- 把 n-1 個盘子從 I 移動到 D，借助 S

我們把它转换成代碼：

```py
def hanoi_move(n, source, dest, intermediate):
    if n >= 1:  # 遞迴出口，只剩一個盘子
        hanoi_move(n-1, source, intermediate, dest)
        print("Move %s -> %s" % (source, dest))
        hanoi_move(n-1, intermediate, dest, source)
hanoi_move(3, 'A', 'C', 'B')

# 输出，建議你手動模擬下。三個盘子 A(Source), B(intermediate), C(Destination)
"""
Move A -> C
Move A -> B
Move C -> B
Move A -> C
Move B -> A
Move B -> C
Move A -> C
"""
```

<center>
![三個盘子的汉诺塔解法](./hanoi.gif)
</center>

是不是很神奇，但是老實說這個過程仅凭大脑空想是比较难以想象出來的。人的大脑『栈』深度很有限，因為你甚至都没法同时记住超過 8 個以上的
无意義数字，所以用大脑模擬不如用紙筆來模擬下。（不排除有些聪明的同學能迅速在脑瓜里完成這個過程）

# 延伸閱讀
遞迴是個非常重要的概念，我們後面的數據結構和算法中還會多次碰到它，我建議你多閱讀一些資料加深理解：

- 《算法图解》第三章 遞迴
- 《Data Structures and Algorithms in Python》 第 10 章 Recursion
- [《Python開启尾遞迴優化!》](https://segmentfault.com/a/1190000007641519)
- [尾调用優化](http://www.ruanyifeng.com/blog/2015/04/tail-call.html)
- [汉诺塔](https://zh.wikipedia.org/wiki/%E6%B1%89%E8%AF%BA%E5%A1%94)

# 思考题
- 你能舉出其他一些使用到遞迴的例子嗎？
- 實現一個 flatten 函数，把嵌套的列表扁平化，你需要用遞迴函数來實現。比如 [[1,2], [1,2,3] -> [1,2,1,2,3]
- 使用遞迴和循環各有什麼優缺點，你能想到嗎？怎麼把一個尾遞迴用迭代替换？
- 遞迴有时候雖然很優雅直觀，但是時間複雜度却不理想，比如斐波那契数列，它的表达式是 F(n) = F(n-1) + F(n-2)，你能计算它的時間複雜度嗎？請你画個树來表示它的计算過程，為什麼這個時間複雜度很不理想？我們怎样去優化它。
- python 内置的 dict 只能用 dict['key'] 的形式訪問比较麻烦，我們想用 dict.key 的形式訪問。tornado web 框架中提供了一個 ObjectDict，請你實現一個遞迴函数接收一個字典，并返回一個可以嵌套訪問的 ObjectDict
