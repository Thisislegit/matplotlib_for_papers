import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib
from palettable.colorbrewer.qualitative import Set2_7
colors = Set2_7.mpl_colors

if __name__ == '__main__':
    params = {
        'axes.labelsize': 20,
        'font.size': 15,
        'legend.fontsize': 15,
        'xtick.labelsize': 20,
        'ytick.labelsize': 20,
        'text.usetex': False,
        'figure.figsize': [20, 2]
    }
    # plt.axhline(10, linewidth=3, linestyle='-', color='grey')
    # fig, ax = plt.subplots(1, 1)
    # plt.grid(axis='y', visible=True, which='major', linestyle='-')
    plt.grid(axis='y', color="0.9", linestyle='-', linewidth=1)
    # ax.grid(axis='x', color="0.9", linestyle='-', linewidth=1)
    
    plt.rcParams.update(params)

    # matplotlib.rcParams.update({'font.size': 15})
    # matplotlib.rcParams.update({'legend.fontsize': 10})
    # fig = plt.figure(figsize=(10, 3))


    all_query = np.asarray([6, 8, 9, 10, 16, 17, 18, 19, 20, 25, 26, 30])
    x = np.arange(len(all_query)+1)  # x轴刻度标签位置

    PG = np.concatenate((PG, np.mean(PG).reshape((-1))))
    Our_data = np.concatenate((Our_data, np.mean(Our_data).reshape((-1))))
    CostEst = np.concatenate((CostEst, np.mean(CostEst).reshape((-1))))
    CardEst = np.concatenate((CardEst, np.mean(CardEst).reshape((-1))))

    width = 0.2  # 柱子的宽度
    plt.bar(x - 2*width, PG, width, label='', fc=colors[0])
    plt.bar(x - width, CardEst, width, label='', fc=colors[3])
    plt.bar(x, CostEst, width, label='', fc=colors[2])
    plt.bar(x + width, Our_data, width, label='', fc=colors[1])
    plt.xlim(-1, 13)
    plt.xlabel('')
    plt.ylabel('')
    plt.yscale('log')
    plt.title(''),

    # x_ = [i for i in range(-1, 34)]
    # y_ = [1 for i in range(len(x_))]
    # plt.plot(x_, y_, color='red', linewidth=1, linestyle=':')
    # x轴刻度标签位置不进行计算
    plt.xticks(x, labels=[6, 8, 9, 10, 16, 17, 18, 19, 20, 25, 26, 30, "AVE"])
    # plt.legend(loc=9)
    # plt.legend(loc='upper center', fontsize=10, mode='expand', ncol=2)
    plt.legend(loc='upper center',
               ncol=4, bbox_to_anchor=(0.5, 1.3))
    plt.tight_layout()
    # plt.savefig('../Figs/all_results_1.pdf', bbox_inches='tight')
    plt.show()

   