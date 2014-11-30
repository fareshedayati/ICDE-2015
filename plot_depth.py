# Author: Arnaud Joly
import os
import operator
import numpy as np
#import pandas as pd
import numpy as np
from math import log
import prettyplotlib as ppl
import matplotlib.pyplot as plt
from math import log10
from prettyplotlib.colors import set2


# (96367, 20025) (96367,)
# 0.0143853519202
# max_depth =  1
# 6.20393419266
# ...
# 5486.93346095
# ----------------------
# max_depth =  3
# 20.425470829
# ...
# 16067.193238
# ----------------------
# max_depth =  5
# 32.995303154
# ...
x = [1, 3, 5, 7]
s1 = [6.20393419266, 20.425470829, 32.995303154, 36.9800310135]
s2 = [5486.93346095, 16067.193238, 19052.12338, 33460.0165029]
filename = "cup"

# x = [1, 2, 5, 10, "unrestricted"]
# s1 = [1.457447052, 2.3896651268, 5.33618307114, 9.51832604408, 28.1223289967]
# s2 = [273.675136089, 354.805790901, 812.156574011, 1236.3957541, 1637.73248761]
# # s1 = [log(s)/log(10) for s in s1]
# # s2 = [log(s)/log(10) for s in s2]
# filename = "20news"

# x = [1, 3, 5, 7, 9, 20, 30, "unrestricted"]
# s1 = [0.07022213935852051, 0.1575300693511963, 0.24751591682434082, 0.38076114654541016, 0.6094520092010498, 1.7255690097808838, 1.8654630184173584, 1.8886289596557617]
# s2 = [0.16304802894592285, 0.35780787467956543, 0.529296875, 0.6921160221099854, 0.8160340785980225, 1.0601880550384521, 1.0887351036071777, 1.0804028511047363]
# (32561, 145)
# 0.112376546028
# filename = "adult"

# x = [1, 3, 5, 7, 9, 20, "unrestricted"]
# s1 = [0.007455110549926758, 0.022521018981933594, 0.0634310245513916, 0.09974098205566406, 0.163316011428833, 0.17904401683807373,  0.18471908569335938]
# s2 = [0.008224010467529297, 0.019938945770263672, 0.04503512382507324, 0.056620121002197266, 0.07207801971435547, 0.07216701316833496, 0.0723731517791748]
# filename = "tic"
# (4000, 85)
# 0.444329411765







x = np.array(x)
ind = np.arange(len(x))
width = 0.35       # the width of the bars

measures = {
    "sparse": np.array(s1),
    "dense": np.array(s2),
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

for rect in ax.patches:
    height = rect.get_height()
    ax.text(rect.get_x()+rect.get_width()/2., 1.025*height, round(height, 2),
                ha='center', va='bottom')

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
plt.savefig("images/"+filename+".pdf")
