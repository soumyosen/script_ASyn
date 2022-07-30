import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

expdata = pd.read_csv('expdata_clean1.csv', sep=" ")
compdata = pd.read_csv('NMRdataMultiFR.dat', sep="\t")

expdata.to_csv('expdata_final.csv', sep="\t", index=False)
compdata.to_csv('compdata_final.csv', sep="\t", index=False)

#print expdata
#print compdata


combined = pd.merge(expdata, compdata, on=['NUM', 'RES', 'ATOMNAME'])
#print combined

#x = np.corrcoef(combined['SHIFT_x'], combined['SHIFT_y'])
#print x
#
#mse = ((combined['SHIFT_x']-combined['SHIFT_y'])**2).mean(axis=None)
combined.columns = ['RES', 'NUM', 'ATOMNAME', 'EXP_SHIFT', 'COMP_SHIFT']
combined.to_csv('compare_exp_comp_shift.csv', sep="\t", index=False)
mse = ((combined['EXP_SHIFT']-combined['COMP_SHIFT'])**2).mean(axis=None)
#print combined
print mse
#
#mse_check = ((combined['EXP_SHIFT']-combined['COMP_SHIFT'])**2).mean()
#print mse_check


combined1 = combined[combined['ATOMNAME']!='N']
#print combined1
#
#x1 = np.corrcoef(combined1['SHIFT_x'], combined1['SHIFT_y'])
#print x1
#
mse1 = ((combined1['EXP_SHIFT']-combined1['COMP_SHIFT'])**2).mean(axis=None)
print mse1

combined2 = combined[(combined['ATOMNAME']=='C') | (combined['ATOMNAME']=='CA') | (combined['ATOMNAME']=='CB')]
#print combined2
mse2 = ((combined2['EXP_SHIFT']-combined2['COMP_SHIFT'])**2).mean(axis=None)
print mse2

#
#plt.scatter(combined['SHIFT_x'], combined['SHIFT_y'], s=10)
#plt.title("Correlation in experimental and computational chemical shift for full fibril")
#plt.xlabel("Experimental")
#plt.ylabel("Computational")
#plt.text(20, 170, r'correlation coefficient = 0.9981')
#plt.text(20, 160, r'mean squared error = 12.73')
#plt.text(20, 150, r'correlation coefficient without N = 0.99976')
#plt.text(20, 140, r'mean squared error without N = 1.83')
#plt.show()
