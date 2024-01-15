# * * * * * * * * * * * * * * * * * * * * Kadai1.py * * * * * * * * * * * * *
#      作成者：XAICHA JAIXIONG, 学績番号：B213379
#      作成日付:2021/10/10(日) 10:00
#   このプログラムは，ニュースのテキストファイルを用いて，ファイルの中にあるカタカナ単語
#        を抽出する。カタカナ単語の出現数と総単語数をカウントするプログラムである。
# 
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#!/usr/bin/env python3

import sys
import re
import datetime

def main():
    dic = {}
    fname = sys.argv[1] # 第一引数でファイル名を与える
    with open(fname) as f:
        line = f.read()# テキストをすべて読み込む。結果はリスト
        new_string = line.strip()#前後のスペースを取り消す
        new_string = re.sub('[a-zA-Zａ-ｚＡ-Ｚ]+', ' ',new_string) # 半角アルファベットと全角は捨てる 
        new_string = re.sub('[0‐9]+', ' ', new_string) # 半角数字もすてる
        new_string = re.sub('[０-９]+', ' ', new_string) # 全角数字もすてる
        new_string = re.sub('\.', ' ', new_string) # ピリオドはすてる
        new_string = re.sub('[\nu3041-\u309F]+', ' ', new_string)#ひらがなはすてる
        #漢字は捨てる
        new_string = re.sub('[\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+', ' ', new_string)
        new_string = re.sub('[\u3000-\u303F]+', ' ', new_string) #日本語の記号は捨てる
        #ASCII記号の全角版および日本語の記号の半角版と合わせる
        new_string = re.sub('[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65\u3000-\u303F]+', ' ', new_string) 
        new_string = re.sub('[\uFF0C]', ' ', new_string)
        new_string = re.sub('[\u2160-\u217F]+', ' ', new_string)#ローマ数字は捨てる
        new_string = re.sub(',', ' ', new_string)#コンマを捨てる
        new_string = re.sub('・', ' ', new_string)#中央のドットは捨てる
        new_string = re.sub('-', ' ', new_string)#中央のドットは捨てる
        # new_string = new_string.strip()
        # print(new_string)
        words = new_string.split() # line.split()
        # print(words)
        for word in words:#単語を一個づつを調べていく
            if word in dic:
                dic[word] = dic[word] + 1 #同じ単語場合は、単語カウントして行く
            else:
                dic[word] = 1 #最初の単語は、カウント1して置く
    
    date = datetime.datetime.now() #現在の日付と日時
    print("*********************************************")
    print("XAICHA JAIXIONG, B213379")
    print("日付: ", date)
    print("課題 1:日本語ニュースからカタカナ文字列の抽出")
    print("入力ニュースファイル:", fname)
    print("*********************************************")

    words_count = 0 #単語のカウント変数を準備して置く 
    for keys, values in dic.items():#辞書の単語を呼び出すのループである
        words_count += 1 #総単語数をカウントする
        print(keys, "\t", values, sep="")#単語と出現数をプリントする
    print()
    print("総単語数 = ", words_count)#総単語数をプリントする
    print("---------------------------------------------")

if __name__ == "__main__":

    main()
