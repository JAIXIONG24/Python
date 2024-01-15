# * * * * * * * * * * * * * * * * * * * * * * * * * * * *kadai3.py * * * * * 
#       作成者：XAICHA JAIXIONG 学籍番号：B213379
#       日付：2021/10/25
#
#
#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

import sys
import os
import datetime

if __name__ == '__main__':
    num_agrs = len(sys.argv)
    if(num_agrs != 2):
        print("npyファイルを最後に追加してください")
        sys.exit()# プログラム終了
    fname = sys.argv[1]# 第一引数でファイル名を与える
    try:
        date = datetime.datetime.now() # 現在の日付と日時
        print("*********************************************")
        print("課題3:", fname,"から単回帰クラスを作成しカロリーを予測")
        print("XAICHA JAIXIONG, B213379")
        print("日付: ", date)
        print("未知データは、「さくらんぼ」「バジル」「豆乳」")
        # print("入力npyファイル:", fname)
        print("*********************************************")
            
    except FileNotFoundError:
        print("ファイル:",fname,"が見つかりません")
        sys.exit()#プログラム終了