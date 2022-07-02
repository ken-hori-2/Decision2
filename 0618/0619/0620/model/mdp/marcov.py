import numpy as np


class Solver(object):

    # def __init__(self, P: np.ndarray, cond_li: [str], current: int):
    def __init__(self, P: np.ndarray, cond_li, current):

        rows, cols = P.shape
        eps = 1e-8
        # 推移行列は正方行列でなければならない。
        if rows != cols:
            raise Exception(f'P must be square. <{(rows, cols)=}>')
        elif rows - 1 < current:
            raise Exception(f'must be rows - 1 >= current. <{(rows, current)=}>')
        elif np.any(np.abs(P.sum(axis=1) - 1) > eps):    # == にできないのは、誤差的な問題
            raise Exception(f'P.sum(axis=1) must be 1. <{P.sum(axis=1)=}>')

        self.P, self.cond_li = P, cond_li
        self.α = α = np.zeros(rows)
        α[current] = 1


    def get_result(self) : # -> {str: str, str: float}:

        α, P = self.α, self.P
        # 明後日の結果を予測する。
        mat = α @ P @ P

        return {'状態': self.cond_li[np.argmax(mat)], '確率': np.max(mat)}



if __name__ == '__main__':

    # P = np.array([[.5,.4,.1],
    #               [.3,.4,.3],
    #               [.2,.3,.5]])
    P = np.array([[1/2,1/3,1/6],
                  [1/6,1/3,1/2],
                  [1/6,1/3,1/2]])
    # cond_li = ['良い', '普通', '悪い']
    cond_li = ['晴れ', '曇り', '雨']
    current = 0 #2

    svr = Solver(P, cond_li, current)
    print(f'result: {svr.get_result()}')