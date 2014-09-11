# Author: Arnaud Joly
import os
import operator
import numpy as np
import pandas as pd
import prettyplotlib as ppl
import matplotlib.pyplot as plt


dataframe = pd.read_csv("density.csv")
mean_chrono = dataframe.groupby("density").mean()
std_chrono = dataframe.groupby("density").std()

plt.figure()
for label in ["sparse", "dense"]:
    plt.errorbar(mean_chrono.index, mean_chrono[label], std_chrono[label],
                 label=label)



ax = plt.gca()
for loc, spine in ax.spines.items():
    if loc in ['left','bottom']:
        spine.set_position(('outward', 10)) # outward by 10 points
        # spine.set_smart_bounds(True)

    elif loc in ['right','top']:
        # spine.set_visible(False)
        spine.set_color('none') # don't draw spine

    else:
        raise ValueError('unknown spine location: %s'%loc)

ax.set_xlim(0., 0.51)

ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax.set_xlabel("Density")
ax.set_ylabel("Time[s]")
# ax.xaxis.set_major_locator(MaxNLocator(6, prune=None))
# ax.yaxis.set_major_locator(MaxNLocator(6, prune=None))

# Sort legend labels
handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=operator.itemgetter(1))
if hl:
    handles2, labels2 = zip(*hl)
    legend = ax.legend(handles2, labels2, loc="best")
    legend.get_frame().set_alpha(0.5)
    legend.get_frame().set_edgecolor('white')

plt.tight_layout()

if not os.path.exists("images"):
    os.makedirs("images")
plt.savefig("images/density.pdf")
