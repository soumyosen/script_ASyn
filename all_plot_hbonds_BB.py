import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce


df1 = pd.read_csv("hbonds_prot1_BB.dat", sep=" ", names=['Time', 'Protofilament 1'])
df2 = pd.read_csv("hbonds_prot2_BB.dat", sep=" ", names=['Time', 'Protofilament 2'])
df3 = pd.read_csv("hbonds_prot1_prot2_BB.dat", sep=" ", names=['Time', 'Inter-protofilament'])
df4 = pd.read_csv("hbonds_BB.dat", sep=" ", names=['Time', 'Total'])

dataframes = [df1, df2, df3, df4]

df = reduce(lambda left,right: pd.merge(left,right, on=['Time']), dataframes)
#df['Total1'] = df['Protofilament 1']+df['Protofilament 2']+df['Inter-protofilament']
#print df
df['Time'] = df['Time']*0.08

plt.plot(df['Time'], df['Protofilament 1'], color='red', linewidth=1.0, label='Protofilament 1')
plt.plot(df['Time'], df['Protofilament 2'], color='blue', linewidth=1.0, label='Protofilament 2')
plt.plot(df['Time'], df['Inter-protofilament'], color='green', linewidth=1.0, label='Inter-protofilament')
plt.plot(df['Time'], df['Total'], color='black', linewidth=1.0, label='Total')
#plt.plot(df['Time'], df['Total1'], color='orange', linewidth=1.0, label='Total1')
plt.xlim(0,100)
plt.ylim(0,1100)
plt.xlabel("Time (ns)", fontsize=16)
plt.ylabel("No. of H-bonds", fontsize=16)
plt.title(" H-bonds in Fibril Backbone", fontsize=16)  
#leg=plt.legend(bbox_to_anchor=(0.665, 0.51))
leg=plt.legend(loc=1)

for line in leg.get_lines():
    line.set_linewidth(2)

plt.grid()
#plt.show()
plt.savefig("hbonds_BB_HR.png", dpi=400)
