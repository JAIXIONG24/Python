'''
	プログラム4-1: SuperクラスとSubクラスのシンプルな事例
'''
import sys
import os
class Shape:
	# 基底クラス
	def __init__(self, R, G, B):
		# コンストラクタ
        self.R = '2'
        self.G =G
        self.B =B
		self.greetings = "Greetings"
	def name(self):
		print("かんきつ類")

class Circle(Shape):
	# 派生クラス: Circle
	def __init__(self, R, G, B):
		# コンストラクタ
        Shape().__init__(R, G, B)
		self.greetings = "Good morning"
	def name(self):
		print("みかん")

class Triangle(Shape):
	# 派生クラス: Triangle
	def __init__(self, R, G, B):
		# コンストラクタ
        Shape().__init__(R, G, B)
		self.greetings = "Good afternoon"
	def name(self):
		print("オレンジ")

class Trapezoid(Shape):
	# 派生クラス: Trapezoid
	def __init__(self, R, G, B):
		# コンストラクタ
        Shape().__init__(R, G, B)
		self.greetings = "Good evening"
	def name(self):
		print("グレープフルーツ: ", end="")
		super().name() # 基底クラスのname()関数を呼び出す

if __name__ == "__main__":
	super_list = [ Circle(1, 2, 3), Triangle(4,5,6), Trapezoid(7,8,9)]
	for list in super_list:
		print(list.greetings, ": ", end="")
		list.name()