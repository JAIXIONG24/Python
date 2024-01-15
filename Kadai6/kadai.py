"""
	プログラム6-1: IrisScatterPlot.py (Irisデータからの散布図描画)
"""
import csv
import sys

class Iris: # あやめクラス
	# Fisher's Iris 
	def __init__(self, data_list):# コンストラクタ
		if not isinstance(data_list, list):
			print("データがリストr形式ではありません")
			return
		self.sepal_length = float(data_list[0]) # がくの長さ
		self.sepal_width = float(data_list[1]) # がくの幅
		self.petal_length = float(data_list[2]) # 花弁の長さ
		self.petal_width = float(data_list[3]) # 花弁の幅
		self.species = data_list[4] # あやめの種類（文字列）

	def printData(self):
		print("がく長={0:5.2f}, がく幅={1:5.2f}, 花弁長={2:5.2f}, 花弁幅={3:5.2f}, "\
		"種類={4:5s}".format(self.sepal_length,self.sepal_width, self.petal_length,\
		self.petal_width,self.species))

# Matplotlibのフォントの制御（大きさや種類）
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm
import matplotlib.colors as mc
import numpy as np

# フォントサイズ設定関数
def getFontProperty(size_str):
	font_prop = fm.FontProperties()
	font_prop.set_style('normal')
	font_prop.set_weight('light')
	font_prop.set_size(size_str)
	return font_prop.copy()

# データラベル（整数変換値）の抽出
def getTarget(data):
	length = len(data)
	target_list = []
	for i in range(length):
		if (data[i].species == 'Setosa'):
			target_list.append(0)
		elif  (data[i].species == 'Versicolor'):
			target_list.append(1)
		elif (data[i].species == 'Virginica'):
			target_list.append(2)
		# target_list.append(data[i].species)
	return np.array(target_list)

# 描画データの抽出
def extract(str, data):# data : list of Iris
	length = len(data)
	ext_list = []
	label = None
	if (str == 'SL'):
		label = 'Sepal Length'
		for i in range(length):
			ext_list.append(data[i].sepal_length)
	elif (str == 'SW'):
		label = 'Sepal Width'
		for i in range(length):
			ext_list.append(data[i].sepal_width)
	elif (str == 'PL'):
		label = 'Petal Length'
		for i in range(length):
			ext_list.append(data[i].petal_length)
	elif (str == 'PW'):
		label = 'Petal Width'
		for i in range(length):
			ext_list.append(data[i].petal_width)
	return np.array(ext_list), label

# 散布図の描画
#		str1, str2: SL, SW, PL, PWのいずれかでstr1 != str2	
def runScatterPlot(str1, str2, data):
	x, label1 = extract(str1, data)
	y, label2 = extract(str2, data)
	labels = getTarget(data)
	
	colors = ['red','green','blue']
	species = ['Setosa','Virginica','Versicolor']
	# 大きさ20のフォント
	fp2 = getFontProperty('20')
	# 大きさ15のフォント
	fp3 = getFontProperty('15')

	# 描画キャンバスの設定
	fig = plt.figure(figsize=(10,10))
	ax = fig.add_axes([0.1,0.1,0.85,0.85])
	
	# 散布図を描画
	scale=50.0
	scatter = plt.scatter(x,y, s=scale, c=labels, cmap=mc.ListedColormap(colors))
	plt.xlabel(label1,fontsize=20,font_properties=fp2)
	plt.ylabel(label2,fontsize=20,font_properties=fp2)
	plt.xticks(fontsize=15)
	plt.yticks(fontsize=15)
	plt.title('IRIS DATA',fontsize=30,font_properties=fp2)

	handles, labels = scatter.legend_elements(prop="colors", alpha=0.6)
	legend = ax.legend(handles, species, loc="best", shadow=True, prop=fp3)

	# 描画結果をファイルにも書き出す
	fname = "Iris-scatter-plot_X_" + str1+"_Y_"+str2
	f1 = fname+".jpg"
	f2 = fname+".pdf"
	plt.savefig(f1) # JPEG描画
	plt.savefig(f2) # PDF描画
	plt.show()

def goodParams(str1, str2):
	str_set = {'SL', 'SW', 'PL', 'PW'}
	if ((str1 != str2) and (str1 in str_set) and (str2 in str_set)):
		return True
	else:
		return False

if __name__ == "__main__":
	num_args = len(sys.argv)
	if (num_args != 3):
		print("python IrisScatterPlot.py [a pair from (SL  SW  PL  PW)] (e.g. SL PL )")
		sys.exit()
	str1 = sys.argv[1]
	str2 = sys.argv[2]
	if (not goodParams(str1, str2)):
		print("入力パラメータはSL,SW,PL,PWの４つの属性名から異なる２つを選択してください")
		sys.exit()
	fname = "iris.csv" # 実行フォルダにこのファイルがあることが前提
	try: # ファイル例外処理
		with open(fname, "r", newline='', encoding='utf-8') as fin:
			lines = csv.reader(fin, delimiter=',')
			data = []
			first = True
			for line in lines:
				if first:
					first = False
					continue
				iris = Iris(line) # Irisクラスデータの生成
				data.append(iris)
			runScatterPlot(str1, str2, data)
	except FileNotFoundError:
		print("ファイル：",fname," が見つかりません")
		sys.exit()