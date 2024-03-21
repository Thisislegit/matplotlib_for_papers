import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Set2_7

# Define the colors for the plots
colors = Set2_7.mpl_colors

# Set the params for large, clear, visible fonts
params = {
    'axes.labelsize': 15,
    'font.size': 15,
    'legend.fontsize': 17,
    'xtick.labelsize': 15,
    'ytick.labelsize': 15,
    'text.usetex': False,
    'figure.figsize': [18, 4.5]  # Modified to make the font larger and clearer
}
plt.rcParams.update(params)

# Creating a 1x4 grid of subplots
fig, axs = plt.subplots(1, 4, figsize=(20, 5))  # Increased figure size for clarity



import job.data, ext.codes.data, tpch.data, stack.data
data_list = [job.data, 
             ext.codes.data, 
             stack.data, 
             tpch.data]

# Iterate over the created axes to plot the simulated data
for i, ax in enumerate(axs.flat):
    # Plot each of the 3 series
    # for j in range(3):
    #     ax.plot(x_values[i], y_values[i * 3 + j], color=colors[j])
    # from job.data import get_data
    data_list[i].get_data(ax)
    
    # Making the same aesthetics adjustments as provided
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
    ax.set_axisbelow(True)

# Adding a legend above the subplots as requested
labels = ['Balsa', 'Bao', 'LEON', 'LEON+']
# set legend color

from matplotlib.lines import Line2D
# fig.legend(labels, loc='upper center', ncol=4, frameon=False)
custom_lines = [Line2D([0], [0], color=colors[2], lw=3),
                Line2D([0], [0], color=colors[0], lw=3),
                Line2D([0], [0], color=colors[1], lw=3),
                Line2D([0], [0], color=colors[3], lw=3)]

# Creating legend with custom handles and labels
fig.legend(custom_lines, labels, loc='upper center', ncol=4, frameon=False)
# plt.tight_layout()
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust the layout to make room for the legend
plt.savefig('curves.pdf')
# plt.show()
