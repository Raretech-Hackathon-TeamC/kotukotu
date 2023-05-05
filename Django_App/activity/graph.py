import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib.dates as mdates
#フォントの日本語対応
from matplotlib import rcParams
rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = "Hiragino Maru Gothic Pro"

#プロットしたグラフを画像データとして出力するための関数
def Output_Graph():
	buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")    #png形式の画像データを取り扱う
	buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
	img   = buffer.getvalue()            #バッファの全内容を含むbytes
	graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
	buffer.close()
	return graph


#グラフをプロットするための関数
def Plot_Graph(x,y):
	y = [i / 60 for i in y]
	plt.switch_backend("AGG")        #スクリプトを出力させない
	plt.figure(figsize=(10,5))       #グラフサイズ
	plt.bar(x,y)                     #グラフ作成
	plt.ylim(0, 6)                   #y軸最小値と最大値
	plt.yticks([0, 2, 4, 6])         #y軸メモリを2単位で表示
	plt.subplots_adjust(bottom=0.3)  #x軸ラベルが重ならないように位置を調整

	#x軸のラベルを設定
	ax = plt.gca()
	ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
	plt.gcf().autofmt_xdate()

	plt.tight_layout()               #レイアウト
	graph = Output_Graph()           #グラフプロット
	return graph