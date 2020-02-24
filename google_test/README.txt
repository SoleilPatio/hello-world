
一開始目錄是空的
git submodule init   ==> 目錄是空的,需要git init初始化
git submodule update ==> fetch 資料,並根據上層專案checkout 合適的commit

重新再init一次
git submodule update --init -f googletest/