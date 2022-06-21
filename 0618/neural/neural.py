
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
    """
    重み付き線形和の関数。
    ※1データ分、つまりxとweightsは「一次元リスト」という前提。
    - 引数：
    x： 入力データをリスト値（各要素はfloat値）で指定する。
    weights： 重みをリスト値（各要素はfloat値）で指定する。
    bias： バイアスをfloat値で指定する。
    - 戻り値：
    線形和の計算結果をfloat値で返す。
    """
    linear_sum = 0.0
    for x_i, w_i in zip(x, weights):
        linear_sum += x_i * w_i  # iは「番号」（数学は基本的に1スタート）
        # print(f'x_i({x_i})×w_i({w_i})＋', end='')
    linear_sum += bias
    # print(f'b({bias})', end='')
    return linear_sum

# 線形代数を使う場合のコード例：
# linear_sum = np.dot(x, weights) + bias

def sum_der(x, weights, bias, with_respect_to='w'):
    """
    重み付き線形和の関数の偏導関数。
    ※1データ分、つまりxとweightsは「一次元リスト」という前提。
    - 引数：
    x： 入力データをリスト値で指定する。
    weights：  重みをリスト値で指定する。
    bias: バイアスをfloat値で指定する。
    with_respect_to: 何に関して偏微分するかを指定する。
        'w'＝ 重み、'b'＝ バイアス、'x'＝ 入力。
    - 戻り値：
    with_respect_toが'w'や'x'の場合はリスト値で、'b'の場合はfloat値で
        線形和の偏微分の計算結果（偏微分係数）を返す。
    """    
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
    """
    順伝播を行う関数。
    - 引数：
    (layers, weights, biases)： モデルを指定する。
    x： 入力データを指定する。
    cache_mode： 予測時はFalse、訓練時はTrueにする。これにより戻り値が変わる。
    - 戻り値：
    cache_modeがFalse時は予測値のみを返す。True時は、予測値だけでなく、
        キャッシュに記録済みの線形和（Σ）値と、活性化関数の出力値も返す。
    """

    cached_sums = []  # 記録した全ノードの線形和（Σ）の値
    cached_outs = []  # 記録した全ノードの活性化関数の出力値

    # まずは、入力層を順伝播する
    print(f'■第1層（入力層）-全て（{len(x)}個）の特徴量：')
    print(f'　●入力データ： ', end='')
    cached_outs.append(x)  # 何も処理せずに出力値を記録
    print(f'何もしない＝out({x})')
    next_x = x  # 現在の層の出力（x）＝次の層への入力（next_x）

    # 次に、隠れ層や出力層を順伝播する
    SKIP_INPUT_LAYER = 1
    for layer_i, layer in enumerate(layers):  # 各層を処理
        if layer_i == 0:
            continue  # 入力層は上で処理済み

        # 各レイヤーのノードごとに処理を行う
        sums = []
        outs = []
        for node_i in range(layer):  # 層の中の各ノードを処理
            print(f'■第{layer_i+1}層-第{node_i+1}ノード：')

            # ノードごとの重みとバイアスを取得
            w = weights[layer_i-SKIP_INPUT_LAYER][node_i]
            b = biases[layer_i-SKIP_INPUT_LAYER][node_i]

            # 1つのノードの処理（1）： 重み付き線形和
            print(f'　●重み付き線形和： ', end='')
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