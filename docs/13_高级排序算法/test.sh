

#!/usr/bin/env bash

# pip install when-changed, 監控文件變動並且文件修改之後自動执行 pytest 單測，方便我們邊修改邊跑測試
 when-changed -v -r -1 -s ./    "py.test -s $1"

