# Python 算法與數據結構影片教程

## 課程簡介
數據結構和算法是每個程序員需要掌握的基礎知識之一，也是面試中跨不過的檻。目前關於 Python 算法和數據結構的系统中文資料比較欠缺，
筆者嘗試錄制影片教程帮助 Python 開發者掌握常用算法和數據結構，提升開發技能。
本教程是付費教程(文字内容和原始碼免費)，因為筆者錄制的過程中除了購買軟體、手寫板等硬體之外，業餘需要花費很多時間和精力來錄制影片、查資料、編寫課件和原始碼，養家糊口不容易，希望大家體谅。

## 鏈接
影片教程已經發布在網易云課堂和 csdn 學院，内容一致，推薦使用網易云課堂。

[網易云課堂: Python數據結構與算法教程](http://study.163.com/course/introduction.htm?courseId=1005526003) 影片教程

[csdn 學院：Python數據結構與算法教程](https://edu.csdn.net/course/detail/8332)

[網上閱讀《Python 算法與數據結構教程 》](http://ningning.today/python_data_structures_and_algorithms/)

[github 鏈接](https://github.com/PegasusWang/python_data_structures_and_algorithms)

[readthedoc 電子書下载](http://python-data-structures-and-algorithms.readthedocs.io/zh/latest/)

[《開源一個 Python 算法和數據結構中文教程[影片]》](https://zhuanlan.zhihu.com/p/36038003)  影片講解示例

## 痛點
- 講 Python 數據結構和算法的資料很少，中文資料更少
- 很多自學 Python 的工程師對基礎不够重視，面試也發現很多數據結構和算法不過關，很多人掛在了基礎的數據結構和算法上
- 缺少工程應用場景下的講解，很多講算法的資料太『教科書化』。本書實現的原始碼工程上可用
- 網上很多影片教程不够循序漸進，不成系统

## 作者簡介
曾就職於[知乎](https://www.zhihu.com/people/pegasus-wang/activities)，任後端工程師，多年 Python 開發經驗。

知乎專欄：

- [《Python 學習之路》](https://zhuanlan.zhihu.com/c_85234576)
- [《玩轉vim(影片)》](https://zhuanlan.zhihu.com/vim-video)

電子書：[《Python web 入坑指南》](http://python-web-guide.readthedocs.io/zh/latest/)

## 課程内容
包括我們在業務開發和面試中常用的算法和數據結構，希望可以帮助 Python 開發者快速上手，很多老手寫業務原始碼寫多了很多基礎知識忘記了，
也可以作為回顧。課程儘量用通俗的方式講解，結合 python 語言和日常開發實践的經驗。書中原始碼可以作為大家的面試筆試参考。
對於每個算法和用到的數據結構我們需要知道:

- 原理
- Python 實現方式
- 時間、空間複雜度
- 使用場景，什麼時候用

## 目錄結構
這裡講解的章節我参考了下邊教材中列舉的一些書籍，並且自己設計了大綱，争取做到循序漸進，簡單實用。因為實現一些高级數據結構的時候會用到
很多底層數據結構，防止跳跃太大導致讀者理解困難。

課程的目錄結構如下，每一章都有配套的文字講義(markdown)，示例原始碼，影片講解，詳細的講解一般會放在影片裡，使用手寫板來
進行板書，包括文字、圖示、手動模擬算法過程等。

- 課程介绍
- 課程簡介之笨方法學算法
- 抽象數據類型 ADT，面向對象編程
- 數组和列表
- 鏈表，高级鏈表。双鏈表，循環双端鏈表
- 陣列，双端陣列，循環双端陣列
- 堆疊，堆疊溢出
- 算法分析，時間複雜度 大O 表示法
- 哈希表，散列衝突
- 字典
- 集合
- 遞迴
- 查找：線性查找和二分查找
- 基本排序算法: 冒泡、選择、插入排序
- 高级排序算法: 归並排序、快排
- 樹，二元樹
- 堆與堆排序
- 優先级陣列
- 二元查找樹
- 圖與圖的尋訪
- python 内置常用數據結構和算法的使用。list, dict, set, collections 模块，heapq 模块
- 面試筆試常考算法

## 編程語言
我們這裡使用最近很火的Python。Python 入門簡單而且是個多面手，在爬蟲、web 後端、運维、數據分析、AI、量化投資等領域都有 Python 的身影，
無論是否是專業程序員， Python 都是一門學習性價比非常高的語言。
知乎、豆瓣、頭條、餓了麼、搜狐等公司都有廣泛使用 Python。筆者日常工作使用也是 Python，有一定實践經驗，
在知乎上維護了一個專欄[《Python 學習之路》](https://zhuanlan.zhihu.com/c_85234576)。

Python 抽象程度比較高， 我們能用更少的原始碼來實現功能，同時不用像 C/C++ 那樣担心記憶體管理、指針操作等底層問題，
把主要心思放在算法邏輯本身而不是語言細節上，Python 也号称偽原始碼語言。所有原始碼示例使用 Python2/3 兼容原始碼，
不過只在 python3.5 下測試過，推薦用相同版本 Python 進行原始碼編寫和測試。

## 對象
想要學習 Python 算法和數據結構的中级同學，包括自學的同學和本科低年级學生等。需要掌握 Python
的基本語法和面向對象編程的一些概念，有一定的 Python 使用經驗。我們這裡儘量只使用最基本的 Python 語法，不會再去介绍用到的 Python 語法糖。
數據結構和算法算是本科教育中偏難的課程，既需要你理解其原理，又需要具有有扎實的編程能力。

**請注意: 本教程不是零基礎教程，著重於使用 Python 實現常用算法和數據結構，不適合從來没有學過算法和數據結構的新手同學，購買之前請慎重考慮，請確保你之前看過一本數據結構和算法的教材，最好有過其他語言實現算法的經驗**

# 預備知識
（注意：有些同學看起來很吃力，為了不花冤枉钱，我建議你先整體瀏覽本電子書的内容和原始碼是否在自己的理解範圍内，再決定是否購買影片。有些概念不是立刻就能理解的，需要反复思考實践）

- 了解基本的數據結構和算法的概念，不適合**完全**没有了解過算法的新手，更不適合 Python 基礎都没掌握的同學。購買之前請慎重考慮
- 無需太多數學基礎，仅在算法時間複雜度分析的時候會用到一些簡單數學知識。對於學習基礎算法，邏輯思维可能更重要一些

## 参考教材和鏈接
這裡我参考過三本書，均可以網購紙本版或者網路上搜索電子版，建議大家先大致閱讀一本教材掌握基本原理：

[《算法圖解》](https://book.douban.com/subject/26979890/): 圖解的形式很適合新手，示例使用的是 python。推薦基礎較少的同學看這本書入門

[《Data Structures and Algorithms in Python》]( https://book.douban.com/subject/10607365/): 適合對 Python
和算法比較熟悉的同學，或者是有其他語言編程經驗的同學。本書是英文版，缺點是書中錯誤真的很多，原始碼有些無法運行而且不够 Pythonic。該書 [勘誤](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=9003&itemId=0470618299&resourceId=35653)

[《算法導論》第三版]( https://book.douban.com/subject/20432061/): 喜欢數學證明和板砖書的同學可以参考，有很多高级主題。使用偽原始碼

## 算法可視化

學習算法的過程中有時候會比較抽象，這裡给大家推薦一些可視化的網站，方便更直觀地理解：

https://github.com/algorithm-visualizer/algorithm-visualizer

https://www.cs.usfca.edu/~galles/visualization/Algorithms.html


## 講課形式

繪圖演示+手寫板+現場編碼

我將使用繪圖軟體+手寫板進行類似於纸筆形式的講解，邊講邊開個终端分成兩個窗口，一個用 vim
編寫原始碼，另一個窗口用來運行原始碼，所有原始碼我將會現場編寫(還是很有挑戰的)。
每個影片我會儘量控制時間，講的内容儘量通俗易懂，擺脱學院派的授課方式。

你可以参考我在知乎發的專欄文章看下：

[那些年，我們一起跪過的算法題[影片]](https://zhuanlan.zhihu.com/p/35175401)

[抱歉，我是開發，你居然讓我寫單測[影片]](https://zhuanlan.zhihu.com/p/35352024)


## 課程特點

- 每個算法和數據結構都有講義、影片(包含講解、圖示、手動模擬)、源原始碼。其中只有影片内容為付費内容
- 講義循序漸進，結合自己的學習和使用經驗講解。github 上實時更新
- 影片演示更加直觀易懂
- 演示原始碼實現思路，所有原始碼在影片裡均現場編寫
- 偏向工程應用和原始碼實現。原始碼直接可以用。每個文件都是自包含的，你可以直接運行和調試，這是目前大部分書籍做得不到位的地方
- 良好的工程實践：[編碼之前碎碎念(工程實践)](http://python-web-guide.readthedocs.io/zh/latest/codingstyle/codingstyle.html)。
這是很多看了幾本書没有太多业界實践經驗就敢講課的培训班老師教不了的。**知識廉價，經驗無價**
- 每個實現都會有單測來驗證，培養良好的編碼和測試习惯，傳授工程經驗
- 結合 cpython 底層實現講解（比如list 記憶體分配策略等），避免一些使用上的坑。並且會用 python 來模擬内置 dict 等的實現
- 每篇講義後有思考題和延伸閱讀鏈接，帮助大家加深思考和理解。大部分題目答案都可以網路上搜索到

## 資料

- 影片。包含所有講解影片(網易公開課)
- 原始碼示例。所有原始碼我會放到 github 上。
- markdown 講義，包含影片内容的提要等内容
- 延伸閱讀。我會附上一些閱讀資料方便想深入學習的同學

## 如何获取每章原始碼

注意每一章目錄裡都有 py 文件，在電子書裡看不到。clone 下本原始碼仓库找到對應目錄裡的 python 文件即是每章涉及到的原始碼。
由於原始碼實現千差万别，本書原始碼實現具有一定的個人風格，不代表最佳實現，仅供参考。


## 如何學習
筆者講課錄制影片的過程也是自己再整理和學習的過程，錄制影片之前需要参考很多資料
希望對所講到的内容，你能够

- 理解所講的每個數據結構和算法的
    - 原理
    - Python 實現方式
    - 時間、空間複雜度
    - 使用場景，什麼時候用
- 自己嘗試實現，如果抛開影片自己寫起來有困難可以反复多看幾次影片，一定要自己手動實現。很多面試可能會讓手寫。一次不行就看完原理後多實践幾次，直到能自己独立完成。
- 每章講義後面都會有我設計的幾個小問題，最好能够回答上來。同時還有原始碼練習題，你可以挑戰下自己的掌握程度。
- 最好按照顺序循序漸進，每章都會有铺垫和联系，後面的章節可能會使用到前面提到的數據結構
- 根據自己的基礎結合我列舉的教材和影片學習，第一次理解不了的可以反复多看幾次，多編寫原始碼練習到熟练為止

## 課程目標
掌握基本的算法和數據結構原理，能独立使用 Python 語言實現，能在日常開發中灵活選用數據結構。
對於找工作的同學提升面試成功率。


## 開發和測試工具

推薦使用以下工具進行開發，如果使用編辑器最好装對 應 Python 插件，筆者影片演示中使用了 vim，讀者可以自己挑選自己喜欢的開發工具：

- Pycharm
- Sublime
- Atom
- Vscode
- Vim/Emacs

注意影片中使用到了 pytest 測試框架和 when-changed 文件變動監控工具(方便我們修改完原始碼保存後自動執行測試)，你需要用 pip 安装

```py
pip install pytest
pip install when-changed
```

影片演示裡我使用到了一個簡單的 test.sh 脚本文件，内容如下:

```sh
#!/usr/bin/env bash

# pip install when-changed, 監控文件變動並且文件修改之後自動執行 pytest 單測，方便我們邊修改邊跑測試
 when-changed -v -r -1 -s ./    "py.test -s $1"
```
將以上内容放到 test.sh 文件後加上可執行權限, `chmod +x test.sh`，之後就可以用

```
'./test.sh somefile.py'
```
每次我們改動了原始碼，就會自動執行原始碼裡的單元測試了。pytest 會自動發現以 test
開頭的函數並執行測試原始碼。良好的工程需要我們用單測來保證，將來即使修改了内部實現邏輯也方便做回归驗證。

或者你可以在的 ~/.bashrc  or  ~/.zshrc 裡邊加上這個映射（别忘記加上之後source下）:

```sh
# 監控當前文件夹文件變動自動執行命令
alias watchtest='when-changed -v -r -1 -s ./ '
```

然後在你的原始碼目錄裡頭執行 `watchtest pytest -s somefile.py` 一樣的效果


## 測試用例設計

筆者在刚學習編程的時候总是忘記處理一些特例(尤其是動态語言可以傳各種值)，為了養成良好的編程和測試习惯，在編寫單元測試用例的時候，
我們注意考慮下如下測試用例(等價類划分)：

- 正常值功能測試
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
    如何設計測試用例：
    - 正常值功能測試
    - 邊界值（比如最大最小，最左最右值）
    - 异常值（比如 None，空值，非法值）
    """
    # 正常值，包含有和無兩種結果
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

當然我們也不用做的非常細致，要不然寫測試是一件非常繁琐累人的事情，甚至有時候為了測試而測試，只是為了讓單測覆盖率好看點。
當然如果是web應用用户輸入，我們要假設所有的参數都是不可信的。 但是很多内部調用的函數我們基於约定來編程，如果你瞎傳参數，那就是調用者的責任了。


## 勘誤

輸出其實也是一種再學習的過程，中途需要查看大量資料、編寫講義、影片錄制、原始碼編寫等，難免有疏漏甚至錯誤之處。
有出版社找過筆者想讓我出書，一來自己對出書興趣不大，另外感覺書籍相對影片不够直觀，有錯誤也不能及時修改，打算直接把所有文字内容講義和原始碼等放到 github 上，供大家免費查阅。

如果你發現文字内容、原始碼内容、影片内容有錯誤或者有疑問，欢迎在 github 上提 issue 討論(或者網易公開課评論區)，或者直接提 Merge Request，我會儘量及時修正相關内容，防止對讀者产生誤導。
同時非常感谢认真學習並及時發現書中錯誤的同學，非常欢迎針對知識本身的交流和討論，任何建議和修正我都會认真求證。
對於提出修正意見或者提交原始碼的同學，由於人數比較多這裡就不一一列舉了，可以在以下列表查看，再次感谢你们。筆者信奉開源精神，『眼睛足够多，bug 無處藏』。
如果您發現影片中的原始碼有誤，請及時使用 git pull 拉取本项目的原始碼更新，最好用目前最新的原始碼來學習和實践。

[issue](https://github.com/PegasusWang/python_data_structures_and_algorithms/issues?q=is%3Aissue+is%3Aclosed)

[contributors](https://github.com/PegasusWang/python_data_structures_and_algorithms/graphs/contributors)

## 如何更新原始碼(寫给不熟悉 git 的同學)
如果你直接 clone 的本项目的原始碼仓库，可以直接使用 `git pull origin master` 拉取更新。
如果你先 fork 到了自己的仓库，然後 clone 到本地的是你自己的仓库，你可以編辑本地项目的 `.git/config`，
增加如下配置：

```sh
[remote "pegasuswang"]
	url = https://github.com/PegasusWang/python_data_structures_and_algorithms.git
	fetch = +refs/heads/*:refs/remotes/origin/*
```

然後使用 `git pull pegasuswang master` 拉取更新。

## 如何提問？
如果讀者關於原始碼、影片、講義有任何疑問，欢迎一起討論
請注意以下幾點：

- 優先在網易云課堂的討論區提問，方便别的同學瀏覽。如果未購買影片，也可以直接在 github 裡提出 issue，筆者有空會给大家解答和討論。
- 描述儘量具體，影片或者原始碼哪一部分有問題？請儘量把涉及章節和原始碼贴出來，方便定位問題。
- 如果涉及到原始碼，提問時請保持原始碼的格式


## 本電子書制作和寫作方式
使用 mkdocs 和 markdown 构建，使用  Python-Markdown-Math 完成數學公式。
markdown 語法参考：http://xianbai.me/learn-md/article/about/readme.html

安装依赖：
```sh
pip install mkdocs    # 制作電子書, http://markdown-docs-zh.readthedocs.io/zh_CN/latest/
# https://stackoverflow.com/questions/27882261/mkdocs-and-mathjax/31874157
pip install https://github.com/mitya57/python-markdown-math/archive/master.zip

# 或者直接
pip install -r requirements.txt

# 如果你 fork 了本项目，可以定期拉取主仓库的原始碼來获取更新，目前還在不断更新相關章節
```

你可以 clone 本项目後在本地編寫和查看電子書：
```sh
mkdocs serve     # 修改自動更新，瀏覽器打開 http://localhost:8000 訪問
# 數學公式参考 https://www.zybuluo.com/codeep/note/163962
mkdocs gh-deploy    # 部署到自己的 github pages
```

扫碼加入課程：

![扫碼加入課程返現30%](https://camo.githubusercontent.com/a217604a83d60fdc610ba91e5c771664a4645a79/687474703a2f2f376b747574792e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f53637265656e25323053686f74253230323031382d30362d3032253230617425323032302e33372e34362e706e67)
