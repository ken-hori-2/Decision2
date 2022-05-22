import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from matplotlib import pyplot as plt

# データを用意する------------------------------------------
df = pd.DataFrame()                                          # データフレーム初期化
n = 20                                                       # 1クラス毎のデータ数
for i in range(3):                                           # データ作成ループ
    if i == 0:
        x = pd.Series(np.random.uniform(0.5, 2.8, n))
        y = pd.Series(x * np.random.uniform(0.8, 1.2, n))
    elif i == 1:
        x = pd.Series(np.random.uniform(2.2, 3.8, n))
        y = pd.Series(np.random.uniform(0.5, 1.8, n))
    else:
        x = pd.Series(np.random.uniform(3.2, 3.8, n))
        y = pd.Series(np.random.uniform(2.2, 3.8, n))
    label = pd.Series(np.full(n, i))                         # ラベル（クラス）を作成
    temp_df = pd.DataFrame(np.c_[x, y, label])               # クラス毎のデータフレームを作成
    df = pd.concat([df, temp_df])                            # 作成されたクラス毎のデータを逐次結合
df.index = np.arange(0, len(df), 1)                          # index(行ラベル)を初期化
# クラス毎のデータフレームに分離（プロット用）
class_0 = df[df[2] == 0]                                     # ラベル0を抽出
class_1 = df[df[2] == 1]                                     # ラベル1を抽出
class_2 = df[df[2] == 2]                                     # ラベル2を抽出
# ----------------------------------------------------------

# 学習させる値(訓練データ)とクラス(正解ラベル)に分離
data = df[[0, 1]]                                            # 訓練データ
data_class = pd.Series(df[2])                                # 正解ラベル

# 決定木による学習
clf = RandomForestClassifier(n_estimators=100,               # 決定木の数
                             criterion='gini',               # 不純度評価指標の種類(ジニ係数）
                             max_depth=3,                    # 木の深さ
                             min_samples_leaf=1,             # 1ノード（葉）の最小クラス数
                             max_features='auto')            # 最大特徴量数
clf.fit(data, data_class)                                    # フィッティング
r2 = clf.score(data, data_class)                             # 決定係数を算出

# dotファイルの生成
# for j in range(len(clf.estimators_)):
#     tree.export_graphviz(clf.estimators_[j],
#                          out_file='dir\\'+'tree'+str("{:03}".format(j))+'.dot', # 決定木の.dotファイル名自動ナンバリング
#                          filled=True,                                   # 色を塗る
#                          rounded=True,                                  # 角を丸める
#                          feature_names=['feature1', 'feature2'],        # 特徴量名
#                          class_names=['0', '1', '2'],                   # クラス名
#                          proportion=True)                               # 位置調整True

# 決定境界可視化用
grid_line = np.arange(-10, 10, 0.05)                         # グリッドデータのための配列を生成
X, Y = np.meshgrid(grid_line, grid_line)                     # グリッドを作成
Z = clf.predict(np.array([X.ravel(), Y.ravel()]).T)          # .predictが使えるデータshapeに変換して予測
Z = Z.reshape(X.shape)                                       # 3Dプロットするためにshapeを再変換

# ここからグラフ描画----------------------------------------
# フォントの種類とサイズを設定する。
plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Times New Roman'

# 目盛を内側にする。
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig = plt.figure()
ax1 = plt.subplot(111)

# グラフの上下左右に目盛線を付ける。
ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')

# 軸のラベルを設定する。
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# スケールの設定をする。
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 4)

# データプロットする。
ax1.contourf(X, Y, Z, cmap='coolwarm')
ax1.scatter(class_0[0], class_0[1], label='class=0', edgecolors='black')
ax1.scatter(class_1[0], class_1[1], label='class=1', edgecolors='black')
ax1.scatter(class_2[0], class_2[1], label='class=2', edgecolors='black')
plt.text(0.5, 2.2, '$\ R^{2}=$' + str(round(r2, 2)), fontsize=20)

plt.legend()

# グラフを表示する。
plt.show()
# plt.close()
# ----------------------------------------------------------



import glob
import os
import cv2
import numpy as np

def root_node_adjuster(dir):
    path_list = glob.glob(dir + '\*.png')                    # 指定されたディレクトリ内の.pngファイルを取得

    h_list = []                                              # 全画像の高さサイズリスト初期化
    w_list = []                                              # 全画像の幅サイズリスト初期化
    root_w_list = []                                         # 全画像のルートノード幅リスト初期化
    root_c_list = []                                         # 全画像のルートノード中心位置リスト初期化
    img_list = []                                            # 画像リスト初期化

    for i in range(len(path_list)):                          # 全画像のサイズとルート位置情報を取得するループ
        img = cv2.imread(path_list[i], 1)                    # カラー画像として読み込み
        img_list.append(img)
        h, w, ch = img.shape[:3]                             # 縦(h)横(w)画像サイズを取得
        h_list.append(h)                                     # hをリストに追加
        w_list.append(w)                                     # wをリストに追加

        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # 二値化のためのグレースケール化
        ret, i_binary = cv2.threshold(img_g,                 # 二値化処理
                                      250,                   # 閾値（この値以上が白)
                                      255,                   # 画像の最大輝度値
                                      cv2.THRESH_BINARY)     # 実行アルゴリズム（単純二値化）
        line = i_binary[50, :]                               # ルートノードのボックス部分を横方向にスライス
        index = np.where(line == 0)                          # 0と一致する指標を検索
        index = np.array(list(index)).ravel()                # 1D配列化
        root_w = index[-1] - index[0]                        # ルートノードの幅
        root_c = int(index[0] + root_w / 2)                  # ルートノードの幅方向中心座標
        root_w_list.append(root_w)                           # root_wをリストに追加
        root_c_list.append(root_c)                           # root_cをリストに追加

    h_max = np.max(h_list)                                   # 全画像の中で最大高さを算出
    w_max = np.max(root_c_list) * 2                          # 背景画像のサイズを設定(ルートノードが最も右にあるものを中心にする)
    size = h_max, w_max, 3

    for j in range(len(path_list)):                          # 全画像(決定木)のルートノード位置を補正するループ
        img_out = np.full(size, 255)                         # 出力するベース画像を白紙にする
        img_roi = img_list[j]                                # 決定木画像(カラー)をリストから取り出す
        calibration = int((w_max / 2) - root_c_list[j])      # 幅方向補正量

        # ベースの白紙画像にルートノードで位置補正した決定木画像を貼り付ける
        img_out[0:h_list[j], calibration:calibration + w_list[j]] = img_roi

        file = os.path.basename(path_list[j])                # 拡張子ありファイル名を取得
        name, ext = os.path.splitext(file)                   # 拡張子なしファイル名と拡張子を取得
        out_path = os.path.join(*[dir, 'cal_' + name + ext]) # 保存パスを作成
        cv2.imwrite(out_path, img_out)                       # 補正後の画像を保存
    return

root_node_adjuster('dir')