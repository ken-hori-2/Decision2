# データ前処理
import numpy as np
import pandas as pd

# データ可視化
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
# %matplotlib inline

# グラフの日本語表記対応
from matplotlib import rcParams
rcParams["font.family"]     = "sans-serif"
rcParams["font.sans-serif"] = "Hiragino Maru Gothic Pro"

# データセット読込
from sklearn.datasets import load_boston
boston = load_boston()

# DataFrame作成
df = pd.DataFrame(boston.data)
df.columns = boston.feature_names
df["MEDV"] = boston.target

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

""" モデル学習 """
# 変数定義
X = df[['LSTAT']].values  # 説明変数
y = df['MEDV'].values     # 目的変数（住宅価格の中央値）

# データ分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# ランダムフォレスト回帰
forest = RandomForestRegressor(n_estimators=100,
                               criterion='mse', 
                               max_depth=None, 
                               min_samples_split=2, 
                               min_samples_leaf=1, 
                               min_weight_fraction_leaf=0.0, 
                               max_features='auto', 
                               max_leaf_nodes=None, 
                               min_impurity_decrease=0.0, 
                               bootstrap=True, 
                               oob_score=False, 
                               n_jobs=None, 
                               random_state=None, 
                               verbose=0, 
                               warm_start=False, 
                               ccp_alpha=0.0, 
                               max_samples=None
                              )
# モデル学習
forest.fit(X_train, y_train)

# 推論
y_train_pred = forest.predict(X_train)
y_test_pred  = forest.predict(X_test)


""" グラフ可視化 """
# flatten：1次元の配列を返す、argsort：ソート後のインデックスを返す
sort_idx = X_train.flatten().argsort()

# 可視化用に加工
X_train_plot  = X_train[sort_idx]
Y_train_plot  = y_train[sort_idx]
train_predict = forest.predict(X_train_plot)

# 可視化
plt.scatter(X_train_plot, Y_train_plot, color='lightgray', s=70, label='Traning Data')
plt.plot(X_train_plot, train_predict, color='blue', lw=2, label="Random Forest Regression")    

# グラフの書式設定
plt.xlabel('LSTAT（低所得者の割合）')
plt.ylabel('MEDV（住宅価格の中央値）')
plt.legend(loc='upper right')
plt.show()