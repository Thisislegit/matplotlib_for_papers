import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Set2_7

# Since the code provided by the user does not include data to be plotted,
# I'm going to simulate some data that could resemble what's shown in the uploaded image.
# I will also set up the figure to have 1 row and 4 columns of subplots as requested.

# Simulating data
import numpy as np

# Assume there are 3 series for each subplot
np.random.seed(0)  # For reproducibility
x_values = [np.linspace(0, 10, 100), np.linspace(0, 20, 200), np.linspace(0, 20, 200), np.linspace(0, 8, 80)]
y_values = [np.random.rand(100) + i for i in range(3)]
y_values += [np.random.rand(200) + i for i in range(3)]
y_values += [np.random.rand(200) + i for i in range(3)]
y_values += [np.random.rand(80) + i for i in range(3)]

# Normalize the data as per the graph
y_values = [y / (i + 1) for i, y in enumerate(y_values)]

# Smooth the data to resemble the chart
def smooth(y, box_pts):
    box = np.ones(box_pts) / box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

y_values = [smooth(y, 5) for y in y_values]

# Define the colors for the plots
colors = Set2_7.mpl_colors

# Set the params for large, clear, visible fonts
params = {
    'axes.labelsize': 15,
    'font.size': 15,
    'legend.fontsize': 15,
    'xtick.labelsize': 15,
    'ytick.labelsize': 15,
    'text.usetex': False,
    'figure.figsize': [18, 4.5]  # Modified to make the font larger and clearer
}
plt.rcParams.update(params)

# Creating a 1x4 grid of subplots
fig, axs = plt.subplots(1, 4, figsize=(20, 5))  # Increased figure size for clarity

# Iterate over the created axes to plot the simulated data
for i, ax in enumerate(axs.flat):
    # Plot each of the 3 series
    for j in range(3):
        ax.plot(x_values[i], y_values[i * 3 + j], color=colors[j])

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
labels = ['Balsa', 'Bao', 'LEON']
fig.legend(labels, loc='upper center', ncol=3, frameon=False)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust the layout to make room for the legend
plt.show()
