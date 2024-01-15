# * * * * * * * * * * * * * * * * * * * * * * * * * * * kadai2.py * * * *
#           作成者：XAICHA JAIXIONG 学籍番号：B213379
#           日付：2021/10/18
#
#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

import sys
import numpy as np

def Fibonacchi(n):
	if n < 0:
		return -1
	elif n == 0:
		return 0
	elif n == 1 or n==2:
		return 1
	else:
		return Fibonacchi(n-1)+Fibonacchi(n-2) # 再帰
		
if __name__ == '__main__':
	num_args = len(sys.argv)
	if (num_args != 3):
		print("python Fibonacchi number")
		sys.exit()
    fname = sys.argv[1]
    im = np.load(fname)
    print(im.shape)
    print(im)

	try:
		n = int(sys.argv[2]) # 第一引数をフィボナッチの数列nとする
		result = Fibonacchi(n)
		if result < 0:
			print("フィボナッチ関数の引数に負の整数が入力されました.")
			sys.exit(-1)
		else:
			print("数：n = ", n, " のフィボナッチ数は",result,"です")
	except ValueError:
		print("フィボナッチ関数の引数に整数以外が入力されました.")
		sys.exit(1)









