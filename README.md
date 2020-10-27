# Python 算法与數據結構影片教程

## 课程简介
數據結構和算法是每個程序员需要掌握的基础知识之一，也是面试中跨不過的槛。目前關于 Python 算法和數據結構的系统中文资料比较欠缺，
笔者嘗試录制影片教程帮助 Python 開發者掌握常用算法和數據結構，提升開發技能。
本教程是付费教程(文字内容和代碼免费)，因為笔者录制的過程中除了购买软件、手写板等硬件之外，业余需要花费很多時間和精力來录制影片、查资料、编写课件和代碼，养家糊口不容易，希望大家體谅。

## 鏈接
影片教程已經發布在网易云课堂和 csdn 学院，内容一致，推荐使用网易云课堂。

[网易云课堂: Python數據結構与算法教程](http://study.163.com/course/introduction.htm?courseId=1005526003) 影片教程

[csdn 学院：Python數據結構与算法教程](https://edu.csdn.net/course/detail/8332)

[网上閱讀《Python 算法与數據結構教程 》](http://ningning.today/python_data_structures_and_algorithms/)

[github 鏈接](https://github.com/PegasusWang/python_data_structures_and_algorithms)

[readthedoc 电子书下载](http://python-data-structures-and-algorithms.readthedocs.io/zh/latest/)

[《開源一個 Python 算法和數據結構中文教程[影片]》](https://zhuanlan.zhihu.com/p/36038003)  影片講解示例

## 痛點
- 講 Python 數據結構和算法的资料很少，中文资料更少
- 很多自学 Python 的工程师對基础不够重视，面试也發现很多數據結構和算法不過關，很多人挂在了基础的數據結構和算法上
- 缺少工程应用场景下的講解，很多講算法的资料太『教科书化』。本书實現的代碼工程上可用
- 网上很多影片教程不够循序渐进，不成系统

## 作者简介
曾就职于[知乎](https://www.zhihu.com/people/pegasus-wang/activities)，任後端工程师，多年 Python 開發經验。

知乎专栏：

- [《Python 学习之路》](https://zhuanlan.zhihu.com/c_85234576)
- [《玩转vim(影片)》](https://zhuanlan.zhihu.com/vim-video)

电子书：[《Python web 入坑指南》](http://python-web-guide.readthedocs.io/zh/latest/)

## 课程内容
包括我們在業務開發和面试中常用的算法和數據結構，希望可以帮助 Python 開發者快速上手，很多老手写業務代碼写多了很多基础知识忘记了，
也可以作為回顾。课程尽量用通俗的方式講解，結合 python 语言和日常開發實践的經验。书中代碼可以作為大家的面试笔试参考。
對于每個算法和用到的數據結構我們需要知道:

- 原理
- Python 實現方式
- 時間、空間複雜度
- 使用场景，什么时候用

## 目录結構
這裡講解的章節我参考了下邊教材中列举的一些书籍，并且自己设计了大纲，争取做到循序渐进，簡單實用。因為實現一些高级數據結構的时候會用到
很多底层數據結構，防止跳跃太大导致讀者理解困难。

课程的目录結構如下，每一章都有配套的文字講義(markdown)，示例代碼，影片講解，详细的講解一般會放在影片里，使用手写板來
进行板书，包括文字、图示、手動模擬算法過程等。

- 课程介绍
- 课程简介之笨方法学算法
- 抽象數據类型 ADT，面向對象编程
- 数组和列表
- 鏈表，高级鏈表。双鏈表，循環双端鏈表
- 队列，双端队列，循環双端队列
- 栈，栈溢出
- 算法分析，時間複雜度 大O 表示法
- 哈希表，散列冲突
- 字典
- 集合
- 遞迴
- 查找：線性查找和二分查找
- 基本排序算法: 冒泡、选择、插入排序
- 高级排序算法: 归并排序、快排
- 树，二叉树
- 堆与堆排序
- 優先级队列
- 二叉查找树
- 图与图的遍历
- python 内置常用數據結構和算法的使用。list, dict, set, collections 模块，heapq 模块
- 面试笔试常考算法

## 编程语言
我們這裡使用最近很火的Python。Python 入门簡單而且是個多面手，在爬虫、web 後端、运维、數據分析、AI、量化投资等领域都有 Python 的身影，
无论是否是专业程序员， Python 都是一门学习性價比非常高的语言。
知乎、豆瓣、头條、饿了么、搜狐等公司都有广泛使用 Python。笔者日常工作使用也是 Python，有一定實践經验，
在知乎上维护了一個专栏[《Python 学习之路》](https://zhuanlan.zhihu.com/c_85234576)。

Python 抽象程度比较高， 我們能用更少的代碼來實現功能，同时不用像 C/C++ 那样担心内存管理、指針操作等底层問題，
把主要心思放在算法逻辑本身而不是语言细節上，Python 也号称伪代碼语言。所有代碼示例使用 Python2/3 兼容代碼，
不過只在 python3.5 下測试過，推荐用相同版本 Python 进行代碼编写和測试。

## 受众
想要学习 Python 算法和數據結構的中级同学，包括自学的同学和本科低年级学生等。需要掌握 Python
的基本语法和面向對象编程的一些概念，有一定的 Python 使用經验。我們這裡尽量只使用最基本的 Python 语法，不會再去介绍用到的 Python 语法糖。
數據結構和算法算是本科教育中偏难的课程，既需要你理解其原理，又需要具有有扎實的编程能力。

**請注意: 本教程不是零基础教程，着重于使用 Python 實現常用算法和數據結構，不适合从來没有学過算法和數據結構的新手同学，购买之前請慎重考虑，請确保你之前看過一本數據結構和算法的教材，最好有過其他语言實現算法的經验**

# 预备知识
（注意：有些同学看起來很吃力，為了不花冤枉钱，我建議你先整體浏览本电子书的内容和代碼是否在自己的理解范围内，再决定是否购买影片。有些概念不是立马就能理解的，需要反复思考實践）

- 了解基本的數據結構和算法的概念，不适合**完全**没有了解過算法的新手，更不适合 Python 基础都没掌握的同学。购买之前請慎重考虑
- 无需太多数学基础，仅在算法時間複雜度分析的时候會用到一些簡單数学知识。對于学习基础算法，逻辑思维可能更重要一些

## 参考教材和鏈接
這裡我参考過三本书，均可以网购纸质版或者网络上搜索电子版，建議大家先大致閱讀一本教材掌握基本原理：

[《算法图解》](https://book.douban.com/subject/26979890/): 图解的形式很适合新手，示例使用的是 python。推荐基础较少的同学看這本书入门

[《Data Structures and Algorithms in Python》]( https://book.douban.com/subject/10607365/): 适合對 Python
和算法比较熟悉的同学，或者是有其他语言编程經验的同学。本书是英文版，缺點是书中错誤真的很多，代碼有些无法运行而且不够 Pythonic。该书 [勘誤](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=9003&itemId=0470618299&resourceId=35653)

[《算法导论》第三版]( https://book.douban.com/subject/20432061/): 喜欢数学证明和板砖书的同学可以参考，有很多高级主题。使用伪代碼

## 算法可视化

学习算法的過程中有时候會比较抽象，這裡给大家推荐一些可视化的网站，方便更直觀地理解：

https://github.com/algorithm-visualizer/algorithm-visualizer

https://www.cs.usfca.edu/~galles/visualization/Algorithms.html


## 講课形式

绘图演示+手写板+现场编碼

我将使用绘图软件+手写板进行类似于纸笔形式的講解，邊講邊開個终端分成兩個窗口，一個用 vim
编写代碼，另一個窗口用來运行代碼，所有代碼我将會现场编写(還是很有挑战的)。
每個影片我會尽量控制时长，講的内容尽量通俗易懂，摆脱学院派的授课方式。

你可以参考我在知乎發的专栏文章看下：

[那些年，我們一起跪過的算法题[影片]](https://zhuanlan.zhihu.com/p/35175401)

[抱歉，我是開發，你居然让我写單測[影片]](https://zhuanlan.zhihu.com/p/35352024)


## 课程特點

- 每個算法和數據結構都有講義、影片(包含講解、图示、手動模擬)、源代碼。其中只有影片内容為付费内容
- 講義循序渐进，結合自己的学习和使用經验講解。github 上實时更新
- 影片演示更加直觀易懂
- 演示代碼實現思路，所有代碼在影片里均现场编写
- 偏向工程应用和代碼實現。代碼直接可以用。每個文件都是自包含的，你可以直接运行和调试，這是目前大部分书籍做得不到位的地方
- 良好的工程實践：[编碼之前碎碎念(工程實践)](http://python-web-guide.readthedocs.io/zh/latest/codingstyle/codingstyle.html)。
這是很多看了几本书没有太多业界實践經验就敢講课的培训班老师教不了的。**知识廉價，經验无價**
- 每個實現都會有單測來验证，培养良好的编碼和測试习惯，傳授工程經验
- 結合 cpython 底层實現講解（比如list 内存分配策略等），避免一些使用上的坑。并且會用 python 來模擬内置 dict 等的實現
- 每篇講義後有思考题和延伸閱讀鏈接，帮助大家加深思考和理解。大部分题目答案都可以网络上搜索到

## 资料

- 影片。包含所有講解影片(网易公開课)
- 代碼示例。所有代碼我會放到 github 上。
- markdown 講義，包含影片内容的提要等内容
- 延伸閱讀。我會附上一些閱讀资料方便想深入学习的同学

## 如何获取每章代碼

注意每一章目录里都有 py 文件，在电子书里看不到。clone 下本代碼仓库找到對应目录里的 python 文件即是每章涉及到的代碼。
由于代碼實現千差万别，本书代碼實現具有一定的個人風格，不代表最佳實現，仅供参考。


## 如何学习
笔者講课录制影片的過程也是自己再整理和学习的過程，录制影片之前需要参考很多资料
希望對所講到的内容，你能够

- 理解所講的每個數據結構和算法的
    - 原理
    - Python 實現方式
    - 時間、空間複雜度
    - 使用场景，什么时候用
- 自己嘗試實現，如果抛開影片自己写起來有困难可以反复多看几次影片，一定要自己手動實現。很多面试可能會让手写。一次不行就看完原理後多實践几次，直到能自己独立完成。
- 每章講義後面都會有我设计的几個小問題，最好能够回答上來。同时還有代碼练习题，你可以挑战下自己的掌握程度。
- 最好按照顺序循序渐进，每章都會有铺垫和联系，後面的章節可能會使用到前面提到的數據結構
- 根據自己的基础結合我列举的教材和影片学习，第一次理解不了的可以反复多看几次，多编写代碼练习到熟练為止

## 课程目标
掌握基本的算法和數據結構原理，能独立使用 Python 语言實現，能在日常開發中灵活选用數據結構。
對于找工作的同学提升面试成功率。


## 開發和測试工具

推荐使用以下工具进行開發，如果使用编辑器最好装對 应 Python 插件，笔者影片演示中使用了 vim，讀者可以自己挑选自己喜欢的開發工具：

- Pycharm
- Sublime
- Atom
- Vscode
- Vim/Emacs

注意影片中使用到了 pytest 測试框架和 when-changed 文件變動監控工具(方便我們修改完代碼保存後自動执行測试)，你需要用 pip 安装

```py
pip install pytest
pip install when-changed
```

影片演示里我使用到了一個簡單的 test.sh 脚本文件，内容如下:

```sh
#!/usr/bin/env bash

# pip install when-changed, 監控文件變動并且文件修改之後自動执行 pytest 單測，方便我們邊修改邊跑測试
 when-changed -v -r -1 -s ./    "py.test -s $1"
```
将以上内容放到 test.sh 文件後加上可执行权限, `chmod +x test.sh`，之後就可以用

```
'./test.sh somefile.py'
```
每次我們改動了代碼，就會自動执行代碼里的單元測试了。pytest 會自動發现以 test
開头的函数并执行測试代碼。良好的工程需要我們用單測來保证，将來即使修改了内部實現逻辑也方便做回归验证。

或者你可以在的 ~/.bashrc  or  ~/.zshrc 里邊加上這個映射（别忘记加上之後source下）:

```sh
# 監控當前文件夹文件變動自動执行命令
alias watchtest='when-changed -v -r -1 -s ./ '
```

然後在你的代碼目录里头执行 `watchtest pytest -s somefile.py` 一样的效果


## 測试用例设计

笔者在刚学习编程的时候总是忘记处理一些特例(尤其是動态语言可以傳各種值)，為了养成良好的编程和測试习惯，在编写單元測试用例的时候，
我們注意考虑下如下測试用例(等價类划分)：

- 正常值功能測试
- 邊界值（比如最大最小，最左最右值）
- 异常值（比如 None，空值，非法值）

```
def binary_search(array, target):
    if not array:
        return -1
    beg, end = 0, len(array)
    while beg < end:
        mid = beg + (end - beg) // 2  # py3
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid
        else:
            beg = mid + 1
    return -1


def test():
    """
    如何设计測试用例：
    - 正常值功能測试
    - 邊界值（比如最大最小，最左最右值）
    - 异常值（比如 None，空值，非法值）
    """
    # 正常值，包含有和无兩種結果
    assert binary_search([0, 1, 2, 3, 4, 5], 1) == 1
    assert binary_search([0, 1, 2, 3, 4, 5], 6) == -1
    assert binary_search([0, 1, 2, 3, 4, 5], -1) == -1
    # 邊界值
    assert binary_search([0, 1, 2, 3, 4, 5], 0) == 0
    assert binary_search([0, 1, 2, 3, 4, 5], 5) == 5
    assert binary_search([0], 0) == 0

    # 异常值
    assert binary_search([], 1) == -1
```

當然我們也不用做的非常细致，要不然写測试是一件非常繁琐累人的事情，甚至有时候為了測试而測试，只是為了让單測覆盖率好看點。
當然如果是web应用用户输入，我們要假设所有的参数都是不可信的。 但是很多内部调用的函数我們基于约定來编程，如果你瞎傳参数，那就是调用者的责任了。


## 勘誤

输出其實也是一種再学习的過程，中途需要查看大量资料、编写講義、影片录制、代碼编写等，难免有疏漏甚至错誤之处。
有出版社找過笔者想让我出书，一來自己對出书興趣不大，另外感覺书籍相對影片不够直觀，有错誤也不能及时修改，打算直接把所有文字内容講義和代碼等放到 github 上，供大家免费查阅。

如果你發现文字内容、代碼内容、影片内容有错誤或者有疑问，欢迎在 github 上提 issue 讨论(或者网易公開课评论區)，或者直接提 Merge Request，我會尽量及时修正相關内容，防止對讀者产生誤导。
同时非常感谢认真学习并及时發现书中错誤的同学，非常欢迎針對知识本身的交流和讨论，任何建議和修正我都會认真求证。
對于提出修正意見或者提交代碼的同学，由于人数比较多這裡就不一一列举了，可以在以下列表查看，再次感谢你们。笔者信奉開源精神，『眼睛足够多，bug 无处藏』。
如果您發现影片中的代碼有誤，請及时使用 git pull 拉取本项目的代碼更新，最好用目前最新的代碼來学习和實践。

[issue](https://github.com/PegasusWang/python_data_structures_and_algorithms/issues?q=is%3Aissue+is%3Aclosed)

[contributors](https://github.com/PegasusWang/python_data_structures_and_algorithms/graphs/contributors)

## 如何更新代碼(写给不熟悉 git 的同学)
如果你直接 clone 的本项目的代碼仓库，可以直接使用 `git pull origin master` 拉取更新。
如果你先 fork 到了自己的仓库，然後 clone 到本地的是你自己的仓库，你可以编辑本地项目的 `.git/config`，
增加如下配置：

```sh
[remote "pegasuswang"]
	url = https://github.com/PegasusWang/python_data_structures_and_algorithms.git
	fetch = +refs/heads/*:refs/remotes/origin/*
```

然後使用 `git pull pegasuswang master` 拉取更新。

## 如何提问？
如果讀者關于代碼、影片、講義有任何疑问，欢迎一起讨论
請注意以下几點：

- 優先在网易云课堂的讨论區提问，方便别的同学浏览。如果未购买影片，也可以直接在 github 里提出 issue，笔者有空會给大家解答和讨论。
- 描述尽量具體，影片或者代碼哪一部分有問題？請尽量把涉及章節和代碼贴出來，方便定位問題。
- 如果涉及到代碼，提问时請保持代碼的格式


## 本电子书制作和写作方式
使用 mkdocs 和 markdown 构建，使用  Python-Markdown-Math 完成数学公式。
markdown 语法参考：http://xianbai.me/learn-md/article/about/readme.html

安装依赖：
```sh
pip install mkdocs    # 制作电子书, http://markdown-docs-zh.readthedocs.io/zh_CN/latest/
# https://stackoverflow.com/questions/27882261/mkdocs-and-mathjax/31874157
pip install https://github.com/mitya57/python-markdown-math/archive/master.zip

# 或者直接
pip install -r requirements.txt

# 如果你 fork 了本项目，可以定期拉取主仓库的代碼來获取更新，目前還在不断更新相關章節
```

你可以 clone 本项目後在本地编写和查看电子书：
```sh
mkdocs serve     # 修改自動更新，浏览器打開 http://localhost:8000 訪問
# 数学公式参考 https://www.zybuluo.com/codeep/note/163962
mkdocs gh-deploy    # 部署到自己的 github pages
```

扫碼加入课程：

![扫碼加入课程返现30%](https://camo.githubusercontent.com/a217604a83d60fdc610ba91e5c771664a4645a79/687474703a2f2f376b747574792e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f53637265656e25323053686f74253230323031382d30362d3032253230617425323032302e33372e34362e706e67)
