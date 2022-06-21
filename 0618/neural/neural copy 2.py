import numpy as np

# ニューラルネットワークは3層構成
layers = [
    2,  # 入力層の入力（特徴量）の数
    3,  # 隠れ層1のノード（ニューロン）の数
    1]  # 出力層のノードの数

# 重みとバイアスの初期値
weights = [
    [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], # 入力層→隠れ層1
    [[0.0, 0.0, 0.0]] # 隠れ層1→出力層
]
biases = [
    [0.0, 0.0, 0.0],  # 隠れ層1
    [0.0]  # 出力層
]

# モデルを定義
model = (layers, weights, biases)

# 仮の訓練データ（1件分）を準備
x = [0.05, 0.1]  # x_1とx_2の2つの特徴量

def summation(x, weights, bias):
    # 線形代数を使う場合のコード例：
    linear_sum = np.dot(x, weights) + bias
    return linear_sum

def sum_der(x, weights, bias, with_respect_to='w'):
    
    if with_respect_to == 'w':
        return x  # 線形和uを各重みw_iで偏微分するとx_iになる（iはノード番号）。
    elif with_respect_to == 'b':
        return 1.0  # 線形和uをバイアスbで偏微分すると1になる。
    elif with_respect_to == 'x':
        return weights  # 線形和uを各入力x_iで偏微分するとw_iになる。

import math

def sigmoid(x):
    """
    シグモイド関数。
    - 引数：
    x： 入力データをfloat値で指定する。
    - 戻り値：
    シグモイド関数の計算結果をfloat値で返す。
    """
    return 1.0 / (1.0 + math.exp(-x))

# 線形代数の場合はmathをnpに変える（事前にimport numpy as np）

def sigmoid_der(x):
    """
    シグモイド関数の（偏）導関数。
    - 引数：
    x： 入力データをfloat値で指定する。
    - 戻り値：
    シグモイド関数の（偏）微分の計算結果（微分係数）をfloat値で返す。
    """
    output = sigmoid(x)
    return output * (1.0 - output)

def identity(x):
    """
    恒等関数の関数。
    - 引数：
    x： 入力データをfloat値で指定する。
    - 戻り値：
    恒等関数の計算結果（そのまま）をfloat値で返す。
    """
    return x

def identity_der(x):
    """
    恒等関数の（偏）導関数。
    - 引数：
    x： 入力データをfloat値で指定する。
    - 戻り値：
    恒等関数の（偏）微分の計算結果（微分係数）をfloat値で返す。
    """
    return 1.0


#実装

def forward_prop(layers, weights, biases, x, cache_mode=False):
    
    

    # ノードごとの重みとバイアスを取得
    w = weights[layer_i-SKIP_INPUT_LAYER][node_i]
    b = biases[layer_i-SKIP_INPUT_LAYER][node_i]

    
    node_sum = summation(next_x, w, b)
    print(f'＝sum({node_sum})')

    # 1つのノードの処理（2）： 活性化関数
    if layer_i < len(layers)-1:  # -1は出力層以外の意味
        # 隠れ層（シグモイド関数）
        print(f'　●活性化関数（隠れ層はシグモイド関数）： ', end='')
        node_out = sigmoid(node_sum)
        print(f'sigmoid({node_sum})＝out({node_out})')
    else:
        # 出力層（恒等関数）
        print(f'　●活性化関数（出力層は恒等関数）： ', end='')
        node_out = identity(node_sum)
        print(f'identity({node_sum})＝out({node_out})')

    # 各ノードの線形和と（活性化関数の）出力をリストにまとめていく
    sums.append(node_sum)
    outs.append(node_out)

    # 各層内の全ノードの線形和と出力を記録
    cached_sums.append(sums)
    cached_outs.append(outs)
    next_x = outs  # 現在の層の出力（outs）＝次の層への入力（next_x）

    if cache_mode:
        return (cached_outs[-1], cached_outs, cached_sums)

    return cached_outs[-1]


# 訓練時の（1）順伝播の実行例
y_pred, cached_outs, cached_sums = forward_prop(*model, x, cache_mode=True)
# ※先ほど作成したモデルと訓練データを引数で受け取るよう改変した

print(f'cached_outs={cached_outs}')
print(f'cached_sums={cached_sums}')
# 出力例：
# cached_outs=[[0.05, 0.1], [0.5, 0.5, 0.5], [0.0]]  # 入力層／隠れ層1／出力層
# cached_sums=[[0.0, 0.0, 0.0], [0.0]]  # 隠れ層1／出力層（※入力層はない）