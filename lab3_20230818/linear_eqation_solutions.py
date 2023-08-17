#####################################################
# @Author: Abhilash Sarwade
# @Date:   2023-08-17 04:37:21 pm
# @email: sarwade@ursc.gov.in
# @File Name: linear_eqation_solutions.py
# @Project: lab3_20230818
#
# @Last Modified time: 2023-08-17 05:57:45 pm
#####################################################

import numpy as np


def lu_decomposition(mtrx):
    mtrx = np.array(mtrx)

    if mtrx.shape[0] != mtrx.shape[1]:
        print('Matrix is not sqaure. Exiting')
        return -1
    
    d = mtrx.shape[0]
    # Initiate L and U matrices
    l_mtrx = np.zeros((d,d))
    u_mtrx = np.zeros((d,d))

    for k in range(d):
        l_mtrx[k,k] = 1

    u_mtrx[0,:] = mtrx[0,:]
    l_mtrx[:,0] = mtrx[:,0]/u_mtrx[0,0]

    for i in range(1,d):
        j = i-1
        u_mtrx[i,i:] = mtrx[i,i:]
        while j >=0:
            u_mtrx[i,i:] = u_mtrx[i,i:] - l_mtrx[i,j]*u_mtrx[j,i:]
            j = j - 1
        
        j = i-1
        l_mtrx[i:,i] = mtrx[i:,i]
        while j >=0:
            l_mtrx[i:,i] = l_mtrx[i:,i] - l_mtrx[i:,j]*u_mtrx[j,i]
            j = j - 1
        l_mtrx[i:,i] = l_mtrx[i:,i]/u_mtrx[i,i]

