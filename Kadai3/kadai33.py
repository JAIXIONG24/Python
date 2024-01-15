'''
	プログラム3-1: CSVデータのReader例
'''
import csv # CSV readerを使うためインポートします
import sys

class Iris: # あやめクラス
	# Fisher's Iris 
	def __init__(self, data_list):# コンストラクタ
		if not isinstance(data_list, list):
			print("データがリスト形式ではありません")
			return
		# メンバー変数への代入
		self.sepal_length = float(data_list[0]) # がくの長さ
		self.sepal_width = float(data_list[1]) # がくの幅
		self.petal_length = float(data_list[2]) # 花弁の長さ
		self.petal_width = float(data_list[3]) # 花弁の幅
		self.species = data_list[4] # あやめの種類（文字列）

	def printData(self):
		print("がく長={0:5.2f}, がく幅={1:5.2f}, 花弁長={2:5.2f}, 花弁幅={3:5.2f}, "\
		"種類={4:5s}".format(self.sepal_length,self.sepal_width, self.petal_length,self.\
		petal_width,self.species))

		''' 以下のようにしても同様
		print("がく長=%5.2f, がく幅=%5.2f, 花弁長=%5.2f, 花弁幅=%5.2f, "\
		"種類=%5s" % (self.sepal_length,self.sepal_width, self.petal_length,\
		self.petal_width,self.species))
		'''
		
if __name__ == "__main__":
	num_args = len(sys.argv)
	if (num_args != 2):
		print("python CSVReader.py csv_filename")
		sys.exit()
	fname = sys.argv[1]
	try: # ファイル例外処理
		with open(fname, "r", newline='', encoding='utf-8') as fin:
			# lines = csv.reader(fin, delimiter=',')
            reader = csv.reader(fin, delimiter=",")
            for row in reader:
                print(row)
            # print(lines)
			# data = []
			# first = True
			# for line in lines:
			# 	if first:
			# 		first = False
			# 		continue
			# 	iris = Iris(line) # Irisクラスデータの生成
			# 	data.append(iris)
			# for ith in data: # リストに保持されたクラスのインスタンスからprintData関数を呼び出す
			# 	ith.printData()
	except FileNotFoundError:
		print("ファイル：",fname," が見つかりません")
		sys.exit()