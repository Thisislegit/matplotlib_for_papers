import os
import json
import copy
# import pandas as pd
import datetime
import math
# import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import matplotlib
import numpy as np
import re
import scipy
import scipy.ndimage
import random
from palettable.colorbrewer.qualitative import Set2_7
colors = Set2_7.mpl_colors


def perc(data):
    median = np.zeros(data.shape[1])
    perc_25 = np.zeros(data.shape[1])
    perc_75 = np.zeros(data.shape[1])
    for i in range(0, len(median)):
        median[i] = np.median(data[:, i])
        perc_25[i] = np.percentile(data[:, i], 0)
        perc_75[i] = np.percentile(data[:, i], 100)
    return median, perc_25, perc_75


if __name__ == "__main__":
    params = {
        'axes.labelsize': 15,
        'font.size': 15,
        'legend.fontsize': 15,
        'xtick.labelsize': 15,
        'ytick.labelsize': 15,
        'text.usetex': False,
        'figure.figsize': [4.5, 4.5]
    }
    plt.rcParams.update(params)
    fig, ax = plt.subplots(1, 1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.tick_params(axis='x', direction='out')
    ax.tick_params(axis='y', length=0)
    for spine in ax.spines.values():
        spine.set_position(('outward', 5))
    ax.grid(axis='y', color="0.9", linestyle='-', linewidth=1)
    # put the grid behind
    ax.set_axisbelow(True)
    # optional
    plt.plot(np.arange(30), [1]*len(np.arange(30)),
             linewidth=3, linestyle='-', color='black')



########################################################################################################
# Enter Your Data Here
########################################################################################################


    all__ratio = []
    minLen = np.Inf
    for _ratio in [_abs_ratio_1, _abs_ratio_2, _abs_ratio_3]:
        if len(_ratio) < minLen:
            minLen = len(_ratio)
        all__ratio.append(np.asarray(_ratio).reshape((-1, 1)))
    all__ratio = np.concatenate([i[:minLen]
                                    for i in all__ratio], axis=1)
    median, low_plot_data, up_plot_data = perc(
        all__ratio.T, datatype='')
    
    # Smooth for better visualization
    # median = scipy.ndimage.gaussian_filter1d(
    #     median, sigma=0.8).reshape((-1, 1))

    plt.plot(_time_1[:minLen], median - 0.1, linestyle='-', label='',
             linewidth=3, color=colors[1])
    plt.fill_between(_time_1[:minLen], low_plot_data, up_plot_data,
                     alpha=0.25, linewidth=0, color=colors[1])
    plt.xlabel('Training Time (h)')
    plt.ylabel('Normalized Runtime')
    plt.legend()
    frame = plt.legend().get_frame()
    frame.set_facecolor('1.0')
    frame.set_edgecolor('1.0')
    plt.title('')
    plt.tight_layout()
    # plt.ylim(0, 9)
    # plt.xlim(0, 12)
    plt.show()
    # plt.savefig("../Figs/Curve.pdf")
