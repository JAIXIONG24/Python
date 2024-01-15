# * * * * * * * * * * * * * * * * * * * * * * * * * * * *kadai5.py * * * * * 
#       作成者：XAICHA JAIXIONG 学籍番号：B213379
#       日付：2021/11/08
# このプログラムは、Python 言語で演算子のオーバーローディングを用いて二つ行列の加算、減算、
# 乗算(要素ごとの積)、除算（要素ごとの除算)を計算するプログラムである. そして、計算した結果
# をkadai5.txtに出力すること
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

import sys
import datetime
import random
import numpy as np

def divzero_warning(func): # 関数デコレータ(@divzero_warning)
    a = np.zeros(shape=(2, 2)) # 配列ゼロ a　を生成する
    b = np.zeros(shape=(2, 2)) # 配列ゼロ b　を生成する
    def inner(a, b):
        #　配列 b の要素に 1 つでも 0 があれば, プログラムを警告を出し終了するループ
        for i in range(len(b.mat)):
            for j in range(len(b.mat[0])):
                if b.mat[i][j] == 0:
                    # print("ゼロ割り算が発生しました")
                    return "ゼロ割り算が発生しました"
        return func(a, b)
    return inner

class Matrix: # Matrix クラス
    def __init__(self, row, col, mat): # コンストラクタ
        self.row = row # 変数rowをセットする
        self.col = col # 変数colをセットする
        self.mat = mat # 配列matをセットする

    def __add__(self, other): # 行列の加算演算子のオーバーローディング
        if self.row != other.row and self.col != other.col: # サイズが一致しない場合の処理
            print("AとBのサイズが一致しない")
            return self.mat # 左辺の行列返す 

        C = np.zeros(shape=(self.row, self.col))
        # 行列の加算を計算するループ
        for i in range(self.row):
            for j in range(self.col):
                C[i][j] = self.mat[i][j] + other.mat[i][j]
    
        return C

    def __sub__(self, other): # 行列の減算演算子のオーバーローディング
        if self.row != other.row and self.col != other.col: # サイズが一致しない場合の処理
            print("AとBのサイズが一致しない")
            return self.mat # 左辺の行列返す
        
        C = np.zeros(shape=(self.row, self.col))
        # 行列の加算を計算するループ
        for i in range(self.row):
            for j in range(self.col):
                C[i][j] = self.mat[i][j] - other.mat[i][j]
    
        return C
    
    def __mul__(self, other): # 行列の乗算演算子のオーバーローディング
        if self.row != other.row and self.col != other.col: # サイズが一致しない場合の処理
            print("AとBのサイズが一致しない")
            return self.mat # 左辺の行列返す

        C = np.zeros(shape=(self.row, self.col))
        # 行列の加算を計算するループ
        for i in range(self.row):
            for j in range(self.col):
                C[i][j] = self.mat[i][j] * other.mat[i][j]
    
        return C

    @divzero_warning 
    def __truediv__(self, other): # 行列の除算演算子のオーバーローディング
        C = np.zeros(shape=(self.row, self.col))
        # 行列の加算を計算するループ
        for i in range(self.row):
            for j in range(self.col):
                C[i][j] = self.mat[i][j] / other.mat[i][j]
    
        return C
    

if __name__ == '__main__':
    num_agrs = len(sys.argv)
    if(num_agrs != 4):
        print("pythonファイルの後にM行N列flagの整数を入力してください")
        sys.exit()# プログラム終了
    
    try: 
        M = int(sys.argv[1]) # 行列の変数　M （行)
        N = int(sys.argv[2]) # 行列の変数　N　(列)
        flag = int(sys.argv[3]) # 2 パターンの変数flag

        if (N < 2 or M < 2 ) or (N > 5 or M > 5): # コマンドラインで指定(2 <= M, N <= 5)
            print("M 行 N 列の実数行列は(2 <= M, N <= 5, flag は 0 または 1)を入力してください")
            sys.exit() # プログラムを終了する

        if flag == 0: # 1 パターン目の場合の処理
            A = np.random.uniform(-10, 10, (M, N))
            B = np.random.uniform(-10, 10, (M, N))
        elif flag == 1: # 2 パターン目の場合の処理
            A = np.random.uniform(-10, 10, (M, N))
            B = np.random.uniform(-10, 10, (M, N))
            B[0][0] = 0.0 
        else: # 2パターン以外の処理
            print("flag は 0 また は 1入力してください")
            sys.exit() # プログラムを終了する

        date = datetime.datetime.now() # 現在の日付と日時
        print("$ python %s %d %d %d" %(sys.argv[0], M, N, flag))
        print("*********************************************")
        print("XAICHA JAIXIONG, B213379")
        print("日付: ", date)
        print("内容：行列演算(演算子のオーバーローディング)")
        print("      およびデコレータ関数利用例")
        print("*********************************************")
        
        print("入力された値 %d %d %d"%(M, N, flag))
        print("A:")
        # A 行列をプリントするループ
        for i in range(M):
            print("|", end="")
            for j in range(N):
                print("%3.4f " %A[i][j], end="")

            print("|")

        print("B:")
        # B 行列をプリントするループ
        for i in range(M):
            print("|", end="")
            for j in range(N):
                print("%3.4f " %B[i][j], end="")
                
            print("|")
        
        Matrix_A = Matrix(M, N, A)
        Matrix_B = Matrix(M, N, B)

        AB_add = Matrix_A + Matrix_B # 加算（__add__)
        AB_sub = Matrix_A - Matrix_B # 減算（__sub__)
        AB_mul = Matrix_A * Matrix_B # 乗算（__mul__)
        AB_div = Matrix_A / Matrix_B # 除算（__truediv__)   
        
        print("C=A+B:")
        # C=A+B行列をプリントするループ
        for i in range(len(AB_add)):
            print("|", end="")
            for j in range(len(AB_add[0])):
                print("%3.4f " %AB_add[i][j], end="")
            print("|")

        print("C=A-B:")
        # C=A-B行列をプリントするループ
        for i in range(len(AB_sub)):
            print("|", end="")
            for j in range(len(AB_sub[0])):
                print("%3.4f " %AB_sub[i][j], end="")
            print("|")
        
        print("C=A*B:")
        # C=A*B行列をプリントするループ
        for i in range(len(AB_mul)):
            print("|", end="")
            for j in range(len(AB_mul[0])):
                print("%3.4f " %AB_mul[i][j], end="")
            print("|")

        print("C=A/B:")
        # C=A/B行列をプリントするループ
        if type(AB_div) == str:
            print("ゼロ割り算が発生しました")
        else:
            for i in range(len(AB_div)):
                print("|", end="")
                for j in range(len(AB_div[0])):
                    print("%3.4f " %AB_div[i][j], end="")
                print("|")
        
        print("-"*47)
       
    except ValueError:
        print("関数の引数に整数以外が入力されました")
        sys.exit()#プログラム終了

