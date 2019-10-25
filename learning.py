#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:07:25 2019

@author: peng wang

a python/mne learning script
"""
# 1 envioronment test
# 1.1 import the needed packages
from mne import io

#1.2 import some packages
data_path = '/Users/wang/mne/sample_data/'
raw_fname = data_path + '/MNE-sample-data/MEG/sample/sample_audvis_filt-0-40_raw.fif'
raw = io.read_raw_fif(raw_fname, preload=False)
