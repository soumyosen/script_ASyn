import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce


df1 = pd.read_csv("hbonds_prot1.dat", sep=" ", names=['Time', 'Protofilament 1'])
df2 = pd.read_csv("hbonds_prot2.dat", sep=" ", names=['Time', 'Protofilament 2'])
df3 = pd.read_csv("hbonds_prot1_prot2.dat", sep=" ", names=['Time', 'Inter-protofilament'])
df4 = pd.read_csv("hbonds.dat", sep=" ", names=['Time', 'Total'])

dataframes = [df1, df2, df3, df4]

df = reduce(lambda left,right: pd.merge(left,right, on=['Time']), dataframes)
#df['Total1'] = df['Protofilament 1']+df['Protofilament 2']+df['Inter-protofilament']
#print df
df['Time'] = df['Time']*0.04


df1BB = pd.read_csv("hbonds_prot1_BB.dat", sep=" ", names=['Time', 'Protofilament 1'])
df2BB = pd.read_csv("hbonds_prot2_BB.dat", sep=" ", names=['Time', 'Protofilament 2'])
df3BB = pd.read_csv("hbonds_prot1_prot2_BB.dat", sep=" ", names=['Time', 'Inter-protofilament'])
df4BB = pd.read_csv("hbonds_BB.dat", sep=" ", names=['Time', 'Total'])

dataframesBB = [df1BB, df2BB, df3BB, df4BB]

dfBB = reduce(lambda left,right: pd.merge(left,right, on=['Time']), dataframesBB)
dfBB['Time'] = dfBB['Time']*0.04

fig, ax1 = plt.subplots()


ax1.plot(df['Time'], df['Protofilament 1'], color='red', linewidth=1.0, label='Protofilament 1')
ax1.plot(df['Time'], df['Protofilament 2'], color='blue', linewidth=1.0, label='Protofilament 2')
ax1.plot(df['Time'], df['Inter-protofilament'], color='green', linewidth=1.0, label='Inter-protofilament')
ax1.plot(df['Time'], df['Total'], color='black', linewidth=1.0, label='Total')
#plt.plot(df['Time'], df['Total1'], color='orange', linewidth=1.0, label='Total1')
ax1.set_xlim(0,100)
ax1.set_ylim(0,1100)
ax1.set_xlabel("Time (ns)", fontsize=16)
ax1.set_ylabel("No. of H-bonds", fontsize=16)
ax1.set_title(" H-bonds in Fibril", fontsize=16)  
#leg=ax1.legend(bbox_to_anchor=(0.665, 0.58))
leg=ax1.legend(bbox_to_anchor=(0.6, 0.58), frameon=False)
plt.grid()

for line in leg.get_lines():
    line.set_linewidth(2)


#left, bottom, width, height = [0.62, 0.21, 0.25, 0.17]
#left, bottom, width, height = [0.42, 0.21, 0.45, 0.17]
left, bottom, width, height = [0.52, 0.21, 0.35, 0.17]
ax2 = fig.add_axes([left, bottom, width, height])

ax2.plot(dfBB['Time'], dfBB['Protofilament 1'], color='red', linewidth=1.0, label='Protofilament 1')
ax2.plot(dfBB['Time'], dfBB['Protofilament 2'], color='blue', linewidth=1.0, label='Protofilament 2')
ax2.plot(dfBB['Time'], dfBB['Inter-protofilament'], color='green', linewidth=1.0, label='Inter-protofilament')
ax2.plot(dfBB['Time'], dfBB['Total'], color='black', linewidth=1.0, label='Total')
ax2.set_xlim(0,100)
ax2.set_ylim(0,1100)
ax2.set_xlabel("Time (ns)", fontsize=10)
ax2.set_ylabel("No. of H-bonds", fontsize=10)
ax2.set_title(" H-bonds in Fibril Backbone", fontsize=10)
ax2.set_yticks(np.arange(0, 1100, step=200))



#plt.show()
plt.savefig("hbonds_hbondsBB_2a_HR.png", dpi=400)
