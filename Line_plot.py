import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import scipy
from scipy import ndimage

def plot_1(path_to_save, right, wrong):
    right_ = ndimage.gaussian_filter1d(right, sigma=2).tolist()
    wrong_ = ndimage.gaussian_filter1d(wrong, sigma=2).tolist()
    lth = len(right_)
    idx_right_ = [i for i in range(1, len(right) + 1)]
    idx_wrong_ = [i for i in range(1, len(wrong) + 1)]
    right = []
    wrong = []
    idx_right = []
    idx_wrong = []
    for i in range(0, lth, 5):
        right.append(right_[i])
        wrong.append(wrong_[i])
        idx_right.append(idx_right_[i])
        idx_wrong.append(idx_wrong_[i])

    plt.figure(figsize=(15, 6))
    # 参数设置参考文档：https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams
    plt.rcParams["font.size"] = 20
    # plt.rcParams['font.family'] = 'Times New Roman'

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html?highlight=grid#matplotlib.pyplot.grid
    plt.grid(visible=True, which='major', linestyle='-')
    plt.grid(visible=True, which='minor', linestyle='--', alpha=0.5)
    # plt.minorticks_on()

    # REMOVE DROPOUT FOR THIS PLOT TO APPEAR AS EXPECTED !!
    # DROPOUT INTERFERES WITH HOW THE SAMPLED SOURCES ARE PLOTTED
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot#matplotlib.pyplot.plot
    plt.plot(idx_right, right, 'o-.', color='red', label='Correct', linewidth=1, markersize=5)
    plt.plot(idx_wrong, wrong, 'o-.', color='blue', label='Wrong', linewidth=1)
    # plt.plot(idx_pred, prediction, 'o-.', color='limegreen', label='prediction sequence', linewidth=1)
    # o-  o--
    # plt.title("Comparing Var")
    plt.xlabel("Epoch")
    plt.ylabel("Uncertainty")
    plt.legend()    # loc=1 upper right

    plt.tight_layout()

    # plt.savefig(path_to_save + f"/Epoch_200.png")
    # plt.show()
    plt.close()

def plot_box():
    pass

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        files = f.readlines()
    right = []
    wrong = []
    for line in files:
        if 'mean' in line:
            pattern = re.compile(r'\d+\.?\d*')
            res = pattern.findall(line)
            if res and len(res) == 2:
                right.append(float(res[0]))
                wrong.append(float(res[1]))
    return right, wrong

if __name__ == "__main__":
    path_to_save = "output"
    # 读取文件中所有数据，注意CSV文件是
    right, wrong =  read_file('./data/var_3.txt')
    plot_1(path_to_save, right, wrong)