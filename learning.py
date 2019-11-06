#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:07:25 2019

@author: peng wang

a python/mne learning script
"""
# 1 envioronment test
# =============================================================================
# # 1.1 try to load data with mne default
# from mne import io
# data_path = '/Users/wang/mne/sample_data/'
# raw_fname = data_path + '/MNE-sample-data/MEG/sample/sample_audvis_filt-0-40_raw.fif'
# raw = io.read_raw_fif(raw_fname, preload=False)
#
# =============================================================================

# =============================================================================
# #1.2 try to read, check and save a neuroscan .cnt file
# #1.2.1 prepare the needed packages
# import mne
# import os
# import matplotlib.pyplot as plt
# import numpy as np
# #1.2.2 load headers data
# fin = '/Volumes/pwang/5PL/1raw/ZouDX/cnt/ZouDX3/08.cnt'
# raw = mne.io.read_raw_cnt(fin, montage='deprecated', eog=(), misc=(), ecg=(), emg=(),
#                           data_format='int32', date_format='mm/dd/yy', preload=False,
#                           stim_channel=False, verbose=None)
# #1.2.3 get the data and then plot, to check whether int32 or int16 is more realistic
# tmp = raw[0, :]
# y = np.matrix.transpose(tmp[0])
# x = tmp[1]
# h = plt.plot(x[0:2000], y[0:2000], 'o')
# fout = '/Users/wang/Documents/5PL/2pro/ZouDX_cnt_3_08.raw.fif.gz'
# raw.save(fname=fout)
# =============================================================================

# =============================================================================
# #1.3 try to identify the files to be loaded, ugly nested loops
# import os
# basepath = '/Volumes/pwang/5PL/1raw/'
# for entry_level1 in os.listdir(basepath):
# #    print(os.path.join(basepath, entry_level1))
#     if os.path.isfile(os.path.join(basepath, entry_level1)) and \
#         entry_level1.endswith('.cnt'):
#         print(entry_level1, ' is a data file')
#     elif os.path.isdir(os.path.join(basepath, entry_level1)):
#         print(entry_level1, ' is a folder, checking inside ...')
#         for entry_level2 in os.listdir(os.path.join(basepath, entry_level1)):
# #            print(os.path.join(basepath, entry_level1, entry_level2))
#             if os.path.isfile(os.path.join(basepath, entry_level1, entry_level2)) and \
#                 entry_level2.endswith('.cnt'):
#                 print(entry_level2, ' is a data file')
#             elif os.path.isdir(os.path.join(basepath, entry_level1, entry_level2)):
#                 print(entry_level2, 'is a folder too, checking inside ...')
#                 for entry_level3 in os.listdir(os.path.join(basepath, entry_level1, entry_level2)):
#         #            print(os.path.join(basepath, entry_level1, entry_level2))
#                     if os.path.isfile(os.path.join(basepath, entry_level1, entry_level2, entry_level3)) and \
#                         entry_level3.endswith('.cnt'):
#                         print(entry_level3, ' is a data file')
#                     elif os.path.isdir(os.path.join(basepath, entry_level1, entry_level2, entry_level3)):
#                         print(entry_level3, 'is a folder too, checking inside ...')
#                         for entry_level4 in os.listdir(os.path.join(basepath, entry_level1, entry_level2, entry_level3)):
#                 #            print(os.path.join(basepath, entry_level1, entry_level2))
#                             if os.path.isfile(os.path.join(basepath, entry_level1, entry_level2, entry_level3, entry_level4)) and \
#                                 entry_level4.endswith('.cnt'):
#                                 print(entry_level4, ' is a data file')
#                             elif os.path.isdir(os.path.join(basepath, entry_level1, entry_level2, entry_level3, entry_level4)):
#                                 print(entry_level4, 'is a folder too, checking inside ...')
#
# =============================================================================

# =============================================================================
# #1.4 an example of os.walk
# import os
# from os.path import join, getsize
# basepath = '/Volumes/pwang/5PL/1raw/DuanXY'
# for root, dirs, files in os.walk(basepath):
#     print(root, "consumes",
#           sum(os.path.getsize(os.path.join(root, name)) for name in files),
#           "bytes in", len(files), "non-directory files")
#
# =============================================================================

# =============================================================================
# 1.5 try to identify the files to be loaded, better solution with recursive functions of os.walk
# 1.5.1 prepare the environment
#import os
#import shutil
#basepath = '/Volumes/pwang/5PL/'
##newpath = os.path.join(basepath, '2pro', '01cnt2raw')
#newpath = '/Users/wang/Dropbox/09Temp/'
##os.makedirs(newpath)
#ct = 0
#et = 0
#ct2 = 0
#et2 = 0
## 1.5.2 go through the directory
#for root, dirs, files in os.walk(os.path.join(basepath, '1raw')):
#    for name in files:
#        if '0' <= name[0] <= '9' and '0' <= name[1] <= '9' and name[2:6] == '.cnt' :
#            tmp1 = root.split('/')
#            if root[-2] == '-':
#                if tmp1[5] == tmp1[7][0:-2]:
#                    if tmp1[7][-1] == '1':
#                        newname = os.path.join(newpath, tmp1[5]+'_s4b'+name[0:2]+'.raw.fif.gz')
#                        ct += 1
#                    elif tmp1[7][-1] == '3':
#                        newname = os.path.join(newpath, tmp1[5]+'_s3b'+name[0:2]+'.raw.fif.gz')
#                        ct += 1
#                    else:
#                        newname = 'XXX'
#                        et += 1
##                    print(os.path.join(root, name), '->', newname)
#                else:
#                    print(tmp1[5], tmp1[7], ': mismatch')
#                    et += 1
#            else:
#                if tmp1[5] == tmp1[7][0:-1]:
#                    if tmp1[7][-1] == '1':
#                        newname = os.path.join(newpath, tmp1[5]+'_s1b'+name[0:2]+'.raw.fif.gz')
#                        ct += 1
#                    elif tmp1[7][-1] == '3':
#                        newname = os.path.join(newpath, tmp1[5]+'_s2b'+name[0:2]+'.raw.fif.gz')
#                        ct += 1
#                    else:
#                        newname = 'XXX'
#                        et += 1
##                    print(os.path.join(root, name), '->', newname)
#                else:
#                    print(tmp1[5], tmp1[7], ': mismatch')
#                    et += 1
#        elif name.endswith('.3dd') or name.endswith('.3DD'):
#            tmp1 = root.split('/')
#            if tmp1[5].lower() == name[0:len(tmp1[5])].lower():
#               newname = os.path.join(newpath, name.lower())
#               ct2 += 1
#               shutil.copy(os.path.join(root, name), newname)
#               print(os.path.join(root, name), '->', newname)
#            else:
#               et2 += 1
#               print(os.path.join(root, name), 'XXX')
#
#print(ct2, ' vs. ', et2)
# =============================================================================

# =============================================================================
# #1.6 read text file for information
# fin = open(r"/Users/wang/Dropbox/09Temp/X.DAT","r")
# #print(fin.read())
# tmp1 = fin.read()
# fin.close()
# tmp2 = tmp1.split('\n')
# ct = 0
# for tmp3 in tmp2:
#    tmp3[ct] = tmp3.split('\t')
#    ct += 1
# =============================================================================

#2 test on real data, e.g. generate the leadfield, head model etc.
#2.1 read the sensor locations, and normalize them to the template (subject RenP)
# 2.1.1 visualize the bem
import os.path as op
import mne
mne.viz.plot_bem(subject='PL_RP', subjects_dir='/Users/wang/Documents/FreeSurfer/',
                 brain_surfaces='white', orientation='sagittal')
#2.1.2 read the subject's sensor locations and check
ten_twenty_montage = mne.channels.make_standard_montage('standard_1020')
ten_twenty_montage.plot(show_names=False)
fig = ten_twenty_montage.plot(kind='3d')
fig.gca().view_init(azim=70, elev=15)



