import matplotlib.pyplot as plt
import numpy as np

import os
import json
import copy
import random

import pandas as pd
import datetime
import math
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

import re
from palettable.colorbrewer.qualitative import Set2_7
colors = Set2_7.mpl_colors

Leon_color = colors[1]
Bao_color = colors[0]

params = {
    'axes.labelsize': 15,
    'font.size': 15,
    'legend.fontsize': 15,
    'xtick.labelsize': 15,
    'ytick.labelsize': 15,
    'text.usetex': False,
    'figure.figsize': [4.5, 3.5]
}
plt.rcParams.update(params)




tick_label = ['30', '40', '50']
# plt.ylim(0,2)

# First, set the plt.rcParams as provided
plt.rcParams.update(params)

# Create the figure and subplots based on the provided layout
fig, axs = plt.subplots(1, 2, figsize=(4.5, 3.5))
# plt.grid(axis='y', color="0.9", linestyle='-', linewidth=1)


# Set up the bar parameters and positions
total_width, n = 0.7, 3
width = total_width / n
x = [1, 2, 3]

# Labels for the bars
tick_label0 = ['40', '50', '60']

# Plotting the bars and setting the title for the first subplot


new_pg = [0.93, 0.88, 0.74]
bars1 = axs[0].bar(x, new_pg, width=width, label='Static', fc=colors[0], hatch='/')
for i in range(len(x)):
    x[i] = x[i] + width
new_leon = [0.63, 0.55, 0.52]
bars2 = axs[0].bar(x, new_leon, width=width, label='Dynamic', fc=colors[2], hatch='x', tick_label=tick_label0)


# Remove the y ticks and labels
# axs[0].set_yticks([])
axs[0].set_xlabel("# of Q-Template")
axs[0].set_ylabel('Normalized Runtime')


# Repeat the process for the second subplot
tick_label1 = ['0.1%', '1%', '10%']
new_pg = [1.4, 1.02, 0.95]
x = [1, 2, 3]  # Reset x position for the next set of bars
bars1 = axs[1].bar(x, new_pg, width=width, label='Bottom Up', fc=colors[1], hatch='-')
for i in range(len(x)):
    x[i] = x[i] + width
new_leon = [0.67, 0.56, 0.53]
bars2 = axs[1].bar(x, new_leon, width=width, label='Top Down', fc=colors[3], hatch='+', tick_label=tick_label1)

axs[1].set_xlabel("Exploration Rate")

from matplotlib.patches import Patch

# Create custom legend handles with hatching
custom_lines = [
    Patch(facecolor=colors[2], label='Sta', hatch='/', edgecolor='black'),
    Patch(facecolor=colors[0], label='Dyn', hatch='x', edgecolor='black'),
    Patch(facecolor=colors[1], label='BU', hatch='-', edgecolor='black'),
    Patch(facecolor=colors[3], label='TD',hatch='+', edgecolor='black')
]

# Creating legend with custom handles and labels
fig.legend(custom_lines, ['Sta', 'Dyn', 'BU', 'TD'], ncol=4, columnspacing=1.0, frameon=False, loc='upper center', bbox_to_anchor=(0.5, 1.05))

# Apply tight layout and show plot
plt.tight_layout()
plt.show()
