import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce

seglist = ["B2", "C1", "C2", "D1", "D2", "E1", "E2", "F1", "F2", "G1", "G2", "H1", "H2", "I1", "I2", "J1", "J2", "K1", "K2", "L1", "L2", "M1", 
	  "M2", "N1", "N2", "O1", "O2", "P1", "P2", "Q1", "Q2", "R1", "R2", "S1", "S2"]

dfall = pd.read_csv("100ns_B1.dat", sep=" ", names=['Time', '1'])
for (i,j) in zip(range(2, 37),seglist):
	df = pd.read_csv("100ns_%s.dat" % j, " ", names=['Time', '%s' % i])
	dfall["%s" % i] = df["%s" % i]
	


#print dfall.head()

collist = str(range(1, 37))
#print collist

dfrmsd = dfall.drop('Time', axis=1)
dfall['Mean'] = dfrmsd.mean(axis = 1)
dfall['Std Dev'] = dfrmsd.std(axis = 1)
#print dfall


dffull = pd.read_csv("rmsd_trj_100ns.dat", sep=" ", names=['Time', 'RMSD'])

fig, ax1 = plt.subplots()

ax1.plot(dfall['Time'], dfall['Mean'], color='blue', linewidth=2.0, label="Individual Protomers")
ax1.errorbar(dfall['Time'], dfall['Mean'], yerr=dfall['Std Dev'], ecolor="red", elinewidth=0.1)
ax1.plot(dffull['Time'], dffull['RMSD'], color='green', linewidth=2.0, label="Full Fibril")
ax1.set_xlim(0,100)
ax1.set_ylim(0,4.0)
ax1.set_xlabel("Time (ns)", fontsize=16)
ax1.set_ylabel("RMSD ($\AA$)", fontsize=16)
ax1.set_title(" RMSD of Residue 35 to 46 and 62 to 96", fontsize=16)  
leg=ax1.legend(["Individual Protomers", "Full Fibril"], bbox_to_anchor=(0.60, 0.55), frameon=False)
#leg=plt.legend(loc=1)
#
for line in leg.get_lines():
    line.set_linewidth(2)
#
plt.grid()
plt.savefig("RMSD_RMSDeachchain_100ns_HR_final.png", dpi=400)

#plt.show()
