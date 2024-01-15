# * * * * * * * * * * * * * * * * * * * * * * * * * * * *kadai4.py * * * * * 
#       作成者：XAICHA JAIXIONG 学籍番号：B213379
#       日付：2021/11/01
#このプログラムは、円、三角形と台形を乱数で生成して,　生成した各図形の成分をPostScriptの
#ファイルに実行結果を書き込む。このプトグラムは、各面積を計算して、最後に総面積を計算する
#生成するの図形は2から20の間を三角形と台形と円を、それぞれ N 個を生成とする
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

import math
import sys
import datetime
import random

class Shape:
    # 基底クラス
    def __init__(self, R, G, B):
        # コンストラクタ
        self.R = R # Rにセットする
        self.G = G # Gにセットする
        self.B = B # B にセットする

    def area(self): # 面積計算

        return 0 # 実数値を戻り値とする

    def ps_print(self): # 色を PS で書き出す
        print("%% 色:") 
        print("%3.6f %3.6f %3.6f setrgbcolor" %(self.R, self.G, self.B))


class Circle(Shape):
    # 派生クラス: Circl
    def __init__(self, R, G, B, x1, y1, radius):
        # コンストラクタ
        super().__init__(R, G, B)
        self.x1 = x1 # x1にセットする
        self.y1 = y1 # y1にセットする
        self.radius = radius # 半径にセットする

    def area(self): # 円の面積を計算する
        Area = math.pi*(self.radius**2) # 面積を計算する (A = πr^2)
        
        return Area # 面積の値をreturn する

    def ps_print(self): # PS で書き出す
        super().ps_print() # superクラスのps_print()関数を呼び出す
        print("newpath")
        print("%3.5f %3.5f %3.5f 0 360 arc" %(self.x1, self.y1, self.radius))
        print("stroke")
    

class Triangle(Shape):
    # 派生クラス: Triangle
    def __init__(self, R, G, B, x1, y1, x2, y2, x3, y3):
        # コンストラクタ
        super().__init__(R, G, B)
        self.x1 = x1 # x1にセットする
        self.y1 = y1 # y1にセットする
        self.x2 = x2 # x2にセットする
        self.y2 = y2 # y2にセットする
        self.x3 = x3 # x3にセットする
        self.y3 = y3 # y3にセットする

    def area(self): # 三角形の面積を計算する
        area_1 = self.x1*self.y2 + self.x2*self.y3 + self.x3*self.y1 # 正の部分を計算する
        area_2 = self.x2*self.y1 + self.x3*self.y2 + self.x1*self.y3 # 負の部分を計算する

        Area = abs(0.5*(area_1 - area_2)) # 正の部分と負の部分足し算して絶対値をする(abs = 絶対値計算する)

        return Area # 面積の値をreturn する

    def ps_print(self):# PS で書き出す
        super().ps_print() # superクラスのps_print()関数を呼び出す
        print("newpath")
        print("%3.5f %3.5f moveto" %(self.x1, self.y1))
        print("%3.5f %3.5f lineto" %(self.x2, self.y2))
        print("%3.5f %3.5f lineto" %(self.x3, self.y3))
        print("closepath")
        print("stroke")
        

class Trapezoid(Shape):
    # 派生クラス: Triangle
    def __init__(self, R, G, B, x1, y1, x2, y2, x3, y3, x4, y4):
        # コンストラクタ
        super().__init__(R, G, B)
        self.x1 = x1 # x1にセットする
        self.y1 = y1 # y1にセットする
        self.x2 = x2 # x2にセットする
        self.y2 = y2 # y2にセットする
        self.x3 = x3 # x3にセットする
        self.y3 = y3 # y3にセットする
        self.x4 = x4 # x4にセットする
        self.y4 = y4 # y4にセットする

    def area(self): # 台形の面積を計算する
        area_1 = self.x1*self.y2 + self.x2*self.y3 + self.x3*self.y4 + self.x4*self.y1 # 正の部分を計算する
        area_2 = self.x2*self.y1 + self.x3*self.y2 + self.x4*self.y3 + self.x1*self.y4 # 負の部分を計算する

        Area = abs(area_1 - area_2) # 正の部分と負の部分足し算して絶対値をする(abs = 絶対値計算する)

        return Area # 面積の値をreturn する

    def ps_print(self):# PS で書き出す
        super().ps_print() # superクラスのps_print()関数を呼び出す
        print("newpath")
        print("%3.5f %3.5f moveto" %(self.x1, self.y1))
        print("%3.5f %3.5f lineto" %(self.x2, self.y2))
        print("%3.5f %3.5f lineto" %(self.x4, self.y4))
        print("%3.5f %3.5f lineto" %(self.x3, self.y3))
        print("closepath")
        print("stroke")


if __name__ == '__main__':
    num_agrs = len(sys.argv)
    if(num_agrs != 2):
        print("[2,20]の間の図形の総数を引数で与えてください")
        sys.exit()# プログラム終了

    (XRANGE,YRANGE )  = (580.0, 700.0) # x や y の範囲

    Area_list = [] # 面積を入れるのリスト
    
    try: 
        n = int(sys.argv[1]) # 発生する図形総数:変動可
        if 2 > n or n > 20:
            print("図形の総数は2から20の間の数にしてください")
            sys.exit() # プログラムを終了する

        print("%%!PS-Adobe-2.0")
        print("%%File: kadai4.ps")
        date = datetime.datetime.now() # 現在の日付と日時
        print("%%*********************************************")
        print("%%XAICHA JAIXIONG, B213379")
        print("%%日付: ", date)
        print("%%内容：クラスの継承を用いた2次元図形クラスの作成")
        print("%%*********************************************")
        circle_n = triangle_n = trapezoid_n = 0

        for i in range(3*n): # 図を生成するのループ
            # 三角形と台形と円を、それぞれ N 個をランダムに発生する
            if circle_n == n: # 円が N 個になったとき
                if triangle_n == n:# 三角形が N個になったときの処理
                    shapeIndex = 2
                elif trapezoid_n == n:# 台形が N 個になったとき
                    shapeIndex = 1
                else:
                    shapeIndex = random.randint(1, 2) # return 0 ro 1 or 2
            elif trapezoid_n == n: # 台形が N 個になったとき
                if circle_n == n: # 円が N 個になったとき
                    shapeIndex = 1
                elif triangle_n == n:# 三角形が N個になったときの処理
                    shapeIndex = 0
                else:
                    shapeIndex = random.randint(0, 1) # return 0 ro 1 or 2
            elif triangle_n == n: # 三角形が N個になったときの処理
                if circle_n == n: # 円が N 個になったとき
                    shapeIndex = 2
                elif trapezoid_n == n:# 台形が N 個になったとき
                    shapeIndex = 0
                else:
                    shapeIndex = random.randrange(0, 3, 2) # return 0 ro 2 
            else: # 各図形が　N 個になっていない時の処理
                shapeIndex = random.randint(0, 2) # return 0 ro 1 or 2

            if shapeIndex == 0: # 円を生成：circle
                c_Red = random.uniform(0.0, 1.0) # 乱数で赤色を生成する
                c_Green = random.uniform(0.0, 1.0) # 乱数で緑色を生成する
                c_Blue = random.uniform(0.0, 1.0) # 乱数で青色を生成する
                c_x1 = random.uniform(0, XRANGE) # 乱数で中心点のxを生成する
                c_y1 = random.uniform(0, YRANGE) # 乱数で中心点のyを生成する
                c_radius = random.uniform(0, 0.25*XRANGE)# 乱数で半径を生成する
                # 派生クラス (円) のインスタンス生成
                circle = Circle(c_Red, c_Green, c_Blue, c_x1, c_y1, c_radius)
                Area_list.append(circle.area())# 円の面積をArea_listに追加する
                print("%% ",i+1,"番目の図形は円です")
                print("%% 円 : 面積 = %3.1f" %circle.area())
                circle.ps_print() # ps_print()の関数を呼び出す
                circle_n += 1

            elif shapeIndex == 1: # 三角形を生成：triangle 
                T3_Red = random.uniform(0.0, 1.0) # 乱数で赤色を生成する
                T3_Green = random.uniform(0.0, 1.0) # 乱数で緑色を生成する
                T3_Blue = random.uniform(0.0, 1.0) # 乱数で青色を生成する
                T3_x1 = random.uniform(0.0, XRANGE)
                T3_y1 = random.uniform(0.0, YRANGE)
                T3_x2 = random.uniform(0.0, XRANGE)
                T3_y2 = random.uniform(0.0, YRANGE)
                T3_x3 = random.uniform(0.0, XRANGE)
                T3_y3 = random.uniform(0.0, YRANGE)

                # 派生クラス (三角形) のインスタンス生成
                triangle = Triangle(T3_Red, T3_Green, T3_Blue, T3_x1, T3_y1, T3_x2, T3_y2, T3_x3, T3_y3)
                Area_list.append(triangle.area())# 三角形の面積をArea_listに追加する
                print("%% ",i+1,"番目の図形は三角形です")
                print("%% 三角形 : 面積 = %3.1f" %triangle.area())
                triangle.ps_print()# ps_print()の関数を呼び出す
                triangle_n += 1

            elif shapeIndex == 2: # 台形を生成：trapezoid
                T4_Red = random.uniform(0.0, 1.0) # 乱数で赤色を生成する
                T4_Green = random.uniform(0.0, 1.0) # 乱数で緑色を生成する
                T4_Blue = random.uniform(0.0, 1.0) # 乱数で青色を生成する
                T4_x1 = random.uniform(0.0, XRANGE)
                T4_y1 = random.uniform(0.0, YRANGE)
                T4_x2 = random.uniform(0.0, XRANGE)
                T4_x3 = random.uniform(0.0, XRANGE)
                T4_y2 = random.uniform(0.0, YRANGE)
                T4_x4 = random.uniform(0.0, XRANGE)
                # 台形の上底と下底は X 軸と平行とし、x1 < x2 ,x3 < x4 とする
                if T4_x1 > T4_x2: # x1 < x2　とする
                    item1 = T4_x1
                    T4_x1 = T4_x2
                    T4_x2 = item1
                if T4_x3 > T4_x4: # x3 < x4 とする
                    item2 = T4_x3
                    T4_x3 = T4_x4
                    T4_x4 = item2

                # 派生クラス (台形) のインスタンス生成
                trapezoid = Trapezoid(T4_Red, T4_Green, T4_Blue, T4_x1, T4_y1, T4_x2, T4_y1, T4_x3, T4_y2, T4_x4, T4_y2)
                Area_list.append(trapezoid.area()) # 台形の面積をArea_listに追加する
                print("%% ",i+1,"番目の図形は台形です")
                print("%% 台形 : 面積 = %3.1f" %trapezoid.area())
                trapezoid.ps_print() # ps_print()の関数を呼び出す
                trapezoid_n += 1

        sum_area = 0 # 総面積を計算するの変数を用意する
        # print("%%circle_n = %f" % circle_n)
        # print("%%triangle_n = %f" % triangle_n)
        # print("%%trapezoid_n = %f" % trapezoid_n)
        # print("%%n = ", n)

        for i in range(len(Area_list)): # 総面積を計算するのループ
            sum_area += Area_list[i] #　総面積を計算する

        print()   
        print("%%総面積は %3.5f です" %sum_area)# 総面積をプリントする
        print("%%-----------------------------------------------------------")

    except ValueError:
        print("関数の引数に整数以外が入力されました")
        sys.exit()#プログラム終了

