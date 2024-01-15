# * * * * * * * * * * * * * * * * * * * * * * * * * * * *kadai6.py * * * * * 
#       作成者：XAICHA JAIXIONG 学籍番号：B213379
#       日付：2021/11/14
#
# 今回の課題は、第 6 回の資料にある「あやめ」のデータの散布図にならい、「酵母」(Yeast)
#データの散布図を作成するプログラム。
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

import csv
import sys
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm
import matplotlib.colors as mc
import numpy as np
import datetime

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
	target_list = []  # empty list for in put the data 
	cyt = []
	nuc = []
	mit = []
	me1 = []
	me2 = []
	me3 = []
	exc = []
	vac = []
	pox = []
	erl = []
	for i in range(length):# データラベル（整数変換値)のループ
		if (data[i] == 'CYT'): # CYTのデータ
			cyt.append(0) # リストに追加する
		elif  (data[i] == 'NUC'):
			nuc.append(1)
		elif (data[i] == 'MIT'):
			mit.append(2)
		elif (data[i] == 'ME1'):
			me1.append(3)
		elif (data[i] == 'ME2'):
			me2.append(4)
		elif  (data[i] == 'ME3'):
			me3.append(5)
		elif (data[i] == 'EXC'):
			exc.append(6)
		elif (data[i] == 'VAC'):
			vac.append(7)
		elif (data[i] == 'POX'):
			pox.append(8)
		elif (data[i] == 'ERL'):
			erl.append(9)
	
	target_list.extend(cyt)
	target_list.extend(nuc)
	target_list.extend(mit)
	target_list.extend(me1)
	target_list.extend(me2)
	target_list.extend(me3)
	target_list.extend(exc)
	target_list.extend(vac)
	target_list.extend(pox)
	target_list.extend(erl)

		# target_list.append(data[i].species)
	return np.array(target_list) # return list

# 描画データの抽出
def extract(str, data, label_name):
	length = len(label_name)
	ext_list = [] # データを入れるリストを用意しておく
	cyt = []# データを入れるリストを用意しておく
	nuc = []# データを入れるリストを用意しておく
	mit = []# データを入れるリストを用意しておく
	me1 = []# データを入れるリストを用意しておく
	me2 = []# データを入れるリストを用意しておく
	me3 = []# データを入れるリストを用意しておく
	exc = []# データを入れるリストを用意しておく
	vac = []# データを入れるリストを用意しておく
	pox = []# データを入れるリストを用意しておく
	erl = []# データを入れるリストを用意しておく
	# 横軸と縦軸を 2 か ら9コラムに該当するの処理
	if (str == 'MCG'):
		label = 'MCG: McGeogh 法:信号列認識法'
		for i in range(length):
			if (label_name[i] == 'CYT'): # if the Positin in i label_name is CYT and input the i data in to CYT
				cyt.append(data[i]) # append the data to the list cyt
			elif (label_name[i] =='NUC'):
				nuc.append(data[i])
			elif (label_name[i] == 'MIT'):
				mit.append(data[i])
			elif (label_name[i] == 'ME1'):
				me1.append(data[i])
			elif (label_name[i] == 'ME2'):
				me2.append(data[i])
			elif (label_name[i]=='ME3'):
				me3.append(data[i])
			elif (label_name[i] == 'EXC'):
				exc.append(data[i])
			elif (label_name[i] == 'VAC'):
				vac.append(data[i])
			elif (label_name[i] == 'POX'):
				pox.append(data[i])
			elif (label_name[i] == 'ERL'):
				erl.append(data[i])

	elif (str == 'GVH'):
		label = 'GVH: von Heijne 法:信号列認識法'
		for i in range(length):
			if (label_name[i] == 'CYT'):
				cyt.append(data[i])
			elif (label_name[i] =='NUC'):
				nuc.append(data[i])
			elif (label_name[i] == 'MIT'):
				mit.append(data[i])
			elif (label_name[i] == 'ME1'):
				me1.append(data[i])
			elif (label_name[i] == 'ME2'):
				me2.append(data[i])
			elif (label_name[i]=='ME3'):
				me3.append(data[i])
			elif (label_name[i] == 'EXC'):
				exc.append(data[i])
			elif (label_name[i] == 'VAC'):
				vac.append(data[i])
			elif (label_name[i] == 'POX'):
				pox.append(data[i])
			elif (label_name[i] == 'ERL'):
				erl.append(data[i])
	elif (str == 'ALM'):
		label = 'ALM: ALOM 膜のスコア'
		for i in range(length):
			if (label_name[i] == 'CYT'):
				cyt.append(data[i])
			elif (label_name[i] =='NUC'):
				nuc.append(data[i])
			elif (label_name[i] == 'MIT'):
				mit.append(data[i])
			elif (label_name[i] == 'ME1'):
				me1.append(data[i])
			elif (label_name[i] == 'ME2'):
				me2.append(data[i])
			elif (label_name[i]=='ME3'):
				me3.append(data[i])
			elif (label_name[i] == 'EXC'):
				exc.append(data[i])
			elif (label_name[i] == 'VAC'):
				vac.append(data[i])
			elif (label_name[i] == 'POX'):
				pox.append(data[i])
			elif (label_name[i] == 'ERL'):
				erl.append(data[i])
	elif (str == 'MIT'):
		label = 'MIT: 真・非ミトコンドリアタンパク質に関するアミノ酸解析スコア'
		for i in range(length):
			if (label_name[i] == 'CYT'):
				cyt.append(data[i])
			elif (label_name[i] =='NUC'):
				nuc.append(data[i])
			elif (label_name[i] == 'MIT'):
				mit.append(data[i])
			elif (label_name[i] == 'ME1'):
				me1.append(data[i])
			elif (label_name[i] == 'ME2'):
				me2.append(data[i])
			elif (label_name[i]=='ME3'):
				me3.append(data[i])
			elif (label_name[i] == 'EXC'):
				exc.append(data[i])
			elif (label_name[i] == 'VAC'):
				vac.append(data[i])
			elif (label_name[i] == 'POX'):
				pox.append(data[i])
			elif (label_name[i] == 'ERL'):
				erl.append(data[i])
	elif (str == 'NUC'): 
		label = 'NUC: 核または非核タンパク質の核局所化信号スコア'
		for i in range(length):
			if (label_name[i] == 'CYT'):
				cyt.append(data[i])
			elif (label_name[i] =='NUC'):
				nuc.append(data[i])
			elif (label_name[i] == 'MIT'):
				mit.append(data[i])
			elif (label_name[i] == 'ME1'):
				me1.append(data[i])
			elif (label_name[i] == 'ME2'):
				me2.append(data[i])
			elif (label_name[i]=='ME3'):
				me3.append(data[i])
			elif (label_name[i] == 'EXC'):
				exc.append(data[i])
			elif (label_name[i] == 'VAC'):
				vac.append(data[i])
			elif (label_name[i] == 'POX'):
				pox.append(data[i])
			elif (label_name[i] == 'ERL'):
				erl.append(data[i])
    # リストを一つにする
	ext_list.extend(cyt)
	ext_list.extend(nuc)
	ext_list.extend(mit)
	ext_list.extend(me1)
	ext_list.extend(me2)
	ext_list.extend(me3)
	ext_list.extend(exc)
	ext_list.extend(vac)
	ext_list.extend(pox)
	ext_list.extend(erl)
	
	return np.array(ext_list), label

	
# 散布図の描画	
def runScatterPlot(str1, str2, data1, data2, label_name):
	# x, label1 = extract(str1, data1, label_name)
	# y, label2 = extract(str2, data2, label_name)
	label1 = "hello"
	label2 = "World"
	x, y = data1, data2
	labels = getTarget(label_name)
	
	colors = ['green','red','fuchsia','darkblue','cyan','blue','beige','orchid','black']
	species = ['CYT','NUC','MIT','ME1','ME2','ME3','EXC','VAC','POX','ERL']
	# 大きさ20のフォント
	fp2 = getFontProperty('10')
	# 大きさ15のフォント
	fp3 = getFontProperty('10')

	# 描画キャンバスの設定
	fig = plt.figure(figsize=(10,15))
	ax = fig.add_axes([0.1,0.1, 0.85,0.85])
	
	# 散布図を描画
	scale=15.0
	# scatter1 = plt.scatter(x1,y1)
	# ax.plot(x, y)
	# ax.set_xlim(0.0, 10.0)
	# ax.set_ylim(0.0, 10,0)
	scatter = plt.scatter(x,y, s=scale, c=labels, cmap=mc.ListedColormap(colors))
	plt.xlabel(label1,fontsize=15,font_properties=fp2)
	plt.ylabel(label2,fontsize=15,font_properties=fp2)

	plt.xticks(fontsize=5)
	plt.yticks(fontsize=5)
	# plt.xticks(np.arange(0, 1, step=0.1))
	# plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
	date = datetime.datetime.now() # 現在の日付と日時
	plt.title('散布図(Yeast): XAICHA JAIXIONG  %s' %date ,fontsize=30,font_properties=fp2)

	# handles, labels = scatter.legend_elements(prop="colors", alpha=0.2)
	# legend = ax.legend(handles, species, loc="best", shadow=True, prop=fp3)

	# 描画結果をファイルにも書き出す
	fname = "Yeast_" + str1+"_Y_"+str2
	f1 = fname+".jpg"
	f2 = fname+".pdf"
	plt.savefig(f1) # JPEG描画
	plt.savefig(f2) # PDF描画
	plt.show()

def goodParams(str1, str2): # 　入力したコマンドラインが存在するかどうか調べるmethod
	str_set = {'MCG', 'GVH', 'ALM', 'MIT', 'NUC'}
	if ((str1 != str2) and (str1 in str_set) and (str2 in str_set)):
		return True
	else:
		return False

if __name__ == "__main__":
	num_args = len(sys.argv)
	if (num_args != 3):
		print("python IrisScatterPlot.py [a pair from (MCG GVH ALM MIT NUC)] (e.g. MCG NUC )")
		sys.exit()
	str1 = sys.argv[1]
	str2 = sys.argv[2]
	if (not goodParams(str1, str2)): #　入力したコマンドラインが存在しない時の処理
		print("入力パラメータはMCG,GVH,ALM,MIT,NUCの5つの属性名から異なる２つを選択してください")
		sys.exit()
	fname = "yeast.csv" # 実行フォルダにこのファイルがあることが前提
	
	label_name = []
	items1 = []
	items2 = []
	try: # ファイル例外処理
		with open(fname, "r", newline='', encoding='utf-8') as fin:
			lines = csv.reader(fin, delimiter=',')
			for line_no, row in enumerate(lines, 1):
				# 入力した データを判断するループ
				# print(row[1])
				if (str1 == 'MCG'):
					# mcg.append(row[1])
					items1.append(row[1])
				elif (str1 == 'GVH'):
					items1.append(row[2])
				elif (str1 == 'ALM'):
					items1.append(row[3])
				elif (str1 == 'MIT'):
					items1.append(row[4])
				elif (str1 == 'NUC'):
					items1.append(row[8])
				
				label_name.append(row[9])
                # 入力した データを判断するループ
				if (str2 == 'MCG'):
					# mcg.append(row[1])
					items2.append(row[1])
				elif (str2 == 'GVH'):
					items2.append(row[2])
				elif (str2 == 'ALM'):
					items2.append(row[3])
				elif (str2 == 'MIT'):
					items2.append(row[4])
				elif (str2 == 'NUC'):
					items2.append(row[8])

		runScatterPlot(str1, str2, items1, items2, label_name) # 散布図を描くmethodに処理する
		# print(items1)
			
	except FileNotFoundError:
		print("ファイル：",fname," が見つかりません")
		sys.exit()