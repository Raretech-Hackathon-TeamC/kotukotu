import matplotlib.pyplot as plt
import base64
from io import BytesIO
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
	plt.switch_backend("AGG")        #スクリプトを出力させない
	plt.figure(figsize=(10,5))       #グラフサイズ
	plt.bar(x,y)                     #グラフ作成
	# plt.title("Revenue per Date")  #グラフタイトル
	plt.ylim(0, 480)                 #y軸最小値と最大値
	plt.xlabel("date")               #xラベル
	plt.ylabel("duration")           #yラベル
	plt.tight_layout()               #レイアウト
	graph = Output_Graph()           #グラフプロット
	return graph