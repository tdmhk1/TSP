import numpy as np

def calc_dist_matrix(points):
    length = points.shape[0]
    matrix = np.zeros((length, length))
    for i in range(length):
        for j in range(i+1, length):
            matrix[i][j] = np.linalg.norm(points[i] - points[j])
            matrix[j][i] = matrix[i][j]
    return matrix

def calc_route_dist(dist_matrix, route):
    return sum([dist_matrix[route[i]][route[(i + 1) % len(route)]] for i in range(0, len(route))])

def energy_function(state_matrix, dist_matrix, A=1, B=1, C=1, D=1):
    length = len(state_matrix)
    row_energy = sum([state_matrix[x][i] * state_matrix[x][j] for x in range(length)
                      for i in range(length) for j in range(length) if j != i])
    col_energy = sum([state_matrix[x][i] * state_matrix[y][i] for i in range(length)
                     for x in range(length) for y in range(length) if y != x])
    matrix_energy = (np.sum(state_matrix) - length) ** 2
    dist_energy = sum([dist_matrix[x][y] * state_matrix[x][i] * (state_matrix[y][(i + 1) % length] + state_matrix[y][(i - 1) % length])
                       for x in range(length) for y in range(length) if y != x for i in range(length)])
    return (A / 2) * row_energy + (B / 2) * col_energy + (C / 2) * matrix_energy + (D / 2) * dist_energy

def find_route_greedy(dist_matrix, start_city=0):
    length = len(dist_matrix)
    city_set = {i for i in range(length)}
    present_city = start_city
    route = []
    route.append(present_city)
    city_set.discard(present_city)
    for i in range(length - 1):
        dist_city_pair = {dist_matrix[present_city][j]:j for j in city_set}
        present_city = dist_city_pair[min(dist_city_pair.keys())]
        route.append(present_city)
        city_set.discard(present_city)
    return route

import random
def calc_state_matrix(state_matrix, dist_matrix, iterateNum=10000, A=1, B=1, C=1, D=1, N=None, gain=1):
    state = state_matrix.copy()
    size = len(dist_matrix)
    size_square = size ** 2
    if N is None:
        N = size
    for i in range(0, iterateNum):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        row_activate = -A * (np.sum(state[row, :]) - state[row][col])
        col_activate = -B * (np.sum(state[:, col]) - state[row][col])
        matrix_activate = -C * (np.sum(state) - N)
        p, n = (col + 1) % size, (col - 1) % size
        dist_activate = -D * np.dot(dist_matrix[row, :], (state[:, n] + state[:, p]))
        activate = row_activate + col_activate + matrix_activate + dist_activate
        state[row][col] = sigmoid(activate, gain)
    return state

def sigmoid(u, u_0=0.02):
    return (1 + np.tanh(u / u_0)) / 2

def generate_initial_state(size):
    state = np.zeros((size, size))
    x = 1 / size
    for i in range(0, size):
        for j in range(0, size):
            noise = 0.2 * random.random() - 0.1
            state[i][j] = x + noise
    return state
