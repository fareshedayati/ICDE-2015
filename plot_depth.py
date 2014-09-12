# Author: Arnaud Joly
import os
import operator
import numpy as np
import pandas as pd
import prettyplotlib as ppl
import matplotlib.pyplot as plt

from prettyplotlib.colors import set2

x = np.array([1, 2, 10, "unrestricted"])

ind = np.arange(len(x))
width = 0.35       # the width of the bars

measures = {
    "sparse": np.array([2.6, 5.3, 21.1, 68.89]),
    "dense": np.array([76.8, 134.1, 472.174, 974.68]),
}


fig, ax = plt.subplots(1)
plt.bar(ind, measures["sparse"], width, color=set2[0], label="sparse")
plt.bar(ind + width, measures["dense"], width, color=set2[1], label="dense")

# for label in measures:
#     if "unrestricted" in label:
#         ppl.plot(x, measures[label], label=label)
#     else:
#         ppl.plot(x, measures[label], "-o", label=label)

#     ppl.bar(mean_chrono.index, mean_chrono[label], yerr=std_chrono, label=label)


ax = plt.gca()
for loc, spine in ax.spines.items():
    if loc in ['left','bottom']:
        spine.set_position(('outward', 10)) # outward by 10 points
        spine.set_smart_bounds(True)

    elif loc in ['right','top']:
        # spine.set_visible(False)
        spine.set_color('none') # don't draw spine

    else:
        raise ValueError('unknown spine location: %s'%loc)

ax.set_xticks(ind+width)
ax.set_xticklabels(x)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax.set_xlabel("Maximal depth")
ax.set_ylabel("Time [s]")

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
plt.savefig("images/depth.pdf")
