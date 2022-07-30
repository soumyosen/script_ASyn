import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce


df1 = pd.read_csv("contact_protofilament1.dat", sep=" ", names=['Time', 'Protofilament 1'])
df2 = pd.read_csv("contact_protofilament2.dat", sep=" ", names=['Time', 'Protofilament 2'])
df3 = pd.read_csv("contact_interprotofilament.dat", sep=" ", names=['Time', 'Inter-protofilament'])

dataframes = [df1, df2, df3]

df = reduce(lambda left,right: pd.merge(left,right, on=['Time']), dataframes)
df['Total'] = df['Protofilament 1']+df['Protofilament 2']+df['Inter-protofilament']
#print df


plt.plot(df['Time'], df['Protofilament 1'], color='red', linewidth=1.0, label='Protofilament 1')
plt.plot(df['Time'], df['Protofilament 2'], color='blue', linewidth=1.0, label='Protofilament 2')
plt.plot(df['Time'], df['Inter-protofilament'], color='green', linewidth=1.0, label='Inter-protofilament')
plt.plot(df['Time'], df['Total'], color='black', linewidth=1.0, label='Total')
plt.xlim(0,100)
plt.ylim(0,20000)
plt.xlabel("Time (ns)", fontsize=16)
plt.ylabel("No. of Contacts", fontsize=16)
plt.title("No. of Inter-chain Heavy Atom Contacts", fontsize=16)  
leg=plt.legend(bbox_to_anchor=(0.58, 0.55))

for line in leg.get_lines():
    line.set_linewidth(2)

plt.grid()
plt.show()

#plt.savefig("interchain_contact_100ns_HR.png", dpi=400)
