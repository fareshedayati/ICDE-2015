# Author: Arnaud Joly
import os
import operator
import numpy as np
import pandas as pd
import prettyplotlib as ppl
import matplotlib.pyplot as plt

x = np.array([1, 2, 10])


measures = {
    "sparse": np.array([2.6, 5.3, 21.1]),
    "dense": np.array([76.8, 134.1, 472.174]),
    "sparse unrestricted depth": 68.89 * np.ones_like(x),
    "dense unrestricted depth": 974.68 * np.ones_like(x),
}


plt.figure()
for label in measures:
    if "unrestricted" in label:
        ppl.plot(x, measures[label], label=label)
    else:
        ppl.plot(x, measures[label], "-o", label=label)



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

ax.set_xlim(0, np.max(x)+1)

ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax.set_xlabel("Maximal depth")
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
plt.savefig("images/depth.pdf")
