
import os
import json
import copy
import random

import pandas as pd
import datetime
import math
import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib
from palettable.colorbrewer.qualitative import Set2_7
colors = Set2_7.mpl_colors

matplotlib.use('TkAgg')


def print_regression(y_value, label):
    regres = [i for i in y_value if i >= 1]
    print(f'{label} regression No: ', len(regres))
    print(f'{label} All No ', len(y_value))


if __name__ == '__main__':
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
    ax.grid(axis='x', color="0.9", linestyle='-', linewidth=1)
    # put the grid behind
    ax.set_axisbelow(True)

    ##################################################### data ######################
    # Enter Your Data Here
    #################################################################################

    size = 40
    plt.scatter(_x, _y, label='', marker='*', s=size, color=colors[1])
    plt.scatter(_x, _y, label='', marker='v', s=size, color=colors[0])
    plt.scatter(_x, _y, label='', marker='x', s=size, color=colors[2])

    # print_regression()
    # print_regression()
    # print_regression()

    plt.axhline(1, linewidth=3, linestyle='-', color='black')
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel('PostgreSQL Runtime (s) [log]')
    plt.ylabel('Normalized Runtime [log]')
    plt.legend()
    plt.title('')
    plt.tight_layout()
    plt.show()
    # plt.savefig('../Figs/Scatter_plot.pdf')
