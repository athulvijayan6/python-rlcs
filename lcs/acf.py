#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Athul
# @Date:   2016-02-03 11:33:25
# @Last Modified by:   Athul
# @Last Modified time: 2016-02-04 14:27:47
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def window(x, nhat, width, type='rectangular'):
    frame = x[nhat-width:nhat]
    if type=="rectangular":
        return frame

def ccf(x, y, max_lag=-1, ax=None, title='CACF'):
    if y.size < x.size:
        z = np.zeros(x.size - y.size)
        y = np.concatenate([y, z])
    if max_lag == -1:
        max_lag = np.absolute(y.size - x.size)
    xmu = np.mean(x)
    ymu = np.mean(y)
    sx  = np.std(x)
    sy  = np.std(y)
    n = x.size
    ccfHat = np.zeros((max_lag + 1))
    for l in xrange(max_lag+1):
        num = 0
        for i in xrange(n):
            num += (x[i] - xmu)*(y[i+l] - ymu)
        num = num/(n*sx*sy)
        ccfHat[l] = num
    if ax != None:
        lags = np.arange(ccfHat.size)
        ax.scatter(lags, ccfHat, s=15, color='red')
        ax.vlines(lags, np.zeros(ccfHat.size), ccfHat, alpha=0.4)
        ax.set_xlim([-5, ccfHat.size+5])
        ax.set_ylim([-1.2, 1.2])
        ax.set_xlabel('lag')
        ax.set_ylabel('CACF')
        ax.set_title(title)
        return ccfHat, ax
    else:
        return ccfHat




