"""
	プログラム6-1: IrisScatterPlot.py (Irisデータからの散布図描画)
"""
import csv
import sys
import datetime
     
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
# def getTarget(data):
# 	length = len(data)
# 	target_list = []
# 	for i in range(length):
# 		if (data[i] == 'CYT'):
# 			target_list.append(0)
# 		elif  (data[i] == 'NUC'):
# 			target_list.append(1)
# 		elif (data[i] == 'MIT'):
# 			target_list.append(2)
#         # elif (data[i] == 'ME1'):
# 			target_list.append(3)
#         # elif (data[i] == 'ME2'):
# 			target_list.append(4)
#         # elif (data[i] == 'ME3'):
# 			target_list.append(5)
#         # elif (data[i] == 'EXC'):
# 		# 	target_list.append(6)
#         # elif (data[i] == 'VAC'):
# 		# 	target_list.append(7)
#         # elif (data[i] == 'POX'):
# 		# 	target_list.append(8)
#         # elif (data[i] == 'ERL'):
# 			target_list.append(9)
        
# 		target_list.append(data[i])
# 	return np.array(target_list)

# 描画データの抽出
# def extract(str, data, items):# data : list of Iris
# 	length = len(data)
# 	ext_list = []
# 	label = None
# 	if (str == 'MCG'):
# 		label = 'MCG: McGeogh 法:信号列認識法'
# 	elif (str == 'GVH'):
# 		label = 'GVH: von Heijne 法:信号列認識法'
		
# 	elif (str == 'ALM'):
# 		label = 'ALM: ALOM 膜のスコア'
# 	elif (str == 'MIT'):
# 		label = 'MIT: 真・非ミトコンドリアタンパク質に関するアミノ酸解析スコア'
		
# 	elif (str == 'NUC'):
# 		label = 'NUC: 核または非核タンパク質の核局所化信号スコア'
		

# 	return np.array(ext_list), label

# 散布図の描画
#		str1, str2: SL, SW, PL, PWのいずれかでstr1 != str2	
def runScatterPlot(str1, str2,items1, items2, label_name):
	# x, label1 = extract(str1, data, items1)
	# y, label2 = extract(str2, data, items2)
    label1 = "hello world"
    label2 = " World"
    x = items1
    y = items2
	# labels = getTarget(label_name)
	
	# colors = ['green','red','fuchsia','darkblue','cyan','blue','beige','orchid','black']
	# species = ['CYT','NUC','MIT','ME1','ME2','ME3','EXC','VAC','POX','ERL']
	# 大きさ20のフォント
	# fp2 = getFontProperty('20')
	# 大きさ15のフォント
	# fp3 = getFontProperty('15')

	# 描画キャンバスの設定
	fig = plt.figure(figsize=(10,10))
	ax = fig.add_axes([0.1,0.1,0.85,0.85])
	
	# 散布図を描画
	scale=50.0
    date = datetime.datetime.now()
	scatter = plt.scatter(x,y, s=scale, c=labels, cmap=mc.ListedColormap(colors))
	plt.xlabel(label1,fontsize=20,font_properties=fp2)
	plt.ylabel(label2,fontsize=20,font_properties=fp2)
	plt.xticks(fontsize=15)
	plt.yticks(fontsize=15)
	plt.title('散布図(Yeast): XAICHA JAIXIONG ',fontsize=30,font_properties=fp2)

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
	str_set = {'MCG', 'GVH', 'ALM', 'MIT', 'NUC'}
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
		print("入力パラメータはMCG,GVH,ALM,MIT,NUCの5つの属性名から異なる２つを選択してください")
		sys.exit()

	fname = "yeast.csv" # 実行フォルダにこのファイルがあることが前提
    mcg = []
	gvh = []
	alm = []
	mit = []
	nuc = []
	label_name = []
	data = []
	try: # ファイル例外処理
		with open(fname, "r", newline='', encoding='utf-8') as fin:
			lines = csv.reader(fin, delimiter=',')
			for line_no1, row1 in enumerate(lines, 1):
                label_name.append(row1[9])
                mcg.append(row[1])
				gvh.append(row[2])
				alm.append(row[3])
				mit.append(row[4])
				nuc.append(row[8])

        runScatterPlot(str1, str2, gcg, gvh, labe_name)     

	except FileNotFoundError:
		print("ファイル：",fname," が見つかりません")
		sys.exit()