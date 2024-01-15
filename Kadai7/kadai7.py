# * * * * * * * * * * * * * * * * * * * * * * * * * * * *kadai7.py * * * * * 
#       作成者：XAICHA JAIXIONG 学籍番号：B213379
#       日付：2021/11/22
#   今回の課題は、pythonで簡単データセットから検索プログラムを作成した。データセットを検索する
# のは、乱数で生成した５つのIDを用いて、検索対象データセット(合計2000データ)を検索する。
# そして、文書ベクトル間のコサイン類似度も計算する。
# -  データセットを検索のは、プログラムの122行目からにある。
# -  コサイン類似度も計算するの関数は, similarity()である
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
import os
from datetime import datetime
import random
import sys
import numpy as np

def similarity(x_list, y_list):
    dot = 0.0 # xとyの内積
    x2 = 0.0 # xの長さの二乗
    y2 = 0.0 # yの長さの二乗

    for i in range(len(x_list)): # コサイン類似度計算
        dot += x_list[i]*y_list[i] #　各成分の内積を計算する 
        x2 += x_list[i]*x_list[i] # xの長さの二乗を計算する
        y2 += y_list[i]*y_list[i] # yの長さの二乗を計算する

    try:# 例外処理
        return dot/np.sqrt(x2*y2)
    except ZeroDivisionErro: # ゼロ割り算が発生した時の処理
        print("ゼロ割り算エラー")
        return 0.0

def SortedIndex(items): # ンデックスのソートする関数
    list_sorted = items.copy() # itemsのリストをlist_sortedリストにcopyする
    list_sorted.sort() # list_sortedをソートする

    list_index = [] # ンデックスを入れるの空リスト用意している
    for i in list_sorted: # maximum値のンデックス順にlist_indexに追加して行くのループ
        list_index.insert(0, items.index(i)) # list_indexにンデックスを追加する

    return list_index # ンデックスのリストを返す

# 上位 10 文書にクエリ文書のクラスと同じクラスが含まれている割合を計算する関数
def SameClassDividePercent(list_index, id2000_lines): 
    list_count = [] # conut1~10までの値を入れるの空リストを用意するため
    count1 = 0 # count1~10までは同じクラスかどうか10個の中で一個つつ調べていく
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    for i in range(10): # 上位 10 の中に同じクラスがあるかを調べるのループ
        if id2000_lines[list_index[0]] == id2000_lines[list_index[i]]: # 位 1には位 2~10の中に同じクラスかを調べる
            count1 += 1 # 同じクラスがある場合は、countに1を増える
        elif id2000_lines[list_index[1]] == id2000_lines[list_index[i]]: # 位 2には位 1,3~10の中に同じクラスかを調べる
            count2 += 1 # 同じクラスがある場合は、countに1を増える
        elif id2000_lines[list_index[2]] == id2000_lines[list_index[i]]:# 位 3には位 1~2,4~10の中に同じクラスかを調べる
            count3 += 1 # 同じクラスがある場合は、countに1を増える
        elif id2000_lines[list_index[3]] == id2000_lines[list_index[i]]:
            count4 += 1
        elif id2000_lines[list_index[4]] == id2000_lines[list_index[i]]:
            count5 += 1
        elif id2000_lines[list_index[5]] == id2000_lines[list_index[i]]:
            count6 += 1
        elif id2000_lines[list_index[6]] == id2000_lines[list_index[i]]:
            count7 += 1
        elif id2000_lines[list_index[7]] == id2000_lines[list_index[i]]:
            count8 += 1
        elif id2000_lines[list_index[8]] == id2000_lines[list_index[i]]:
            count9 += 1
        elif id2000_lines[list_index[9]] == id2000_lines[list_index[i]]:
            count10 += 1

    list_count.extend([count1, count2, count3, count4, count5, count6, count7, count8, count9, count10]) # countの最終の結果をlist_countに入れる
    list_count = sorted(list_count, reverse=True) # list_countをmaximum順にソートする

    percent_divide = float((list_count[0]/len(list_count))*100) # 同じクラスが含ま れている割合(パーセント)計算する

    return percent_divide # パーセントを返す
    
if __name__ == '__main__':
    date = datetime.now() # 現在の日付と日時
    min_value = 0 # 乱数の最小値
    max_value = 399 # 乱数の最大値
    input_fname = sys.argv[0]
    # class_id = [145, 252, 371, 150, 89]
    class_id = [] #５つの検索IDを入れるの空リストを用意する
    items = [] #文書ベクトル間のコサイン類似度を計算した結果入れる空リスト

    try:
        # 作者や日付の表示する部分
        print()
        print("$python3 %s " %input_fname)
        print("*********************************************")
        print("XAICHA JAIXIONG, B213379")
        print("日付: ", date)
        print("内容：文書ベクトルの類似度を用いた文書検索")
        print("*********************************************")

        with open('QueryClassId.txt', "r", newline='', encoding='utf-8') as fin: # QueryClassId.txtの中身を読む
            id_lines = fin.read().splitlines()# テキストをすべて読み込む。結果はリスト
            
        with open('QuerySubject.txt', "r", newline='', encoding='utf-8') as fin: # QuerySubject.txtの中身を読む 
            subject_lines = fin.read().splitlines()# テキストをすべて読み込む。結果はリスト
           
        with open('ClassId.txt', "r", newline='', encoding='utf-8') as fin: # ClassId.txtの中身を読む
            id2000_lines = fin.read().splitlines()# テキストをすべて読み込む。結果はリスト
            
        with open('Subject.txt', "r", newline='', encoding='utf-8') as fin: # Subject.txtの中身を読む
            subject2000_lines = fin.read().splitlines()# テキストをすべて読み込む。結果はリスト, splitlines()は改行記号を削除するため
          
        random.seed(date) # 現在時刻を初期値とする乱数
        for i in range(5):# 乱数で5種類発生するループ
            ID = int(min_value+(max_value-min_value)*random.random()) # 乱数で5種類発生する
            class_id.append(ID) # 生成した乱数をclass_idのリストに入れて置く
        
        im1 = np.load('20news400query.npy') # load the 20news400query.npyファイル
        im2 = np.load('20news2000.npy') # load the 20news2000.npyファイル
        for i in range(len(class_id)): #生成した５つのIDを用いて検索するループ
            # ５つのIDを用いてクエリの Subject（id_lines), クエリのクラス(subject_lines)のファイルに検索する
            print("Query ID = %d class = [%s]%s" %(class_id[i], id_lines[class_id[i]], subject_lines[class_id[i]]))
            print("-"*50)
            for j in range(len(im2)): # 類似する上位 10 個のコサイン類似度を計算するループ
                items.append(similarity(im1[class_id[i]], im2[j])) # 類似度を計算する関数を呼び出して、結果はitemsのリストに入れる

            list_index = SortedIndex(items) # 類似度を計算した結果(itemsリスト)インデックスをソートする
            for k in range(10): # 上位 10 個の文書のタイトル, 個々の文書が属するクラス ID をプリントするループ
                print("Rank %d (%d) %3.3f %s class = [%d]" %(k+1, list_index[k], items[list_index[k]], subject2000_lines[list_index[k]], int(id2000_lines[list_index[k]])))

            percent_divide = SameClassDividePercent(list_index, id2000_lines) # 同じクラスが含ま れている割合する関数を呼ぶ出す
            print("同じクラスがランク10位までに見つかった割合 = ",percent_divide,"%")
            items.clear() # 一個IDを検索が終わったら、itemsの中身のデータを削除する
            list_index.clear() # 一個IDを検索が終わったら、list_idexの中身のデータを削除する
            print("*"*50)
            print()
            
    except FileNotFoundError: # ファイルが見つからない場合の処理
        print("一つのファイルが見つかりません")
        sys.exit()#プログラム終了