import numpy as np
import random
import math

# ヘッブ則
def hebbLearn(patterns):
    length = patterns.shape[1]
    weights = np.zeros((length, length))
    for pattern in patterns:
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                weights[i][j] += pattern[i] * pattern[j]
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            weights[i][j] /= length
            weights[j][i] = weights[i][j]
    return weights

# 学習した重みを使ってパタ－ンを想起する
def associate(input_state, weights, iterateNum):
    length = len(input_state)
    state = input_state.copy()
    for i in range(0, iterateNum):
        index = random.randint(0, length - 1)
        a = sum([weights[index][i] * state[i] for i in range(0, length)])
        state[index] = threshold(a)
    return state

# 可視化のためにn^2次元ベクトルをn*n行列に変換する
def deserialize(data):
    size = round(math.sqrt(len(data)))
    matrix = np.zeros((size, size), dtype=int)
    for i in range(0, size):
        matrix[i] = data[size * i : size * (i + 1)]
    return matrix

# 2データ間の距離
def distance(data1, data2):
    return sum([abs(data1[i] - data2[i]) for i in range(0, len(data1))]) / 2
