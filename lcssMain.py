#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Athul
# @Date:   2016-02-23 16:00:11
# @Last Modified by:   Athul
# @Last Modified time: 2016-03-22 11:16:00
from __future__ import division
import numpy as np
import scipy.io
from lcs import rlcs as rlcs
import matplotlib.pyplot as plt
plt.style.use('ggplot')

plotDir = './'

# ============================ Loading neuronal data here ===============
X = np.load('sample-data/X.npy')
Y = np.load('sample-data/Y.npy')

# At the end of loading your data, Have query as X and reference as Y
# Both X and Y are numpy arrays
# In 1D case, both will be vectors
# in multidimensional, rows of X and Y denote each sample.
# and columns denote feature dimension
# ======================== RLCS start here ======================
tau_dist = 0.005
score, diag, cost = rlcs.rlcs(X, Y, tau_dist= tau_dist,  delta=0.5)

segment = rlcs.backtrack(X, Y, score, diag, cost)
lenSeg = segment.shape[0]

# ========================= Plots here ===========================
# Plot the score matrix
fig, ax = rlcs.plotLCS(segment, X, Y)

ax.set_xlabel('query')
ax.set_ylabel('reference')
ax.set_title('Match of signals after backtrack with dist_thres ' + str(tau_dist))

fig.savefig(plotDir+'rlcsMain_backtrack.eps')

plt.show()