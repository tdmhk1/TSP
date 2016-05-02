import sys
import numpy as np
import TSP
import os

def tspfile_to_points(path):
    points = []
    with open(path, 'r') as f:
        for line in f.readlines():
            words = line.split(" ")
            if (len(words) > 1) and (words[1].isdigit()):
                points.append(np.array([float(words[2]), float(words[3])]))
    return np.array(points)

# 指定された.tspのファイルから点集合と距離行列をファイルへ書き出す
if __name__ == "__main__":
    path = sys.argv[1]
    points = tspfile_to_points(path)
    dist_matrix = TSP.calc_dist_matrix(points)
    filename = os.path.splitext(os.path.basename(path))[0]
    np.savetxt("points_"+filename+".txt", points)
    np.savetxt("dist_"+filename+".txt", dist_matrix)
