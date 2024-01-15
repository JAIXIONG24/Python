# * * * * * * * * * * * * * * * * * * * * * * * * * * * *kadai4.py * * * * * 
#       作成者：XAICHA JAIXIONG 学籍番号：B213379
#       日付：2021/10/25
#
#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
import sys
import os
import datetime
import random

class Shape:
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def area(self):
    # def ps_print(self):

    
class Circle(Shape):
    def __init__(self, R, G, B, x, y, radius):
        super().__init__(R, G, B)
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):


    def ps_print(self):


class Triangle(Shape):
    def __init__(self, R, G, B, x1, y1, x2, y2, x3, y3):
        super().__init__(R, G, B)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    
    def area(self):


    def ps_print(self):

    
class Trapezoid(Shape):
    def __int__(self, R, G, B, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(R, G, B)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def area(self):


    def ps_print(self):

        

if __name__ == '__main__':
    num_agrs = len(sys.argv)
    if(num_agrs != 2):
        print("csvファイルと一文字(GまたはC)を最後に追加してください")
        sys.exit()# プログラム終了
    (XRANGE,YRANGE )  = (580.0, 700.0)
    RADIUS = 290.0
    
    try: 
        n = (int)(sys.argv[1])
        if 2 > n or n > 20:
            print("図形の総数は2から20の間の数にしてください")
            sys.exit()
        for i in range(n):
            R = random.randfloat(0.0, 1.0)
            G = random.randfloat(0.0, 1.0)
            B = random.randfloat(0.0, 1.0)
            x1 = random.randfloat(0.0, XRANGE)
            y1 = random.randfloat(0.0, YRANGE)
            radius = random.randfloat(0.0, RADIUS)
            
        date = datetime.datetime.now() # 現在の日付と日時
        print("%%*********************************************")
        print("%%XAICHA JAIXIONG, B213379")
        print("%%日付: ", date)
        print("%%内容：クラスの継承を用いた2次元図形クラスの作成")
        print("*********************************************")
        

    except FileNotFoundError:
        print("ファイル:",fname,"が見つかりません")
        sys.exit()#プログラム終了