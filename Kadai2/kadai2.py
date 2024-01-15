# * * * * * * * * * * * * * * * * * * * * * * * * * * * *kadai2.py * * * * * 
#       作成者：XAICHA JAIXIONG 学籍番号：B213379
#       日付：2021/10/18
#このプログラムは、npyのファイルを用いて画像の全体平均色と地域平均色を求めるプログラムである。
#平均色を求める関数は、average_RGB()関数である。もっとも似ていたともっとも似ていなかった
#領域のインデックスをタップルで返す関数は、FindMinMax()関数となる。ユークリッド距離を求め
#る関数は、Euclid()という関数である。
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
import sys
import os
import numpy as np
import numpy
import datetime

def average_RGB(im, x0, y0, w, h): # 画像の(R,G,B)値の平均値を計算する関数
    R = G = B = count = 0
    for i in range(y0, h):
            for j in range(x0, w):
                rgb = im[i][j]
                R += rgb[0] # R色の全体を足し算する
                G += rgb[1] # G色の全体を足し算する
                B += rgb[2] # B色の全体を足し算する
                count += 1  # 全体の個数は何個あるかをカウントアープする
    
    NumPy = np.array((R/count, G/count, B/count))# RGBの平均を計算

    return NumPy # 3 次元の(R,G,B)値の NumPy 配列を返す

def FindMinMax(All_Array): # もっとも似ていたともっとも似ていなかった領域のインデックスをタップルで返す関数
    LT = Euclid(All_Array[0], All_Array[1]) #  all_avgとLTの3 次元空間でのユークリッド距離
    RT = Euclid(All_Array[0], All_Array[2]) #  all_avgとRTの3 次元空間でのユークリッド距離
    LB = Euclid(All_Array[0], All_Array[3]) #  all_avgとLBの3 次元空間でのユークリッド距離
    RB = Euclid(All_Array[0], All_Array[4]) #  all_avgとRBの3 次元空間でのユークリッド距離
    CT = Euclid(All_Array[0], All_Array[5]) #  all_avgとCTの3 次元空間でのユークリッド距離
    
    distance = [LT, RT, LB, RB, CT] # 求めたユークリッド距離を配列作ってインデックスを求める
    # print(distance)
    min_index = distance.index(min(distance)) # ユークリッド距離が最も小さいはもっとも似ていた地域となる
    max_index = distance.index(max(distance)) #　ユークリッド距離が最も大きいはもっとも似ていなかった領域となる
    index = np.array([min_index + 1, max_index + 1])# 前のインデックスと同じように1を足す

    return index # もっとも似ていたともっとも似ていなかった領域のインデックスを返す


def Euclid(A_Point, B_Point): # ユークリッド距離を求める関数
    return np.linalg.norm(A_Point - B_Point) #　ユークリッド距離を返す

 
if __name__ == '__main__':
    num_agrs = len(sys.argv)
    if(num_agrs != 2):
        print("npyファイルを最後に追加してください")
        sys.exit()# プログラム終了
    fname = sys.argv[1]# 第一引数でファイル名を与える
    try:
        im = np.load(fname) #
        h = int(len(im)/4) # 画像の高さ(height)を求める
        w = int(len(im[0])/4) # 画像の長さ(weight)を求める

        avg_all = average_RGB(im, 0, 0, 4*w, 4*h) # 全体の平均色を求める
        avg_LT1 = average_RGB(im, 0, 0, 2*w, h) # Left Top areaの上部分の平均色を求める
        avg_LT2 = average_RGB(im, 0, h, w, 2*h) # Left Top areaの下部分の平均色を求める
        avg_RT1 = average_RGB(im, 2*w, 0, 4*w, h) # Right Top areaの上部分の平均色を求める
        avg_RT2 = average_RGB(im, 3*w, h, 4*w, 2*h) # Right Top areaの下部分の平均色を求める
        avg_LB1 = average_RGB(im, 0, 2*h, w, 3*h) #Left Bottom areaの上部分の平均色を求める
        avg_LB2 = average_RGB(im, 0, 3*h, 2*w, 4*h) # Left Bottom areaの下部分の平均色を求める
        avg_RB1 = average_RGB(im, 3*w, 2*h, 4*w, 3*h) # Right Bottom areaの上部分の平均色を求める
        avg_RB2 = average_RGB(im, 2*w, 3*h, 4*w, 4*h) # Right Bottom areaの下部分の平均色を求める

        avg_LT = (avg_LT1 + avg_LT2)/2 # Left Top Area全体の平均色
        avg_RT = (avg_RT1 + avg_RT2)/2 # Right Top Area全体の平均色
        avg_LB = (avg_LB1 + avg_LB2)/2 # Left Bottom Area全体の平均色
        avg_RB = (avg_RB1 + avg_RB2)/2 # Right Bottom Area全体の平均色
        avg_CT =  average_RGB(im, w, h, 3*w, 3*h) # Central Area全体の平均色
        # 全体の平均の(R,G,B)値と 5 つの領域の平均の(R,G,B)値の合計 6 つの (R,G,B)値から、NumPy 配列
        All_Array = np.array([avg_all, avg_LT, avg_RT, avg_LB, avg_RB, avg_CT])
        Area_name = ['RGB','Left Top', 'Right Top', 'Left Bottom', 'Right Bottom', 'Central']

        date = datetime.datetime.now() # 現在の日付と日時
        print("*********************************************")
        print("XAICHA JAIXIONG, B213379")
        print("日付: ", date)
        print("内容: NumPy 配列と関数(画像 NumPy ファイルの処理)")
        print("入力npyファイル:", fname)
        print("*********************************************")
        
        print("ファイル名：", fname) # 入力npyのファイルを出力する
        # 全体の平均色をプリントアウトする
        print("全体の平均色 = ( %5.3f, %5.3f, %5.3f)" %(avg_all[0], avg_all[1], avg_all[2]))
        index_max_min = FindMinMax(All_Array) # もっとも似ていたともっとも似ていなかった領域のインデックスを求めるインスタンス
        n_index = index_max_min[0] # もっとも似ていた領域のインデックス
        f_index = index_max_min[1]  # もっとも似ていなかった領域のインデックス

        print("平均色がもっとも全体に近い領域は,", Area_name[n_index])
        # 平均色がもっとも全体に近い領域をプリントアウトする
        print("その平均色 = ( %5.3f, %5.3f, %5.3f)" %(All_Array[n_index, 1], All_Array[n_index, 1], All_Array[n_index, 2]))
        # 平均色がもっとも全体と異なる領域をプリントアウトする
        print("平均色がもっとも全体と異なる領域は,", Area_name[f_index])
        print("その平均色 = ( %5.3f, %5.3f, %5.3f)" %(All_Array[f_index,0], All_Array[f_index, 1], All_Array[f_index, 2]))
        print('-'*46)

        # To print out the average of each areas
        # print("LTの平均色 = ( %5.3f, %5.3f, %5.3f)" %(avg_LT[0], avg_LB[1], avg_LT[2]))
        # print("RTの平均色 = ( %5.3f, %5.3f, %5.3f)" %(avg_RT[0], avg_RT[1], avg_RT[2]))
        # print("LBの平均色 = ( %5.3f, %5.3f, %5.3f)" %(avg_LB[0], avg_LB[1], avg_LB[2]))
        # print("RBの平均色 = ( %5.3f, %5.3f, %5.3f)" %(avg_RB[0], avg_RB[1], avg_RB[2]))
        # print("CTの平均色 = ( %5.3f, %5.3f, %5.3f)" %(avg_CT[0], avg_CT[1], avg_CT[2]))
        
    except FileNotFoundError:
        print("ファイル:",fname,"が見つかりません")
        sys.exit()#プログラム終了