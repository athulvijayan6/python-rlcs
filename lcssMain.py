#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Athul
# @Date:   2016-02-23 16:00:11
# @Last Modified by:   Athul
# @Last Modified time: 2016-04-06 10:40:53
from __future__ import division
import numpy as np
import scipy.io
from lcs import rlcs as rlcs
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Location to save the plots
plotDir = './'

# ******************** Loading data here ***********************
X = np.load('sample-data/X.npy')
Y = np.load('sample-data/Y.npy')

# At the end of loading your data, Have query as X and reference as Y
# Both X and Y are numpy arrays
# In 1D case, both will be vectors
# in multidimensional, rows of X and Y denote each sample.
# and columns denote feature dimension

# ********************** RLCS start here ************************
tau_dist = 0.005
# do RLCS
score, diag, cost = rlcs.rlcs(X, Y, tau_dist= tau_dist,  delta=0.5)

# get score of subsequence set
segment = rlcs.backtrack(X, Y, score, diag, cost)
lenSeg = segment.shape[0]

# Retrieve the matched segments
score_thres = 1e-4        # When score goes below this, a subsequence ends.
len_thres = 10            # Return only segments longer than len_thres samples.
xSegs, ySegs = rlcs.getSoftSegments(segment, X, Y, score_thres=score_thres, len_thres=len_thres)

# ************************ Plots ********************************

# ===============Find the longest subsequence and plot them ======
# Obviously, plotting subsequence is only for 1D data
fig, ax = plt.subplots()
lens = [i.shape[0] for i in xSegs]
idx = lens.index(max(lens))
xseg, yseg = xSegs[idx], ySegs[idx]ax.plot(xrange(xseg.size), xseg)
ax.plot(xrange(yseg.size), yseg)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Matched signals for rlcs with dist_thres ' + str(tau_dist))
fig.savefig(plotDir+'rlcsMain_getSegs.eps')

# ====================== Plot the score matrix =====================
fig, ax = rlcs.plotLCS(segment, X, Y)
ax.set_xlabel('query')
ax.set_ylabel('reference')
ax.set_title('Match of signals after backtrack with dist_thres ' + str(tau_dist))
fig.savefig(plotDir+'rlcsMain_backtrack.eps')


plt.show()